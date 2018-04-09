from capy.types import api, space, plist
from capy.runtime import error


def find_in_module(process, prelude, name):
    sym = space.newsymbol(process, name)
    if not api.has(prelude, sym):
        error.throw_1(error.Errors.KEY_ERROR, space.newstring(u"Missing internal trait %s in prelude" % name))
    return api.at(prelude, sym)


def newclass(name, baseclass):
    from capy.types.space import newemptyclass
    return newemptyclass(name, baseclass)


class StdClasses:
    def __init__(self, symbols):
        _s = symbols.symbol
        self.Object = newclass(_s(u"Object"), space.newnil())
        self.Class = newclass(_s(u"Class"), self.Object)

        newtype = lambda name: newclass(name, self.Object)
        newtype_2 = lambda name, parent: newclass(name, parent)

        self.Bool = newtype(_s(u"Bool"))

        self.Char = newtype(_s(u"Char"))

        self.Number = newtype(_s(u"Number"))

        self.Int = newtype_2(_s(u"Int"), self.Number)

        self.Float = newtype_2(_s(u"Float"), self.Number)

        self.Symbol = newtype(_s(u"Symbol"))

        self.String = newtype(_s(u"String"))

        self.Array = newtype(_s(u"Array"))

        self.Seq = newtype(_s(u"Seq"))

        self.ArraySeq = newtype_2(_s(u"ArraySeq"), self.Seq)

        self.TableSeq = newtype_2(_s(u"TableSeq"), self.Seq)

        self.Tuple = newtype(_s(u"Tuple"))

        self.Table = newtype(_s(u"Table"))

        self.Function = newtype(_s(u"Function"))

        self.FiberChannel = newtype(_s(u"FiberChannel"))

        self.File = newtype(_s(u"File"))

        self.IO = newtype(_s(u"IO"))

        self.Coroutine = newtype(_s(u"Coroutine"))

        self.Env = newtype(_s(u"Env"))

        self.PID = newtype(_s(u"PID"))


class Functions:
    def __init__(self):
        self.new = None

    def setup(self, process):
        prelude = process.classes.prelude
        self.new = self.find_function(process, prelude, u"__new__")

    def find_function(self, process, module, name):
        _fun = find_in_module(process, module, name)
        error.affirm_type(_fun, space.isfunction)
        return _fun


class Std:
    def __init__(self, symbols):
        # self.functions = Functions()
        self.classes = StdClasses(symbols)
        self.initialized = False

    def postsetup(self, process):
        # self.functions.setup(process)
        self.initialized = True
