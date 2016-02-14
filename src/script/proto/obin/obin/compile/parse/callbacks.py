from obin.compile.parse.basic import *
from obin.compile.parse.node_type import *
from obin.compile.parse import nodes
from obin.compile.parse.nodes import (node_token as __ntok, node_0, node_1, node_2, node_3)
from obin.types import space
from obin.misc import strutil

NODE_TYPE_MAPPING = {
    TT_DOT: NT_LOOKUP_SYMBOL,
    TT_TRUE: NT_TRUE,
    TT_FALSE: NT_FALSE,
    TT_NIL: NT_NIL,
    TT_INT: NT_INT,
    TT_FLOAT: NT_FLOAT,
    TT_STR: NT_STR,
    TT_CHAR: NT_CHAR,
    TT_WILDCARD: NT_WILDCARD,
    TT_NAME: NT_NAME,
    TT_DEF: NT_DEF,
    TT_IF: NT_IF,
    TT_WHEN: NT_WHEN,
    TT_MATCH: NT_MATCH,
    TT_IMPORT: NT_IMPORT,
    TT_EXPORT: NT_EXPORT,
    TT_USE: NT_USE,
    TT_LOAD: NT_LOAD,
    TT_TRAIT: NT_TRAIT,
    TT_GENERIC: NT_GENERIC,
    TT_SPECIFY: NT_SPECIFY,
    TT_RETURN: NT_RETURN,
    TT_THROW: NT_THROW,
    TT_BREAK: NT_BREAK,
    TT_CONTINUE: NT_CONTINUE,
    TT_FOR: NT_FOR,
    TT_WHILE: NT_WHILE,
    TT_ELLIPSIS: NT_REST,
    TT_ASSIGN: NT_ASSIGN,
    TT_OF: NT_OF,
    TT_AS: NT_AS,
    TT_AND: NT_AND,
    TT_OR: NT_OR,
    TT_DOUBLE_DOT: NT_RANGE,
    TT_SHARP: NT_SYMBOL,
    TT_OPERATOR: NT_NAME,
}


def __ntype(node):
    node_type = NODE_TYPE_MAPPING[nodes.node_token_type(node)]
    return node_type


def _init_default_current_0(parser):
    return nodes.node_0(__ntype(parser.node), __ntok(parser.node))


##############################################################
# INFIX
##############################################################

#
def led_infix(parser, op, node, left):
    # TODO CHECK IF THIS CYCLE IS STILL NEEDED
    exp = None
    while exp is None:
        exp = expression(parser, op.lbp)

    return node_2(__ntype(node), __ntok(node), left, exp)


def led_infixr(parser, op, node, left):
    exp = expression(parser, op.lbp - 1)
    return node_2(__ntype(node), __ntok(node), left, exp)


def prefix_nud_function(parser, op, node):
    exp = literal_expression(parser)
    return nodes.create_call_node_name(node, op.prefix_function, [exp])


def led_infix_function(parser, op, node, left):
    exp = None
    while exp is None:
        exp = expression(parser, op.lbp)

    return nodes.create_call_node_name(node, op.infix_function, [left, exp])


def led_infixr_function(parser, op, node, left):
    exp = expression(parser, op.lbp - 1)
    return nodes.create_call_node_name(node, op.infix_function, [left, exp])


def led_infixr_assign(parser, op, node, left):
    ltype = nodes.node_token_type(left)

    if ltype != TT_DOT and ltype != TT_LSQUARE \
            and ltype != TT_NAME and ltype != TT_LCURLY and ltype != TT_LPAREN:
        parse_error(parser, u"Bad lvalue in assignment", left)

    if ltype == TT_LPAREN and nodes.node_arity(left) != 1:
        parse_error(parser, u"Bad lvalue in assignment, wrong tuple destructuring", left)

    if ltype == TT_LCURLY and nodes.node_arity(left) == 0:
        parse_error(parser, u"Bad lvalue in assignment, empty map", left)

    exp = expression(parser, 9)

    return node_2(__ntype(node), __ntok(node), left, exp)


