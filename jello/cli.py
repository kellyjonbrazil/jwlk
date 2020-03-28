#!/usr/bin/env python3
"""jello - query JSON at the command line with python syntax"""

import os
import sys
import textwrap
import json
import signal
from contextlib import redirect_stdout
import io
import ast

__version__ = '0.3.1'


def ctrlc(signum, frame):
    """exit with error on SIGINT"""
    sys.exit(1)


def get_stdin():
    """return STDIN data"""
    if sys.stdin.isatty():
        return None

    return sys.stdin.read()


def helptext():
    print_error(textwrap.dedent('''\
        jello:   query JSON at the command line with python syntax

        Usage:  <JSON Data> | jello [OPTIONS] QUERY

                -c    compact JSON output
                -l    output as lines suitable for a bash array
                -n    print selected null values
                -r    raw string output (no quotes)
                -v    version info
                -h    help

        Use '_' as the input data and assign the result to 'r'. Use python dict syntax.

        Example:
                <JSON Data> | jello 'r = _["foo"]'
    '''))


def print_error(message):
    """print error messages to STDERR and quit with error code"""
    print(message, file=sys.stderr)
    sys.exit(1)


def print_json(data, compact=False, nulls=None, lines=None, raw=None):
    if isinstance(data[0], (list, dict)):
        if not lines:
            if compact:
                print(json.dumps(data[0]))
            else:
                print(json.dumps(data[0], indent=2))

        elif lines:
            for line in data[0]:
                if line is None:
                    if nulls:
                        print('null')
                    else:
                        print('')

                elif line is True:
                    print('true')

                elif line is False:
                    print('false')

                elif isinstance(line, str):
                    if raw:
                        print(line)
                    else:
                        print(f'"{line}"')

                else:
                    if compact:
                        print(json.dumps(line))
                    else:
                        print(json.dumps(line, indent=2))

    elif data[0] is None:
        if nulls:
            print('null')
        else:
            print('')

    elif data[0] is True:
        print('true')

    elif data[0] is False:
        print('false')

    elif isinstance(data[0], str):
        if raw:
            print(data[0])
        else:
            print(f'"{data[0]}"')


def normalize(data, nulls=None, raw=None):
    result_list = []
    try:
        for entry in data.splitlines():
            try:
                result_list.append(ast.literal_eval(entry.replace(r'\u2063', r'\n')))

            except (ValueError, SyntaxError):
                # if ValueError or SyntaxError exception then it was not a
                # list, dict, bool, None, int, or float - must be a string
                if raw:
                    result_list.append(str(entry).replace(r'\u2063', r'\n'))
                else:
                    result_list.append(str(f'"{entry}"').replace(r'\u2063', r'\n'))

    except Exception as e:
        print(textwrap.dedent(f'''\
            jello:  Normalize Exception: {e}
                    data: {data}
                    result_list: {result_list}
            '''), file=sys.stderr)
        sys.exit(1)

    return result_list


def pyquery(data, query):
    _ = data
    query = 'r = None\n' + query + '\nprint(r)'
    output = None

    f = io.StringIO()
    try:
        with redirect_stdout(f):
            print(exec(compile(query, '<string>', 'exec')))
            output = f.getvalue()[0:-6]

    except KeyError as e:
        print(textwrap.dedent(f'''\
            jello:  Key does not exist: {e}
        '''), file=sys.stderr)
        sys.exit(1)

    except IndexError as e:
        print(textwrap.dedent(f'''\
            jello:  {e}
        '''), file=sys.stderr)
        sys.exit(1)

    except SyntaxError as e:
        print(textwrap.dedent(f'''\
            jello:  {e}
                    {e.text}
        '''), file=sys.stderr)
        sys.exit(1)

    except TypeError as e:
        if output is None:
            output = ''
        else:
            print(textwrap.dedent(f'''\
                jello:  TypeError: {e}
            '''), file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(textwrap.dedent(f'''\
            jello:  Query Exception: {e}
                    _: {_}
                    query: {query}
                    output: {output}
        '''), file=sys.stderr)
        sys.exit(1)

    return output


def load_json(data):
    # replace newline characters in the input text with unicode separator \u2063
    data = data.strip().replace(r'\n', '\u2063')

    # load the JSON or JSON Lines data
    try:
        json_dict = json.loads(data)

    except Exception:
        # if json.loads fails, assume the data is json lines and parse
        data = data.splitlines()
        data_list = []
        for i, jsonline in enumerate(data):
            try:
                entry = json.loads(jsonline)
                data_list.append(entry)
            except Exception as e:
                # can't parse the data. Throw a nice message and quit
                print(textwrap.dedent(f'''\
                    jello:  JSON Load Exception: {e}
                            Cannot parse line {i + 1} (Not JSON or JSON Lines data):
                            {str(jsonline)[:70]}
                    '''), file=sys.stderr)
                sys.exit(1)

        json_dict = data_list

    return json_dict


def main():
    # break on ctrl-c keyboard interrupt
    signal.signal(signal.SIGINT, ctrlc)
    stdin = get_stdin()
    # for debugging
    # stdin = r'''["word", null, false, 1, 3.14, true, "multiple words", false, "words\nwith\nnewlines", 42]'''

    query = 'r = _'

    options = []
    long_options = {}
    for arg in sys.argv[1:]:
        if arg.startswith('-') and not arg.startswith('--'):
            options.extend(arg[1:])

        elif arg.startswith('--'):
            try:
                k, v = arg[2:].split('=')
                long_options[k] = int(v)
            except Exception:
                helptext()

        else:
            query = arg

    compact = 'c' in options
    lines = 'l' in options
    nulls = 'n' in options
    raw = 'r' in options
    version_info = 'v' in options
    helpme = 'h' in options

    if helpme:
        helptext()

    if version_info:
        print_error(f'jello:   version {__version__}\n')

    if stdin is None:
        print_error('jello:  missing piped JSON or JSON Lines data\n')

    list_dict_data = load_json(stdin)
    raw_response = pyquery(list_dict_data, query)
    normalized_response = normalize(raw_response, raw=raw, nulls=nulls)  # returns a list of results
    # result = process(normalized_response, lines=lines)
    print_json(normalized_response, compact=compact, nulls=nulls, raw=raw, lines=lines)


if __name__ == '__main__':
    main()
