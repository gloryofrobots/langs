from arza.types.root import W_Hashable
from arza.types import api, space, plist, tuples
from arza.misc import platform
from arza.runtime import error


class W_Record(W_Hashable):
    def __init__(self, type, values):
        W_Hashable.__init__(self)
        self.values = values
        self.type = type
        self.current_type = type

    def _call_(self, process, args):
        new_args = space.newtuple([self, args])
        api.call(process, process.std.functions.call, new_args)

    def _to_string_(self):
        res = []

        for f in self.type.fields:
            i = api.at(self.type.descriptors, f)
            v = api.at_index(self.values, api.to_i(i))
            res.append("%s = %s" % (api.to_s(f), api.to_s(v)))

        return "<record: %s (%s)>" % (api.to_s(self.type), ", ".join(res))

    def _to_repr_(self):
        res = []

        for f in self.type.fields:
            i = api.at(self.type.descriptors, f)
            v = api.at_index(self.values, api.to_i(i))
            res.append("%s = %s" % (api.to_r(f), api.to_r(v)))

        return "<record: %s (%s)>" % (api.to_r(self.type), ", ".join(res))

    def _cast_(self, process, _type):
        if api.equal_b(self.type, _type):
            # do not return self because current_type may be downcasted
            return W_Record(self.type, self.values)

        supertype = self.type.supertype
        while space.isdatatype(supertype):
            if api.equal_b(supertype, _type):
                rec = W_Record(self.type, self.values)
                rec.current_type = _type
                return rec

            supertype = supertype.supertype

        return error.throw_3(error.Errors.TYPE_ERROR, space.newstring(u"Invalid cast operation"), self.type, _type)

    def _type_(self, process):
        return self.current_type

    def _at_(self, name):
        if space.isint(name):
            return self._at_index_(api.to_i(name))

        idx = api.lookup(self.type.descriptors, name, space.newvoid())
        if space.isvoid(idx):
            error.throw_1(error.Errors.KEY_ERROR, name)
        return api.at(self.values, idx)

    def _contains_(self, name):
        if space.isint(name):
            return self._at_index_(api.to_i(name))

        idx = api.lookup(self.type.descriptors, name, space.newvoid())
        value = api.lookup(self.values, idx, space.newvoid())
        return not space.isvoid(value)

    def _at_index_(self, idx):
        # accessing protected method instead of api.at_index for avoiding multiple 0 < idx < length check
        return self.values._at_index_(idx)

    def _put_(self, key, value):
        if space.isint(key):
            key_i = api.to_i(key)
            if key_i < 0 or key_i > api.length_i(self.values):
                error.throw_1(error.Errors.KEY_ERROR, key)
            idx = key
        else:
            idx = api.lookup(self.type.descriptors, key, space.newvoid())
            if space.isvoid(idx):
                error.throw_1(error.Errors.KEY_ERROR, key)

        newvalues = api.put(self.values, idx, value)
        return W_Record(self.type, newvalues)

    def _length_(self):
        return api.length_i(self.values)

    def _equal_(self, other):
        if not isinstance(other, W_Record):
            return False
        if not api.equal_b(self.type, other.type):
            return False
        return api.equal_b(self.values, other.values)

    def keys(self):
        return self.type.fields

    def values(self):
        return self.values

    def index_of(self, val):
        idx = self.values.index(val)
        if platform.is_absent_index(idx):
            error.throw_1(error.Errors.VALUE_ERROR, val)
        return idx


def descriptors(fields):
    d = space.newassocarray()
    for i in range(len(fields)):
        f = fields[i]
        d = api.put(d, f, space.newint(i))
    return d


