import math

from obin.objects.space import _w, isint, newint, newbool
from obin.runtime.exception import ObinTypeError, ObinReferenceError
from obin.objects import api
from obin.objects.types.value import W_String, W_Integer, W_Float
from obin.objects.space import _w, isint, isstring, isfloat, newbool, newint, newfloat
from rpython.rlib.rarithmetic import ovfcheck, intmask
from rpython.rlib.rfloat import isnan, isinf
from rpython.rlib.objectmodel import specialize
from obin.builtins.number_builtins import w_NAN, w_POSITIVE_INFINITY, w_NEGATIVE_INFINITY
from rpython.rlib import jit
from obin.utils import tb


def plus(r, lprim, rprim):
    if isstring(lprim) or isstring(rprim):
        sleft = api.to_native_string(lprim)
        sright = api.to_native_string(rprim)
        return W_String(sleft + sright)
    # hot path
    if isint(lprim) and isint(rprim):
        ileft = api.to_native_integer(lprim)
        iright = api.to_native_integer(rprim)
        try:
            return newint(ovfcheck(ileft + iright))
        except OverflowError:
            return newfloat(float(ileft) + float(iright))
    else:
        fleft = api.to_native_float(lprim)
        fright = api.to_native_float(rprim)
        return newfloat(fleft + fright)


def sub(r, nleft, nright):
    if isint(nleft) and isint(nright):
        ileft = api.to_native_integer(nleft)
        iright = api.to_native_integer(nright)
        try:
            return newint(ovfcheck(ileft - iright))
        except OverflowError:
            return newfloat(float(ileft) - float(iright))

    fleft = api.to_native_float(nleft)
    fright = api.to_native_float(nright)
    return newfloat(fleft - fright)


def mult(r, nleft, nright):
    if isint(nleft) and isint(nright):
        ileft = api.to_native_integer(nleft)
        iright = api.to_native_integer(nright)
        try:
            return newint(ovfcheck(ileft * iright))
        except OverflowError:
            return newfloat(float(ileft) * float(iright))

    fleft = api.to_native_float(nleft)
    fright = api.to_native_float(nright)
    return newfloat(fleft * fright)


def mod(r, w_left, w_right):
    fleft = api.to_native_float(w_left)
    fright = api.to_native_float(w_right)

    if isnan(fleft) or isnan(fright):
        return w_NAN

    if isinf(fright) or fright == 0:
        return w_NAN

    if isinf(fright):
        return w_left

    if fleft == 0:
        return w_left

    return newfloat(math.fmod(fleft, fright))


def sign(x):
    from math import copysign
    return copysign(1.0, x)


def sign_of(a, b):
    sign_a = sign(a)
    sign_b = sign(b)
    return sign_a * sign_b


def w_signed_inf(sign):
    if sign < 0.0:
        return w_NEGATIVE_INFINITY
    return w_POSITIVE_INFINITY


# 11.5.2
def division(r, nleft, nright):
    fleft = api.to_native_float(nleft)
    fright = api.to_native_float(nright)
    if isnan(fleft) or isnan(fright):
        return w_NAN

    if isinf(fleft) and isinf(fright):
        return w_NAN

    if isinf(fleft) and fright == 0:
        s = sign_of(fleft, fright)
        return w_signed_inf(s)

    if isinf(fright):
        return newfloat(0.0)

    if fleft == 0 and fright == 0:
        return w_NAN

    if fright == 0:
        s = sign_of(fleft, fright)
        return w_signed_inf(s)

    val = fleft / fright
    return newfloat(val)


@specialize.argtype(0, 1)
def _compare_gt(x, y):
    return x > y


@specialize.argtype(0, 1)
def _compare_ge(x, y):
    return x >= y


def _base_compare(x, y, _compare):
    if isint(x) and isint(y):
        n1 = api.to_native_integer(x)
        n2 = api.to_native_integer(y)
        return _compare(n1, n2)

    if isfloat(x) and isfloat(y):
        n1 = api.to_native_float(x)
        n2 = api.to_native_float(y)
        return _compare(n1, n2)

    if isstring(x) and isstring(y):
        n1 = api.to_native_string(x)
        n2 = api.to_native_string(y)
        return _compare(n1, n2)
    else:
        raise ObinTypeError(u"Invalid comparison operation")


def compare_gt(r, x, y):
    return newbool(_base_compare(x, y, _compare_gt))


def compare_ge(r, x, y):
    return newbool(_base_compare(x, y, _compare_ge))


def compare_lt(r, x, y):
    return newbool(_base_compare(y, x, _compare_gt))


def compare_le(r, x, y):
    return newbool(_base_compare(y, x, _compare_ge))


