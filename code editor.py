import customtkinter as ctk
import re
from main import Tokenizer


def get_tokens():
    text_content = text_widget.get("1.0", "end-1c")
    tokenizer = Tokenizer(text_content)
    return tokenizer.tokenize()

def display_tokens():

    tokens = get_tokens()
    output.delete("1.0","end-1c")
    for token in tokens:
        output.insert("end",f"{token}\n")
    print(f"tokens:{tokens}")



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Simple Text Editor with Syntax Highlighting")
root.geometry("500x400")


keywords = re.compile(
    r"\bauto\b|\bbreak\b|\bcase\b|\bchar\b|\bconst\b|\bcontinue\b|\bdefault\b|\bdefault\b|\bdouble\b|\belse\b|\benum\b|\bextern\b|\bfloat\b|\bfor\b|\bgoto\b|\bif\b|\binline\b|\bint\b|\blong\b|\bregister\b|\brestrict\b|\breturn\b|\bshort\b|\bsigned\b|\bsizeof\b|\bstatic\b|\bstruct\b|\bswitch\b|\btypedef\b|\bunion\b|\bunsigned\b|\bvoid\b|\bvolatile\b|\bwhile\b|\b_Bool\b|\b_Complex\b|\b_Imaginary\b")
operator_pattern = re.compile(r"\+{1,2}|-{1,2}|={1,2}|&{1,2}|\|{1,2}|!|\/|%|\*|<<|>>|<|>|<=|>=|==|!=|\^|\?|\:")
identifier_pattern = re.compile(r"[_a-zA-Z][_a-zA-Z0-9]*")
comment_pattern = re.compile(r"//.*|/\*[\s\S]*?\*/$")



def highlight_syntax(event=None):

    text_widget.tag_remove("keyword", "1.0", "end")
    text_widget.tag_remove("identifier", "1.0", "end")
    text_widget.tag_remove("operator", "1.0", "end")
    text_widget.tag_remove("comment", "1.0", "end")


    text_content = text_widget.get("1.0", "end-1c")


    for match in keywords.finditer(text_content):
        start_idx = f"1.0 + {match.start()} chars"
        end_idx = f"1.0 + {match.end()} chars"
        text_widget.tag_add("keyword", start_idx, end_idx)

    for match in identifier_pattern.finditer(text_content):
        if keywords.fullmatch(match.group()) is None:
            start_idx = f"1.0 + {match.start()} chars"
            end_idx = f"1.0 + {match.end()} chars"
            text_widget.tag_add("identifier", start_idx, end_idx)


    for match in operator_pattern.finditer(text_content):
        start_idx = f"1.0 + {match.start()} chars"
        end_idx = f"1.0 + {match.end()} chars"
        text_widget.tag_add("operator", start_idx, end_idx)
    for match in comment_pattern.finditer(text_content):
        start_idx = f"1.0 + {match.start()} chars"
        end_idx = f"1.0 + {match.end()} chars"
        text_widget.tag_add("comment", start_idx, end_idx)

text_widget = ctk.CTkTextbox(root, wrap="word", font=("Consolas", 12), undo=True)
text_widget.pack(expand=True, fill="both", padx=10, pady=10)
text_widget.tag_config("keyword", foreground="#ADD8E6")
text_widget.tag_config("operator", foreground="#006400")
text_widget.tag_config("identifier", foreground="#FF8C00")
text_widget.tag_config("comment", foreground="#cdffcd")

run_button = ctk.CTkButton(master=root, text="run", command=display_tokens).pack()

output = ctk.CTkTextbox(master=root, wrap="word", font=("Consolas", 12), undo=False)
output.pack(expand=True, fill="both", padx=10, pady=10)

text_widget.bind("<KeyRelease>", highlight_syntax)


root.mainloop()


