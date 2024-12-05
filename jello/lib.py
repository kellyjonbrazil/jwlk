"""jello - query JSON at the command line with python syntax"""

import collections.abc
from io import StringIO
import os
import sys
import types
import ast
import json
import shutil
from keyword import iskeyword
from textwrap import TextWrapper
from jello.dotmap import DotMap

# make pygments import optional
try:
    from pygments import highlight
    from pygments.style import Style
    from pygments.token import (Name, Number, String, Keyword)
    from pygments.lexers import JsonLexer
    from pygments.lexers.javascript import JavascriptLexer
    from pygments.formatters import Terminal256Formatter
    from pygments.formatters import HtmlFormatter
    PYGMENTS_INSTALLED = True
except Exception:
    PYGMENTS_INSTALLED = False


def is_valid_variable_name(name: str) -> bool:
    dict_methods = [
        '__class__', '__class_getitem__', '__contains__', '__delattr__',
        '__delitem__', '__dir__', '__eq__', '__format__', '__ge__',
        '__getattribute__', '__getitem__', '__getstate__', '__gt__',
        '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__',
        '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__',
        '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__',
        '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear',
        'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
        'setdefault', 'update', 'values'
    ]
    return name.isidentifier() and not iskeyword(name) and name not in dict_methods


class opts:
    initialize = None
    version_info = None
    helpme = None
    compact = None
    empty = None
    nulls = None
    raw = None
    raw_input = None
    lines = None
    force_color = None
    mono = None
    schema = None
    types = None
    keyname_color = None
    keyword_color = None
    number_color = None
    string_color = None
    flatten = None
    stream_input = None


class JelloTheme:
    if PYGMENTS_INSTALLED:
        theme = {
            Name: 'bold ansiblue',
            Keyword: 'ansibrightblack',
            Number: 'ansimagenta',
            String: 'ansigreen'
        }

    def set_colors(self):
        """
        Updates the JelloTheme.theme dictionary used by the JelloStyle class.

        Grab custom colors from JELLO_COLORS environment variable and opts class set by .jelloconf.py file.
        Individual colors from JELLO_COLORS take precedence over .jelloconf.py. Individual colors from
        JELLO_COLORS will fall back to .jelloconf.py or default if the env variable color is set to 'default'

        JELLO_COLORS env variable takes 4 comma separated string values and should be in the format of:

        JELLO_COLORS=<keyname_color>,<keyword_color>,<number_color>,<string_color>

        Where colors are: black, red, green, yellow, blue, magenta, cyan, gray, brightblack, brightred,
                          brightgreen, brightyellow, brightblue, brightmagenta, brightcyan, white, default

        Default colors:
            JELLO_COLORS=blue,brightblack,magenta,green
            or
            JELLO_COLORS=default,default,default,default
        """
        env_colors = os.getenv('JELLO_COLORS')
        input_error = False

        if env_colors:
            color_list = env_colors.split(',')

        if env_colors and len(color_list) != 4:
            input_error = True

        if env_colors:
            for color in color_list:
                if color not in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'gray', 'brightblack', 'brightred',
                                 'brightgreen', 'brightyellow', 'brightblue', 'brightmagenta', 'brightcyan', 'white', 'default']:
                    input_error = True
        else:
            color_list = ['default', 'default', 'default', 'default']

        # if there is an issue with the env variable, just set all colors to default and move on
        if input_error:
            warning_message(['could not parse JELLO_COLORS environment variable'])
            color_list = ['default', 'default', 'default', 'default']

        if PYGMENTS_INSTALLED:
            # first set theme from opts class or fallback to defaults
            self.theme = {
                Name: f'bold ansi{opts.keyname_color}' if opts.keyname_color else self.theme[Name],
                Keyword: f'ansi{opts.keyword_color}' if opts.keyword_color else self.theme[Keyword],
                Number: f'ansi{opts.number_color}' if opts.number_color else self.theme[Number],
                String: f'ansi{opts.string_color}' if opts.string_color else self.theme[String]
            }

            # then set theme from JELLO_COLORS env variable or fallback to existing colors
            self.theme = {
                Name: f'bold ansi{color_list[0]}' if not color_list[0] == 'default' else self.theme[Name],
                Keyword: f'ansi{color_list[1]}' if not color_list[1] == 'default' else self.theme[Keyword],
                Number: f'ansi{color_list[2]}' if not color_list[2] == 'default' else self.theme[Number],
                String: f'ansi{color_list[3]}' if not color_list[3] == 'default' else self.theme[String]
            }


