# ************************ OBIN NODES*****************************
NT_TRUE = 0
NT_FALSE = 1
NT_NIL = 2
NT_INT = 3
NT_FLOAT = 4
NT_STR = 5
NT_CHAR = 6
NT_WILDCARD = 7
NT_NAME = 8
NT_SYMBOL = 9
NT_MAP = 10
NT_LIST = 11
NT_TUPLE = 12
NT_UNIT = 13
NT_DEF = 14
NT_FUN = 15
NT_IF = 16
NT_WHEN = 17
NT_WHEN_NO_ELSE = 18
NT_MATCH = 19
NT_TRY = 20
NT_MODULE = 21
NT_IMPORT = 22
NT_EXPORT = 23
NT_LOAD = 24
NT_USE = 25
NT_TRAIT = 26
NT_GENERIC = 27
NT_SPECIFY = 28
NT_BIND = 29
NT_RETURN = 30
NT_THROW = 31
NT_BREAK = 32
NT_CONTINUE = 33
NT_FOR = 34
NT_WHILE = 35
NT_REST = 36
NT_ASSIGN = 37
NT_CALL = 38
NT_CALL_MEMBER = 39
NT_LOOKUP = 40
NT_LOOKUP_SYMBOL = 41
NT_SLICE = 42
NT_RANGE = 43
NT_MODIFY = 44
NT_OF = 45
NT_AS = 46
NT_VAR = 47
NT_LAZY = 48
NT_AND = 49
NT_OR = 50
NT_OPERATOR = 51
NT_GOTO = 52
# ************************ OBIN NODES REPR *****************************
__NT_REPR__ = ["NT_TRUE", "NT_FALSE", "NT_NIL", "NT_INT", "NT_FLOAT", "NT_STR", "NT_CHAR", "NT_WILDCARD", "NT_NAME",
               "NT_SYMBOL", "NT_MAP", "NT_LIST", "NT_TUPLE", "NT_UNIT", "NT_DEF", "NT_FUN", "NT_IF", "NT_WHEN",
               "NT_WHEN_NO_ELSE", "NT_MATCH", "NT_TRY", "NT_MODULE", "NT_IMPORT", "NT_EXPORT", "NT_LOAD", "NT_USE",
               "NT_TRAIT", "NT_GENERIC", "NT_SPECIFY", "NT_BIND", "NT_RETURN", "NT_THROW", "NT_BREAK", "NT_CONTINUE",
               "NT_FOR", "NT_WHILE", "NT_REST", "NT_ASSIGN", "NT_CALL", "NT_CALL_MEMBER", "NT_LOOKUP",
               "NT_LOOKUP_SYMBOL", "NT_SLICE", "NT_RANGE", "NT_MODIFY", "NT_OF", "NT_AS", "NT_VAR", "NT_LAZY", "NT_AND",
               "NT_OR", "NT_OPERATOR", "NT_GOTO", ]


def node_type_to_str(ttype):
    return __NT_REPR__[ttype]
