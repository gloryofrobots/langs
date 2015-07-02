/*EACH Embedded type must have its own trait  delete this method afterwords*/

ObinAny obin_tostring(ObinState* state, ObinAny any) {
	ObinNativeTraits* traits;
	obin_method method;

	switch (any.type) {
	case EOBIN_TYPE_TRUE:
		return state->interns.strings.True;
		break;
	case EOBIN_TYPE_FALSE:
		return state->interns.strings.False;
		break;
	case EOBIN_TYPE_NIL:
		return state->interns.strings.Nil;
		break;
	case EOBIN_TYPE_NOTHING:
		return state->interns.strings.Nothing;
		break;

	default:
		method = _base(any, __tostring__);
		if(!method) {
				return obin_raise_type_error(state, "__tostring__ must be supported", any);
		}

		return method(state, any);
	}
}