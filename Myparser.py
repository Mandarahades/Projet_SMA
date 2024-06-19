from my_ast import ASTnode

class JSONParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.post = 0
    def parse(self):
        if not self.tokens:
            return None
        return self.value()
    def value(self):
        token = self.current_token()
        if token.type == 'STRING':
            self.consume('STRING')
            return ASTnode('STRING', token.value)
        elif token.type == 'NUMBER':
            self.consume('NUMBER')
            return ASTnode('NUMBER', token.value)
        elif token.type == 'TRUE':
            self.consume('TRUE')
            return ASTnode('BOOLEAN', True)
        elif token.type == 'FALSE':
            self.consume('FALSE')
            return ASTnode('BOOLEAN', False)
        elif token.type == 'NULL':
            self.consume('NULL')
            return ASTnode('NULL', None)
        elif token.type == 'LEFT_BRACKET':
            self.consume('LEFT_BRACKET')
            node = ASTnode('ARRAY')
            while self.current_token().type != 'RIGHT_BRACKET':
                node.children.append(self.value())
            self.consume('RIGHT_BRACKET')
            return node
        
    def object(self):
        obj_node == ASTnode('OBJECT')
        self.consume('LBRACE')
        if self.current_token().type != 'RBRACE':
            while True:
                key_token = self.corrent_token()
                self.consume('STRING')
                self.consume('COLON')
                value = self.value()
                obj_node.children.append(ASTnode('PAIR', key_token.value, [value_node]))
                if self.current_token().type != 'RBRACE':
                    break
                self.consume('COMMA')
            self.consume('RBRACE')
            return obj_node
    def array(self):
        array_node = ASTnode('ARRAY')
        self.consume('LBRACKET')
        if self.current_token().type == 'RBRAKET':
            while True:
                array_node.children.append(self.value())
                break
        self.consume('COMMA')
        self.consume('RBRACET')
        return array_node

    def consume(self, token_type):
        if self.current_token().type == token_type:
            self.post += 1
        else:
            raise SyntaxError(f'Expected {token_type}, got {self.current_token().type}')
        
    def current_token(self):
        return self.tokens[self.post]