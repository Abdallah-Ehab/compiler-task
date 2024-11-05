import re

symbol_table = [
    ("comment", r"//.*|/\*[\s\S]*?\*/$"),
    ("keyword", r"\bauto\b|\bbreak\b|\bcase\b|\bchar\b|\bconst\b|\bcontinue\b|\bdefault\b|\bdefault\b|\bdouble\b|\belse\b|\benum\b|\bextern\b|\bfloat\b|\bfor\b|\bgoto\b|\bif\b|\binline\b|\bint\b|\blong\b|\bregister\b|\brestrict\b|\breturn\b|\bshort\b|\bsigned\b|\bsizeof\b|\bstatic\b|\bstruct\b|\bswitch\b|\btypedef\b|\bunion\b|\bunsigned\b|\bvoid\b|\bvolatile\b|\bwhile\b|\b_Bool\b|\b_Complex\b|\b_Imaginary\b"),
    ("identifier", r"[_a-zA-Z][_a-zA-Z0-9]*"),
    ("String", r"\"[\w_&$-]*\""),
    ("float", r"\d+\.\d+"),
    ("int", r"\d+"),
    ("operator", r"\+{1,2}|-{1,2}|={1,2}|&{1,2}|\|{1,2}|!|\/|%|\*|<<|>>|<|>|<=|>=|==|!=|\^|\?|\:"),
    ("special_character", r"[(){};,\.\"\']"),
    ("new_line",r"\n"),
    ("white_space", r"\s+"),
    ("tab", r"\t"),
]

class Token:
    def __init__(self, lexeme, val, type, position):
        self.lexeme = lexeme
        self.val = val
        self.type = type
        self.position = position

    def __repr__(self):
        return f"Token(lexeme is {self.lexeme}, type={self.type}, val={self.val}, position={self.position})"

class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.position = 0

    def tokenize(self):
        tokens = []
        while self.position < len(self.text):
            match = False
            for type, pattern in symbol_table:
                regex = re.compile(pattern)
                matched = regex.match(self.text, self.position)
                if matched:
                    match = True
                    lexeme = self.text[matched.start():matched.end()]
                    if type == "float":
                        token = Token(lexeme, float(lexeme), type, self.position)
                    elif type == "int":
                        token = Token(lexeme, int(lexeme), type, self.position)
                    elif type in ["keyword", "identifier", "operator", "white_space", "comment","new_line","special_character"]:
                        token = Token(lexeme, None, type, self.position)
                    elif type == "string":
                        token = Token(lexeme, lexeme, type, self.position)

                    tokens.append(token)
                    self.position = matched.end()
                    break
            if not match:
                tokens.append(f"Unknown token at position {self.position} of value '{self.text[self.position]}'")
                self.position += 1
        return tokens


## to do parser: (to be continued) :



