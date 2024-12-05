"""jello - query JSON at the command line with python syntax"""

import contextlib
import json
import os
import sys
import signal
import shutil
import textwrap
import traceback
from textwrap import TextWrapper
import jello
import jello.lib as lib
from jello.lib import opts, load_json, read_file, pyquery, format_response


def ctrlc(signum, frame):
    """exit with error on SIGINT"""
    sys.exit(1)


def get_stdin():
    """return STDIN data"""
    if sys.stdin.isatty():
        return None
    else:
        return sys.stdin


def print_help():
    print(textwrap.dedent('''\
        jello:  query JSON at the command line with python syntax

        Usage:  cat data.json | jello [OPTIONS] [QUERY | -q <query_file>]
                jello [OPTIONS] [QUERY | -q <query_file>] [-f <input_files>]

                -c   compact JSON output
                -C   force color output even when using pipes (overrides -m)
                -e   empty data (don't process data from STDIN or file)
                -f   load input data from JSON file or JSON Lines files
                -F   flatten output list/iterator to newline-delimited json
                -i   initialize environment with .jelloconf.py
                     located at ~ (linux) or %appdata% (Windows)
                -l   output as lines suitable for assignment to a bash array
                -m   monochrome output
                -n   print selected null values
                -q   load query from a file
                -r   raw string output (no quotes)
                -R   raw string input (don't auto convert input to dict/list)
                -s   print the JSON schema in grep-able format
                -S   stream input newline-delimited json from STDIN or file
                     from -f.  "_" is an iterator providing the entries
                -t   print type annotations in schema view
                -v   version info
                -h   help

        Use '_' as the input data and use python dict and list bracket syntax
        or dot notation to filter the results and/or rebuild the output.

        Examples:
                cat data.json | jello _.foo
                jello _.foo -f data.json
                jello '_["foo"]' -f data.json
                variable=($(cat data.json | jello -l _.foo))
    '''))
    sys.exit()


def print_error(message):
    """print error messages to STDERR and quit with error code"""
    print(message, file=sys.stderr)
    sys.exit(1)


def print_exception(e=None, data='', query='', response='', ex_type='Runtime'):
    exception_message = ''
    term_width = shutil.get_terminal_size().columns or 80
    split_length = int(term_width)
    if split_length < 10:
        split_length = 10

    # prepare short info where the error occurred
    stacktrace = traceback.extract_tb(e.__traceback__)
    stacklines = []
    if len(stacktrace):
        if stacktrace[-1].filename == "<string>":
            # we get <string> as filename when exception occurs in a exec() call
            stacklines.append(f"Jello query, line {stacktrace[-1].lineno}")
            # lineno begins with 1, lists with 0 -> subtract 1
            stacklines.append("  " + query.split('\n')[stacktrace[-1].lineno-1])

    wrapper = TextWrapper(width=term_width,
                                initial_indent='',
                                subsequent_indent=' ' * 12)
    exception_message = wrapper.fill(f'jello:  {ex_type} Exception:  {e.__class__.__name__}') + '\n'

    wrapper = TextWrapper(width=term_width,
                          initial_indent=' ' * 8,
                          subsequent_indent=' ' * 12)

    # add pre-formatted stacktrace text: flatten the info into lines, normalize newlines
    for errstring in stacklines:
        for errline in errstring.split('\n'):
            if len(errline.replace('\n', '')):
                exception_message += wrapper.fill(errline.replace('\n', '')) + '\n'

    exception_message += wrapper.fill(f'{e}') + '\n'

    e_text = ''
    if hasattr(e, 'text'):
        e_text = str(e.text).replace('\n', '')

    detail = {
        f'{e.__class__.__name__}': e_text,
        'query': str(query).replace('\n', '\\n'),
        'data': str(data).replace('\n', '\\n'),
        'response': str(response).replace('\n', '\\n')
    }

    for item in detail:
        if len(detail[item]) > (split_length * 2) + 10:
            detail[item] = f'{item}:  {detail[item][:split_length]} ... {detail[item][-split_length:]}'
        elif detail[item]:
            detail[item] = f'{item}:  {detail[item]}'

        if detail[item]:
            detail[item] = wrapper.fill(detail[item])
            exception_message += f'{detail[item]}' + '\n'

    print(exception_message, file=sys.stderr)
    sys.exit(1)


