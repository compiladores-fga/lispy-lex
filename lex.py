import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

def createRegex():
    token_specification = [
        ('NUMBER', r'[-+]?\d+(\.\d*)?'),
        ('COMMA', r','),               
        ("STRING", r"\".*\""),
        ("QUOTE", r"[\'\"]"),
        ("NAME", r"[-+_\w\d\<\>\?\!\%\=\*\/\.]+"),  
        ("CHAR", r"#\\[\w]+"),
        ("LPAR", r"\("), 
        ("RPAR", r"\)"), 
        ("BOOL", r"#([fF]|[tT])"),
        ('MISMATCH', r'.'),            
    ]
    regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    return regex
        
def lex(stringInput: str) -> Iterable[Token]:
    
    stringInput = stringInput.split(";;", 1)[0]
    
    for token in re.finditer(createRegex(), stringInput):
        kind = token.lastgroup
        value = token.group()
        if kind != "MISMATCH":
            yield Token(kind, value)

            