class Schema(JelloTheme):
    """Inherits theme and set_colors() from JelloTheme"""

    def __init__(self):
        self._schema_list = []

    def color_output(self, data):
        if not opts.mono and PYGMENTS_INSTALLED:
            class JelloStyle(Style):
                styles = self.theme

            lexer = JavascriptLexer()
            formatter = Terminal256Formatter(style=JelloStyle)
            return highlight(data, lexer, formatter)[0:-1]

        else:
            return data

    def html_output(self, data):
        class JelloStyle(Style):
            styles = self.theme

        lexer = JavascriptLexer()
        formatter = HtmlFormatter(style=JelloStyle, noclasses=True)
        return highlight(data, lexer, formatter)

    def create_schema(self, data):
        self._schema_gen(data)
        myschema = '\n'.join(self._schema_list)
        # unsure if this is helpful, but trying to reduce memory footprint by clearing the list
        self._schema_list *= 0
        return myschema

    def _schema_gen(self, src, path='_'):
        """
        Creates a grep-able schema representation of the JSON.
        This method is recursive, and output is stored within self._schema_list (list).
        """
        if isinstance(src, list):
            # print empty brackets as first list definition
            val = '[]'
            val_type = ''
            padding = ''
            if opts.types:
                val_type = '//   (array)'
                padding = '  '
                if len(path) + len(val) + len(val_type) < 76:
                    padding = ' ' * (76 - (len(path) + len(val) + len(val_type)))

            self._schema_list.append(f'{path} = {val};{padding}{val_type}')

            for i, item in enumerate(src):
                self._schema_gen(item, path=f'{path}[{i}]')

        elif isinstance(src, dict):
            # print empty curly brackets as first object definition
            val = '{}'
            val_type = ''
            padding = ''
            if opts.types:
                val_type = '//  (object)'
                padding = '  '
                if len(path) + len(val) + len(val_type) < 76:
                    padding = ' ' * (76 - (len(path) + len(val) + len(val_type)))

            self._schema_list.append(f'{path} = {val};{padding}{val_type}')

            for k, v in src.items():
                # encapsulate key in brackets if it is not a valid variable name
                if is_valid_variable_name(k):
                    k = f'.{k}'
                else:
                    k = f'["{k}"]'

                if isinstance(v, list):
                    # print empty brackets as first list definition
                    val = '[]'
                    val_type = ''
                    padding = ''
                    if opts.types:
                        val_type = '//   (array)'
                        padding = '  '
                        if len(path) + len(val) + len(val_type) < 76:
                            padding = ' ' * (76 - (len(f'{path}{k}') + len(val) + len(val_type)))

                    self._schema_list.append(f'{path}{k} = {val};{padding}{val_type}')

                    for i, item in enumerate(v):
                        self._schema_gen(item, path=f'{path}{k}[{i}]')

                elif isinstance(v, dict):
                    self._schema_gen(v, path=f'{path}{k}')

                else:
                    val = json.dumps(v, ensure_ascii=False)
                    val_type = ''
                    padding = ''
                    if opts.types:
                        if val == 'true' or val == 'false':
                            val_type = '// (boolean)'
                        elif val == 'null':
                            val_type = '//    (null)'
                        elif val.replace('.', '', 1).isdigit():
                            val_type = '//  (number)'
                        else:
                            val_type = '//  (string)'

                        padding = '  '
                        if len(path) + len(k) + len(val) + len(val_type) < 76:
                            padding = ' ' * (76 - (len(path) + len(k) + len(val) + len(val_type)))

                    self._schema_list.append(f'{path}{k} = {val};{padding}{val_type}')

        else:
            val = json.dumps(src, ensure_ascii=False)
            val_type = ''
            padding = ''
            if opts.types:
                if val == 'true' or val == 'false':
                    val_type = '// (boolean)'
                elif val == 'null':
                    val_type = '//    (null)'
                elif val.replace('.', '', 1).isdigit():
                    val_type = '//  (number)'
                else:
                    val_type = '//  (string)'

                padding = '  '
                if len(path) + len(val) + len(val_type) < 76:
                    padding = ' ' * (76 - (len(path) + len(val) + len(val_type)))

            self._schema_list.append(f'{path} = {val};{padding}{val_type}')


