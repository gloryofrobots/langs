from obin.types import space, api
from obin.builtins import builtins
from obin.runtime.process import Process
from obin.runtime import process_data, error
from obin.runtime.load import import_module, evaluate_module_file

def newprocess(libdirs):
    core_prelude = space.newemptyenv(space.newstring(u"prelude"))
    proc_data = process_data.create(libdirs, core_prelude)
    process = Process(proc_data)
    builtins.presetup(process, core_prelude, process.std)
    return process

def load_prelude_script(process, script_name):
    result = import_module(process, space.newsymbol(process, script_name))
    if process.is_terminated():
        # error here
        return process, result

    process.modules.set_prelude(result)
    return process, None

# TODO MOVE ALL OF IT TO PROCESS
def initialize(libdirs):
    process = newprocess(libdirs)
    # space.initialise(process)
    scripts = [u"prelude"]
    for script in scripts:
        process, err = load_prelude_script(process, script)
        if err is not None:
            return process, err

    builtins.postsetup(process)
    return process, None


def evaluate_file(process, filename):
    try:
        module = evaluate_module_file(process, space.newsymbol(process, u"__main__"), filename)
    except error.ObinSignal as e:
        return e.signal

    main = api.at(module, space.newsymbol(process, u"main"))
    result = process.subprocess(main, space.newtuple([space.newunit()]))

    if process.is_terminated():
        # error here
        return result

    return space.newtuple([space.newsymbol(process, u"ok"), result])