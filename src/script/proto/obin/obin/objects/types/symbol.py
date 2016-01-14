from obin.objects.types.string import W_String
from obin.runtime.error import *
from obin.objects import api


class W_Symbol():
    # _immutable_fields_ = ['value']

    def __init__(self, string):
        self.string = string

    def _compare_(self, other):
        arg = string_or_symbol(other)
        if arg is None:
            raise RuntimeError("Invalid operation")

        return self.string._compare_(arg)

    def __eq__(self, other):
        arg = string_or_symbol(other)
        if arg is None:
            raise RuntimeError("Invalid operation")

        return self.string.__eq__(arg)

    def __hash__(self):
        return self._hash_()

    def _hash_(self):
        return self.string._hash_()

    def _equal_(self, other):
        arg = string_or_symbol(other)
        if arg is None:
            raise RuntimeError("I")

        return self.string._equal_(arg)

    def _tostring_(self):
        return self.string._tostring_()

    def _iterator_(self):
        return self.string._iterator_()

    def _length_(self):
        return self.string._length_()

    def _at_index_(self, i):
        return self.string._at_index_(i)

    def _get_index_(self, obj):
        return self.string._get_index_(obj)

    def _at_(self, i):
        return self.string._at_index_(i)

    def _behavior_(self, process):
        return process.std.behaviors.Symbol


def string_or_symbol(var):
    if isinstance(var, W_String):
        return var
    if isinstance(var, W_Symbol):
        return var.string
    return None