class Json(JelloTheme):
    """Inherits theme and set_colors() from JelloTheme"""

    def color_output(self, data):
        if not opts.mono and PYGMENTS_INSTALLED:
            class JelloStyle(Style):
                styles = self.theme

            lexer = JsonLexer()
            formatter = Terminal256Formatter(style=JelloStyle)
            return highlight(data, lexer, formatter)[0:-1]

        else:
            return data

    def html_output(self, data):
        class JelloStyle(Style):
            styles = self.theme

        lexer = JsonLexer()
        formatter = HtmlFormatter(style=JelloStyle, noclasses=True)
        return highlight(data, lexer, formatter)

    def create_json(self, data):
        separators = None
        indent = 2

        if opts.compact or opts.lines:
            separators = (',', ':')
            indent = None

        if isinstance(data, dict):
            return json.dumps(data, separators=separators, indent=indent, ensure_ascii=False)

        if isinstance(data, list):
            if not opts.lines:
                return json.dumps(data, separators=separators, indent=indent, ensure_ascii=False)

            # print lines
            else:
                flat_list = ''
                for entry in data:
                    if entry is None:
                        if opts.nulls:
                            flat_list += 'null\n'
                        else:
                            flat_list += '\n'

                    elif isinstance(entry, (dict, list, bool, int, float)):
                        flat_list += json.dumps(entry, separators=separators, ensure_ascii=False) + '\n'

                    elif isinstance(entry, str):
                        # replace \n with \\n here so lines with newlines literally print the \n char
                        entry = entry.replace('\n', '\\n')
                        if opts.raw:
                            flat_list += f'{entry}' + '\n'
                        else:
                            flat_list += f'"{entry}"' + '\n'

                return flat_list.rstrip()

        # naked single item return case
        elif data is None:
            if opts.nulls:
                return 'null'
            else:
                return ''

        elif isinstance(data, (bool, int, float)):
            return json.dumps(data, ensure_ascii=False)

        elif isinstance(data, str):
            # replace \n with \\n here so lines with newlines literally print the \n char
            data = data.replace('\n', '\\n')
            if opts.raw:
                return f'{data}'
            else:
                return f'"{data}"'

        # only non-serializable types are left. Force an exception from json.dumps()
        else:
            json.dumps(data)
            # this code should not run, but just in case something slips by above
            raise TypeError(f'Object is not JSON serializable')

 
def format_response(response):
    """Create schema or JSON/JSON-Lines/Lines"""

    if opts.flatten:
        it = None
        if isinstance(response, collections.abc.Iterator):
            it = response
        elif isinstance(response, list):
            it = iter(response)
        else:
            raise TypeError('-F/flatten requires the query to return an iterator/generator or list')
        for item in it:
            _format_single_response(item)
    else:
        _format_single_response(response)


def _format_single_response(response):
    if isinstance(response, collections.abc.Iterator):
        response = list(response)

    if opts.schema:
        schema = Schema()
        output = schema.create_schema(response)

        if not opts.mono and (sys.stdout.isatty() or opts.force_color):
            schema.set_colors()
            output = schema.color_output(output)

    else:
        json_out = Json()
        output = json_out.create_json(response)

        if (not opts.mono and not opts.raw) and (sys.stdout.isatty() or opts.force_color):
            json_out.set_colors()
            output = json_out.color_output(output)

    print(output)


def load_json(data):
    try:
        json_dict = json.loads(data)
    except Exception as e:
        try:
            # if json.loads fails, try loading as json lines
            json_dict = [json.loads(i) for i in data.splitlines() if i.strip()]
        except Exception:
            # raise original JSON exception instead of JSON Lines exception
            raise e

    return json_dict


def warning_message(message_lines):
    """
    Prints warning message for non-fatal issues. The first line is prepended with
    'jello:  Warning - ' and subsequent lines are indented. Wraps text as needed
    based on the terminal width.

    Parameters:

        message:   (list) list of string lines

    Returns:

        None - just prints output to STDERR
    """
    columns = shutil.get_terminal_size().columns

    first_wrapper = TextWrapper(width=columns, subsequent_indent=' ' * 12)
    next_wrapper = TextWrapper(width=columns, initial_indent=' ' * 8,
                               subsequent_indent=' ' * 12)

    first_line = message_lines.pop(0)
    first_str = f'jello:  Warning - {first_line}'
    first_str = first_wrapper.fill(first_str)
    print(first_str, file=sys.stderr)

    for line in message_lines:
        if line == '':
            continue
        message = next_wrapper.fill(line)
        print(message, file=sys.stderr)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def read_data_nonstreaming(initial_data, stdin, data_files):
    sio = StringIO()
    sep = ""
    if initial_data is not None:
        sio.write(initial_data)
        sio.write("\n")
        sep = "\n"
    if stdin:
        sio.write(sep)
        sio.write(stdin.read())
        sep = "\n"
    for file in data_files:
        sio.write(sep)
        # let the JsonDecoderError raise
        sio.write(read_file(file))
        sep = "\n"
    return sio.getvalue()


