from obin.objects.object_space import _w
from obin.compile.code import Code
from obin.runtime.context import Context, FunctionExecutionContext, ObjectExecutionContext, EvalExecutionContext
from obin.runtime.routine import FunctionRoutine, BytecodeRoutine, NativeRoutine, GlobalRoutine, EvalRoutine
from obin.runtime.environment import DeclarativeEnvironment
from obin.compile.astbuilder import parse_to_ast, SymbolMap
from obin.compile.code import ast_to_bytecode
from obin.objects.object import W_BasicObject


class FakeInterpreter(object):
    from obin.runtime.interpreter import InterpreterConfig
    config = InterpreterConfig()

from obin.objects.object_space import object_space
object_space.interpreter = FakeInterpreter()

from obin.objects.object import W_Module
object_space.global_object = W_Module()


class TestJsFunctionAndStuff(object):
    def test_foo1(self):
        code = Code()
        code.emit('LOAD_INTCONSTANT', 1)
        code.emit('LOAD_INTCONSTANT', 1)
        code.emit('ADD')
        code.emit('RETURN')

        f = BytecodeRoutine(code)
        ctx = Context(stack_size=f.estimated_stack_size())
        res = f.run(ctx)
        assert res.value == _w(2)

    def test_foo2(self):
        code = Code()
        code.emit('LOAD_INTCONSTANT', 1)
        code.emit('LOAD_INTCONSTANT', 1)
        code.emit('ADD')
        code.emit('RETURN')

        f = FunctionRoutine(u'foo', code)
        ctx = FunctionExecutionContext(f)
        res = f.run(ctx)

        assert res.value == _w(2)

    def test_foo3(self):
        symbol_map = SymbolMap()
        var_idx = symbol_map.add_parameter(u'a')

        code = Code(symbol_map)
        code.emit('LOAD_VARIABLE', var_idx, u'a')
        code.emit('RETURN')

        f = FunctionRoutine(u'foo', code)
        ctx = FunctionExecutionContext(f, argv=[_w(42)])

        res = f.run(ctx)
        assert res.value == _w(42)

    def test_foo4(self):
        symbol_map = SymbolMap()
        var_idx_a = symbol_map.add_variable(u'a')
        var_idx_b = symbol_map.add_parameter(u'b')

        code = Code(symbol_map)
        code.emit('LOAD_VARIABLE', var_idx_a, u'a')
        code.emit('LOAD_VARIABLE', var_idx_b, u'b')
        code.emit('ADD')
        code.emit('RETURN')

        f = FunctionRoutine(u'foo', code)

        ctx = FunctionExecutionContext(f, formal_parameters=[u'b'], argv=[_w(21)])

        lex = ctx.variable_environment()
        env_rec = lex.environment_record
        env_rec.set_binding(u'a', _w(21), False)

        res = f.run(ctx)
        assert res.value == _w(42)

    def test_foo5(self):
        symbol_map = SymbolMap()
        var_idx_a = symbol_map.add_variable(u'a')
        var_idx_b = symbol_map.add_parameter(u'b')

        code = Code(symbol_map)
        code.emit('LOAD_VARIABLE', var_idx_a, u'a')
        code.emit('LOAD_VARIABLE', var_idx_b, u'b')
        code.emit('ADD')
        code.emit('STORE', var_idx_a, u'a')
        code.emit('RETURN')

        f = FunctionRoutine(u'foo', code)
        ctx = FunctionExecutionContext(f, formal_parameters=[u'b'], argv=[_w(21)])

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record
        env_rec.set_binding(u'a', _w(21), False)

        res = f.run(ctx)

        assert env_rec.get_binding_value(u'a') == _w(42)
        assert res.value == _w(42)

    def test_foo6(self):
        symbol_map = SymbolMap()
        var_idx_a = symbol_map.add_variable(u'a')
        var_idx_b = symbol_map.add_symbol(u'b')

        code = Code(symbol_map)
        code.emit('LOAD_VARIABLE', var_idx_a, u'a')
        code.emit('LOAD_VARIABLE', var_idx_b, u'b')
        code.emit('ADD')
        code.emit('STORE', var_idx_a, u'a')
        code.emit('RETURN')

        outer_env = DeclarativeEnvironment()
        outer_env_rec = outer_env.environment_record

        f = FunctionRoutine(u'foo', code)

        ctx = FunctionExecutionContext(f, scope=outer_env)

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record

        env_rec.set_binding(u'a', _w(21), False)

        outer_env_rec.create_binding(u'b', True)
        outer_env_rec.set_binding(u'b', _w(21), False)

        res = f.run(ctx)

        assert env_rec.get_binding_value(u'a') == _w(42)
        assert outer_env_rec.get_binding_value(u'b') == _w(21)
        assert res.value == _w(42)

    def test_foo7(self):
        symbol_map = SymbolMap()
        var_idx_a = symbol_map.add_variable(u'a')
        var_idx_b = symbol_map.add_symbol(u'b')

        code = Code(symbol_map)
        code.emit('LOAD_VARIABLE', var_idx_a, u'a')
        code.emit('LOAD_VARIABLE', var_idx_b, u'b')
        code.emit('ADD')
        code.emit('STORE', var_idx_b, u'b')
        code.emit('RETURN')

        outer_env = DeclarativeEnvironment()
        outer_env_rec = outer_env.environment_record

        f = FunctionRoutine(u'foo', code)

        ctx = FunctionExecutionContext(f, scope=outer_env)

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record

        env_rec.set_binding(u'a', _w(21), False)

        outer_env_rec.create_binding(u'b', True)
        outer_env_rec.set_binding(u'b', _w(21), False)

        res = f.run(ctx)

        assert env_rec.get_binding_value(u'a') == _w(21)
        assert outer_env_rec.get_binding_value(u'b') == _w(42)
        assert res.value == _w(42)

    def test_foo8(self):
        symbol_map = SymbolMap()
        var_idx_a = symbol_map.add_variable(u'a')
        var_idx_b = symbol_map.add_variable(u'b')
        var_idx_c = symbol_map.add_variable(u'c')

        code = Code(symbol_map)
        code.emit('LOAD_INTCONSTANT', 21)
        code.emit('STORE', var_idx_a, u'a')
        code.emit('POP')
        code.emit('LOAD_INTCONSTANT', 21)
        code.emit('STORE', var_idx_b, u'b')
        code.emit('POP')
        code.emit('LOAD_VARIABLE', var_idx_a, u'a')
        code.emit('LOAD_VARIABLE', var_idx_b, u'b')
        code.emit('ADD')
        code.emit('STORE', var_idx_c, u'c')
        code.emit('RETURN')

        f = GlobalRoutine(code)

        w_global = W_BasicObject()

        ctx = ObjectExecutionContext(f, w_global)
        res = f.run(ctx)

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record

        assert env_rec.get_binding_value(u'a') == _w(21)
        assert env_rec.get_binding_value(u'b') == _w(21)
        assert env_rec.get_binding_value(u'c') == _w(42)
        assert res.value == _w(42)

    def test_foo9(self):
        src = u'''
        var a = 21;
        var b = 21;
        var c = a + b;
        return c;
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        f = GlobalRoutine(code)

        w_global = W_BasicObject()
        ctx = ObjectExecutionContext(f, w_global)
        res = f.run(ctx)

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record

        assert env_rec.get_binding_value(u'a') == _w(21)
        assert env_rec.get_binding_value(u'b') == _w(21)
        assert env_rec.get_binding_value(u'c') == _w(42)
        assert res.value == _w(42)

    def test_foo10(self):
        src = u'''
        function f() {
            return 42;
        }
        var a = f();
        return a;
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        f = GlobalRoutine(code)
        w_global = W_BasicObject()

        ctx = ObjectExecutionContext(f, w_global)
        res = f.run(ctx)

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record

        assert env_rec.get_binding_value(u'a') == _w(42)
        assert res.value == _w(42)

    def test_foo11(self):
        src = u'''
        function f(b) {
            var c = 21;
            return b + c;
        }
        var a = f(21);
        return a;
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        f = GlobalRoutine(code)

        w_global = W_BasicObject()
        ctx = ObjectExecutionContext(f, w_global)
        res = f.run(ctx)

        lex_env = ctx.variable_environment()
        env_rec = lex_env.environment_record

        assert env_rec.get_binding_value(u'a') == _w(42)
        assert env_rec.has_binding(u'b') is False
        assert env_rec.has_binding(u'c') is False
        assert res.value == _w(42)

    def test_foo12(self):
        src = u'''
        function fib(n) {
            if(n<2) {
                return n;
            } else {
                return fib(n-1) + fib(n-2);
            }
        }
        return fib(10);
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        f = GlobalRoutine(code)

        w_global = W_BasicObject()
        ctx = ObjectExecutionContext(f, w_global)
        res = f.run(ctx)

        assert res.value == _w(55)

    def test_foo13(self):
        def f(this, args):
            a = args[0].ToInteger()
            return _w(a + 1)

        func = NativeRoutine(f)
        ctx = FunctionExecutionContext(func, argv=[_w(41)])
        res = func.run(ctx)

        assert res.value == _w(42)

    def test_foo14(self):
        def f(this, args):
            a = args[0].ToInteger()
            return _w(a + 1)

        func = NativeRoutine(f)

        from obin.objects.object import W_Function
        w_func = W_Function(func)

        w_global = W_BasicObject()
        w_global.put(u'f', w_func)

        src = u'''
        return f(41);
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        c = GlobalRoutine(code)
        ctx = ObjectExecutionContext(c, w_global)
        res = c.run(ctx)

        assert res.value == _w(42)

    def test_foo15(self):
        code = Code()
        code.emit('LOAD_INTCONSTANT', 1)
        code.emit('LOAD_INTCONSTANT', 1)
        code.emit('ADD')

        f = BytecodeRoutine(code)

        ctx = Context(stack_size=f.estimated_stack_size())
        res = f.run(ctx)
        assert res.value == _w(2)

    def test_foo16(self):
        src = u'''
        a = 1;
        b = 41;
        a + b;
        '''
        res = self.run_src(src)
        assert res == _w(42)

    def test_foo17(self):
        src = u'''
        function f() {
            a = 42;
        }
        f();
        a;
        '''

        res = self.run_src(src)
        assert res == _w(42)

    def test_foo18(self):
        src = u'''
        a = 42;
        this.a;
        '''

        res = self.run_src(src)
        assert res == _w(42)

    def test_foo19(self):
        src = u'''
        function x() { d=2; return d;}; x();
        '''

        res = self.run_src(src)
        assert res == _w(2)

    def test_foo20(self):
        src = u'''
        ;
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        global_code = GlobalRoutine(code)
        global_object = W_BasicObject()
        global_ctx = ObjectExecutionContext(global_code, global_object)

        src = u'''
        a = 1;
        '''

        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        f = EvalRoutine(code)

        ctx = EvalExecutionContext(f, calling_context=global_ctx)
        res = f.run(ctx)

        assert res.value == _w(1)

    def run_src(self, src):
        ast = parse_to_ast(src)
        symbol_map = ast.symbol_map
        code = ast_to_bytecode(ast, symbol_map)

        c = GlobalRoutine(code)

        w_global = W_BasicObject()
        object_space.global_object = w_global
        ctx = ObjectExecutionContext(c, w_global)
        res = c.run(ctx)
        return res.value
