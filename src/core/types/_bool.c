#include <obin.h>

ObinAny obin_bool_new(obin_bool condition){
	if(condition){
		return ObinTrue;
	}

	return ObinFalse;
}

ObinNativeTraits* obin_bool_traits() {
	return NULL;
}