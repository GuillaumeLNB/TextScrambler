#!/usr/bin/env python3
import html

zwj = html.unescape("&zwj;")
nzwj = html.unescape("&zwnj;")
zwsp = html.unescape("&#8203;")
rlm = html.unescape("&rlm;")
rlm = html.unescape("&rlm;")
nvts = html.unescape("&NegativeVeryThinSpace;")
ensp = html.unescape("&ensp;")

invisible_chars = [zwj, nzwj]
# invisible_chars += [rlm, rlm]
# invisible_chars += [ensp]
# invisible_chars += [zwsp] #can be seen on LibreOffice
# invisible_chars += [nvts]

# the dictionnary keys are in Latin
# Greek
dic_latin_2_greek = {
    "A": "Α",  # alpha
    "B": "Β",  # beta
    "E": "Ε",  # epsilon
    "Z": "Ζ",  # zeta
    "H": "Η",  # Eta
    "Ι": "I",  # Iota
    "Κ": "K",  # kappa
    "M": "Μ",  # mu
    "N": "Ν",  # nu
    "O": "Ο",  # omicron
    "P": "Ρ",  # rho
    "T": "Τ",  # tau
    "Y": "Υ",  # op_silon
    "X": "Χ",  # chi
    "o": "ο",  # omicron
    "F": "Ϝ",  # wau
    "j": "ϳ",  # yot
    "C": "Ϲ",  # Sigma
}

# Cyrillic
dic_latin_2_cyrillic = {
    "A": "А",
    "B": "В",
    "E": "Е",
    "S": "Ѕ",
    "I": "І",
    "J": "Ј",
    "K": "К",
    "M": "М",
    "H": "Н",
    "O": "О",
    "P": "Р",
    "C": "С",
    "T": "Т",
    "X": "Х",
    "s": "ѕ",
    "p": "р",
    "e": "е",
    "a": "а",
    "x": "х",
    "o": "о",
    "j": "ј",
    "i": "і",
    "c": "с",
}

dict_latin = {k: [v] for k, v in dic_latin_2_greek.items()}

for k, v in dic_latin_2_cyrillic.items():
    if k not in dict_latin:
        dict_latin[k] = []
    dict_latin[k].append(v)


dic_digits = {
    "1": html.unescape("&#120823;"),  # MATHEMATICAL MONOSPACE DIGIT
    "2": html.unescape("&#120824;"),  # MATHEMATICAL MONOSPACE DIGIT
    "3": html.unescape("&#120825;"),  # MATHEMATICAL MONOSPACE DIGIT
    "4": html.unescape("&#120826;"),  # MATHEMATICAL MONOSPACE DIGIT
    "5": html.unescape("&#120827;"),  # MATHEMATICAL MONOSPACE DIGIT
    "6": html.unescape("&#120828;"),  # MATHEMATICAL MONOSPACE DIGIT
    "7": html.unescape("&#120829;"),  # MATHEMATICAL MONOSPACE DIGIT
    "8": html.unescape("&#120830;"),  # MATHEMATICAL MONOSPACE DIGIT
    "9": html.unescape("&#120831;"),  # MATHEMATICAL MONOSPACE DIGIT
    "0": html.unescape("&#120822;"),  # MATHEMATICAL MONOSPACE DIGIT
}

# using unicode confusable letters (http://www.unicode.org/Public/security/revision-03/confusablesSummary.txt)
