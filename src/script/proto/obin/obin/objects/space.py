from rpython.rlib.objectmodel import specialize, enforceargs
from rpython.rlib import jit


@enforceargs(int)
def newint(i):
    from obin.objects.types.value import W_Integer
    return W_Integer(i)


@enforceargs(float)
def newfloat(f):
    from obin.objects.types.value import W_Float
    return W_Float(f)


@enforceargs(str)
def newchar(c):
    from obin.objects.types.value import W_Char
    return W_Char(ord(c))


@enforceargs(str)
def newstring_from_str(s):
    if not isinstance(s, str):
        print type(s)
    assert isinstance(s, str)
    return newstring(unicode(s))


# @enforceargs(unicode)
def newstring(s):
    from obin.objects.types.value import W_String
    if not isinstance(s, unicode):
        print type(s)
    assert isinstance(s, unicode)
    return W_String(s)


class Globals:
    def __init__(self):
        self.w_True = None
        self.w_False = None
        self.w_Undefined = None
        self.w_Interrupt = None
        self.w_Null = None


w_Globals = Globals()


def makeglobals():
    global w_Globals
    from obin.objects.types.constant import W_True, W_False, W_Undefined, W_Nil, W_Constant
    w_Globals.w_True = W_True()
    w_Globals.w_False = W_False()
    w_Globals.w_Null = W_Nil()
    w_Globals.w_Undefined = W_Undefined()
    w_Globals.w_Interrupt = W_Constant()

    jit.promote(w_Globals.w_True)
    jit.promote(w_Globals.w_False)
    jit.promote(w_Globals.w_Undefined)
    jit.promote(w_Globals.w_Null)


def newinterrupt():
    return w_Globals.w_Interrupt


def newnull():
    return w_Globals.w_Null


def newundefined():
    return w_Globals.w_Undefined


@enforceargs(bool)
def newbool(val):
    if val:
        return w_Globals.w_True
    return w_Globals.w_False


def newfunc(name, bytecode, scope):
    from obin.objects.types.callable import W_Function
    obj = W_Function(name, bytecode, scope)
    return obj


def newfuncsource(name, bytecode):
    from obin.objects.types.callable import W_FunctionSource
    obj = W_FunctionSource(name, bytecode)
    return obj


def newprimitive(name, function, arity):
    from obin.objects.types.callable import W_Primitive
    obj = W_Primitive(name, function, arity)
    return obj


def newobject():
    from obin.objects.types.object import W_Object
    from obin.objects import api
    obj = W_Object(None)

    obj.set_traits(api.clone(state.traits.ObjectTraits))
    return obj


def newplainobject():
    from obin.objects.types.object import W_Object
    from obin.objects import api
    obj = W_Object(None)
    return obj


def newplainobject_with_slots(slots):
    from obin.objects.types.object import W_Object
    obj = W_Object(slots)
    return obj


def newvector(items):
    assert isinstance(items, list)
    from obin.objects.types.vector import W_Vector
    obj = W_Vector(items)
    return obj


def newtuple(tupl):
    from obin.objects.types.tupletype import W_Tuple
    return W_Tuple(list(tupl))


def newcoroutine(fn):
    from obin.objects.types.callable import W_Coroutine
    obj = W_Coroutine(fn)
    return obj


def newmodule(name, code):
    assert isstring(name)
    from obin.objects.types.module import W_Module
    obj = W_Module(name, code)
    return obj


def newgeneric(name):
    assert isstring(name)
    from obin.objects.types.dispatch.generic import W_Generic
    obj = W_Generic(name)
    return obj


def newtrait(name):
    from obin.objects.types.trait import W_Trait
    return W_Trait(name)


def newtraits(traits):
    return newvector(traits)

def isany(value):
    from obin.objects.types.root import W_Root
    return isinstance(value, W_Root)


def isundefined(value):
    return value is w_Globals.w_Undefined


def isinterrupt(value):
    return value is w_Globals.w_Interrupt


def iscell(value):
    from obin.objects.types.root import W_Cell
    return isinstance(value, W_Cell)


def isobject(value):
    from obin.objects.types.object import W_Object
    return isinstance(value, W_Object)


def isvaluetype(value):
    from obin.objects.types.value import W_ValueType
    return isinstance(value, W_ValueType)


def isfunction(value):
    from obin.objects.types.callable import W_Function, W_Primitive
    return isinstance(value, W_Function) or isinstance(value, W_Primitive)


def isvector(value):
    from obin.objects.types.vector import W_Vector
    return isinstance(value, W_Vector)


