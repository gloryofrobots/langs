from obin.runtime.exception import JsReferenceError
#from pypy.rlib import jit


class Reference(object):
    _immutable_fields_ = ['base_env', 'base_value', 'referenced']

    def __init__(self, base_value=None, base_env=None, referenced=None):
        self.base_env = base_env
        self.base_value = base_value
        self.referenced = referenced

    def get_base(self):
        return self.base_value

    # XXX passing identifier is a obscure hack but cfbolz sayz so!
    def get_referenced_name(self, identifier=None):
        if identifier is not None:
            return identifier
        return self.referenced

    def has_primitive_base(self):
        b = self.base_value
        from obin.objects.object import W_Boolean, W_String, W_Number
        if isinstance(b, W_Boolean) or isinstance(b, W_String) or isinstance(b, W_Number):
            return True
        return False

    def is_property_reference(self):
        from obin.objects.object import W_BasicObject
        if isinstance(self.base_value, W_BasicObject) or self.has_primitive_base() is True:
            return True
        return False

    def is_unresolvable_reference(self):
        if self.base_value is None and self.base_env is None:
            return True
        return False

    def get_value(self, identifier=None):
        return get_value(self, identifier)

    def put_value(self, value, identifier=None):
        put_value(self, value, identifier)


# 8.7.1
def get_value(v, identifier=None):
    if not isinstance(v, Reference):
        return v

    if v.is_unresolvable_reference():
        referenced = v.get_referenced_name()
        raise JsReferenceError(referenced)

    if v.is_property_reference():
        raise NotImplementedError('8.7.1 4.')
    else:
        base_env = v.base_env
        from obin.runtime.lexical_environment import EnvironmentRecord
        assert isinstance(base_env, EnvironmentRecord)
        name = v.get_referenced_name(identifier)
        return base_env.get_binding_value(name)


# 8.7.2
def put_value(v, w, identifier):
    if not isinstance(v, Reference):
        raise JsReferenceError('unresolvable reference')

    if v.is_unresolvable_reference():
        referenced = v.get_referenced_name()
        raise JsReferenceError(referenced)
    elif v.is_property_reference():
        raise NotImplementedError('8.7.2 4.')
    else:
        base_env = v.base_env
        from obin.runtime.lexical_environment import EnvironmentRecord
        assert isinstance(base_env, EnvironmentRecord)
        name = v.get_referenced_name(identifier)
        base_env.set_binding(name, w)
