# ************************ OBIN TOKENS*****************************
TT_ENDSTREAM = 0
TT_INT = 1
TT_FLOAT = 2
TT_STR = 3
TT_CHAR = 4
TT_NAME = 5
TT_NEWLINE = 6
TT_BREAK = 7
TT_CASE = 8
TT_CONTINUE = 9
TT_ELSE = 10
TT_FOR = 11
TT_WHILE = 12
TT_IF = 13
TT_WHEN = 14
TT_ELIF = 15
TT_OF = 16
TT_AS = 17
TT_MATCH = 18
TT_FUNC = 19
TT_AND = 20
TT_OR = 21
TT_NOT = 22
TT_TRUE = 23
TT_FALSE = 24
TT_NIL = 25
TT_UNDEFINED = 26
TT_TRY = 27
TT_THROW = 28
TT_CATCH = 29
TT_FINALLY = 30
TT_IN = 31
TT_IS = 32
TT_ORIGIN = 33
TT_ISNOT = 34
TT_OUTER = 35
TT_FROM = 36
TT_IMPORT = 37
TT_TRAIT = 38
TT_GENERIC = 39
TT_SPECIFY = 40
TT_END = 41
TT_RETURN = 42
TT_ELLIPSIS = 43
TT_ADD_ASSIGN = 44
TT_SUB_ASSIGN = 45
TT_MUL_ASSIGN = 46
TT_DIV_ASSIGN = 47
TT_MOD_ASSIGN = 48
TT_BITAND_ASSIGN = 49
TT_BITXOR_ASSIGN = 50
TT_BITOR_ASSIGN = 51
TT_WILDCARD = 52
TT_GOTO = 53
TT_RSHIFT = 54
TT_URSHIFT = 55
TT_LSHIFT = 56
TT_ARROW = 57
TT_FAT_ARROW = 58
TT_EQ = 59
TT_LE = 60
TT_GE = 61
TT_NE = 62
TT_SEMI = 63
TT_COLON = 64
TT_DOUBLE_COLON = 65
TT_LCURLY = 66
TT_RCURLY = 67
TT_COMMA = 68
TT_ASSIGN = 69
TT_LPAREN = 70
TT_RPAREN = 71
TT_LSQUARE = 72
TT_RSQUARE = 73
TT_DOT = 74
TT_DOUBLE_DOT = 75
TT_BITAND = 76
TT_BITNOT = 77
TT_BITOR = 78
TT_BITXOR = 79
TT_SUB = 80
TT_ADD = 81
TT_MUL = 82
TT_DIV = 83
TT_BACKTICK = 84
TT_MOD = 85
TT_LT = 86
TT_GT = 87
TT_UNKNOWN = 88
# ************************ OBIN TOKENS REPR *****************************
__TT_REPR__ = ["TT_ENDSTREAM", "TT_INT", "TT_FLOAT", "TT_STR", "TT_CHAR", "TT_NAME", "TT_NEWLINE", "TT_BREAK", "TT_CASE", "TT_CONTINUE", "TT_ELSE", "TT_FOR", "TT_WHILE", "TT_IF", "TT_WHEN", "TT_ELIF", "TT_OF", "TT_AS", "TT_MATCH", "TT_FUNC", "TT_AND", "TT_OR", "TT_NOT", "TT_TRUE", "TT_FALSE", "TT_NIL", "TT_UNDEFINED", "TT_TRY", "TT_THROW", "TT_CATCH", "TT_FINALLY", "TT_IN", "TT_IS", "TT_ORIGIN", "TT_ISNOT", "TT_OUTER", "TT_FROM", "TT_IMPORT", "TT_TRAIT", "TT_GENERIC", "TT_SPECIFY", "TT_END", "TT_RETURN", "TT_ELLIPSIS", "TT_ADD_ASSIGN", "TT_SUB_ASSIGN", "TT_MUL_ASSIGN", "TT_DIV_ASSIGN", "TT_MOD_ASSIGN", "TT_BITAND_ASSIGN", "TT_BITXOR_ASSIGN", "TT_BITOR_ASSIGN", "TT_WILDCARD", "TT_GOTO", "TT_RSHIFT", "TT_URSHIFT", "TT_LSHIFT", "TT_ARROW", "TT_FAT_ARROW", "TT_EQ", "TT_LE", "TT_GE", "TT_NE", "TT_SEMI", "TT_COLON", "TT_DOUBLE_COLON", "TT_LCURLY", "TT_RCURLY", "TT_COMMA", "TT_ASSIGN", "TT_LPAREN", "TT_RPAREN", "TT_LSQUARE", "TT_RSQUARE", "TT_DOT", "TT_DOUBLE_DOT", "TT_BITAND", "TT_BITNOT", "TT_BITOR", "TT_BITXOR", "TT_SUB", "TT_ADD", "TT_MUL", "TT_DIV", "TT_BACKTICK", "TT_MOD", "TT_LT", "TT_GT", "TT_UNKNOWN", ]


def token_type_to_str(ttype):
    return __TT_REPR__[ttype]