def print_json_streaming_error(e, query='', ex_type='Json Load'):
    cause = e.__cause__
    data = None
    if isinstance(cause, json.JSONDecodeError):
        data = cause.doc
    print_exception(
        cause,
        data=data,
        query=query,
        ex_type=ex_type
    )


class nullclosing:
    """simpler version of contextlib.nullcontext, which was introduced in 3.7
    (currently support 3.6)"""
    
    def close(self):
        pass


def main(data=None, query='_'):
    # break on ctrl-c keyboard interrupt
    signal.signal(signal.SIGINT, ctrlc)

    # break on pipe error. need try/except for windows compatibility
    try:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except AttributeError:
        pass

    # enable colors for Windows cmd.exe terminal
    if sys.platform.startswith('win32'):
        os.system('')

    stdin = None
    if data is None:
        stdin = get_stdin()

    options = []
    long_options = {}
    arg_section = ''  # can be query_file or data_files
    data_files = []

    for arg in sys.argv[1:]:
        if arg == '-q':
            arg_section = 'query_file'

        elif arg == '-f':
            data = ''
            arg_section = 'data_files'

        elif arg_section == 'query_file':
            try:
                query = read_file(arg)
            except Exception as e:
                print_error(f'jello:  Issue reading query file: {e}')
            finally:
                arg_section = ''

        elif arg_section == 'data_files':
            data_files.append(arg)
            arg_section = ''

        elif arg.startswith('-') and not arg.startswith('--'):
             options.extend(arg[1:])
             arg_section = ''

        elif arg.startswith('--'):
            try:
                k, v = arg[2:].split('=')
                long_options[k] = int(v)
                arg_section = ''
            except Exception:
                print_help()

        else:
            query = arg
            arg_section = ''

    opts.compact = opts.compact or 'c' in options
    opts.initialize = opts.initialize or 'i' in options
    opts.lines = opts.lines or 'l' in options
    opts.empty = opts.empty or 'e' in options
    opts.force_color = opts.force_color or 'C' in options
    opts.flatten = opts.flatten or 'F' in options
    opts.mono = opts.mono or ('m' in options or bool(os.getenv('NO_COLOR')))
    opts.nulls = opts.nulls or 'n' in options
    opts.raw = opts.raw or 'r' in options
    opts.raw_input = opts.raw_input or 'R' in options
    opts.schema = opts.schema or 's' in options
    opts.stream_input = opts.stream_input or 'S' in options
    opts.types = opts.types or 't' in options
    opts.version_info = opts.version_info or 'v' in options
    opts.helpme = opts.helpme or 'h' in options

    if opts.helpme:
        print_help()

    if opts.version_info:
        print(textwrap.dedent(f'''\
            jello:  Version: {jello.__version__}
                    Author: {jello.AUTHOR}
                    Website: {jello.WEBSITE}
                    Copyright: {jello.COPYRIGHT}
                    License: {jello.LICENSE}
        '''))
        sys.exit()

    if not opts.empty and data is None and not stdin and not data_files:
        print_error('jello:  Missing JSON or JSON Lines data via STDIN or file via -f option.\n')

    # read all the file sources
    input_context_manager = contextlib.closing(nullclosing())
    if opts.empty:
        data = '{}'
    elif opts.stream_input:
        data = lib.StreamingJsonInput(data, stdin, data_files)
        input_context_manager = data
    else:
        data = lib.read_data_nonstreaming(data, stdin, data_files)
        if opts.raw_input:
            data = str(data).rstrip('\r\n')
        else:
            try:
                data = load_json(data)
            except json.JSONDecodeError as e:
                print_exception(e, ex_type='JSON Load')

    # closes input data resources
    with input_context_manager as _:
        # Read .jelloconf.py (if it exists) and run the query
        response = ''
        try:
            response = pyquery(data, query)
        except lib.StreamingJsonError as e:
            # when streaming input errors are not raised until the data is
            # pulled by the user query
            print_json_streaming_error(e)
        except Exception as e:
            print_exception(e, data, query, ex_type='Query')

        # reset opts.mono after pyquery since initialization in pyquery can change values
        if opts.force_color:
            opts.mono = False

        # Create and print schema or JSON/JSON-Lines/Lines
        try:
            format_response(response)
        except lib.StreamingJsonError as e:
            # when streaming output using -F we don't parse input and process it
            # until we pull from the output iterator here
            print_json_streaming_error(e)
        except Exception as e:
            print_exception(e, data, query, response, ex_type='Output')


if __name__ == '__main__':
    main()
