#include <obin.h>

OBIN_MODULE_DECLARE(ERROR);

obin_bool obin_module_error_init(ObinState* state) {
	OBIN_MODULE_INIT(ERROR);
	return OTRUE;
}

ObinAny obin_error_new(ObinState* state, ObinAny proto, obin_string message,
		ObinAny args) {
	OBIN_MODULE_CHECK(ERROR);
	obin_panic(message);
	return ObinNothing;
}

ObinAny obin_raise(ObinState* state, ObinAny exception) {
	obin_abort();
	return ObinNothing;
}