from root import W_Cell
from value import NativeListIterator
from obin.runtime.exception import *

class W_Vector(W_Cell):
    _type_ = 'Vector'

    def __init__(self, items):
        assert isinstance(items, list)
        self._items = items

    def _native_iterator_(self):
        return self._items.__iter__()
    # def __str__(self):
    #     return u'W_Vector("%s")' % str(self._items)

    def _put_(self, k, v):
        if self.isfrozen():
            raise ObinRuntimeError("Vector is frozen")
        from obin.objects.space import isint
        from obin.objects import api
        assert isint(k)
        i = api.to_native_integer(k)
        try:
            self._items[i] = v
        except:
            raise ObinKeyError(k)

    def _traits_(self):
        from obin.objects.space import state
        return state.traits.VectorTraits

    def _clone_(self):
        return W_Vector([v for v in self._items])

    def copy(self):
        return W_Vector([v for v in self._items])

    def _at_(self, index):
        from obin.objects.space import newundefined, isint
        from obin.objects import api
        assert isint(index)
        try:
            el = self._items[api.to_native_integer(index)]
        except ObinKeyError:
            return newundefined()

        return el

    def _iterator_(self):
        return NativeListIterator(self._items, self.length())

    def _tobool_(self):
        return bool(self._items)

    def _length_(self):
        return self.length()

    def _delete_(self, key):
        del self._items[key]

    def _tostring_(self):
        return str(self._items)

    def at(self, i):
        return self._items[i]

    def has_index(self, i):
        return i > 0 and i < self.length()

    def get_index(self, obj):
        try:
            return self._items.index(obj)
        except ValueError:
            return -1

    def has(self, obj):
        return obj in self._items

    def length(self):
        return len(self._items)

    def ensure_size(self, size):
        assert size > 0
        l = self.length()
        if size <= l:
            return

        self._items += [None] * (size - l)

    def append(self, v):
        self._items.append(v)

    def prepend(self, v):
        self._items.insert(0, v)

    def set(self, index, v):
        self._items[index] = v

    def insert(self, index, v):
        self._items.insert(index, v)

    def remove(self, v):
        self._items.remove(v)

    def values(self):
        return self._items

    def append_many(self, items):
        self._items += items

    def pop(self):
        return self._items.pop()

    def concat(self, v):
        self._items += v.values()

    def fold_slice_into_itself(self, index):
        rest = W_Vector(self._items[index:])
        self._items = self._items[0:index]
        self._items.append(rest)

    def append_value_multiple_times(self, val, times):
        self._items = self._items + [val] * times

    def exclude_index(self, idx):
        items = self._items
        self._items = items[:idx] + items[idx + 1:]