class StreamingJsonError(Exception):
    '''
    Wraps exceptions raised while loading and parsing json data.
    Raised from exception so that __cause__ provides the underlying error.

    When streaming data is not deserialized until pulled from an iterator during
    user query execution or output formatting (when using -F to flatten and
    stream the output).  One cannot rely on where an exception is caught to
    indicate what went wrong.  This class signifies that an exception occurred
    during reading or deserializing input data even when the exception
    propagates from later function calls.
    '''


class CloseableIterator(collections.abc.Iterator):
    '''
    Iterator that also provides close() method.
    Provides for safe file closing when reading from files within
    iterators/generators, where the scope cannot be controlled to use a context
    manager.
    '''
    closer = None
    it = None

    def __init__(self, closer, it):
        self.closer = closer
        self.it = it

    def close(self):
        self.closer()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.it)


def _generate_json_from_lines_iter(lines_iter):
    """
    Returns iterator of json objects from newline-delimited json input iterable.
    lines_iter is any iterable whose iterator returns strings of individual json
    objects.  For example, a list of strings or a file-like object of ndjson.
    """

    # the set of exceptions file readline() may throw is not documented.
    # separating this apart to isolate exceptions arising from reading an
    # underlying iterator and file.
    it = iter(lines_iter)
    while True:
        try:
            line = next(it)
        except StopIteration:
            return
        except Exception as e:
            raise StreamingJsonError from e

        stripped = line.strip()
        if not stripped:
            continue

        try:
            yield json.loads(stripped)
        except json.JSONDecodeError as e:
            raise StreamingJsonError from e


