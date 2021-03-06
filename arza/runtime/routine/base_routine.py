class BaseRoutine:
    class State:
        IDLE = -1
        COMPLETE = 0
        INPROCESS = 2
        TERMINATED = 3
        SUSPENDED = 4

    def __init__(self, stack):
        self._state = BaseRoutine.State.IDLE
        self.result = None
        self.signal = None
        self.stack = stack
        self.return_pointer = self.stack.pointer()

    def catch(self, signal):
        result = self._catch(signal)
        assert isinstance(result, bool)

        if result is False and not self.is_terminated():
            self.terminate(signal)

        return result

    def _catch(self, signal):
        return False

    def resume(self, process, value):
        # print "RESUME", value
        assert self.is_suspended(), (self._state, self.result, process)
        self._state = BaseRoutine.State.INPROCESS
        self._on_resume(process, value)

    def _on_resume(self, process, value):
        raise NotImplementedError()

    def info(self):
        return self._info()

    def _info(self):
        raise NotImplementedError()

    def inprocess(self):
        assert not self.is_closed()
        self._state = BaseRoutine.State.INPROCESS

    def complete(self, process, result):
        assert not self.is_closed()
        self.result = result
        self.stack.set_pointer(self.return_pointer)
        self._state = BaseRoutine.State.COMPLETE
        self._on_complete(process)

    def _on_complete(self, process):
        raise NotImplementedError()

    def terminate(self, signal):
        # assert not self.is_closed()
        self.result = signal
        self._state = BaseRoutine.State.TERMINATED

    def activate(self):
        self.inprocess()

    def _on_activate(self):
        pass

    def suspend(self):
        assert not self.is_closed()
        self._state = BaseRoutine.State.SUSPENDED

    def execute(self, process):
        if self.is_complete():
            raise RuntimeError("Already complete")
        self._execute(process)

    def _execute(self, process):
        raise NotImplementedError()

    def is_inprocess(self):
        return self._state == BaseRoutine.State.INPROCESS

    def is_idle(self):
        return self._state == BaseRoutine.State.IDLE

    def is_terminated(self):
        return self._state == BaseRoutine.State.TERMINATED

    def is_complete(self):
        return self._state == BaseRoutine.State.COMPLETE

    def is_suspended(self):
        return self._state == BaseRoutine.State.SUSPENDED

    def is_closed(self):
        return self._state == BaseRoutine.State.COMPLETE \
               or self._state == BaseRoutine.State.TERMINATED

