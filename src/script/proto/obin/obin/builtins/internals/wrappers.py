#################### WRAPPERS #################################################
from obin.runtime.routine import complete_native_routine


@complete_native_routine
def builtin_add_i_i(process, routine):
    from obin.builtins.internals.operations import add_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return add_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_add_f_f(process, routine):
    from obin.builtins.internals.operations import add_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return add_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_add_n_n(process, routine):
    from obin.builtins.internals.operations import add_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return add_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_sub_i_i(process, routine):
    from obin.builtins.internals.operations import sub_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return sub_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_sub_f_f(process, routine):
    from obin.builtins.internals.operations import sub_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return sub_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_sub_n_n(process, routine):
    from obin.builtins.internals.operations import sub_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return sub_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_mult_i_i(process, routine):
    from obin.builtins.internals.operations import mult_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return mult_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_mult_f_f(process, routine):
    from obin.builtins.internals.operations import mult_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return mult_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_mult_n_n(process, routine):
    from obin.builtins.internals.operations import mult_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return mult_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_div_i_i(process, routine):
    from obin.builtins.internals.operations import div_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return div_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_div_f_f(process, routine):
    from obin.builtins.internals.operations import div_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return div_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_div_n_n(process, routine):
    from obin.builtins.internals.operations import div_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return div_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_mod_f_f(process, routine):
    from obin.builtins.internals.operations import mod_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return mod_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_mod_n_n(process, routine):
    from obin.builtins.internals.operations import mod_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return mod_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_uplus_n(process, routine):
    from obin.builtins.internals.operations import uplus_n
    arg1 = routine.get_arg(0)
    return uplus_n(process, arg1)


@complete_native_routine
def builtin_uminus_i(process, routine):
    from obin.builtins.internals.operations import uminus_i
    arg1 = routine.get_arg(0)
    return uminus_i(process, arg1)


@complete_native_routine
def builtin_uminus_f(process, routine):
    from obin.builtins.internals.operations import uminus_f
    arg1 = routine.get_arg(0)
    return uminus_f(process, arg1)


@complete_native_routine
def builtin_uminus_n(process, routine):
    from obin.builtins.internals.operations import uminus_n
    arg1 = routine.get_arg(0)
    return uminus_n(process, arg1)


@complete_native_routine
def builtin_not_w(process, routine):
    from obin.builtins.internals.operations import not_w
    arg1 = routine.get_arg(0)
    return not_w(process, arg1)


@complete_native_routine
def builtin_eq_w(process, routine):
    from obin.builtins.internals.operations import eq_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return eq_w(process, arg1, arg2)


@complete_native_routine
def builtin_noteq_w(process, routine):
    from obin.builtins.internals.operations import noteq_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return noteq_w(process, arg1, arg2)


@complete_native_routine
def builtin_in_w(process, routine):
    from obin.builtins.internals.operations import in_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return in_w(process, arg1, arg2)


@complete_native_routine
def builtin_notin_w(process, routine):
    from obin.builtins.internals.operations import notin_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return notin_w(process, arg1, arg2)


@complete_native_routine
def builtin_compare_gt_i_i(process, routine):
    from obin.builtins.internals.operations import compare_gt_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return compare_gt_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_compare_gt_f_f(process, routine):
    from obin.builtins.internals.operations import compare_gt_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return compare_gt_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_compare_gt_n_n(process, routine):
    from obin.builtins.internals.operations import compare_gt_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return compare_gt_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_compare_ge_i_i(process, routine):
    from obin.builtins.internals.operations import compare_ge_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return compare_ge_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_compare_ge_f_f(process, routine):
    from obin.builtins.internals.operations import compare_ge_f_f
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return compare_ge_f_f(process, arg1, arg2)


@complete_native_routine
def builtin_compare_ge_n_n(process, routine):
    from obin.builtins.internals.operations import compare_ge_n_n
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return compare_ge_n_n(process, arg1, arg2)


@complete_native_routine
def builtin_bitnot_i(process, routine):
    from obin.builtins.internals.operations import bitnot_i
    arg1 = routine.get_arg(0)
    return bitnot_i(process, arg1)


@complete_native_routine
def builtin_bitor_i_i(process, routine):
    from obin.builtins.internals.operations import bitor_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return bitor_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_bitxor_i_i(process, routine):
    from obin.builtins.internals.operations import bitxor_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return bitxor_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_bitand_i_i(process, routine):
    from obin.builtins.internals.operations import bitand_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return bitand_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_lsh_i_i(process, routine):
    from obin.builtins.internals.operations import lsh_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return lsh_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_rsh_i_i(process, routine):
    from obin.builtins.internals.operations import rsh_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return rsh_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_ursh_i_i(process, routine):
    from obin.builtins.internals.operations import ursh_i_i
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return ursh_i_i(process, arg1, arg2)


@complete_native_routine
def builtin_as_w_w(process, routine):
    from obin.builtins.internals.operations import as_w_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return as_w_w(process, arg1, arg2)


@complete_native_routine
def builtin_kindof_w_w(process, routine):
    from obin.builtins.internals.operations import kindof_w_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return kindof_w_w(process, arg1, arg2)


@complete_native_routine
def builtin_is_w_w(process, routine):
    from obin.builtins.internals.operations import is_w_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return is_w_w(process, arg1, arg2)


@complete_native_routine
def builtin_isnot_w_w(process, routine):
    from obin.builtins.internals.operations import isnot_w_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return isnot_w_w(process, arg1, arg2)


@complete_native_routine
def builtin_isa_w_w(process, routine):
    from obin.builtins.internals.operations import isa_w_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return isa_w_w(process, arg1, arg2)


@complete_native_routine
def builtin_nota_w_w(process, routine):
    from obin.builtins.internals.operations import nota_w_w
    arg1 = routine.get_arg(0)
    arg2 = routine.get_arg(1)
    return nota_w_w(process, arg1, arg2)


@complete_native_routine
def builtin_len_w(process, routine):
    from obin.builtins.internals.operations import len_w
    arg1 = routine.get_arg(0)
    return len_w(process, arg1)


@complete_native_routine
def builtin_str_w(process, routine):
    from obin.builtins.internals.operations import str_w
    arg1 = routine.get_arg(0)
    return str_w(process, arg1)


@complete_native_routine
def builtin_plist_tuple(process, routine):
    from obin.types.plist import plist_tuple
    arg1 = routine.get_arg(0)
    return plist_tuple(process, arg1)