def infix_when(parser, op, node, left):
    first = condition(parser)
    advance_expected(parser, TT_ELSE)
    exp = expression(parser, 0)
    return node_3(NT_WHEN, __ntok(node), first, left, exp)


def infix_dot(parser, op, node, left):
    check_token_type(parser, TT_NAME)
    symbol = _init_default_current_0(parser)
    advance(parser)
    return node_2(NT_LOOKUP_SYMBOL, __ntok(node), left, symbol)


def infix_lcurly(parser, op, node, left):
    items = []
    if parser.token_type != TT_RCURLY:
        while True:
            # TODO check it
            check_token_types(parser, [TT_NAME, TT_SHARP, TT_INT, TT_STR, TT_CHAR, TT_FLOAT])
            # WE NEED LBP=10 TO OVERRIDE ASSIGNMENT LBP(9)
            key = expression(parser, 10)

            advance_expected(parser, TT_ASSIGN)
            value = expression(parser, 0)

            items.append(nodes.list_node([key, value]))

            if parser.token_type != TT_COMMA:
                break

            advance_expected(parser, TT_COMMA)

    advance_expected(parser, TT_RCURLY)
    return node_2(NT_MODIFY, __ntok(node), left, nodes.list_node(items))


def infix_lsquare(parser, op, node, left):
    exp = expression(parser, 0)
    advance_expected(parser, TT_RSQUARE)
    return node_2(NT_LOOKUP, __ntok(node), left, exp)


def infix_simple_pair(parser, op, node, left):
    check_token_type(parser, TT_NAME)
    name = _init_default_current_0(parser)
    advance(parser)
    return node_2(__ntype(node), __ntok(node), left, name)


def infix_lparen(parser, op, node, left):
    items = []
    if parser.token_type != TT_RPAREN:
        while True:
            items.append(expression(parser, 0))
            if parser.token_type != TT_COMMA:
                break

            advance_expected(parser, TT_COMMA)

    advance_expected(parser, TT_RPAREN)

    if nodes.node_token_type(left) == TT_DOT:
        return node_3(NT_CALL_MEMBER, __ntok(node),
                      nodes.node_first(left),
                      nodes.node_second(left),
                      nodes.list_node(items))
    else:
        return node_2(NT_CALL, __ntok(node), left, nodes.list_node(items))


def infix_at(parser, op, node, left):
    ltype = nodes.node_token_type(left)
    if ltype != TT_NAME:
        parse_error(parser, u"Bad lvalue in pattern binding", left)

    exp = expression(parser, 9)
    return node_2(NT_BIND, __ntok(node), left, exp)


##############################################################
# INFIX
##############################################################


def prefix_nud(parser, op, node):
    exp = literal_expression(parser)
    return node_1(__ntype(node), __ntok(node), exp)


def itself(parser, op, node):
    return node_0(__ntype(node), __ntok(node))


def _parse_name(parser):
    if parser.token_type == TT_SHARP:
        node = parser.node
        advance(parser)
        return _parse_symbol(parser, node)

    check_token_types(parser, [TT_STR, TT_NAME])
    node = parser.node
    advance(parser)
    return node_0(__ntype(node), __ntok(node))


def _parse_symbol(parser, node):
    check_token_types(parser, [TT_NAME, TT_STR, TT_OPERATOR])
    exp = node_0(__ntype(parser.node), __ntok(parser.node))
    advance(parser)
    return node_1(__ntype(node), __ntok(node), exp)


def prefix_sharp(parser, op, node):
    return _parse_symbol(parser, node)


def prefix_backtick(parser, op, node):
    val = strutil.cat_both_ends(nodes.node_value_s(node))
    if not val:
        return parse_error(parser, u"invalid variable name", node)
    return nodes.create_name_node(node, val)


# def prefix_sharp(parser, op, node):
#     check_token_types(parser, [TT_NAME, TT_STR, TT_OPERATOR])
#     if parser.token_type == TT_OPERATOR:
#         exp = node_0(NT_NAME, __ntok(parser.node))
#         advance(parser)
#     else:
#         exp = literal_expression(parser)
#         check_node_types(parser, exp, [NT_NAME, NT_STR])
#
#     return node_1(__ntype(node), __ntok(node), exp)


