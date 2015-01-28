#ifndef OBIN_OCONTEXT_H_
#define OBIN_OCONTEXT_H_
#include "obuiltin.h"

typedef struct {
	ObinAny Nil;
	ObinAny True;
	ObinAny False;
	ObinAny Nothing;
	ObinAny PrintSeparator;
	ObinAny Empty;
} ObinInternalStrings;

typedef struct {
	ObinInternalStrings internal_strings;
} ObinContext;

ObinContext* obin_ctx_get();
#endif /* OCONTEXT_H_ */