from obin.types.root import W_Root
from obin.types import api

class W_SequenceIterator(W_Root):
    def __init__(self, source):
        from obin.types.space import isany
        assert isany(source)
        self.index = 0
        self.source = source
        self.source_length = api.length_i(source)

    def _next_(self):
        from obin.types.space import newvoid
        if self.index >= self.source_length:
            return newvoid()

        el = api.at_index(self.source, self.index)
        self.index += 1
        return el

    def _to_string_(self):
        return "<Iterator %d:%d>" % (self.index, self.source_length)

    def _length_(self):
        return self.source_length - self.index

