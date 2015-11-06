from obin.runtime.reference import Reference
from obin.objects import api
from obin.objects.object_space import isstring

def get_identifier_reference(lex, identifier):
    if lex is None:
        return Reference(referenced=identifier)

    exists = lex.has_binding(identifier)
    if exists:
        ref = Reference(base_env=lex, referenced=identifier)
        return ref
    else:
        outer = lex.outer_environment
        return get_identifier_reference(outer, identifier)

class LexicalEnvironment(object):
    _immutable_fields_ = ['outer_environment']

    def __init__(self, outer_environment=None):
        assert isinstance(outer_environment, LexicalEnvironment) or outer_environment is None
        self.outer_environment = outer_environment

    def get_identifier_reference(self, identifier):
        return get_identifier_reference(self, identifier)

    def has_binding(self, identifier):
        return False

    def set_binding(self, identifier, value):
        raise NotImplementedError

    def get_binding_value(self, identifier):
        raise NotImplementedError


class DeclarativeEnvironment(LexicalEnvironment):
    _immutable_fields_ = ['_binding_slots_', '_binding_resize_', 'outer_environment']

    def __init__(self, outer_environment, env_size):
        from obin.objects.datastructs import Slots
        LexicalEnvironment.__init__(self, outer_environment)
        self.bindings = Slots(env_size)

    def has_binding(self, identifier):
        return self.bindings.contains(identifier)

    def _get_binding(self, name):
        return self.bindings.get(name)

    def _set_binding(self, name, value):
        self.bindings.add(name, value)

    def _del_binding(self, name):
        self.bindings.delete(name)

    # 10.2.1.1.3
    def set_binding(self, identifier, value):
        assert isstring(identifier)
        self._set_binding(identifier, value)

    # 10.2.1.1.4
    def get_binding_value(self, identifier):
        assert isstring(identifier)
        if not self.has_binding(identifier):
            from obin.runtime.exception import ObinReferenceError
            raise ObinReferenceError(identifier)

        return self._get_binding(identifier)


class ObjectEnvironment(LexicalEnvironment):
    _immutable_fields_ = ['binding_object']

    def __init__(self, obj, outer_environment=None):
        LexicalEnvironment.__init__(self, outer_environment)
        self.binding_object = obj

    # 10.2.1.2.1
    def has_binding(self, n):
        return self.binding_object.has(n)

    # 10.2.1.2.3
    def set_binding(self, n, v):
        api.put(self.binding_object, n, v)

    # 10.2.1.2.4
    def get_binding_value(self, n):
        return api.at(self.binding_object, n)


