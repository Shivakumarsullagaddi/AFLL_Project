from lexer import get_lexer
from parser import get_parser

# Test data
test_data = '''
imprt math;
function add(a, b) {
    return a + b;
}
var arr = [1, 2, 3, 4, 5];
'''

# Get lexer and parser
lexer = get_lexer()
parser = get_parser()

# Parse and print the result
result = parser.parse(test_data, lexer=lexer)
print("\nParsed Result:")
print(result)