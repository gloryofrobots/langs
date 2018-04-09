from capy.types import api, space, symbol


def presetup(process, module, stdlib):
    import capy.builtins.lang

    capy.builtins.lang.setup(process, module, stdlib)

    import capy.builtins.classes.setup_object
    capy.builtins.classes.setup_object.setup(process, stdlib)

    import capy.builtins.classes.setup_array
    capy.builtins.classes.setup_array.setup(process, stdlib)

    import capy.builtins.classes.setup_class
    capy.builtins.classes.setup_class.setup(process, stdlib)

    import capy.builtins.classes.setup_number
    capy.builtins.classes.setup_number.setup(process, stdlib)

    setup_classes(module, stdlib.classes)

    module.export_all()


def setup_classes(module, classes):
    # ---------------AUTOGENERATED---------------------
    api.put(module, classes.Object.name, classes.Object)
    api.put(module, classes.Class.name, classes.Class)
    api.put(module, classes.Bool.name, classes.Bool)
    api.put(module, classes.Char.name, classes.Char)
    api.put(module, classes.Int.name, classes.Int)
    api.put(module, classes.Float.name, classes.Float)
    api.put(module, classes.Symbol.name, classes.Symbol)
    api.put(module, classes.String.name, classes.String)
    api.put(module, classes.Array.name, classes.Array)
    api.put(module, classes.Table.name, classes.Table)
    api.put(module, classes.Function.name, classes.Function)

    api.put(module, classes.FiberChannel.name, classes.FiberChannel)
    api.put(module, classes.Coroutine.name, classes.Coroutine)
    api.put(module, classes.Env.name, classes.Env)
    api.put(module, classes.PID.name, classes.PID)
    api.put(module, classes.IO.name, classes.IO)
    api.put(module, classes.File.name, classes.File)


def postsetup(process):
    create_lang_names(process)


def create_lang_names(process):
    from capy.builtins import lang_names
    prelude = process.classes.prelude
    exports = prelude.exports()
    lang_prefix = space.newsymbol_s(process, lang_names.PREFIX)
    for name in exports:
        new_name = symbol.concat_2(process, lang_prefix, name)
        val = api.at(prelude, name)
        api.put(prelude, new_name, val)
