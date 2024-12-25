import ply.yacc as yacc
from lexer import tokens  # Import tokens from lexer.py

# Parser rules
start = 'program'

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                 | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment
                | import_declaration
                | function_declaration
                | if_statement
                | array_declaration
                | return_statement
                | variable_declaration
                | SEMICOLON'''
    p[0] = p[1]

def p_variable_declaration(p):
    '''variable_declaration : VAR ID EQUALS expression SEMICOLON
                          | LET ID EQUALS expression SEMICOLON
                          | CONST ID EQUALS expression SEMICOLON'''
    p[0] = ('variable_declaration', p[1], p[2], p[4])
    print(f"Valid JavaScript {p[1]} declaration")

def p_assignment(p):
    '''assignment : ID EQUALS expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])
    print("Valid JavaScript Assignment")

def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON'''
    p[0] = ('return', p[2])
    print("Valid JavaScript return statement")

def p_import_declaration(p):
    '''import_declaration : IMPORT ID SEMICOLON'''
    p[0] = ('import_declaration', p[2])
    print("Valid JavaScript import declaration")

def p_expression(p):
    '''expression : NUMBER
                 | STRING
                 | ID
                 | binary_expression'''
    p[0] = p[1]

def p_binary_expression(p):
    '''binary_expression : expression GREATER expression
                       | expression PLUS expression'''
    p[0] = ('binary_op', p[2], p[1], p[3])

def p_function_declaration(p):
    '''function_declaration : FUNCTION ID LPAREN parameters RPAREN LBRACE statements RBRACE'''
    p[0] = ('function_declaration', p[2], p[4], p[7])
    print("Valid JavaScript function declaration")

def p_parameters(p):
    '''parameters : ID COMMA parameters
                 | ID
                 | '''
    if len(p) == 1:  # empty parameters
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    p[0] = ('if_statement', p[3], p[6], p[10])
    print("Valid JavaScript if statement")

def p_array_declaration(p):
    '''array_declaration : VAR ID EQUALS LBRACKET array_values RBRACKET SEMICOLON
                       | LET ID EQUALS LBRACKET array_values RBRACKET SEMICOLON
                       | CONST ID EQUALS LBRACKET array_values RBRACKET SEMICOLON'''
    p[0] = ('array_declaration', p[1], p[2], p[5])
    print("Valid JavaScript Array declaration")

def p_array_values(p):
    '''array_values : expression COMMA array_values
                   | expression
                   | '''
    if len(p) == 1:  # empty array
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Error handling rule
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

def get_parser():
    return yacc.yacc()

