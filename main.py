import re


symbol_table = [
    ("keyword", r"\bauto\b|\bbreak\b|\bcase\b|\bchar\b|\bconst\b|\bcontinue\b|\bdefault\b|\bdefault\b|\bdouble\b|\belse\b|\benum\b|\bextern\b|\bfloat\b|\bfor\b|\bgoto\b|\bif\b|\binline\b|\bint\b|\blong\b|\bregister\b|\brestrict\b|\breturn\b|\bshort\b|\bsigned\b|\bsizeof\b|\bstatic\b|\bstruct\b|\bswitch\b|\btypedef\b|\bunion\b|\bunsigned\b|\bvoid\b|\bvolatile\b|\bwhile\b|\b_Bool\b|\b_Complex\b|\b_Imaginary\b"),  
    ("identifier", r"[_a-zA-Z][_a-zA-Z0-9]*"),
    ("String",r"\"[\w_&$-]*\""),
    ("float", r"\d+\.\d+"),
    ("int", r"\d+"),
    ("operator", r"\+{1,2}|-{1,2}|={1,2}|&{1,2}|\|{1,2}|!|\/|%|\*|<<|>>|<|>|<=|>=|==|!=|\^|\?|\:"),
    ("special_character", r"[(){};,.\"\']"),
    ("white_space", r"\s+"),
    ("tab",r"\t"),
    ("comment",r"//[^\n]*") #ً Wait for `//` and take ALL characters except for the newline.
]


def make_pattern():
    pattern = "|".join(pattern for _, pattern in symbol_table)
    regex = re.compile(pattern)
    return regex


def tokenize(text):
    position = 0
    tokens = []

    while position < len(text):
        matched = False

        
        for name, pattern in symbol_table:
            regex = re.compile(pattern)
            matched_obj = regex.match(text, position)

            if matched_obj:
                matched = True
                
                if name not in ["white_space","tab"]:
                    tokens.append((name, matched_obj.group(0)))
                position = matched_obj.end()  
                break  

        if not matched:
            print(f"unexpected word at position {position} of value '{text[position]}'")
            position += 1 

    return tokens