class W_BaseDatatype(W_Hashable):
    def __init__(self, name, supertype, interfaces):
        W_Hashable.__init__(self)
        # list of all known interfaces
        self.interfaces = space.newlist([])
        # 'is_implemented' lookup cache
        self.interfaces_table = space.newassocarray()
        self.name = name
        self.supertype = supertype
        for interface in interfaces:
            self.register_interface(interface)

    def is_subtype_of(self, _type):
        if api.equal_b(self, _type):
            return True

        supertype = self.supertype
        while space.isdatatype(supertype):
            if api.equal_b(supertype, _type):
                return True

            supertype = supertype.supertype

        return False

    def _register_interface(self, iface):
        if self._has_interface(iface):
            return

        api.put(self.interfaces_table, iface, space.newbool(True))
        self.interfaces = plist.cons(iface, self.interfaces)
        iface.register_type(self)

    def register_interface(self, iface):
        for sub in iface.sub_interfaces:
            if not self.is_interface_implemented(sub):
                self._register_interface(sub)
        self._register_interface(iface)

    def _has_interface(self, iface):
        return plist.contains(self.interfaces, iface)

    def is_interface_implemented(self, iface):
        _type = self
        while space.isdatatype(_type):
            old = api.lookup(_type.interfaces_table, iface, space.newvoid())
            if not space.isvoid(old):
                return api.to_b(old)
            else:
                status = _can_implement(_type, iface)
                api.put(self.interfaces_table, iface, space.newbool(status))
                if status:
                    self.register_interface(iface)
                    return status

            _type = _type.supertype

        api.put(self.interfaces_table, iface, space.newbool(False))
        return False

    def _compute_hash_(self):
        return int((1 - platform.random()) * 10000000)

    def _equal_(self, other):
        return other is self


def _can_implement(_type, interface):
    if interface.count_generics() == 0:
        return False

    interfaces = space.newlist([])
    for r in interface.generics:
        generic = api.first(r)
        position = api.second(r)
        idx = api.to_i(position)
        if not generic.is_implemented_for_type(_type, interfaces, idx, True):
            return False
    return True


class W_AbstractType(W_BaseDatatype):
    def __init__(self, name, supertype):
        W_BaseDatatype.__init__(self, name, supertype, plist.empty())

    def _dispatch_(self, process):
        return self

    def _type_(self, process):
        return process.std.types.Datatype

    def _to_string_(self):
        return "<abstract type %s>" % (api.to_s(self.name))

    def _to_repr_(self):
        return api.to_s(self.name)


class W_ConcreteType(W_BaseDatatype):
    def __init__(self, name, supertype, fields, initializer):
        W_BaseDatatype.__init__(self, name, supertype, plist.empty())
        self.fields = fields
        self.arity = api.length_i(self.fields)
        self.descriptors = descriptors(self.fields)
        self.initializer = initializer

    def validate(self, process, record):
        if not space.isrecord(record) or record.type is not self:
            error.throw_4(error.Errors.CONSTRUCTOR_ERROR,
                          space.newstring(u"Constructor must return record of type"),
                          self,
                          space.newstring(u"instead got"),
                          api.get_type(process, record))

        for f in self.fields:
            if not api.contains_b(record, f):
                error.throw_2(error.Errors.CONSTRUCTOR_ERROR,
                              space.newstring(u"Uninitialized record field"),
                              f)
        return record

    def on_result(self, process, value):
        self.validate(process, value)
        return value

    def _to_routine_(self, stack, args):
        # print "TO ROUTINE"
        from arza.runtime.routine.routine import create_callback_routine
        routine = create_callback_routine(stack, self.on_result, None, self.initializer, args)
        return routine

    def _call_(self, process, args):

        if self.initializer is None:
            length = api.length_i(args)
            if length != self.arity:
                error.throw_4(error.Errors.CONSTRUCTOR_ERROR,
                              space.newstring(u"Invalid count of data for initialization of type"),
                              self,
                              api.length(self.fields),
                              args)

            return W_Record(self, space.newpvector(args.to_l()))

        units = space.newpvector([space.newvoid() for _ in range(api.length_i(self.fields))])
        record = W_Record(self, units)
        new_args = tuples.prepend(args, record)
        # new_args = tuples.concat(space.newtuple([self, record]), args)
        process.call_object(self, new_args)
        # api.call(process, self.initializer, new_args)

    def _type_(self, process):
        return process.std.types.Datatype

    def _to_string_(self):
        return "<datatype %s>" % (api.to_s(self.name))

    def _to_repr_(self):
        return self._to_string_()


def get_fields(t):
    error.affirm_type(t, space.isconcretetype)
    return t.fields