def symbol_wildcard(parser, op, node):
    return parse_error(parser, u"Invalid use of _ pattern", node)


def prefix_if(parser, op, node):
    branches = []

    cond = prefix_condition(parser)
    body = statements(parser, TERM_IF)

    branches.append(nodes.list_node([cond, body]))
    check_token_types(parser, TERM_IF)

    while parser.token_type == TT_ELIF:
        advance_expected(parser, TT_ELIF)

        cond = prefix_condition(parser)
        body = statements(parser, TERM_IF)

        branches.append(nodes.list_node([cond, body]))
        check_token_types(parser, TERM_IF)

    advance_expected(parser, TT_ELSE)
    body = statements(parser, TERM_BLOCK)
    branches.append(nodes.list_node([nodes.empty_node(), body]))
    advance_end(parser)

    return node_1(NT_IF, __ntok(node), nodes.list_node(branches))


# separate lparen handle for match case declarations
def prefix_lparen_tuple(parser, op, node):
    if parser.token_type == TT_RPAREN:
        advance_expected(parser, TT_RPAREN)
        return nodes.create_unit_node(node)

    items = []
    while True:
        exp = expression(parser, 0)
        items.append(exp)
        if parser.token_type != TT_COMMA:
            break

        advance_expected(parser, TT_COMMA)

    advance_expected(parser, TT_RPAREN)
    return node_1(NT_TUPLE, __ntok(node), nodes.list_node(items))


def prefix_lparen(parser, op, node):
    if parser.token_type == TT_RPAREN:
        advance_expected(parser, TT_RPAREN)
        return nodes.create_unit_node(node)

    e = expression(parser, 0)
    if parser.token_type != TT_COMMA:
        advance_expected(parser, TT_RPAREN)
        return e

    items = [e]
    advance_expected(parser, TT_COMMA)

    if parser.token_type != TT_RPAREN:
        while True:
            items.append(expression(parser, 0))
            if parser.token_type != TT_COMMA:
                break

            advance_expected(parser, TT_COMMA)

    advance_expected(parser, TT_RPAREN)
    return node_1(NT_TUPLE, __ntok(node), nodes.list_node(items))


def prefix_lsquare(parser, op, node):
    items = []
    if parser.token_type != TT_RSQUARE:
        while True:
            items.append(expression(parser, 0))
            if parser.token_type != TT_COMMA:
                break

            advance_expected(parser, TT_COMMA)

    advance_expected(parser, TT_RSQUARE)
    return node_1(NT_LIST, __ntok(node), nodes.list_node(items))


def on_bind_node(parser, key):
    if nodes.node_type(key) != NT_NAME:
        parse_error(parser, u"Invalid bind name", key)

    advance_expected(parser, TT_AT_SIGN)
    real_key, value = _parse_map_key_pair(parser, [TT_NAME, TT_SHARP, TT_STR], None)

    # allow syntax like {var1@ key}
    if nodes.node_type(real_key) == NT_NAME:
        real_key = nodes.create_symbol_node(real_key, real_key)

    bind_key = nodes.create_bind_node(key, key, real_key)
    return bind_key, value


# this callback used in pattern matching
def prefix_lcurly_patterns(parser, op, node):
    return _prefix_lcurly(parser, op, node, [TT_NAME, TT_SHARP, TT_STR], on_bind_node)


def prefix_lcurly(parser, op, node):
    return _prefix_lcurly(parser, op, node, [TT_NAME, TT_SHARP, TT_INT, TT_STR, TT_CHAR, TT_FLOAT], None)


def _parse_map_key_pair(parser, types, on_unknown):
    check_token_types(parser, types)
    # WE NEED LBP=10 TO OVERRIDE ASSIGNMENT LBP(9)
    key = expression(parser, 10)

    if parser.token_type == TT_COMMA:
        value = nodes.empty_node()
    elif parser.token_type == TT_RCURLY:
        value = nodes.empty_node()
    elif parser.token_type == TT_ASSIGN:
        advance_expected(parser, TT_ASSIGN)
        value = expression(parser, 0)
    else:
        if on_unknown is None:
            parse_error(parser, u"Invalid map declaration syntax", parser.node)
        key, value = on_unknown(parser, key)

    return key, value


