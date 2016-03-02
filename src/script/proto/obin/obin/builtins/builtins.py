from obin.types import api


def setup(process, module, stdlib):
    setup_traits(process, module, stdlib)
    setup_methods(process, module, stdlib)
    setup_types(process, module, stdlib)

    import obin.builtins.prelude
    obin.builtins.prelude.setup(process, module, stdlib)

    # MODULES

    import obin.builtins.modules.module_tvar
    obin.builtins.modules.module_tvar.setup(process, stdlib)

    import obin.builtins.modules.module_list
    obin.builtins.modules.module_list.setup(process, stdlib)

    import obin.builtins.modules.module_fiber
    obin.builtins.modules.module_fiber.setup(process, stdlib)

    module.export_all()


def setup_traits(process, module, stdlib):
    traits = stdlib.traits
    # ---------------AUTOGENERATED---------------------
    api.put(module, traits.Any.name, traits.Any)
    api.put(module, traits.Number.name, traits.Number)
    api.put(module, traits.Callable.name, traits.Callable)
    api.put(module, traits.Collection.name, traits.Collection)
    api.put(module, traits.Seq.name, traits.Seq)
    api.put(module, traits.Indexed.name, traits.Indexed)


def setup_types(process, module, stdlib):
    types = stdlib.types
    # ---------------AUTOGENERATED---------------------
    api.put(module, types.Bool.name, types.Bool)
    api.put(module, types.True.name, types.True)
    api.put(module, types.False.name, types.False)
    api.put(module, types.Option.name, types.Option)
    api.put(module, types.Nil.name, types.Nil)
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
    api.put(module, types.Generic.name, types.Generic)
    api.put(module, types.NativeFunction.name, types.NativeFunction)
    api.put(module, types.Fiber.name, types.Fiber)
    api.put(module, types.Trait.name, types.Trait)
    api.put(module, types.Datatype.name, types.Datatype)
    api.put(module, types.TVar.name, types.TVar)
    api.put(module, types.Env.name, types.Env)

def setup_methods(process, module, stdlib):
    methods = stdlib.methods
    # ---------------AUTOGENERATED---------------------
    # Eq
    api.put(module, methods.eq.name, methods.eq)
    api.put(module, methods.ne.name, methods.ne)
    # Ord
    api.put(module, methods.gt.name, methods.gt)
    api.put(module, methods.ge.name, methods.ge)
    api.put(module, methods.le.name, methods.le)
    api.put(module, methods.lt.name, methods.lt)
    api.put(module, methods.compare.name, methods.compare)
    # Num
    api.put(module, methods.negate.name, methods.negate)
    api.put(module, methods.add.name, methods.add)
    api.put(module, methods.sub.name, methods.sub)
    api.put(module, methods.mul.name, methods.mul)
    api.put(module, methods.div.name, methods.div)
    api.put(module, methods.mod.name, methods.mod)
    # Collection
    api.put(module, methods.in_.name, methods.in_)
    api.put(module, methods.notin.name, methods.notin)
    # Seq
    api.put(module, methods.cons.name, methods.cons)
    api.put(module, methods.concat.name, methods.concat)