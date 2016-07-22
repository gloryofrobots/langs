__author__ = 'gloryofrobots'
from obin.runtime.routine.base_routine import BaseRoutine
from obin.types import api
from obin.types import space

class NativeRoutine(BaseRoutine):
    # _immutable_fields_ = ['_name_', '_function_']

    def __init__(self, stack, name, function, args, arity):
        BaseRoutine.__init__(self, stack)
        from obin.types.space import issymbol
        assert issymbol(name)
        self._name_ = name
        self.native_func = function
        self.arity = arity
        self.count_args = api.length_i(args)
        self._args = args

    # redefine resume because we can call bytecode routine from native and after it resumes as we must complete
    def _on_resume(self, process, value):
        self.result = value

    def _on_complete(self, process):
        pass

    def _info(self):
        return space.newstring(u"obin.%s %s" %
                               (api.to_u(self._name_), api.to_u(self._args)))

    def args(self):
        return self._args

    def get_arg(self, index):
        return api.at_index(self._args, index)

    def _execute(self, process):
        if self.result is not None:
            self.complete(process, self.result)
        else:
            self.suspend()
            self.native_func(process, self)
