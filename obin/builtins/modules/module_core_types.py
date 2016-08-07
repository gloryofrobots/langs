from obin.types import number, space, api
from obin.runtime.routine.routine import complete_native_routine
from obin.runtime import error


def setup(process, stdlib):
    name = space.newsymbol(process, u'obin:lang:_types')
    _module = space.newemptyenv(name)
    setup_types(_module, stdlib.types)
    _module.export_all()
    process.modules.add_module(name, _module)


def setup_types(module, types):
    # ---------------AUTOGENERATED---------------------
    api.put(module, types.Bool.name, types.Bool)
    api.put(module, types.Char.name, types.Char)
    api.put(module, types.Int.name, types.Int)
    api.put(module, types.Float.name, types.Float)
    api.put(module, types.Symbol.name, types.Symbol)
    api.put(module, types.String.name, types.String)
    api.put(module, types.List.name, types.List)
    api.put(module, types.Vector.name, types.Vector)
    api.put(module, types.Tuple.name, types.Tuple)
    api.put(module, types.Map.name, types.Map)
    api.put(module, types.Function.name, types.Function)
    api.put(module, types.Partial.name, types.Partial)
    api.put(module, types.Generic.name, types.Generic)
    api.put(module, types.Interface.name, types.Interface)
    api.put(module, types.Fiber.name, types.Fiber)
    api.put(module, types.Coroutine.name, types.Coroutine)
    api.put(module, types.Trait.name, types.Trait)
    api.put(module, types.Datatype.name, types.Datatype)
    api.put(module, types.Union.name, types.Union)
    api.put(module, types.LazyVal.name, types.LazyVal)
    api.put(module, types.Env.name, types.Env)
