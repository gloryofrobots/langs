from obin.objects import api

class ObinException(Exception):
    def __init__(self, message):
        assert isinstance(message, unicode)
        self.message = message

    def _msg(self):
        return self.message

    def msg(self):
        from obin.objects.space import newstring
        return newstring(self._msg())

    def __str__(self):
        return self._msg()

    def __repr__(self):
        return self.__str__()

class ObinImportError(ObinException):
    pass

class ObinRuntimeError(ObinException):
    pass

class ObinTraitError(ObinException):
    def __init__(self, message, trait):
        self.message = message
        self.trait = trait

    def _msg(self):
        return u'TraitError : %s %s ' % (self.message, self.trait)

class ObinTypeError(ObinException):
    def __init__(self, value):
        # assert isinstance(value, unicode)
        self.value = value

    def _msg(self):
        return u'TypeError : ' + self.value  # % (self.value, )


class ObinReferenceError(ObinException):
    def __init__(self, identifier):
        self.identifier = api.to_native_unicode(identifier)

    def _msg(self):
        return u'ReferenceError: ' + self.identifier + u' is not defined'


class ObinRangeError(ObinException):
    def __init__(self, value):
        self.value = value

    def _msg(self):
        return u'RangeError: %s' % (self.value,)


class ObinKeyError(ObinRangeError):
    def __init__(self, value):
        self.value = value

    def _msg(self):
        return u'KeyError: %s' % (self.value,)


class ObinInvokeError(ObinRangeError):
    def __init__(self, value):
        self.value = value

    def _msg(self):
        return u'InvokeError: expected argument with number %s' % (str(self.value),)


class ObinMethodInvokeError(ObinRangeError):
    def __init__(self, method, args):
        self.arguments = args
        self.method = method

    def _msg(self):
        return u'Method Invoke Error:  Can\'t determine method "%s" for arguments %s' % (str(self.method._name_), str(self.arguments),)


class ObinMethodSpecialisationError(ObinRangeError):
    def __init__(self, method, message):
        self.method = method
        self.message = message

    def _msg(self):
        return u'Method Specialisation Error:  Can\'t specialize method "%s" %s' % (str(self.method._name_), str(self.message),)