class StreamingJsonInput:
    """
    Iterator and context manager for streaming json from stdin and files.
    """

    # these are "closeable iterators" when backed by a closeable file
    current_iterator = None
    # functions to construct remaining cloaseable iterators
    remaining_iterator_factories = None

    def __init__(self, initial_data, stdin, files):
        """
        initial_data.  String from cli.main.
        stdin_or_files.  sys.stdin or data file paths.
        """
        # set up the iterators
        self.remaining_iterator_factories = collections.deque()
        if initial_data:
            self.remaining_iterator_factories.append(
                lambda: CloseableIterator(
                    lambda: None,
                    _generate_json_from_lines_iter(initial_data.splitlines())
                )
            )

        if stdin:
            self.remaining_iterator_factories.append(
                lambda f=stdin: CloseableIterator(
                    # don't close stdin
                    lambda: None,
                    _generate_json_from_lines_iter(f)
                ),
            )

        for file in files:
            def create_file_iterator(f=file):
                # the file must live beyond this function call.
                # StreamingJsonInput closes it as a context manager via
                # CloseableIterator
                # pylint: disable-next=R1732:consider-using-with
                try:
                    opened_file = open(f, 'r')
                except OSError as e:
                    raise StreamingJsonError from e
                return CloseableIterator(
                    lambda f2=opened_file: f2.close(),
                    _generate_json_from_lines_iter(opened_file)
                )
            self.remaining_iterator_factories.append(create_file_iterator)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.current_iterator:
            self.current_iterator.close()

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next json object.
        Raises StreamingJsonException on any deserialization error, with
        __cause__ as the original Exception.
        """
        while True:
            if self.current_iterator is None:
                if not self.remaining_iterator_factories:
                    raise StopIteration
                factory = self.remaining_iterator_factories.popleft()
                self.current_iterator = factory()

            try:
                return next(self.current_iterator)
            except StopIteration:
                self.current_iterator.close()
                self.current_iterator = None


def _compile_query(query):
    """
    Compile the provided python code block into a function to transform json.

    Wrapping in a function allows the block to yield/yield from.

    The last statement, if an expression, will be converted into a return
    statement.  If the function does not return a generator this value will be
    used to serialize json.  If the function does return a generator, and so
    this value will be the "value" of the StopIteration exception, the value
    will later be discarded.

    Returns the compiled AST with the function named "_jello_function".  Any
    free variables must be supplied by placing in "globals" when calling exec.
    Once execed the function may be retrieved from the exec'ed "globals" and
    then called.
    """

    obj = ast.parse(query)
    body = obj.body
    if len(body) < 1:
        raise ValueError('No query found.')
    last_statement = body[-1]
    if isinstance(last_statement, ast.Expr):
        expression = last_statement.value
        return_expr = ast.Return(
            value=expression,
            lineno=last_statement.lineno,
            col_offset=last_statement.col_offset)
        body[-1] = return_expr

    function_def = ast.FunctionDef(
        name="_jello_function",
        args=ast.arguments(
            posonlyargs=[],
            args=[],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
        body=body,
        decorator_list=[],
        returns=None,
        type_comment=None,
        lineno=0,
        col_offset=0
    )
    m = ast.Module(
        body=(
            [function_def]
        ),
        type_ignores=[]
    )
    return compile(source=m, filename="<string>", mode="exec")


def _inialize_config_and_options(_, add_to_scope):
    # read initialization file to set colors, options, and user-defined functions
    jelloconf = ''
    conf_file = ''
    jcnf_dict = {}

    if opts.initialize:
        pyquery._ = _  # allows the data to be available to the initialization file

        if sys.platform.startswith('win32'):
            conf_file_dir = os.environ['APPDATA']
        else:
            conf_file_dir = os.environ["HOME"]

        try:
            conf_file = os.path.join(conf_file_dir, '.jelloconf.py')
            jelloconf = read_file(conf_file)

            # inject the data into the initialization module
            conf_prepend = 'from jello.lib import pyquery as __q__\n'
            conf_prepend += '_ = __q__._\n'
            jelloconf = conf_prepend + jelloconf

            # create and import the modified .jelloconf file as a normal module
            jcnf = types.ModuleType('jcnf')
            exec(jelloconf, jcnf.__dict__)
            jcnf_dict = {f: getattr(jcnf, f) for f in dir(jcnf) if not f.startswith('__')}

        except FileNotFoundError:
            raise FileNotFoundError(f'-i used and initialization file not found: {conf_file}')

    warn_options = False
    warn_colors = False

    for option in [opts.compact, opts.raw, opts.lines, opts.nulls, opts.force_color, opts.mono, opts.schema, opts.types]:
        if not isinstance(option, bool) and option is not None:
            opts.compact = opts.raw = opts.lines = opts.nulls = opts.force_color = opts.mono = opts.schema = opts.types = False
            warn_options = True

    for color_config in [opts.keyname_color, opts.keyword_color, opts.number_color, opts.string_color]:
        valid_colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'gray', 'brightblack',
                        'brightred', 'brightgreen', 'brightyellow', 'brightblue', 'brightmagenta', 'brightcyan',
                        'white']

        if color_config not in valid_colors and color_config is not None:
            opts.keyname_color = opts.keyword_color = opts.number_color = opts.string_color = None
            warn_colors = True

    if warn_options:
        warning_message([
            f'Options must be set to True or False in {conf_file}',
            'Unsetting all options.'
        ])

    if warn_colors:
        valid_colors_string = ', '.join(valid_colors)
        warning_message([
            f'Colors must be set to one of: {valid_colors_string} in {conf_file}',
            'Unsetting all colors.'
        ])

    # add any functions in initialization file to the scope
    scope = {'_': _, 'os': os}
    scope.update(jcnf_dict)
    if add_to_scope is not None:
        scope.update(add_to_scope)
    return jcnf_dict


def _convert_output(output):
    if not isinstance(output, collections.abc.Iterator):
        return _convert_single_output(output)

    def convert_lazily():
        for item in output:
            yield _convert_single_output(item)
    return convert_lazily()


def _convert_single_output(output):
    # convert output back to normal dict
    if isinstance(output, list):
        return [i.toDict() if isinstance(i, DotMap) else i for i in output]

    if isinstance(output, DotMap):
        return output.toDict()

    # if DotMap returns a bound function then we know it was a reserved attribute name
    if hasattr(output, '__self__'):
        raise ValueError('Reserved key name. Use bracket notation to access this key.')

    return output


def pyquery(data, query, add_to_scope=None):
    """Sets options and runs the user's query."""
    output = None

    # read data into '_' variable
    # if data is a list of dictionaries, then need to iterate through and convert all dictionaries to DotMap
    if isinstance(data, list):
        _ = [DotMap(i, _dynamic=False, _prevent_method_masking=True) if isinstance(i, dict)
             else i for i in data]

    elif isinstance(data, dict):
        _ = DotMap(data, _dynamic=False, _prevent_method_masking=True)

    elif isinstance(data, collections.abc.Iterator):
        _ = (DotMap(i, _dynamic=False, _prevent_method_masking=True) if isinstance(i, dict)
             else i for i in data)

    else:
        _ = data

    jcnf_dict = _inialize_config_and_options(_, add_to_scope)

    # add any functions in initialization file to the scope
    scope = {'_': _, 'os': os}
    scope.update(jcnf_dict)

    # run the query
    compiled = _compile_query(query)
    exec(compiled, scope)
    func = scope['_jello_function']

    output = func()
    output = _convert_output(output)

    return output


if __name__ == '__main__':
    pass
