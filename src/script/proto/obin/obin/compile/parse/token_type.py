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
TT_DEF = 20
TT_VAR = 21
TT_LAZY = 22
TT_AND = 23
TT_OR = 24
TT_NOT = 25
TT_TRUE = 26
TT_FALSE = 27
TT_NIL = 28
TT_UNDEFINED = 29
TT_TRY = 30
TT_THROW = 31
TT_CATCH = 32
TT_FINALLY = 33
TT_IN = 34
TT_IS = 35
TT_ORIGIN = 36
TT_NOTIN = 37
TT_ISNOT = 38
TT_ISA = 39
TT_NOTA = 40
TT_OUTER = 41
TT_FROM = 42
TT_IMPORT = 43
TT_TRAIT = 44
TT_GENERIC = 45
TT_SPECIFY = 46
TT_END = 47
TT_RETURN = 48
TT_ELLIPSIS = 49
TT_WILDCARD = 50
TT_GOTO = 51
TT_RSHIFT = 52
TT_URSHIFT = 53
TT_LSHIFT = 54
TT_ARROW = 55
TT_FAT_ARROW = 56
TT_EQ = 57
TT_LE = 58
TT_GE = 59
TT_NE = 60
TT_SEMI = 61
TT_COLON = 62
TT_DOUBLE_COLON = 63
TT_LCURLY = 64
TT_RCURLY = 65
TT_COMMA = 66
TT_ASSIGN = 67
TT_LPAREN = 68
TT_RPAREN = 69
TT_LSQUARE = 70
TT_RSQUARE = 71
TT_DOT = 72
TT_DOUBLE_DOT = 73
TT_BITAND = 74
TT_BITNOT = 75
TT_BITOR = 76
TT_BITXOR = 77
TT_SUB = 78
TT_ADD = 79
TT_MUL = 80
TT_DIV = 81
TT_BACKTICK = 82
TT_MOD = 83
TT_LT = 84
TT_GT = 85
TT_UNKNOWN = 86
# ************************ OBIN TOKENS REPR *****************************
__TT_REPR__ = [u"TT_ENDSTREAM", u"TT_INT", u"TT_FLOAT", u"TT_STR", u"TT_CHAR", u"TT_NAME", u"TT_NEWLINE", u"TT_BREAK",
               u"TT_CASE", u"TT_CONTINUE", u"TT_ELSE", u"TT_FOR", u"TT_WHILE", u"TT_IF", u"TT_WHEN", u"TT_ELIF",
               u"TT_OF", u"TT_AS", u"TT_MATCH", u"TT_FUNC", u"TT_DEF", u"TT_VAR", u"TT_LAZY", u"TT_AND", u"TT_OR",
               u"TT_NOT", u"TT_TRUE", u"TT_FALSE", u"TT_NIL", u"TT_UNDEFINED", u"TT_TRY", u"TT_THROW", u"TT_CATCH",
               u"TT_FINALLY", u"TT_IN", u"TT_IS", u"TT_ORIGIN", u"TT_NOTIN", u"TT_ISNOT", u"TT_ISA", u"TT_NOTA",
               u"TT_OUTER", u"TT_FROM", u"TT_IMPORT", u"TT_TRAIT", u"TT_GENERIC", u"TT_SPECIFY", u"TT_END",
               u"TT_RETURN", u"TT_ELLIPSIS", u"TT_WILDCARD", u"TT_GOTO", u"TT_RSHIFT", u"TT_URSHIFT", u"TT_LSHIFT",
               u"TT_ARROW", u"TT_FAT_ARROW", u"TT_EQ", u"TT_LE", u"TT_GE", u"TT_NE", u"TT_SEMI", u"TT_COLON",
               u"TT_DOUBLE_COLON", u"TT_LCURLY", u"TT_RCURLY", u"TT_COMMA", u"TT_ASSIGN", u"TT_LPAREN", u"TT_RPAREN",
               u"TT_LSQUARE", u"TT_RSQUARE", u"TT_DOT", u"TT_DOUBLE_DOT", u"TT_BITAND", u"TT_BITNOT", u"TT_BITOR",
               u"TT_BITXOR", u"TT_SUB", u"TT_ADD", u"TT_MUL", u"TT_DIV", u"TT_BACKTICK", u"TT_MOD", u"TT_LT", u"TT_GT",
               u"TT_UNKNOWN", ]


def token_type_to_str(ttype):
    return __TT_REPR__[ttype]
