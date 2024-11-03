import re


symbol_table = [
    ("keyword", r"\bif\b|\bwhile\b|\bfor\b|\bswitch\b|\bcase\b|\bint\b|\bdouble\b|\bprint\b"),  
    ("identifier", r"[\w_]+"),
    ("String",r"\"[\w_&$-]*\""),
    ("float", r"\d+\.\d+"),
    ("int", r"\d+"),
    ("operator", r"\+{1,2}|-{1,2}|={1,2}|&{1,2}|\|{1,2}|!"),
    ("special_character", r"[(){};,.\"\']"),
    ("white_space", r"\s+"),
    ("tab",r"\t"),
    ("comment",r"//|/\*.*?\*/$")
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

