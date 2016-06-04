from ply import lex, yacc

reserved = {
    'code': 'CODE',
    'tapes': 'TAPES',
    'write': 'WRITE',
    'move': 'MOVE',
    'state': 'STATE'
}

# Tokens
tokens = [
    'HYPHENS',
    'DOTS',
    'COLON',
    'ID',
    'STRING',
    'NUMBER',
    'INDENT',
    'DEDENT'
] + list(reserved.values())

t_HYPHENS   = r'---'
t_DOTS      = r'\.\.\.'
t_COLON     = r':'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_STRING(t):
    r"'.*?'"
    t.value = t.value.strip("'")
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


indent_stack = [0]

def t_newline(t):
    r'\n[ ]*'
    global indent_stack
    t.lexer.lineno += 1
    indent = len(t.value) - 1
    prev_indents = len(indent_stack)

    if indent_stack[prev_indents - 1] < indent:

        indent_stack.append(indent)
        t.type = 'INDENT'
        t.value = indent
        return t

    elif indent_stack[prev_indents - 1] > indent:

        if indent_stack[prev_indents - 2] >= indent:
            if indent_stack[prev_indents - 2] > indent:
                t.lexer.lexpos = t.lexpos
                t.lexer.lineno -= 1

            indent_stack.pop()
            t.type = 'DEDENT'
            t.value = indent_stack[prev_indents - 2]
            return t
        else:
            print('Indentation error')


t_ignore = ' '

def t_error(t):
    print('Illegal character "{}"'.format(t.value[0]))
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

input_file = open('testInput.txt', 'r')
lexer.input(input_file.read())
input_file.close()

for tok in lexer:
    print(tok)


def p_main_program(p):
    'main_program : HYPHENS code_section tapes_section DOTS'
    print(p)


def p_code_section(p):
    'code_section : CODE COLON INDENT state_list DEDENT'


def p_state_list(p):
    '''
    state_list : state_info
               | state_list state_info
    '''


def p_state_info(p):
    'state_info : ID COLON INDENT symbol_list DEDENT'


def p_symbol_list(p):
    '''
    symbol_list : symbol_info
                | symbol_list symbol_info
    '''


def p_symbol_info(p):
    '''
    symbol_info : STRING COLON INDENT write_stmt DEDENT
                | STRING COLON INDENT move_stmt DEDENT
                | STRING COLON INDENT state_stmt DEDENT
                | STRING COLON INDENT write_stmt move_stmt DEDENT
                | STRING COLON INDENT write_stmt state_stmt DEDENT
                | STRING COLON INDENT move_stmt state_stmt DEDENT
                | STRING COLON INDENT write_stmt move_stmt state_stmt DEDENT
    '''


def p_write_stmt(p):
    'write_stmt : WRITE COLON STRING'


def p_move_stmt(p):
    'move_stmt : MOVE COLON ID'


def p_state_stmt(p):
    'state_stmt : STATE COLON ID'


def p_tapes_section(p):
    'tapes_section : TAPES COLON INDENT tape_list DEDENT'


def p_tape_list(p):
    '''
    tape_list : tape_info
              | tape_list tape_info
    '''


def p_tape_info(p):
    'tape_info : NUMBER COLON STRING'


def p_error(t):
    print('Syntax error at "{}"'.format(t.value))


parser = yacc.yacc()
input_file = open('testInput.txt', 'r')
parser.parse(input_file.read())
input_file.close()