def _prefix_lcurly(parser, op, node, types, on_unknown):
    # on_unknown used for pattern_match in binds {NAME @ name = "Alice"}
    items = []
    if parser.token_type != TT_RCURLY:
        while True:
            # TODO check it
            key, value = _parse_map_key_pair(parser, types, on_unknown)
            items.append(nodes.list_node([key, value]))

            if parser.token_type != TT_COMMA:
                break

            advance_expected(parser, TT_COMMA)

    advance_expected(parser, TT_RCURLY)
    return node_1(NT_MAP, __ntok(node), nodes.list_node(items))


FUN_NAME_TERMINATORS = [TT_LPAREN, TT_CASE, TT_ARROW]


def parse_function(parser, can_has_empty_name):
    if parser.token_type in FUN_NAME_TERMINATORS:
        if can_has_empty_name is True:
            name = nodes.empty_node()
        else:
            return parse_error(parser, u"Expected function name", parser.node)
    else:
        name = terminated_expression(parser.name_parser, 0, FUN_NAME_TERMINATORS)

    funcs = []
    pattern_parser = parser.pattern_parser

    if parser.token_type == TT_CASE:
        while pattern_parser.token_type == TT_CASE:
            advance_expected(pattern_parser, TT_CASE)
            args = expression(pattern_parser, 0)
            args_type = nodes.node_type(args)
            if args_type != NT_UNIT and args_type != NT_TUPLE:
                parse_error(parser, u"Invalid  syntax in function arguments", args)

            advance_expected(parser, TT_ARROW)
            body = statements(parser, TERM_CASE)
            funcs.append(nodes.list_node([args, body]))
    else:
        if parser.token_type == TT_ARROW:
            args = nodes.create_unit_node(parser.node)
        else:
            args = expression(pattern_parser, 0)

        advance_expected(parser, TT_ARROW)
        body = statements(parser, TERM_BLOCK)
        funcs.append(nodes.list_node([args, body]))

    advance_end(parser)
    return name, nodes.list_node(funcs)


def prefix_def(parser, op, node):
    name, funcs = parse_function(parser.expression_parser, False)
    return node_2(NT_DEF, __ntok(node), name, funcs)


def prefix_fun(parser, op, node):
    name, funcs = parse_function(parser, True)
    return node_2(NT_FUN, __ntok(node), name, funcs)


def prefix_try(parser, op, node):
    endofexpression(parser)
    trybody = statements(parser, TERM_TRY)

    advance_expected(parser, TT_CATCH)
    check_token_type(parser, TT_NAME)
    varname = expression(parser, 0)
    catchstmts = statements(parser, TERM_CATCH)
    catchbody = nodes.list_node([varname, catchstmts])
    if parser.token_type == TT_FINALLY:
        advance_expected(parser, TT_FINALLY)
        finallybody = statements(parser, TERM_BLOCK)
    else:
        finallybody = nodes.empty_node()

    advance_end(parser)
    return node_3(NT_TRY, __ntok(node), trybody, catchbody, finallybody)


def prefix_match(parser, op, node):
    exp = expression(parser, 0)

    pattern_parser = parser.pattern_parser
    branches = []
    while pattern_parser.token_type == TT_CASE:
        advance_expected(pattern_parser, TT_CASE)
        pattern = expression(pattern_parser, 0)
        advance_expected(parser, TT_ARROW)

        body = statements(parser, TERM_CASE)

        branches.append(nodes.list_node([pattern, body]))

    advance_end(parser)

    if len(branches) == 0:
        parse_error(parser, u"Empty match expression", node)

    return node_2(NT_MATCH, __ntok(node), exp, nodes.list_node(branches))


def stmt_single(parser, op, node):
    exp = expression(parser, 0)
    endofexpression(parser)
    return node_1(__ntype(node), __ntok(node), exp)