def uminus(routine, obj):
    if isint(obj):
        intval = api.to_native_integer(obj)
        if intval == 0:
            return newfloat(-float(intval))
        return newint(-intval)
    n1 = api.to_native_float(obj)
    return newfloat(-n1)


def _in(routine, left, right):
    from obin.objects.space import iscell
    if not iscell(right):
        raise ObinTypeError(u"TypeError: invalid object for in operator")

    return api.has(right, left)


def _bitand(r, op1, op2):
    return newint(int(op1 & op2))


def _bitxor(r, op1, op2):
    return newint(int(op1 ^ op2))


def _bitor(r, op1, op2):
    return newint(int(op1 | op2))


def bitnot(r, op):
    return newint(~op)


def ursh(r, lval, rval):
    lnum = api.to_native_integer(lval)
    rnum = api.to_native_integer(rval)

    # from rpython.rlib.rarithmetic import ovfcheck_float_to_int

    shift_count = rnum & 0x1F
    res = lnum >> shift_count
    return _w(res)


def rsh(r, lval, rval):
    lnum = api.to_native_integer(lval)
    rnum = api.to_native_integer(rval)

    # from rpython.rlib.rarithmetic import ovfcheck_float_to_int

    shift_count = rnum & 0x1F
    res = lnum >> shift_count
    return _w(res)


def lsh(r, lval, rval):
    rnum = rval.value()
    lnum = lval.value()

    shift_count = intmask(rnum & 0x1F)
    res = lnum << shift_count

    return _w(res)


def uplus(r, op1):
    assert isint(op1)
    return op1


def _not(r, val):
    v = api.to_native_bool(val)
    return newbool(not v)


def eq(r, op1, op2):
    return api.equal(op1, op2)


def noteq(r, op1, op2):
    # TODO api.ne
    return newbool(not api.to_native_bool(api.equal(op1, op2)))


def _isnot(r, op1, op2):
    # TODO api.isnot
    return newbool(not api.to_native_bool(api.strict_equal(op1, op2)))


def _is(r, op1, op2):
    return api.strict_equal(op1, op2)


"""
********************************** WRAPPERS
"""


def apply_binary_on_unboxed_integers(routine, operation):
    right = api.to_native_integer(routine.stack.pop())
    left = api.to_native_integer(routine.stack.pop())
    routine.stack.push(operation(routine, left, right))


def apply_binary(routine, operation):
    right = routine.stack.pop()
    left = routine.stack.pop()
    routine.stack.push(operation(routine, left, right))


def apply_unary(routine, operation):
    val = routine.stack.pop()
    routine.stack.push(operation(routine, val))


def apply_unary_on_unboxed_integer(routine, operation):
    val = api.to_native_integer(routine.stack.pop())
    routine.stack.push(operation(routine, val))


def primitive_IN(routine):
    apply_binary(routine, _in)


def primitive_SUB(routine):
    apply_binary(routine, sub)


def primitive_ADD(routine):
    apply_binary(routine, plus)


def primitive_MUL(routine):
    apply_binary(routine, mult)


def primitive_DIV(routine):
    apply_binary(routine, division)


def primitive_MOD(routine):
    apply_binary(routine, mod)


def primitive_BITAND(routine):
    apply_binary_on_unboxed_integers(routine, _bitand)


def primitive_BITXOR(routine):
    apply_binary_on_unboxed_integers(routine, _bitxor)


def primitive_BITOR(routine):
    apply_binary_on_unboxed_integers(routine, _bitor)


def primitive_BITNOT(routine):
    apply_unary_on_unboxed_integer(routine, bitnot)


def primitive_URSH(routine):
    apply_binary(routine, ursh)


def primitive_RSH(routine):
    apply_binary(routine, rsh)


def primitive_LSH(routine):
    apply_binary(routine, lsh)


def primitive_UPLUS(routine):
    apply_unary(routine, uplus)


def primitive_UMINUS(routine):
    apply_unary(routine, uminus)


def primitive_NOT(routine):
    apply_unary(routine, _not)


def primitive_GT(routine):
    apply_binary(routine, compare_gt)


def primitive_GE(routine):
    apply_binary(routine, compare_ge)


def primitive_LT(routine):
    apply_binary(routine, compare_lt)


def primitive_LE(routine):
    apply_binary(routine, compare_le)


def primitive_EQ(routine):
    apply_binary(routine, eq)


def primitive_NE(routine):
    apply_binary(routine, noteq)


def primitive_IS(routine):
    apply_binary(routine, _is)


def primitive_ISNOT(routine):
    apply_binary(routine, _isnot)
