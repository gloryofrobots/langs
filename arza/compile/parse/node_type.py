# ************************ OBIN NODES*****************************
NT_GOTO = 0
NT_TRUE = 1
NT_FALSE = 2
NT_VOID = 3
NT_INT = 4
NT_FLOAT = 5
NT_STR = 6
NT_MULTI_STR = 7
NT_CHAR = 8
NT_WILDCARD = 9
NT_NAME = 10
NT_TEMPORARY = 11
NT_SYMBOL = 12
NT_TYPE = 13
NT_MAP = 14
NT_LIST = 15
NT_TUPLE = 16
NT_UNIT = 17
NT_CONS = 18
NT_COMMA = 19
NT_CASE = 20
NT_LITERAL = 21
NT_FUN = 22
NT_DEF = 23
NT_DEF_PLUS = 24
NT_USE = 25
NT_LAMBDA = 26
NT_DISPATCH = 27
NT_FARGS = 28
NT_CONDITION = 29
NT_WHEN = 30
NT_MATCH = 31
NT_TRY = 32
NT_MODULE = 33
NT_IMPORT = 34
NT_IMPORT_HIDING = 35
NT_IMPORT_FROM = 36
NT_IMPORT_FROM_HIDING = 37
NT_EXPORT = 38
NT_LOAD = 39
NT_TRAIT = 40
NT_EXTEND = 41
NT_GENERIC = 42
NT_METHOD = 43
NT_INTERFACE = 44
NT_DESCRIBE = 45
NT_BIND = 46
NT_THROW = 47
NT_REST = 48
NT_ASSIGN = 49
NT_CALL = 50
NT_JUXTAPOSITION = 51
NT_UNDEFINE = 52
NT_LOOKUP = 53
NT_IMPORTED_NAME = 54
NT_HEAD = 55
NT_TAIL = 56
NT_DROP = 57
NT_RANGE = 58
NT_MODIFY = 59
NT_OF = 60
NT_IS_IMPLEMENTED = 61
NT_AS = 62
NT_DELAY = 63
NT_LET = 64
NT_NOT = 65
NT_AND = 66
NT_OR = 67
NT_END_EXPR = 68
NT_END = 69
# ************************ OBIN NODES REPR *****************************
__NT_REPR__ = ["NT_GOTO", "NT_TRUE", "NT_FALSE", "NT_VOID", "NT_INT", "NT_FLOAT", "NT_STR", "NT_MULTI_STR", "NT_CHAR",
               "NT_WILDCARD", "NT_NAME", "NT_TEMPORARY", "NT_SYMBOL", "NT_TYPE", "NT_MAP", "NT_LIST", "NT_TUPLE",
               "NT_UNIT", "NT_CONS", "NT_COMMA", "NT_CASE", "NT_LITERAL", "NT_FUN", "NT_DEF", "NT_DEF_PLUS", "NT_USE",
               "NT_LAMBDA", "NT_DISPATCH", "NT_FARGS", "NT_CONDITION", "NT_WHEN", "NT_MATCH", "NT_TRY", "NT_MODULE",
               "NT_IMPORT", "NT_IMPORT_HIDING", "NT_IMPORT_FROM", "NT_IMPORT_FROM_HIDING", "NT_EXPORT", "NT_LOAD",
               "NT_TRAIT", "NT_EXTEND", "NT_GENERIC", "NT_METHOD", "NT_INTERFACE", "NT_DESCRIBE", "NT_BIND", "NT_THROW",
               "NT_REST", "NT_ASSIGN", "NT_CALL", "NT_JUXTAPOSITION", "NT_UNDEFINE", "NT_LOOKUP", "NT_IMPORTED_NAME",
               "NT_HEAD", "NT_TAIL", "NT_DROP", "NT_RANGE", "NT_MODIFY", "NT_OF", "NT_IS_IMPLEMENTED", "NT_AS",
               "NT_DELAY", "NT_LET", "NT_NOT", "NT_AND", "NT_OR", "NT_END_EXPR", "NT_END", ]


def node_type_to_s(ntype):
    return __NT_REPR__[ntype]