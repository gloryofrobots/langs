from lalan.types import space, api
from lalan.builtins import builtins
from lalan.runtime.process import Process
from lalan.runtime import process_data, error
from lalan.runtime.load import import_module, evaluate_module_file

PRELUDE_FILE = u"prelude"
# PRELUDE_FILE = u"prelude_debug"

STD_MODULES = [u"bool", u"num", u"bit", u"env",
               u"string", u"vector",
               u"list", u"function", u"coro", u"trait",
               u"tuple", u"map", u"seq",
               u"datatype",
               ]
# STD_MODULES = []


def newprocess(libdirs):
    core_prelude = space.newemptyenv(space.newstring(u"prelude"))
    proc_data = process_data.create(libdirs, core_prelude)
    process = Process(proc_data)
    builtins.presetup(process, core_prelude, process.std)
    return process


def load_prelude(process, script_name):
    result = import_module(process, space.newsymbol(process, script_name))
    if process.is_terminated():
        # error here
        return result

    process.modules.set_prelude(result)
    return None


def load_module(process, script_name):
    result = import_module(process, space.newsymbol(process, script_name))
    if process.is_terminated():
        # error here
        return result
    return None


# TODO MOVE ALL OF IT TO PROCESS
def initialize(libdirs):
    path = space.newlist([space.newstring_s(p) for p in libdirs])

    process = newprocess(path)
    err = load_prelude(process, PRELUDE_FILE)
    if err is not None:
        return process, err

    # HERE ORDER IS IMPORTANT!!!!!
    # imports derive.lal
    process.std.postsetup(process)
    error.initialise(process)
    builtins.postsetup(process)

    for module_name in STD_MODULES:
        err = load_module(process, module_name)
        if err is not None:
            return process, err

    print "INITIALIZED"
    return process, None


def evaluate_file(process, filename):
    try:
        module = evaluate_module_file(process, space.newsymbol(process, u"__main__"), filename)
    except error.LalanSignal as e:
        return e.signal

    main = api.at(module, space.newsymbol(process, u"main"))
    result = process.subprocess(main, space.newunit())

    if process.is_terminated():
        # error here
        return result

    return space.newtuple([space.newsymbol(process, u"ok"), result])