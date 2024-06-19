from lexer import JSONLexer
from my_ast import ASTnode
from Myparser import JSONParser

def main():
    file_path = './index.Json'
    with open(file_path, 'r') as file:
        text = file.read()
    
    lexer = JSONLexer(text)
    tokens = lexer.tokenize()
    
    parser = JSONParser(tokens)
    ast = parser.parse()
    
    print("Abstract Syntax Tree (AST):")
    print(ast)
    



    
if __name__ == '__main__':
    main()