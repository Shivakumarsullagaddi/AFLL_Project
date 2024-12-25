import ply.lex as lex

# List of token names - defining in lexer and sharing with parser
tokens = (
    'FUNCTION',
    'IF',
    'ELSE',
    'VAR',
    'LET',
    'RETURN',
    'CONST',
    'ID',
    'EQUALS',
    'SEMICOLON', 
    'NUMBER',
    'STRING',
    'LBRACKET',
    'RBRACKET',
    'LPAREN', 
    'RPAREN',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'PLUS',
    'GREATER',
    'IMPORT',
)

# Regular expression rules for simple tokens
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PLUS = r'\+'
t_GREATER = r'>'

# Keywords defined as functions to prevent conflicts with ID
def t_CONST(t):
    r'const'
    return t

def t_VAR(t):
    r'var'
    return t

def t_LET(t):
    r'let'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

# Regular expression for identifying numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regular expression for identifying strings
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove the double quotes
    return t

# Regular expression rule for identifiers (variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Characters to ignore (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build and return the lexer
def get_lexer():
    return lex.lex()

if __name__ == '__main__':
    # Test the lexer
    lexer = get_lexer()
    test_data = '''
    const z = 1;
    import math;
    function add(a, b) {
        return a + b;
    }
    '''
    lexer.input(test_data)
    
    # Tokenize and print each token
    print("Testing lexer with sample input:")
    for tok in lexer:
        print(f"Token: {tok.type}, Value: {tok.value}, Line: {tok.lineno}, Position: {tok.lexpos}")