def stmt_loop_flow(parser, op, node):
    endofexpression(parser)
    if parser.token_type not in LOOP_CONTROL_TOKENS:
        parse_error(parser, u"Unreachable statement", node)
    return node_0(__ntype(node), __ntok(node))


def stmt_while(parser, op, node):
    cond = prefix_condition(parser)
    stmts = statements(parser, TERM_BLOCK)
    advance_end(parser)
    return node_2(NT_WHILE, __ntok(node), cond, stmts)


def stmt_for(parser, op, node):
    # set big lbp to overriding IN binding power
    variables = [literal_expression(parser)]
    while parser.token_type == TT_COMMA:
        advance(parser)
        if parser.token_type != TT_NAME:
            parse_error(parser, u"Wrong variable name in for loop", node)

        variables.append(expression(parser, 0))

    vars = nodes.list_node(variables)
    advance_expected(parser, TT_IN)
    exp = expression(parser, 0)
    # CALL endofexpression for one line for i in 1..2; i end
    endofexpression(parser)

    stmts = statements(parser, TERM_BLOCK)

    advance_end(parser)
    return node_3(NT_FOR, __ntok(node), vars, exp, stmts)


def stmt_when(parser, op, node):
    cond = prefix_condition(parser)
    body = statements(parser, TERM_BLOCK)
    advance_end(parser)
    return node_2(NT_WHEN_NO_ELSE, __ntok(node), cond, body)


###############################################################
# MODULE STATEMENTS
###############################################################

def parse_specify_fn(_parser, _signature_parser):
    signature = []

    advance_expected(_parser, TT_LPAREN)
    while _parser.token_type != TT_RPAREN:
        sig = expression(_signature_parser, 0)
        signature.append(sig)

        if _parser.token_type != TT_COMMA:
            break

        advance_expected(_signature_parser, TT_COMMA)

    advance_expected(_parser, TT_RPAREN)
    advance_expected(_parser, TT_ARROW)

    body = statements(_parser, TERM_CASE)
    return nodes.list_node([nodes.list_node(signature), body])


def parse_specify_funcs(parser):
    generic_signature_parser = parser.generic_signature_parser
    funcs = []
    if parser.token_type == TT_LPAREN:
        func = parse_specify_fn(parser.expression_parser, generic_signature_parser)
        funcs.append(func)
        advance_end(parser)
    else:
        # advance_expected(parser, TT_COLON)
        while parser.token_type == TT_CASE:
            advance_expected(generic_signature_parser, TT_CASE)
            func = parse_specify_fn(parser.expression_parser, generic_signature_parser)
            funcs.append(func)

        advance_end(parser)

    if len(funcs) == 0:
        parse_error(parser, u"Empty specify statement", parser.node)

    return nodes.list_node(funcs)


def stmt_specify(parser, op, node):
    # name = closed_expression(parser.name_parser, 0)
    name = terminated_expression(parser.name_parser, 0, [TT_CASE, TT_LPAREN])
    check_node_types(parser, name, [NT_SYMBOL, NT_NAME, NT_LOOKUP_SYMBOL, NT_LOOKUP])

    check_token_types(parser, [TT_CASE, TT_LPAREN])
    # name = _parse_name(parser)
    # check_node_types(parser, name, [NT_SYMBOL, NT_NAME])

    funcs = parse_specify_funcs(parser)
    return node_2(NT_SPECIFY, __ntok(node), name, funcs)


def stmt_module(parser, op, node):
    name = literal_terminated_expression(parser)
    check_node_type(parser, name, NT_NAME)
    stmts = statements(parser, TERM_BLOCK)
    advance_end(parser)
    return node_2(NT_MODULE, __ntok(node), name, stmts)


def stmt_generic(parser, op, node):
    # name = literal_expression(parser.name_parser)
    # name = _parse_name(parser)
    name = terminated_expression(parser.name_parser, 0, [TT_CASE, TT_LPAREN])
    check_node_types(parser, name, [NT_SYMBOL, NT_NAME])

    if parser.token_type == TT_CASE or parser.token_type == TT_LPAREN:
        funcs = parse_specify_funcs(parser)
        return node_2(NT_GENERIC, __ntok(node), name, funcs)
    else:
        return node_1(NT_GENERIC, __ntok(node), name)


