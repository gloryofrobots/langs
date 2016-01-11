from obin.runtime.routine import complete_native_routine
from obin.objects import api
from obin.objects import space
from rpython.rlib.rstring import UnicodeBuilder
from obin.runistr import encode_unicode_utf8

def setup(process, module, stdlib):
    _install(process, module, stdlib)
    _specify(process, module, stdlib)

def _install(process, module, stdlib):

    generics = stdlib.generics
    # AUTIGENERATED generic_gen.py
    api.put(module, generics.Add.name, generics.Add)
    api.put(module, generics.Sub.name, generics.Sub)
    api.put(module, generics.Mul.name, generics.Mul)
    api.put(module, generics.Div.name, generics.Div)
    api.put(module, generics.Mod.name, generics.Mod)
    api.put(module, generics.UnaryPlus.name, generics.UnaryPlus)
    api.put(module, generics.UnaryMinus.name, generics.UnaryMinus)
    api.put(module, generics.Not.name, generics.Not)
    api.put(module, generics.Equal.name, generics.Equal)
    api.put(module, generics.NotEqual.name, generics.NotEqual)
    api.put(module, generics.Compare.name, generics.Compare)
    api.put(module, generics.In.name, generics.In)
    api.put(module, generics.GreaterThen.name, generics.GreaterThen)
    api.put(module, generics.GreaterEqual.name, generics.GreaterEqual)
    api.put(module, generics.BitNot.name, generics.BitNot)
    api.put(module, generics.BitOr.name, generics.BitOr)
    api.put(module, generics.BitXor.name, generics.BitXor)
    api.put(module, generics.BitAnd.name, generics.BitAnd)
    api.put(module, generics.LeftShift.name, generics.LeftShift)
    api.put(module, generics.RightShift.name, generics.RightShift)
    api.put(module, generics.UnsignedRightShift.name, generics.UnsignedRightShift)
    api.put(module, generics.Len.name, generics.Len)
    api.put(module, generics.Str.name, generics.Str)
    api.put(module, generics.List.name, generics.List)


