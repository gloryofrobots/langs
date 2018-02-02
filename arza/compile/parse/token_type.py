# ************************ OBIN TOKENS*****************************
TT_ENDSTREAM = 0
TT_INT = 1
TT_FLOAT = 2
TT_STR = 3
TT_MULTI_STR = 4
TT_CHAR = 5
TT_NAME = 6
TT_TICKNAME = 7
TT_TYPENAME = 8
TT_OPERATOR = 9
TT_VOID = 10
TT_FUN = 11
TT_MATCH = 12
TT_WITH = 13
TT_CASE = 14
TT_BREAK = 15
TT_CONTINUE = 16
TT_WHILE = 17
TT_DEF = 18
TT_DEF_PLUS = 19
TT_TYPE = 20
TT_IF = 21
TT_ELIF = 22
TT_ELSE = 23
TT_THEN = 24
TT_WHEN = 25
TT_OF = 26
TT_LET = 27
TT_IN = 28
TT_IS = 29
TT_AS = 30
TT_NOT = 31
TT_AND = 32
TT_OR = 33
TT_TRUE = 34
TT_FALSE = 35
TT_TRY = 36
TT_THROW = 37
TT_CATCH = 38
TT_FINALLY = 39
TT_MODULE = 40
TT_IMPORT = 41
TT_FROM = 42
TT_HIDING = 43
TT_HIDE = 44
TT_EXPORT = 45
TT_USE = 46
TT_TRAIT = 47
TT_FOR = 48
TT_INTERFACE = 49
TT_DESCRIBE = 50
TT_END = 51
TT_END_EXPR = 52
TT_NEWLINE = 53
TT_INDENT = 54
TT_DEDENT = 55
TT_INFIXL = 56
TT_INFIXR = 57
TT_PREFIX = 58
TT_ELLIPSIS = 59
TT_WILDCARD = 60
TT_GOTO = 61
TT_ARROW = 62
TT_FAT_ARROW = 63
TT_BACKARROW = 64
TT_DISPATCH = 65
TT_AT_SIGN = 66
TT_DOLLAR = 67
TT_SHARP = 68
TT_JUXTAPOSITION = 69
TT_LCURLY = 70
TT_RCURLY = 71
TT_COMMA = 72
TT_ASSIGN = 73
TT_INFIX_DOT_LCURLY = 74
TT_INFIX_DOT_LSQUARE = 75
TT_LPAREN = 76
TT_RPAREN = 77
TT_LSQUARE = 78
TT_RSQUARE = 79
TT_DOT = 80
TT_COLON = 81
TT_DOUBLE_COLON = 82
TT_TRIPLE_COLON = 83
TT_DOUBLE_DOT = 84
TT_BACKTICK_NAME = 85
TT_BACKTICK_OPERATOR = 86
TT_UNKNOWN = 87
# ************************ OBIN TOKENS REPR *****************************
__TT_REPR__ = [u"TT_ENDSTREAM", u"TT_INT", u"TT_FLOAT", u"TT_STR", u"TT_MULTI_STR", u"TT_CHAR", u"TT_NAME",
               u"TT_TICKNAME", u"TT_TYPENAME", u"TT_OPERATOR", u"TT_VOID", u"TT_FUN", u"TT_MATCH", u"TT_WITH",
               u"TT_CASE", u"TT_BREAK", u"TT_CONTINUE", u"TT_WHILE", u"TT_DEF", u"TT_DEF_PLUS", u"TT_TYPE", u"TT_IF",
               u"TT_ELIF", u"TT_ELSE", u"TT_THEN", u"TT_WHEN", u"TT_OF", u"TT_LET", u"TT_IN", u"TT_IS", u"TT_AS",
               u"TT_NOT", u"TT_AND", u"TT_OR", u"TT_TRUE", u"TT_FALSE", u"TT_TRY", u"TT_THROW", u"TT_CATCH",
               u"TT_FINALLY", u"TT_MODULE", u"TT_IMPORT", u"TT_FROM", u"TT_HIDING", u"TT_HIDE", u"TT_EXPORT", u"TT_USE",
               u"TT_TRAIT", u"TT_FOR", u"TT_INTERFACE", u"TT_DESCRIBE", u"TT_END", u"TT_END_EXPR", u"TT_NEWLINE",
               u"TT_INDENT", u"TT_DEDENT", u"TT_INFIXL", u"TT_INFIXR", u"TT_PREFIX", u"TT_ELLIPSIS", u"TT_WILDCARD",
               u"TT_GOTO", u"TT_ARROW", u"TT_FAT_ARROW", u"TT_BACKARROW", u"TT_DISPATCH", u"TT_AT_SIGN", u"TT_DOLLAR",
               u"TT_SHARP", u"TT_JUXTAPOSITION", u"TT_LCURLY", u"TT_RCURLY", u"TT_COMMA", u"TT_ASSIGN",
               u"TT_INFIX_DOT_LCURLY", u"TT_INFIX_DOT_LSQUARE", u"TT_LPAREN", u"TT_RPAREN", u"TT_LSQUARE",
               u"TT_RSQUARE", u"TT_DOT", u"TT_COLON", u"TT_DOUBLE_COLON", u"TT_TRIPLE_COLON", u"TT_DOUBLE_DOT",
               u"TT_BACKTICK_NAME", u"TT_BACKTICK_OPERATOR", u"TT_UNKNOWN", ]


def token_type_to_u(ttype):
    return __TT_REPR__[ttype]


def token_type_to_s(ttype):
    return str(__TT_REPR__[ttype])