def trait_name(parser):
    check_token_type(parser, TT_NAME)
    exp = expression(parser, 0)
    if nodes.node_type(exp) != NT_NAME:
        parse_error(parser, u"Invalid trait name", parser.node)
    return exp


def stmt_trait(parser, op, node):
    names = [trait_name(parser)]
    while parser.token_type == TT_COMMA:
        advance_expected(parser, TT_COMMA)
        names.append(trait_name(parser))

    return node_1(NT_TRAIT, __ntok(node), nodes.list_node(names))


def stmt_load(parser, op, node):
    imported = expression(parser.load_parser, 0)
    return node_1(NT_LOAD, __ntok(node), imported)


def symbol_or_name_value(parser, name):
    if nodes.node_type(name) == NT_SYMBOL:
        data = nodes.node_first(name)
        if nodes.node_type(data) == NT_NAME:
            return nodes.node_value(data)
        elif nodes.node_type(data) == NT_STR:
            return strutil.unquote_w(nodes.node_value(data))
        else:
            assert False, "Invalid symbol"
    elif nodes.node_type(name) == NT_NAME:
        return nodes.node_value(name)
    else:
        assert False, "Invalid name"


def stmt_module_at(parser, op, node):
    """
    @infixl(#+, ___add, 10)
    @infixr(#::, ___cons, 10)
    @prefix(#+, ___unary_plus)
    """
    check_token_type(parser, TT_NAME)
    type_node = parser.node
    advance(parser)
    if nodes.node_value_s(type_node) == "prefix":
        return _meta_prefix(parser, node)
    elif nodes.node_value_s(type_node) == "infixl":
        return _meta_infix(parser, node, led_infix_function)
    elif nodes.node_value_s(type_node) == "infixr":
        return _meta_infix(parser, node, led_infixr_function)
    else:
        return parse_error(parser, u"Invalid operator type expected infixl, infixr or prefix", parser.node)


def _meta_infix(parser, node, infix_function):
    options_tuple = expression(parser.name_parser, 0)
    check_node_type(parser, options_tuple, NT_TUPLE)
    options = nodes.node_first(options_tuple)
    if api.length_i(options) != 3:
        return parse_error(parser, u"Invalid prefix operator options", parser.node)
    op_node = options[0]
    func_node = options[1]
    precedence_node = options[2]
    check_node_type(parser, op_node, NT_NAME)
    check_node_types(parser, func_node, [NT_NAME, NT_SYMBOL])
    check_node_type(parser, precedence_node, NT_INT)

    op_value = symbol_or_name_value(parser, op_node)
    func_value = symbol_or_name_value(parser, func_node)
    try:
        precedence = strutil.string_to_int(nodes.node_value_s(precedence_node))
    except:
        return parse_error(parser, u"Invalid infix operator precedence", precedence_node)

    op = parser_current_scope_find_operator_or_create_new(parser, op_value)
    op = operator_infix(op, precedence, infix_function, func_value)
    endofexpression(parser)
    parser_current_scope_add_operator(parser, op_value, op)


def _meta_prefix(parser, node):
    options_tuple = expression(parser.name_parser, 0)
    check_node_type(parser, options_tuple, NT_TUPLE)
    options = nodes.node_first(options_tuple)
    if api.length_i(options) != 2:
        return parse_error(parser, u"Invalid prefix operator options", parser.node)
    op_node = options[0]
    func_node = options[1]
    check_node_type(parser, op_node, NT_NAME)
    check_node_types(parser, func_node, [NT_NAME, NT_SYMBOL])

    op_value = symbol_or_name_value(parser, op_node)
    func_value = symbol_or_name_value(parser, func_node)

    op = parser_current_scope_find_operator_or_create_new(parser, op_value)
    op = operator_prefix(op, prefix_nud_function, func_value)

    endofexpression(parser)
    parser_current_scope_add_operator(parser, op_value, op)


