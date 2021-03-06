from arza.misc.platform import jit
from arza.types.space import isany
from arza.runtime import error
from arza.runtime.routine.code_routine import CodeRoutine
from arza.runtime.routine.native_routine import NativeRoutine
from arza.types import api, space


def complete_or_interrupt_native_routine(func):
    def func_wrapper(process, routine):
        result = func(process, routine)
        assert isany(result)
        if space.isinterrupt(result):
            return
        if not routine.is_closed():
            routine.complete(process, result)

    return func_wrapper


def complete_native_routine(func):
    def func_wrapper(process, routine):
        result = func(process, routine)
        assert space.isany(result), (func, routine.args(), result)
        assert not space.isvoid(result), (func, routine.args(), result)
        if not routine.is_closed():
            routine.complete(process, result)

    return func_wrapper


def create_native_routine(stack, name, native, args, arity):
    return NativeRoutine(stack, name, native, args, arity)


def create_callback_routine(stack, on_result, on_complete, function, args):
    from arza.runtime.routine.callback_routine import CallbackRoutine
    return CallbackRoutine(stack, on_result, on_complete, function, args)


def create_module_routine(name, stack, code, env):
    return jit.promote(CodeRoutine(space.newvoid(), stack, None, name, code, env))


def create_function_routine(stack, func, args, outer_env):
    code = func.bytecode
    scope = code.scope
    name = func.name

    env = create_function_environment(func, scope, args, outer_env)
    routine = jit.promote(CodeRoutine(func, stack, args, name, code, env))
    return routine


def create_function_environment(func, scope, args, outer_env):
    declared_args_count = scope.arg_count if not scope.is_variadic else scope.arg_count - 1
    args_count = api.length_i(args)

    if not scope.is_variadic:
        if args_count != declared_args_count:
            return error.throw_5(error.Errors.INVALID_ARG_COUNT_ERROR,
                                 space.newint(args_count), space.newstring(u"!="), space.newint(declared_args_count),
                                 func, args)
    if args_count < declared_args_count:
        return error.throw_5(error.Errors.INVALID_ARG_COUNT_ERROR,
                             space.newint(args_count), space.newstring(u"<"), space.newint(declared_args_count),
                             func.name, args)

    env = space.newenv(func.name, scope, outer_env)
    return env
