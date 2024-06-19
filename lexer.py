import re

class JSONToken:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f'Token({self.type}, {self.value})'
    
class JSONLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.token_specs = [
            ('NUMBER', r'\d+'),
            ('STRING', r'"[^"]*"'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('LBRACKET', r'\['),
            ('RBRACKET', r'\]'),
            ('COMMA', r','),
            ('COLON', r':'),
            ('TRUE', r'true'),
            ('FALSE', r'false'),
            ('NULL', r'null'),
            ('EOF', r'$'),
            ('SKIP', r'[ \t\n\r]+'),
            ('MISMATCH', r'.'),
            ('COMMENT', r'//[^\n]*'),
            ('COMMENT', r'/\*[^*]*\*+(?:[^*/][^*]*\*+)*/'),
            ('COMMENT', r'/\*(.|\n)*?\*/'),
            ('COMMENT', r'/\*(.|\n)*?\*/'),
            
        ]
    def tokenize(self):
        for mo in re.finditer('|'.join('(?P<%s>%s)' % pair for pair in self.token_specs), self.source_code):
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind == 'STRING':
                value = value[1:-1]
            elif kind == 'NUMBER':
                            value = float(value) if '.' in value or 'e' in value or 'E' in value else int(value)
            elif kind == 'TRUE':
                value = True
            elif kind == 'FALSE':
                value = False
            elif kind == 'NULL':
                value = None
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Unexpected token {value}')
            self.tokens.append(JSONToken(kind, value))
        return self.tokens 