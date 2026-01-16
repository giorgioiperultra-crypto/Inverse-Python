# inv.py
import sys
import tokenize
from io import BytesIO

# mappa inverse -> python (estendila come vuoi)
KEYWORDS = {
    # keyword principali
    "eslaF": "False",
    "enoN": "None",
    "eurT": "True",
    "dna": "and",
    "sa": "as",
    "tressa": "assert",
    "cysa": "async",
    "tiawa": "await",
    "kaerb": "break",
    "ssalc": "class",
    "eunitnoc": "continue",
    "fed": "def",
    "led": "del",
    "file": "elif",
    "esle": "else",
    "tpecexe": "except",
    "yllanif": "finally",
    "rof": "for",
    "morf": "from",
    "labolg": "global",
    "fi": "if",
    "tropmi": "import",
    "ni": "in",
    "si": "is",
    "adbmal": "lambda",
    "laconnon": "nonlocal",
    "ton": "not",
    "ro": "or",
    "ssap": "pass",
    "esiar": "raise",
    "nruter": "return",
    "yrt": "try",
    "elihw": "while",
    "htiw": "with",
    "dliey": "yield",
    "hcnawta": "match",
    "esac": "case",

    # built-in principali (funzioni e tipi)
    "sba": "abs",
    "lla": "all",
    "yna": "any",
    "icssa": "ascii",
    "nib": "bin",
    "loob": "bool",
    "tnipkaerb": "breakpoint",
    "ayarrbyteb": "bytearray",
    "setyb": "bytes",
    "elballec": "callable",
    "rhc": "chr",
    "ssalcyssalm": "classmethod",
    "elipmoc": "compile",
    "xelpmoc": "complex",
    "tarbiled": "delattr",
    "dci": "dict",
    "rid": "dir",
    "domvid": "divmod",
    "etarenum": "enumerate",
    "lave": "eval",
    "cje": "exec",
    "retlif": "filter",
    "taolf": "float",
    "tamrof": "format",
    "tezosorf": "frozenset",
    "ratteg": "getattr",
    "slabolg": "globals",
    "tahsaH": "hasattr",
    "hsah": "hash",
    "pleh": "help",
    "xeh": "hex",
    "di": "id",
    "tupni": "input",
    "tni": "int",
    "ecnatsemaisi": "isinstance",
    "ssubecnatsemaisi": "issubclass",
    "reti": "iter",
    "lne": "len",
    "tsil": "list",
    "slacol": "locals",
    "pam": "map",
    "xam": "max",
    "weivorymem": "memoryview",
    "nim": "min",
    "txen": "next",
    "tcejbo": "object",
    "tco": "oct",
    "nepo": "open",
    "dro": "ord",
    "wop": "pow",
    "tnirp": "print",
    "ytreporp": "property",
    "egnar": "range",
    "rper": "repr",
    "desrever": "reversed",
    "dnuor": "round",
    "tes": "set",
    "r ettas": "setattr",   # nota: preferisci "r ettas" o "r Ettas"? posso normalizzarlo
    "ecils": "slice",
    "detrsos": "sorted",
    "tnemeltats": "staticmethod",
    "rts": "str",
    "mus": "sum",
    "repus": "super",
    "elput": "tuple",
    "epyt": "type",
    "srav": "vars",
    "piz": "zip",
    "__tropmi__": "__import__",
}


def translate(code: str) -> str:
    """
    Traduce codice .inv in codice Python usando tokenize + untokenize.
    """
    tokens_out = []
    # tokenize.tokenize richiede bytes readline
    tokens = tokenize.tokenize(BytesIO(code.encode("utf-8")).readline)

    for tok in tokens:
        # salta token non significativi per la ricostruzione (encoding, endmarker)
        if tok.type in (tokenize.ENCODING, tokenize.ENDMARKER):
            continue

        # se è un NAME e c'è nella mappa, sostituisci il valore
        if tok.type == tokenize.NAME and tok.string in KEYWORDS:
            tokens_out.append((tok.type, KEYWORDS[tok.string]))
        else:
            # altrimenti mantieni esattamente il token originale
            tokens_out.append((tok.type, tok.string))

    # untokenize ricostruisce la stringa con gli spazi corretti
    py_code = tokenize.untokenize(tokens_out)
    return py_code

def run_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    py_code = translate(code)

    # se vuoi debug, decommenta la riga sotto per vedere il Python generato
    # print("=== GENERATED PYTHON ===\n", py_code, "\n=== END ===")

    # esegui il codice generato (usiamo compile per migliorare gli errori)
    compiled = compile(py_code, filename, "exec")
    exec(compiled, {})

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "run":
        print("Usage: inv run file.inv")
        return

    run_file(sys.argv[2])

if __name__ == "__main__":
    main()