def istrait(w):
    from obin.objects.types.trait import W_Trait
    return isinstance(w, W_Trait)


def isgeneric(w):
    from obin.objects.types.dispatch.generic import W_Generic
    return isinstance(w, W_Generic)


def istuple(w):
    from obin.objects.types.tupletype import W_Tuple
    return isinstance(w, W_Tuple)


def ismodule(w):
    from obin.objects.types.module import W_Module
    return isinstance(w, W_Module)


def isboolean(value):
    return value is w_Globals.w_False or value is w_Globals.w_True


def isnull(value):
    return value is w_Globals.w_Null


def isint(w):
    from obin.objects.types.value import W_Integer
    return isinstance(w, W_Integer)


def isstring(w):
    from obin.objects.types.value import W_String
    return isinstance(w, W_String)


def isfloat(w):
    from obin.objects.types.value import W_Float
    return isinstance(w, W_Float)


def isconstant(w):
    from obin.objects.types.constant import W_Constant
    return isinstance(w, W_Constant)


def isnull_or_undefined(obj):
    if isnull(obj) or isundefined(obj):
        return True
    return False


class State:
    class Traits:
        def __init__(self):
            self.Any = newtrait(newstring(u"Any"))
            self.Boolean = newtrait(newstring(u"Boolean"))

            self.True = newtrait(newstring(u"True"))
            self.TrueTraits = newtraits([self.True, self.Boolean, self.Any])

            self.False = newtrait(newstring(u"False"))
            self.FalseTraits = newtraits([self.False, self.Boolean, self.Any])

            self.Nil = newtrait(newstring(u"Nil"))
            self.NilTraits = newtraits([self.Nil, self.Any])

            self.Undefined = newtrait(newstring(u"Undefined"))
            self.UndefinedTraits = newtraits([self.Undefined, self.Any])

            self.Char = newtrait(newstring(u"Char"))
            self.CharTraits = newtraits([self.Char, self.Any])

            self.Number = newtrait(newstring(u"Number"))
            self.Integer = newtrait(newstring(u"Integer"))
            self.IntegerTraits = newtraits([self.Integer, self.Number, self.Any])

            self.Float = newtrait(newstring(u"Float"))
            self.FloatTraits = newtraits([self.Float, self.Number, self.Any])

            self.Symbol = newtrait(newstring(u"Symbol"))
            self.SymbolTraits = newtraits([self.Symbol, self.Any])

            self.String = newtrait(newstring(u"String"))
            self.StringTraits = newtraits([self.String, self.Any])

            self.List = newtrait(newstring(u"List"))

            self.Vector = newtrait(newstring(u"Vector"))
            self.VectorTraits = newtraits([self.Vector, self.Any])

            self.Tuple = newtrait(newstring(u"Tuple"))
            self.TupleTraits = newtraits([self.Tuple, self.Any])

            self.Function = newtrait(newstring(u"Function"))
            self.FunctionTraits = newtraits([self.Function, self.Any])

            self.Coroutine = newtrait(newstring(u"Coroutine"))
            self.CoroutineTraits = newtraits([self.Coroutine, self.Function, self.Any])

            self.Generic = newtrait(newstring(u"Generic"))
            self.GenericTraits = newtraits([self.Generic, self.Any])

            self.Primitive = newtrait(newstring(u"Primitive"))
            self.PrimitiveTraits = newtraits([self.Primitive, self.Any])

            self.Object = newtrait(newstring(u"Object"))
            self.ObjectTraits = newtraits([self.Object, self.Any])

            self.Module = newtrait(newstring(u"Object"))
            self.ModuleTraits = newtraits([self.Module, self.Any])

    def __init__(self):
        self.traits = State.Traits()
        self.process = None


state = State()


def newprocess(libdirs):
    makeglobals()
    from obin.builtins import setup_builtins
    from obin.runtime.process import Process
    process = Process()
    for path in libdirs:
        process.add_path(path)
    state.process = process
    setup_builtins(process.builtins)
    return process


@specialize.argtype(0)
def _w(value):
    from obin.objects.types.root import W_Root
    if value is None:
        return newnull()
    elif isinstance(value, W_Root):
        return value
    elif isinstance(value, bool):
        return newbool(value)
    elif isinstance(value, int):
        return newint(value)
    elif isinstance(value, float):
        return newfloat(value)
    elif isinstance(value, unicode):
        return newstring(value)
    elif isinstance(value, str):
        u_str = unicode(value)
        return newstring(u_str)
    elif isinstance(value, list):
        return newvector(value)

    raise TypeError("ffffuuu %s" % (str(type(value)),))
