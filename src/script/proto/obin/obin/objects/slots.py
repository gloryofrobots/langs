from obin.objects.space import newvector
from obin.utils.builtins import odict
from obin.objects.hashtable import newhashtable

class Slots:
    def __init__(self):
        self.property_values = None
        self.property_bindings = None
        self.index = 0

    def to_dict(self):
        m = {}
        for n, v in self.property_bindings.items():
            m[n] = self.property_values.at(v)

        return m

    def __str__(self):
        return str(self.to_dict())
        pass

    def __repr__(self):
        return self.__str__()

    def copy(self):
        clone = Slots()
        values = self.property_values
        if values is not None:
            clone.property_values = self.property_values.copy()
            clone.property_bindings = self.property_bindings.copy()
            clone.index = self.index

        return clone

    def contains(self, name):
        return name in self.property_bindings

    def length(self):
        return self.property_values.length()

    def keys(self):
        return self.property_bindings.keys()

    def get(self, name):
        from obin.objects.space import newundefined
        idx = self.get_index(name)
        if idx == -1000:
            return newundefined()

        return self.get_by_index(idx)

    def get_index(self, name):
        from obin.objects import api
        print "get_index", api.to_native_string(name)
        try:
            idx = self.property_bindings.get(name)
            return idx
        except Exception as e:
            print "get_index Exception", e
            for k in self.property_bindings:
                print api.to_native_string(k),
            return -1000

    def set_by_index(self, idx, value):
        self.property_values.set(idx, value)

    def get_by_index(self, idx):
        print "Slots.get_by_index", idx
        return self.property_values.at(idx)

    def set(self, name, value):
        from obin.objects.space import isany
        assert isany(name)
        assert isany(value)
        idx = self.get_index(name)
        self.set_by_index(idx, value)

    def add(self, name, value):
        from obin.objects.space import isany
        assert isany(name)
        assert isany(value)
        from obin.objects import api
        print "Slots_ass", api.to_native_string(name), api.to_native_string(value)
        idx = self.get_index(name)
        # print "Slots_add, IDX", idx
        if idx == -1000:
            idx = self.index
            self.property_bindings.set(name, idx)
            self.index += 1

        # print "Slots_add, IDX >>", idx
        self.property_values.ensure_size(idx + 1)
        # if idx >= self.property_values.length():
        #     values = self.property_values.values()
        #     values = values + ([None] * (1 + idx - len(values)))
        #     self.property_values.set_values(values)

        self.set_by_index(idx, value)
        return idx

    def delete(self, name):
        idx = self.get_index(name)
        if idx is -1000:
            return

        assert idx >= 0
        self.property_values.exclude_index(idx)
        del self.property_bindings[name]


def newslots(values, bindings, index):
    slots = Slots()
    slots.property_bindings = bindings
    slots.property_values = values
    slots.index = index
    return slots

def newslots_with_size(size):
    return newslots(newvector([None] * size), newhashtable(), 0)

def newslots_empty():
    return newslots(newvector([]), newhashtable(), 0)

def newslots_with_values_from_slots(values, protoslots):
    l = protoslots.length()
    size = values.length()
    diff = l - size
    assert diff >= 0
    if diff > 0:
        values.append_value_multiple_times(None, diff)

    bindings = protoslots.property_bindings.copy()
    index = protoslots.index
    return newslots(values, bindings, index)