def _specify(process, module, stdlib):
    import obin.builtins.internals.wrappers as wrappers
    from obin.objects.types.dispatch.generic import specify_single
    from obin.objects.space import newtuple, newnativefunc, newstring
    generics = stdlib.generics
    traits = stdlib.traits

    # AUTOGENERATED
    specify_single(process, generics.Add,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"add_i_i"), wrappers.builtin_add_i_i, 2))

    specify_single(process, generics.Add,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"add_f_f"), wrappers.builtin_add_f_f, 2))

    specify_single(process, generics.Add,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"add_n_n"), wrappers.builtin_add_n_n, 2))

    specify_single(process, generics.Sub,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"sub_i_i"), wrappers.builtin_sub_i_i, 2))

    specify_single(process, generics.Sub,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"sub_f_f"), wrappers.builtin_sub_f_f, 2))

    specify_single(process, generics.Sub,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"sub_n_n"), wrappers.builtin_sub_n_n, 2))

    specify_single(process, generics.Mul,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"mult_i_i"), wrappers.builtin_mult_i_i, 2))

    specify_single(process, generics.Mul,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"mult_f_f"), wrappers.builtin_mult_f_f, 2))

    specify_single(process, generics.Mul,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"mult_n_n"), wrappers.builtin_mult_n_n, 2))

    specify_single(process, generics.Div,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"div_i_i"), wrappers.builtin_div_i_i, 2))

    specify_single(process, generics.Div,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"div_f_f"), wrappers.builtin_div_f_f, 2))

    specify_single(process, generics.Div,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"div_n_n"), wrappers.builtin_div_n_n, 2))

    specify_single(process, generics.Mod,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"mod_f_f"), wrappers.builtin_mod_f_f, 2))

    specify_single(process, generics.Mod,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"mod_n_n"), wrappers.builtin_mod_n_n, 2))

    specify_single(process, generics.UnaryPlus,
                 newtuple([traits.Number, ]),
                 newnativefunc(newstring(u"uplus_n"), wrappers.builtin_uplus_n, 1))

    specify_single(process, generics.UnaryMinus,
                 newtuple([traits.Integer, ]),
                 newnativefunc(newstring(u"uminus_i"), wrappers.builtin_uminus_i, 1))

    specify_single(process, generics.UnaryMinus,
                 newtuple([traits.Float, ]),
                 newnativefunc(newstring(u"uminus_f"), wrappers.builtin_uminus_f, 1))

    specify_single(process, generics.UnaryMinus,
                 newtuple([traits.Number, ]),
                 newnativefunc(newstring(u"uminus_n"), wrappers.builtin_uminus_n, 1))

    specify_single(process, generics.Not,
                 newtuple([traits.Any, ]),
                 newnativefunc(newstring(u"not_w"), wrappers.builtin_not_w, 1))

    specify_single(process, generics.Equal,
                 newtuple([traits.Any, traits.Any, ]),
                 newnativefunc(newstring(u"eq_w"), wrappers.builtin_eq_w, 2))

    specify_single(process, generics.NotEqual,
                 newtuple([traits.Any, traits.Any, ]),
                 newnativefunc(newstring(u"noteq_w"), wrappers.builtin_noteq_w, 2))

    specify_single(process, generics.In,
                 newtuple([traits.Any, traits.Any, ]),
                 newnativefunc(newstring(u"in_w"), wrappers.builtin_in_w, 2))

    specify_single(process, generics.GreaterThen,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"compare_gt_i_i"), wrappers.builtin_compare_gt_i_i, 2))

    specify_single(process, generics.GreaterThen,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"compare_gt_f_f"), wrappers.builtin_compare_gt_f_f, 2))

    specify_single(process, generics.GreaterThen,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"compare_gt_n_n"), wrappers.builtin_compare_gt_n_n, 2))

    specify_single(process, generics.GreaterEqual,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"compare_ge_i_i"), wrappers.builtin_compare_ge_i_i, 2))

    specify_single(process, generics.GreaterEqual,
                 newtuple([traits.Float, traits.Float, ]),
                 newnativefunc(newstring(u"compare_ge_f_f"), wrappers.builtin_compare_ge_f_f, 2))

    specify_single(process, generics.GreaterEqual,
                 newtuple([traits.Number, traits.Number, ]),
                 newnativefunc(newstring(u"compare_ge_n_n"), wrappers.builtin_compare_ge_n_n, 2))

    specify_single(process, generics.BitNot,
                 newtuple([traits.Integer, ]),
                 newnativefunc(newstring(u"bitnot_i"), wrappers.builtin_bitnot_i, 1))

    specify_single(process, generics.BitOr,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"bitor_i_i"), wrappers.builtin_bitor_i_i, 2))

    specify_single(process, generics.BitXor,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"bitxor_i_i"), wrappers.builtin_bitxor_i_i, 2))

    specify_single(process, generics.BitAnd,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"bitand_i_i"), wrappers.builtin_bitand_i_i, 2))

    specify_single(process, generics.LeftShift,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"lsh_i_i"), wrappers.builtin_lsh_i_i, 2))

    specify_single(process, generics.RightShift,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"rsh_i_i"), wrappers.builtin_rsh_i_i, 2))

    specify_single(process, generics.UnsignedRightShift,
                 newtuple([traits.Integer, traits.Integer, ]),
                 newnativefunc(newstring(u"ursh_i_i"), wrappers.builtin_ursh_i_i, 2))

    specify_single(process, generics.Len,
                 newtuple([traits.Any, ]),
                 newnativefunc(newstring(u"len_w"), wrappers.builtin_len_w, 1))

    specify_single(process, generics.Str,
                 newtuple([traits.Any, ]),
                 newnativefunc(newstring(u"str_w"), wrappers.builtin_str_w, 1))

    specify_single(process, generics.List,
                 newtuple([traits.Vector, ]),
                 newnativefunc(newstring(u"plist_vec"), wrappers.builtin_plist_vec, 1))

    specify_single(process, generics.List,
                 newtuple([traits.Tuple, ]),
                 newnativefunc(newstring(u"plist_tuple"), wrappers.builtin_plist_tuple, 1))