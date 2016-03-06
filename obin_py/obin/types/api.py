__author__ = 'gloryofrobots'
# TODO REMOVE UNNECESSARRY ASSERTS OR REPLACE THEM WITH DEBUG MODE

from obin.types import space
from obin.runtime import error


# *************************
# type conversions
# **************************************
# PYTHON TYPES
def to_u(obj):
    return unicode(obj._to_string_())


def to_i(obj):
    return obj._to_integer_()


def to_f(obj):
    return obj._to_float_()


def to_s(obj):
    s = obj._to_string_()
    assert isinstance(s, str)
    return s


def to_b(obj):
    if obj is space.w_True:
        return True
    elif obj is space.w_False:
        return False

    error.throw_2(error.Errors.TYPE, space.newstring(u"Bool expected"), obj)


def to_string(obj):
    s = obj._to_string_()
    assert isinstance(s, str)
    return space.newstring(unicode(s))


def to_integer(obj):
    return space.newint(obj._to_integer_())


def to_float(obj):
    return space.newfloat(obj._to_float_())


def to_bool(obj):
    return space.newbool(to_b(obj))


"""
collection stuff
"""


def delete(obj, k):
    assert not space.isvoid(k)
    return obj._delete_(k)


def at(obj, k):
    assert not space.isvoid(k)
    v = obj._at_(k)
    assert v is not None
    if space.isvoid(v):
        return error.throw_2(error.Errors.KEY_ERROR, k, obj)
    return v


def lookup(obj, k, default):
    v = obj._at_(k)
    assert v is not None
    if space.isvoid(v):
        return default
    return v


def slice(obj, start, end):
    v = obj._slice_(start, end)
    assert v is not None
    if space.isvoid(v):
        return error.throw_3(error.Errors.SLICE, obj, start, end)
    return v


def is_empty(obj):
    return space.newbool(is_empty_b(obj))


def is_empty_b(obj):
    return obj._length_() == 0


def contains_index_b(obj, i):
    assert space.isint(i)

    l = length_i(obj)
    if i > 0 and i < l:
        return True
    return False


def contains(obj, k):
    return space.newbool(contains_b(obj, k))


def contains_b(obj, k):
    assert not space.isvoid(k)
    v = obj._contains_(k)
    assert isinstance(v, bool)
    return v


def notin(k, obj):
    return space.newbool(not contains_b(obj, k))


def put(obj, k, v):
    assert not space.isvoid(v)
    assert not space.isvoid(k)
    return obj._put_(k, v)


def at_index(obj, i):
    assert isinstance(i, int)
    v = obj._at_index_(i)
    return v


def get_index(obj, k):
    return obj._get_index_(k)


def put_at_index(obj, i, v):
    assert isinstance(i, int)
    return obj._put_at_index_(i, v)


def length(obj):
    return space.newint(length_i(obj))


def length_i(obj):
    return obj._length_()


def isempty(obj):
    return obj._length_() == 0


def iterator(obj):
    return obj._iterator_()


"""
Traits
"""


def get_type(process, obj):
    return obj._type_(process)


def traits(process, obj):
    b = get_type(process, obj)
    return b.traits


def kindof(process, obj, trait):
    return space.newbool(kindof_b(process, obj, trait))


def kindof_b(process, obj, kind):
    if space.istrait(kind):
        return traitof_b(process, obj, kind)
    elif space.isdatatype(kind):
        return typeof_b(process, obj, kind)
    else:
        return error.throw_3(error.Errors.TYPE, obj, kind, space.newstring(u"Wrong kindof argument"))


def traitof(process, obj, trait):
    return traitof_b(process, obj, trait)


def traitof_b(process, obj, trait):
    if not space.istrait(trait):
        return error.throw_2(error.Errors.TYPE, trait, space.newstring(u"Trait expected"))

    obj_type = get_type(process, obj)
    return obj_type.implements_trait(trait)


def typeof(process, obj, _type):
    return typeof_b(process, obj, _type)


def typeof_b(process, obj, _type):
    from obin.types import datatype
    if not space.isdatatype(_type):
        return error.throw_2(error.Errors.TYPE, _type, space.newstring(u"Datatype expected"))

    # if Nothing kindof Nothing
    if space.isdatatype(obj) and space.isdatatype(_type):
        if equal_b(obj, _type):
            return True

    obj_type = get_type(process, obj)
    return datatype.can_coerce(obj_type, _type)


"""
basic
"""


def hash_i(obj):
    return obj._hash_()


def clone(obj):
    c = obj._clone_()
    return c


def is_(obj, other):
    return space.newbool(obj is other)


def not_(obj):
    return space.newbool(not to_b(obj))


def isnot(obj, other):
    return space.newbool(obj is not other)


def equal(obj, other):
    res = equal_b(obj, other)
    return space.newbool(res)


def equal_b(obj, other):
    v = obj._equal_(other)
    return v


def not_equal(obj, other):
    v = obj._equal_(other)
    return space.newbool(not v)


def compare(process, obj, other):
    if space.isuniquetype(obj):
        return error.throw_2(error.Errors.TYPE, obj, space.newstring(u"Unique expected"))

    v = obj._compare_(other)

    return space.newint(v)


def next(obj):
    return obj._next_()


"""
Callable
"""


def call(process, obj, args):
    assert space.istuple(args)
    return obj._call_(process, args)


def to_routine(obj, stack, args):
    assert space.istuple(args)
    return obj._to_routine_(stack, args)


"""
put helpers
"""


def put_symbol(process, obj, k, v):
    put(obj, space.newsymbol(process, k), v)


def put_native_function(process, obj, name, func, arity):
    put_symbol(process, obj, name, space.newnativefunc(space.newsymbol(process, name), func, arity))