def get_supertype(t):
    error.affirm_type(t, space.isdatatype)
    return t.supertype


def get_init(t):
    error.affirm_type(t, space.isconcretetype)
    if t.initializer is None:
        return space.newunit()

    return t.initializer


def has_init(t):
    error.affirm_type(t, space.isconcretetype)
    return t.initializer is not None


def record_index_of(record, obj):
    error.affirm_type(record, space.isrecord)
    return record.index_of(obj)


def record_keys(record):
    error.affirm_type(record, space.isrecord)
    return record.keys()


def record_values(record):
    error.affirm_type(record, space.isrecord)
    return record.values()


def derive(process, t, interfaces):
    _derive(process, t, interfaces, False)


def derive_strict(process, t, interfaces):
    _derive(process, t, interfaces, True)


def _derive(process, t, interfaces, strictmode):
    error.affirm_type(t, space.isdatatype)
    error.affirm_type(interfaces, space.islist)
    to_be_implemented = []
    # bp = 1
    # api.d.pbp(bp, "================", t)
    # api.d.pbp(bp, interfaces)
    # api.d.pbp(bp, t.interfaces)
    old_interfaces = t.interfaces
    for interface in interfaces:
        # api.d.pbp(bp, "I", interface)
        if t.is_interface_implemented(interface):
            if process.std.interfaces.is_default_derivable_interface(interface):
                continue
            else:
                if strictmode:
                    continue
                else:
                    # INTERNAL CHECK
                    return error.throw_3(
                        error.Errors.IMPLEMENTATION_ERROR,
                        space.newstring(u"Interface already implemented"),
                        t,
                        interface
                    )

        # derive according to future interfaces
        new_interfaces = plist.remove(interfaces, interface)
        maybe_interfaces = plist.concat(new_interfaces, old_interfaces)

        error.affirm_type(interface, space.isinterface)
        for r in interface.generics:
            generic = api.first(r)
            position = api.second(r)
            idx = api.to_i(position)
            # api.d.pbp(bp, "G", generic, idx, maybe_interfaces)
            if not generic.is_implemented_for_type(t, maybe_interfaces, idx, strictmode):
                error.throw_5(
                    error.Errors.IMPLEMENTATION_ERROR,
                    space.newstring(u"Not implemented interface method"),
                    t,
                    interface,
                    generic,
                    position
                )

        to_be_implemented.append(interface)

    for interface in to_be_implemented:
        t.register_interface(interface)


def newabstractdatatype(name, supertype):
    return W_AbstractType(name, supertype)


def newrecordtype(name, supertype, fields):
    if space.isconcretetype(supertype):
        fields = plist.concat(supertype.fields, fields)

    return W_ConcreteType(name, supertype, fields, None)


def newtype(process, name, supertype, fields, initializer):
    real_fields = []
    if space.isconcretetype(supertype):
        for f in supertype.fields:
            real_fields.append(f)

    for f in fields:
        if space.issymbol(f):
            real_fields.append(f)
        elif space.isconcretetype(f):
            for mf in f.fields:
                real_fields.append(mf)
        else:
            error.throw_2(
                error.Errors.COMPILE_ERROR,
                space.newstring(u"Invalid type mixin"),
                fields,
            )

    fields = space.newlist(real_fields)

    if plist.is_empty(fields):
        if not space.isabstracttype(supertype):
            error.throw_2(
                error.Errors.COMPILE_ERROR,
                space.newstring(u"Supertype must be abstract"),
                supertype,
            )
        _type = W_AbstractType(name, supertype)
    else:
        if not plist.is_hetero(fields):
            error.throw_2(
                error.Errors.COMPILE_ERROR,
                space.newstring(u"Dublicated fields in type declaration"),
                fields,
            )

        if space.isunit(initializer):
            initializer = None
        _type = W_ConcreteType(name, supertype, fields, initializer)

    if process.std.initialized:
        derived = process.std.interfaces.get_derived(_type)
        derive(process, _type, derived)
    return _type


def get_interfaces(process, t):
    error.affirm_type(t, space.isdatatype)
    return t.interfaces
