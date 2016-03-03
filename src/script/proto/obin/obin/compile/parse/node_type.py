# ************************ OBIN NODES*****************************
NT_GOTO = 0
NT_TRUE = 1
NT_FALSE = 2
NT_NIL = 3
NT_INT = 4
NT_FLOAT = 5
NT_STR = 6
NT_CHAR = 7
NT_WILDCARD = 8
NT_NAME = 9
NT_SYMBOL = 10
NT_UNION = 11
NT_TYPE = 12
NT_MAP = 13
NT_LIST = 14
NT_TUPLE = 15
NT_UNIT = 16
NT_COMMA = 17
NT_FUN = 18
NT_FENV = 19
NT_CONDITION = 20
NT_TERNARY_CONDITION = 21
NT_WHEN = 22
NT_MATCH = 23
NT_TRY = 24
NT_MODULE = 25
NT_IMPORT = 26
NT_IMPORT_HIDING = 27
NT_IMPORT_FROM = 28
NT_IMPORT_FROM_HIDING = 29
NT_EXPORT = 30
NT_LOAD = 31
NT_TRAIT = 32
NT_IMPLEMENT = 33
NT_GENERIC = 34
NT_SPECIFY = 35
NT_BIND = 36
NT_RETURN = 37
NT_THROW = 38
NT_BREAK = 39
NT_CONTINUE = 40
NT_FOR = 41
NT_WHILE = 42
NT_REST = 43
NT_ASSIGN = 44
NT_CALL = 45
NT_JUXTAPOSITION = 46
NT_CALL_MEMBER = 47
NT_LOOKUP = 48
NT_LOOKUP_SYMBOL = 49
NT_LOOKUP_MODULE = 50
NT_SLICE = 51
NT_RANGE = 52
NT_MODIFY = 53
NT_OF = 54
NT_AS = 55
NT_VAR = 56
NT_LAZY = 57
NT_AND = 58
NT_OR = 59
# ************************ OBIN NODES REPR *****************************
__NT_REPR__ = ["NT_GOTO", "NT_TRUE", "NT_FALSE", "NT_NIL", "NT_INT", "NT_FLOAT", "NT_STR", "NT_CHAR", "NT_WILDCARD",
               "NT_NAME", "NT_SYMBOL", "NT_UNION", "NT_TYPE", "NT_MAP", "NT_LIST", "NT_TUPLE", "NT_UNIT", "NT_COMMA",
               "NT_FUN", "NT_FENV", "NT_CONDITION", "NT_TERNARY_CONDITION", "NT_WHEN", "NT_MATCH", "NT_TRY",
               "NT_MODULE", "NT_IMPORT", "NT_IMPORT_HIDING", "NT_IMPORT_FROM", "NT_IMPORT_FROM_HIDING", "NT_EXPORT",
               "NT_LOAD", "NT_TRAIT", "NT_IMPLEMENT", "NT_GENERIC", "NT_SPECIFY", "NT_BIND", "NT_RETURN", "NT_THROW",
               "NT_BREAK", "NT_CONTINUE", "NT_FOR", "NT_WHILE", "NT_REST", "NT_ASSIGN", "NT_CALL", "NT_JUXTAPOSITION",
               "NT_CALL_MEMBER", "NT_LOOKUP", "NT_LOOKUP_SYMBOL", "NT_LOOKUP_MODULE", "NT_SLICE", "NT_RANGE",
               "NT_MODIFY", "NT_OF", "NT_AS", "NT_VAR", "NT_LAZY", "NT_AND", "NT_OR", ]


def node_type_to_str(ttype):
    return __NT_REPR__[ttype]
