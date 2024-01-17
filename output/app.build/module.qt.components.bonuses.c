/* Generated code for Python module 'qt$components$bonuses'
 * created by Nuitka version 1.9.5
 *
 * This code is in part copyright 2023 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module_qt$components$bonuses" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_qt$components$bonuses;
PyDictObject *moduledict_qt$components$bonuses;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[126];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[126];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(PyThreadState *tstate) {
    if (constants_created == false) {
        loadConstantsBlob(tstate, &mod_consts[0], UNTRANSLATE("qt.components.bonuses"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 126; i++) {
            mod_consts_hash[i] = DEEP_HASH(tstate, mod_consts[i]);
        }
#endif
    }
}

// We want to be able to initialize the "__main__" constants in any case.
#if 0
void createMainModuleConstants(PyThreadState *tstate) {
    createModuleConstants(tstate);
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_qt$components$bonuses(PyThreadState *tstate) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 126; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(tstate, mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_6bf2c041525e6e64362c99311da263cd;
static PyCodeObject *codeobj_2c75e018e9ac1b4024c4dde109bbdf2c;
static PyCodeObject *codeobj_aefc3212dc3c30828b9bdb225a7b2afa;
static PyCodeObject *codeobj_c6d31f9da8bc34e06ddad249a420ba82;
static PyCodeObject *codeobj_314a5deb612b7e8d61fb4a2a255bbf78;
static PyCodeObject *codeobj_68ce670cce80fe3ce987e15cd74f3c85;
static PyCodeObject *codeobj_bed27f74d7af26fbf540226f0e111d85;
static PyCodeObject *codeobj_a59296a7f8c550f17b41865cc1aa23c7;
static PyCodeObject *codeobj_41196fb28ed1cff61af2ccc3c6c2ae89;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[119]); CHECK_OBJECT(module_filename_obj);
    codeobj_6bf2c041525e6e64362c99311da263cd = MAKE_CODE_OBJECT(module_filename_obj, 1, 0, mod_consts[120], mod_consts[120], NULL, NULL, 0, 0, 0);
    codeobj_2c75e018e9ac1b4024c4dde109bbdf2c = MAKE_CODE_OBJECT(module_filename_obj, 220, 0, mod_consts[117], mod_consts[117], mod_consts[121], NULL, 0, 0, 0);
    codeobj_aefc3212dc3c30828b9bdb225a7b2afa = MAKE_CODE_OBJECT(module_filename_obj, 6, 0, mod_consts[88], mod_consts[88], mod_consts[121], NULL, 0, 0, 0);
    codeobj_c6d31f9da8bc34e06ddad249a420ba82 = MAKE_CODE_OBJECT(module_filename_obj, 20, 0, mod_consts[90], mod_consts[90], mod_consts[121], NULL, 0, 0, 0);
    codeobj_314a5deb612b7e8d61fb4a2a255bbf78 = MAKE_CODE_OBJECT(module_filename_obj, 213, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[105], mod_consts[105], mod_consts[122], NULL, 2, 0, 0);
    codeobj_68ce670cce80fe3ce987e15cd74f3c85 = MAKE_CODE_OBJECT(module_filename_obj, 7, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[1], mod_consts[1], mod_consts[123], mod_consts[121], 1, 0, 0);
    codeobj_bed27f74d7af26fbf540226f0e111d85 = MAKE_CODE_OBJECT(module_filename_obj, 221, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[1], mod_consts[1], mod_consts[123], mod_consts[121], 1, 0, 0);
    codeobj_a59296a7f8c550f17b41865cc1aa23c7 = MAKE_CODE_OBJECT(module_filename_obj, 21, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[1], mod_consts[1], mod_consts[124], mod_consts[121], 1, 0, 0);
    codeobj_41196fb28ed1cff61af2ccc3c6c2ae89 = MAKE_CODE_OBJECT(module_filename_obj, 216, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[86], mod_consts[86], mod_consts[125], NULL, 1, 0, 0);
}

// The module function declarations.
NUITKA_CROSS_MODULE PyObject *impl___main__$$$function__1__mro_entries_conversion(PyThreadState *tstate, PyObject **python_pars);


static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__1___init__(struct Nuitka_CellObject **closure);


static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__2___init__(struct Nuitka_CellObject **closure);


static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__3___getitem__();


static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__4_items();


static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__5___init__(struct Nuitka_CellObject **closure);


// The module function definitions.
static PyObject *impl_qt$components$bonuses$$$function__1___init__(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[0];
    PyObject *var_layout = NULL;
    struct Nuitka_FrameObject *frame_68ce670cce80fe3ce987e15cd74f3c85;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    bool tmp_result;
    static struct Nuitka_FrameObject *cache_frame_68ce670cce80fe3ce987e15cd74f3c85 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_68ce670cce80fe3ce987e15cd74f3c85)) {
        Py_XDECREF(cache_frame_68ce670cce80fe3ce987e15cd74f3c85);

#if _DEBUG_REFCOUNTS
        if (cache_frame_68ce670cce80fe3ce987e15cd74f3c85 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_68ce670cce80fe3ce987e15cd74f3c85 = MAKE_FUNCTION_FRAME(tstate, codeobj_68ce670cce80fe3ce987e15cd74f3c85, module_qt$components$bonuses, sizeof(void *)+sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_68ce670cce80fe3ce987e15cd74f3c85->m_type_description == NULL);
    frame_68ce670cce80fe3ce987e15cd74f3c85 = cache_frame_68ce670cce80fe3ce987e15cd74f3c85;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_68ce670cce80fe3ce987e15cd74f3c85);
    assert(Py_REFCNT(frame_68ce670cce80fe3ce987e15cd74f3c85) == 2);

    // Framed code:
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_type_arg_value_1;
        PyObject *tmp_object_arg_value_1;
        PyObject *tmp_call_result_1;
        if (Nuitka_Cell_GET(self->m_closure[0]) == NULL) {

            FORMAT_UNBOUND_CLOSURE_ERROR(&exception_type, &exception_value, mod_consts[0]);
            exception_tb = NULL;
            NORMALIZE_EXCEPTION(tstate, &exception_type, &exception_value, &exception_tb);
            CHAIN_EXCEPTION(tstate, exception_value);

            exception_lineno = 8;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }

        tmp_type_arg_value_1 = Nuitka_Cell_GET(self->m_closure[0]);
        CHECK_OBJECT(par_self);
        tmp_object_arg_value_1 = par_self;
        tmp_called_instance_1 = BUILTIN_SUPER0(tstate, moduledict_qt$components$bonuses, tmp_type_arg_value_1, tmp_object_arg_value_1);
        if (tmp_called_instance_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 8;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 8;
        tmp_call_result_1 = CALL_METHOD_NO_ARGS(tstate, tmp_called_instance_1, mod_consts[1]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_call_result_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 8;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_called_value_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[2]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[2]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 9;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 9;
        tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_1);
        if (tmp_assign_source_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 9;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        assert(var_layout == NULL);
        var_layout = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_instance_2;
        PyObject *tmp_call_result_2;
        PyObject *tmp_args_element_value_1;
        CHECK_OBJECT(par_self);
        tmp_called_instance_2 = par_self;
        CHECK_OBJECT(var_layout);
        tmp_args_element_value_1 = var_layout;
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 10;
        tmp_call_result_2 = CALL_METHOD_WITH_SINGLE_ARG(tstate, tmp_called_instance_2, mod_consts[3], tmp_args_element_value_1);
        if (tmp_call_result_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 10;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_called_value_2;
        PyObject *tmp_assattr_target_1;
        tmp_called_value_2 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[4]);

        if (unlikely(tmp_called_value_2 == NULL)) {
            tmp_called_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[4]);
        }

        if (tmp_called_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 12;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 12;
        tmp_assattr_value_1 = CALL_FUNCTION_WITH_POSARGS1(tstate, tmp_called_value_2, mod_consts[5]);

        if (tmp_assattr_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 12;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_assattr_target_1 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_1, mod_consts[6], tmp_assattr_value_1);
        Py_DECREF(tmp_assattr_value_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 12;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_3;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_3;
        PyObject *tmp_args_element_value_2;
        PyObject *tmp_expression_value_2;
        CHECK_OBJECT(var_layout);
        tmp_expression_value_1 = var_layout;
        tmp_called_value_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_1, mod_consts[7]);
        if (tmp_called_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 13;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_2 = par_self;
        tmp_args_element_value_2 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_2, mod_consts[6]);
        if (tmp_args_element_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_3);

            exception_lineno = 13;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 13;
        tmp_call_result_3 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_3, tmp_args_element_value_2);
        Py_DECREF(tmp_called_value_3);
        Py_DECREF(tmp_args_element_value_2);
        if (tmp_call_result_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 13;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_3);
    }
    {
        PyObject *tmp_assattr_value_2;
        PyObject *tmp_called_value_4;
        PyObject *tmp_assattr_target_2;
        tmp_called_value_4 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_4 == NULL)) {
            tmp_called_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 14;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 14;
        tmp_assattr_value_2 = CALL_FUNCTION_WITH_ARGS1_VECTORCALL(tstate, tmp_called_value_4, &PyTuple_GET_ITEM(mod_consts[9], 0), mod_consts[10]);
        if (tmp_assattr_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 14;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_assattr_target_2 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_2, mod_consts[11], tmp_assattr_value_2);
        Py_DECREF(tmp_assattr_value_2);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 14;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_5;
        PyObject *tmp_expression_value_3;
        PyObject *tmp_call_result_4;
        PyObject *tmp_args_element_value_3;
        PyObject *tmp_expression_value_4;
        CHECK_OBJECT(var_layout);
        tmp_expression_value_3 = var_layout;
        tmp_called_value_5 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_3, mod_consts[7]);
        if (tmp_called_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 15;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_4 = par_self;
        tmp_args_element_value_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_4, mod_consts[11]);
        if (tmp_args_element_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_5);

            exception_lineno = 15;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 15;
        tmp_call_result_4 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_5, tmp_args_element_value_3);
        Py_DECREF(tmp_called_value_5);
        Py_DECREF(tmp_args_element_value_3);
        if (tmp_call_result_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 15;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_4);
    }
    {
        PyObject *tmp_assattr_value_3;
        PyObject *tmp_called_value_6;
        PyObject *tmp_assattr_target_3;
        tmp_called_value_6 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_6 == NULL)) {
            tmp_called_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 16;
        tmp_assattr_value_3 = CALL_FUNCTION_WITH_ARGS1_VECTORCALL(tstate, tmp_called_value_6, &PyTuple_GET_ITEM(mod_consts[12], 0), mod_consts[10]);
        if (tmp_assattr_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_assattr_target_3 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_3, mod_consts[13], tmp_assattr_value_3);
        Py_DECREF(tmp_assattr_value_3);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_7;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_call_result_5;
        PyObject *tmp_args_element_value_4;
        PyObject *tmp_expression_value_6;
        CHECK_OBJECT(var_layout);
        tmp_expression_value_5 = var_layout;
        tmp_called_value_7 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_5, mod_consts[7]);
        if (tmp_called_value_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 17;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_6 = par_self;
        tmp_args_element_value_4 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_6, mod_consts[13]);
        if (tmp_args_element_value_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_7);

            exception_lineno = 17;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame.f_lineno = 17;
        tmp_call_result_5 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_7, tmp_args_element_value_4);
        Py_DECREF(tmp_called_value_7);
        Py_DECREF(tmp_args_element_value_4);
        if (tmp_call_result_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 17;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_5);
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_68ce670cce80fe3ce987e15cd74f3c85, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_68ce670cce80fe3ce987e15cd74f3c85->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_68ce670cce80fe3ce987e15cd74f3c85, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_68ce670cce80fe3ce987e15cd74f3c85,
        type_description_1,
        par_self,
        var_layout,
        self->m_closure[0]
    );


    // Release cached frame if used for exception.
    if (frame_68ce670cce80fe3ce987e15cd74f3c85 == cache_frame_68ce670cce80fe3ce987e15cd74f3c85) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_68ce670cce80fe3ce987e15cd74f3c85);
        cache_frame_68ce670cce80fe3ce987e15cd74f3c85 = NULL;
    }

    assertFrameObject(frame_68ce670cce80fe3ce987e15cd74f3c85);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto try_except_handler_1;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_layout);
    Py_DECREF(var_layout);
    var_layout = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_layout);
    var_layout = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_qt$components$bonuses$$$function__2___init__(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[0];
    PyObject *var_layout = NULL;
    PyObject *var_tabs = NULL;
    PyObject *var_tab = NULL;
    PyObject *var_tab_layout = NULL;
    struct Nuitka_FrameObject *frame_a59296a7f8c550f17b41865cc1aa23c7;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    bool tmp_result;
    int tmp_res;
    static struct Nuitka_FrameObject *cache_frame_a59296a7f8c550f17b41865cc1aa23c7 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_a59296a7f8c550f17b41865cc1aa23c7)) {
        Py_XDECREF(cache_frame_a59296a7f8c550f17b41865cc1aa23c7);

#if _DEBUG_REFCOUNTS
        if (cache_frame_a59296a7f8c550f17b41865cc1aa23c7 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_a59296a7f8c550f17b41865cc1aa23c7 = MAKE_FUNCTION_FRAME(tstate, codeobj_a59296a7f8c550f17b41865cc1aa23c7, module_qt$components$bonuses, sizeof(void *)+sizeof(void *)+sizeof(void *)+sizeof(void *)+sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_a59296a7f8c550f17b41865cc1aa23c7->m_type_description == NULL);
    frame_a59296a7f8c550f17b41865cc1aa23c7 = cache_frame_a59296a7f8c550f17b41865cc1aa23c7;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_a59296a7f8c550f17b41865cc1aa23c7);
    assert(Py_REFCNT(frame_a59296a7f8c550f17b41865cc1aa23c7) == 2);

    // Framed code:
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_type_arg_value_1;
        PyObject *tmp_object_arg_value_1;
        PyObject *tmp_call_result_1;
        if (Nuitka_Cell_GET(self->m_closure[0]) == NULL) {

            FORMAT_UNBOUND_CLOSURE_ERROR(&exception_type, &exception_value, mod_consts[0]);
            exception_tb = NULL;
            NORMALIZE_EXCEPTION(tstate, &exception_type, &exception_value, &exception_tb);
            CHAIN_EXCEPTION(tstate, exception_value);

            exception_lineno = 22;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }

        tmp_type_arg_value_1 = Nuitka_Cell_GET(self->m_closure[0]);
        CHECK_OBJECT(par_self);
        tmp_object_arg_value_1 = par_self;
        tmp_called_instance_1 = BUILTIN_SUPER0(tstate, moduledict_qt$components$bonuses, tmp_type_arg_value_1, tmp_object_arg_value_1);
        if (tmp_called_instance_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 22;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 22;
        tmp_call_result_1 = CALL_METHOD_NO_ARGS(tstate, tmp_called_instance_1, mod_consts[1]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_call_result_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 22;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_called_value_1;
        PyObject *tmp_args_element_value_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[14]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 23;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_args_element_value_1 = par_self;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 23;
        tmp_assign_source_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_1, tmp_args_element_value_1);
        if (tmp_assign_source_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 23;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        assert(var_layout == NULL);
        var_layout = tmp_assign_source_1;
    }
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = MAKE_DICT_EMPTY();
        CHECK_OBJECT(par_self);
        tmp_assattr_target_1 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_1, mod_consts[15], tmp_assattr_value_1);
        Py_DECREF(tmp_assattr_value_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 25;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_2;
        PyObject *tmp_called_value_2;
        tmp_called_value_2 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[16]);

        if (unlikely(tmp_called_value_2 == NULL)) {
            tmp_called_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[16]);
        }

        if (tmp_called_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 27;
        tmp_assign_source_2 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_2);
        if (tmp_assign_source_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        assert(var_tabs == NULL);
        var_tabs = tmp_assign_source_2;
    }
    {
        PyObject *tmp_called_instance_2;
        PyObject *tmp_call_result_2;
        PyObject *tmp_args_element_value_2;
        CHECK_OBJECT(var_layout);
        tmp_called_instance_2 = var_layout;
        CHECK_OBJECT(var_tabs);
        tmp_args_element_value_2 = var_tabs;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 28;
        tmp_call_result_2 = CALL_METHOD_WITH_SINGLE_ARG(tstate, tmp_called_instance_2, mod_consts[7], tmp_args_element_value_2);
        if (tmp_call_result_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 28;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }
    {
        PyObject *tmp_assign_source_3;
        PyObject *tmp_called_value_3;
        tmp_called_value_3 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_3 == NULL)) {
            tmp_called_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 30;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 30;
        tmp_assign_source_3 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_3);
        if (tmp_assign_source_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 30;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        assert(var_tab == NULL);
        var_tab = tmp_assign_source_3;
    }
    {
        PyObject *tmp_assign_source_4;
        PyObject *tmp_called_value_4;
        PyObject *tmp_args_element_value_3;
        tmp_called_value_4 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_4 == NULL)) {
            tmp_called_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 31;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_3 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 31;
        tmp_assign_source_4 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_4, tmp_args_element_value_3);
        if (tmp_assign_source_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 31;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        assert(var_tab_layout == NULL);
        var_tab_layout = tmp_assign_source_4;
    }
    {
        PyObject *tmp_called_instance_3;
        PyObject *tmp_call_result_3;
        PyObject *tmp_args_element_value_4;
        PyObject *tmp_args_element_value_5;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_3 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_4 = var_tab;
        tmp_args_element_value_5 = mod_consts[20];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 32;
        {
            PyObject *call_args[] = {tmp_args_element_value_4, tmp_args_element_value_5};
            tmp_call_result_3 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_3,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 32;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_3);
    }
    {
        PyObject *tmp_ass_subvalue_1;
        PyObject *tmp_called_value_5;
        PyObject *tmp_args_element_value_6;
        PyObject *tmp_args_element_value_7;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_subscript_value_1;
        PyObject *tmp_ass_subscribed_1;
        PyObject *tmp_expression_value_2;
        PyObject *tmp_ass_subscript_1;
        tmp_called_value_5 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_5 == NULL)) {
            tmp_called_value_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_6 = mod_consts[22];
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_1 = mod_consts[22];
        tmp_args_element_value_7 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_1, tmp_subscript_value_1);
        if (tmp_args_element_value_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 34;
        {
            PyObject *call_args[] = {tmp_args_element_value_6, tmp_args_element_value_7};
            tmp_ass_subvalue_1 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_5, call_args);
        }

        Py_DECREF(tmp_args_element_value_7);
        if (tmp_ass_subvalue_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_2 = par_self;
        tmp_ass_subscribed_1 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_2, mod_consts[15]);
        if (tmp_ass_subscribed_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_1);

            exception_lineno = 34;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_1 = mod_consts[22];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_1, tmp_ass_subscript_1, tmp_ass_subvalue_1);
        Py_DECREF(tmp_ass_subscribed_1);
        Py_DECREF(tmp_ass_subvalue_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_6;
        PyObject *tmp_expression_value_3;
        PyObject *tmp_call_result_4;
        PyObject *tmp_args_element_value_8;
        PyObject *tmp_expression_value_4;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_subscript_value_2;
        PyObject *tmp_args_element_value_9;
        PyObject *tmp_args_element_value_10;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_3 = var_tab_layout;
        tmp_called_value_6 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_3, mod_consts[7]);
        if (tmp_called_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 35;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_5 = par_self;
        tmp_expression_value_4 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_5, mod_consts[15]);
        if (tmp_expression_value_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_6);

            exception_lineno = 35;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_2 = mod_consts[22];
        tmp_args_element_value_8 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_4, tmp_subscript_value_2);
        Py_DECREF(tmp_expression_value_4);
        if (tmp_args_element_value_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_6);

            exception_lineno = 35;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_9 = mod_consts[24];
        tmp_args_element_value_10 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 35;
        {
            PyObject *call_args[] = {tmp_args_element_value_8, tmp_args_element_value_9, tmp_args_element_value_10};
            tmp_call_result_4 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_6, call_args);
        }

        Py_DECREF(tmp_called_value_6);
        Py_DECREF(tmp_args_element_value_8);
        if (tmp_call_result_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 35;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_4);
    }
    {
        PyObject *tmp_ass_subvalue_2;
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        PyObject *tmp_called_value_7;
        PyObject *tmp_args_value_1;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_expression_value_6;
        PyObject *tmp_subscript_value_3;
        PyObject *tmp_kwargs_value_1;
        PyObject *tmp_ass_subscribed_2;
        PyObject *tmp_expression_value_7;
        PyObject *tmp_ass_subscript_2;
        tmp_dict_key_1 = mod_consts[25];
        tmp_called_value_7 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_7 == NULL)) {
            tmp_called_value_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_6 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_6 == NULL)) {
            tmp_expression_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_3 = mod_consts[26];
        tmp_tuple_element_1 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_6, tmp_subscript_value_3);
        if (tmp_tuple_element_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_1 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_1, 0, tmp_tuple_element_1);
        tmp_tuple_element_1 = mod_consts[27];
        PyTuple_SET_ITEM0(tmp_args_value_1, 1, tmp_tuple_element_1);
        tmp_kwargs_value_1 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 38;
        tmp_dict_value_1 = CALL_FUNCTION(tstate, tmp_called_value_7, tmp_args_value_1, tmp_kwargs_value_1);
        Py_DECREF(tmp_args_value_1);
        Py_DECREF(tmp_kwargs_value_1);
        if (tmp_dict_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_2 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_2, tmp_dict_key_1, tmp_dict_value_1);
        Py_DECREF(tmp_dict_value_1);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_7 = par_self;
        tmp_ass_subscribed_2 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_7, mod_consts[15]);
        if (tmp_ass_subscribed_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_2);

            exception_lineno = 37;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_2 = mod_consts[26];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_2, tmp_ass_subscript_2, tmp_ass_subvalue_2);
        Py_DECREF(tmp_ass_subscribed_2);
        Py_DECREF(tmp_ass_subvalue_2);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_8;
        PyObject *tmp_expression_value_8;
        PyObject *tmp_call_result_5;
        PyObject *tmp_args_element_value_11;
        PyObject *tmp_expression_value_9;
        PyObject *tmp_expression_value_10;
        PyObject *tmp_expression_value_11;
        PyObject *tmp_subscript_value_4;
        PyObject *tmp_subscript_value_5;
        PyObject *tmp_args_element_value_12;
        PyObject *tmp_args_element_value_13;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_8 = var_tab_layout;
        tmp_called_value_8 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_8, mod_consts[7]);
        if (tmp_called_value_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 40;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_11 = par_self;
        tmp_expression_value_10 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_11, mod_consts[15]);
        if (tmp_expression_value_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_8);

            exception_lineno = 40;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_4 = mod_consts[26];
        tmp_expression_value_9 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_10, tmp_subscript_value_4);
        Py_DECREF(tmp_expression_value_10);
        if (tmp_expression_value_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_8);

            exception_lineno = 40;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_5 = mod_consts[25];
        tmp_args_element_value_11 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_9, tmp_subscript_value_5);
        Py_DECREF(tmp_expression_value_9);
        if (tmp_args_element_value_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_8);

            exception_lineno = 40;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_12 = mod_consts[29];
        tmp_args_element_value_13 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 40;
        {
            PyObject *call_args[] = {tmp_args_element_value_11, tmp_args_element_value_12, tmp_args_element_value_13};
            tmp_call_result_5 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_8, call_args);
        }

        Py_DECREF(tmp_called_value_8);
        Py_DECREF(tmp_args_element_value_11);
        if (tmp_call_result_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 40;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_5);
    }
    {
        PyObject *tmp_ass_subvalue_3;
        PyObject *tmp_dict_key_2;
        PyObject *tmp_dict_value_2;
        PyObject *tmp_called_value_9;
        PyObject *tmp_args_value_2;
        PyObject *tmp_tuple_element_2;
        PyObject *tmp_expression_value_12;
        PyObject *tmp_subscript_value_6;
        PyObject *tmp_kwargs_value_2;
        PyObject *tmp_ass_subscribed_3;
        PyObject *tmp_expression_value_13;
        PyObject *tmp_ass_subscript_3;
        tmp_dict_key_2 = mod_consts[30];
        tmp_called_value_9 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_9 == NULL)) {
            tmp_called_value_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 42;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_12 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_12 == NULL)) {
            tmp_expression_value_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 42;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_6 = mod_consts[31];
        tmp_tuple_element_2 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_12, tmp_subscript_value_6);
        if (tmp_tuple_element_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 42;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_2 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_2, 0, tmp_tuple_element_2);
        tmp_tuple_element_2 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_2, 1, tmp_tuple_element_2);
        tmp_kwargs_value_2 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 42;
        tmp_dict_value_2 = CALL_FUNCTION(tstate, tmp_called_value_9, tmp_args_value_2, tmp_kwargs_value_2);
        Py_DECREF(tmp_args_value_2);
        Py_DECREF(tmp_kwargs_value_2);
        if (tmp_dict_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 42;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_3 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_3, tmp_dict_key_2, tmp_dict_value_2);
        Py_DECREF(tmp_dict_value_2);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_13 = par_self;
        tmp_ass_subscribed_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_13, mod_consts[15]);
        if (tmp_ass_subscribed_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_3);

            exception_lineno = 41;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_3 = mod_consts[31];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_3, tmp_ass_subscript_3, tmp_ass_subvalue_3);
        Py_DECREF(tmp_ass_subscribed_3);
        Py_DECREF(tmp_ass_subvalue_3);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 41;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_10;
        PyObject *tmp_expression_value_14;
        PyObject *tmp_call_result_6;
        PyObject *tmp_args_element_value_14;
        PyObject *tmp_expression_value_15;
        PyObject *tmp_expression_value_16;
        PyObject *tmp_expression_value_17;
        PyObject *tmp_subscript_value_7;
        PyObject *tmp_subscript_value_8;
        PyObject *tmp_args_element_value_15;
        PyObject *tmp_args_element_value_16;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_14 = var_tab_layout;
        tmp_called_value_10 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_14, mod_consts[7]);
        if (tmp_called_value_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 44;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_17 = par_self;
        tmp_expression_value_16 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_17, mod_consts[15]);
        if (tmp_expression_value_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_10);

            exception_lineno = 44;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_7 = mod_consts[31];
        tmp_expression_value_15 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_16, tmp_subscript_value_7);
        Py_DECREF(tmp_expression_value_16);
        if (tmp_expression_value_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_10);

            exception_lineno = 44;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_8 = mod_consts[30];
        tmp_args_element_value_14 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_15, tmp_subscript_value_8);
        Py_DECREF(tmp_expression_value_15);
        if (tmp_args_element_value_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_10);

            exception_lineno = 44;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_15 = mod_consts[33];
        tmp_args_element_value_16 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 44;
        {
            PyObject *call_args[] = {tmp_args_element_value_14, tmp_args_element_value_15, tmp_args_element_value_16};
            tmp_call_result_6 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_10, call_args);
        }

        Py_DECREF(tmp_called_value_10);
        Py_DECREF(tmp_args_element_value_14);
        if (tmp_call_result_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 44;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_6);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_called_value_11;
        tmp_called_value_11 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_11 == NULL)) {
            tmp_called_value_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 46;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 46;
        tmp_assign_source_5 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_11);
        if (tmp_assign_source_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 46;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_5;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_called_value_12;
        PyObject *tmp_args_element_value_17;
        tmp_called_value_12 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_12 == NULL)) {
            tmp_called_value_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 47;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_17 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 47;
        tmp_assign_source_6 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_12, tmp_args_element_value_17);
        if (tmp_assign_source_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 47;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_6;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_4;
        PyObject *tmp_call_result_7;
        PyObject *tmp_args_element_value_18;
        PyObject *tmp_args_element_value_19;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_4 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_18 = var_tab;
        tmp_args_element_value_19 = mod_consts[34];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 48;
        {
            PyObject *call_args[] = {tmp_args_element_value_18, tmp_args_element_value_19};
            tmp_call_result_7 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_4,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 48;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_7);
    }
    {
        PyObject *tmp_ass_subvalue_4;
        PyObject *tmp_called_value_13;
        PyObject *tmp_args_element_value_20;
        PyObject *tmp_args_element_value_21;
        PyObject *tmp_expression_value_18;
        PyObject *tmp_subscript_value_9;
        PyObject *tmp_ass_subscribed_4;
        PyObject *tmp_expression_value_19;
        PyObject *tmp_ass_subscript_4;
        tmp_called_value_13 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_13 == NULL)) {
            tmp_called_value_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 50;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_20 = mod_consts[35];
        tmp_expression_value_18 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_18 == NULL)) {
            tmp_expression_value_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 50;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_9 = mod_consts[35];
        tmp_args_element_value_21 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_18, tmp_subscript_value_9);
        if (tmp_args_element_value_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 50;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 50;
        {
            PyObject *call_args[] = {tmp_args_element_value_20, tmp_args_element_value_21};
            tmp_ass_subvalue_4 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_13, call_args);
        }

        Py_DECREF(tmp_args_element_value_21);
        if (tmp_ass_subvalue_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 50;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_19 = par_self;
        tmp_ass_subscribed_4 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_19, mod_consts[15]);
        if (tmp_ass_subscribed_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_4);

            exception_lineno = 50;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_4 = mod_consts[35];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_4, tmp_ass_subscript_4, tmp_ass_subvalue_4);
        Py_DECREF(tmp_ass_subscribed_4);
        Py_DECREF(tmp_ass_subvalue_4);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 50;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_14;
        PyObject *tmp_expression_value_20;
        PyObject *tmp_call_result_8;
        PyObject *tmp_args_element_value_22;
        PyObject *tmp_expression_value_21;
        PyObject *tmp_expression_value_22;
        PyObject *tmp_subscript_value_10;
        PyObject *tmp_args_element_value_23;
        PyObject *tmp_args_element_value_24;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_20 = var_tab_layout;
        tmp_called_value_14 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_20, mod_consts[7]);
        if (tmp_called_value_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_22 = par_self;
        tmp_expression_value_21 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_22, mod_consts[15]);
        if (tmp_expression_value_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_14);

            exception_lineno = 51;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_10 = mod_consts[35];
        tmp_args_element_value_22 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_21, tmp_subscript_value_10);
        Py_DECREF(tmp_expression_value_21);
        if (tmp_args_element_value_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_14);

            exception_lineno = 51;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_23 = mod_consts[24];
        tmp_args_element_value_24 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 51;
        {
            PyObject *call_args[] = {tmp_args_element_value_22, tmp_args_element_value_23, tmp_args_element_value_24};
            tmp_call_result_8 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_14, call_args);
        }

        Py_DECREF(tmp_called_value_14);
        Py_DECREF(tmp_args_element_value_22);
        if (tmp_call_result_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_8);
    }
    {
        PyObject *tmp_ass_subvalue_5;
        PyObject *tmp_dict_key_3;
        PyObject *tmp_dict_value_3;
        PyObject *tmp_called_value_15;
        PyObject *tmp_kw_call_value_0_1;
        PyObject *tmp_list_element_1;
        PyObject *tmp_ass_subscribed_5;
        PyObject *tmp_expression_value_25;
        PyObject *tmp_ass_subscript_5;
        tmp_dict_key_3 = mod_consts[36];
        tmp_called_value_15 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[4]);

        if (unlikely(tmp_called_value_15 == NULL)) {
            tmp_called_value_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[4]);
        }

        if (tmp_called_value_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_list_element_1 = mod_consts[37];
        tmp_kw_call_value_0_1 = MAKE_LIST_EMPTY(3);
        {
            PyObject *tmp_expression_value_23;
            PyObject *tmp_subscript_value_11;
            PyObject *tmp_expression_value_24;
            PyObject *tmp_subscript_value_12;
            PyList_SET_ITEM0(tmp_kw_call_value_0_1, 0, tmp_list_element_1);
            tmp_expression_value_23 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_23 == NULL)) {
                tmp_expression_value_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_23 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_1 = "oooooc";
                goto list_build_exception_1;
            }
            tmp_subscript_value_11 = mod_consts[38];
            tmp_list_element_1 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_23, tmp_subscript_value_11);
            if (tmp_list_element_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_1 = "oooooc";
                goto list_build_exception_1;
            }
            PyList_SET_ITEM(tmp_kw_call_value_0_1, 1, tmp_list_element_1);
            tmp_expression_value_24 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_24 == NULL)) {
                tmp_expression_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_24 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_1 = "oooooc";
                goto list_build_exception_1;
            }
            tmp_subscript_value_12 = mod_consts[39];
            tmp_list_element_1 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_24, tmp_subscript_value_12);
            if (tmp_list_element_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_1 = "oooooc";
                goto list_build_exception_1;
            }
            PyList_SET_ITEM(tmp_kw_call_value_0_1, 2, tmp_list_element_1);
        }
        goto list_build_noexception_1;
        // Exception handling pass through code for list_build:
        list_build_exception_1:;
        Py_DECREF(tmp_kw_call_value_0_1);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_1:;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 54;
        {
            PyObject *kw_values[1] = {tmp_kw_call_value_0_1};
            tmp_dict_value_3 = CALL_FUNCTION_WITH_POSARGS1_KWSPLIT(tstate, tmp_called_value_15, mod_consts[40], kw_values, mod_consts[41]);
        }

        Py_DECREF(tmp_kw_call_value_0_1);
        if (tmp_dict_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_5 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_5, tmp_dict_key_3, tmp_dict_value_3);
        Py_DECREF(tmp_dict_value_3);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_25 = par_self;
        tmp_ass_subscribed_5 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_25, mod_consts[15]);
        if (tmp_ass_subscribed_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_5);

            exception_lineno = 53;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_5 = mod_consts[38];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_5, tmp_ass_subscript_5, tmp_ass_subvalue_5);
        Py_DECREF(tmp_ass_subscribed_5);
        Py_DECREF(tmp_ass_subvalue_5);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 53;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_16;
        PyObject *tmp_expression_value_26;
        PyObject *tmp_call_result_9;
        PyObject *tmp_args_element_value_25;
        PyObject *tmp_expression_value_27;
        PyObject *tmp_expression_value_28;
        PyObject *tmp_expression_value_29;
        PyObject *tmp_subscript_value_13;
        PyObject *tmp_subscript_value_14;
        PyObject *tmp_args_element_value_26;
        PyObject *tmp_args_element_value_27;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_26 = var_tab_layout;
        tmp_called_value_16 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_26, mod_consts[7]);
        if (tmp_called_value_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 56;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_29 = par_self;
        tmp_expression_value_28 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_29, mod_consts[15]);
        if (tmp_expression_value_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_16);

            exception_lineno = 56;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_13 = mod_consts[38];
        tmp_expression_value_27 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_28, tmp_subscript_value_13);
        Py_DECREF(tmp_expression_value_28);
        if (tmp_expression_value_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_16);

            exception_lineno = 56;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_14 = mod_consts[36];
        tmp_args_element_value_25 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_27, tmp_subscript_value_14);
        Py_DECREF(tmp_expression_value_27);
        if (tmp_args_element_value_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_16);

            exception_lineno = 56;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_26 = mod_consts[29];
        tmp_args_element_value_27 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 56;
        {
            PyObject *call_args[] = {tmp_args_element_value_25, tmp_args_element_value_26, tmp_args_element_value_27};
            tmp_call_result_9 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_16, call_args);
        }

        Py_DECREF(tmp_called_value_16);
        Py_DECREF(tmp_args_element_value_25);
        if (tmp_call_result_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 56;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_9);
    }
    {
        PyObject *tmp_ass_subvalue_6;
        PyObject *tmp_dict_key_4;
        PyObject *tmp_dict_value_4;
        PyObject *tmp_called_value_17;
        PyObject *tmp_args_value_3;
        PyObject *tmp_tuple_element_3;
        PyObject *tmp_expression_value_30;
        PyObject *tmp_subscript_value_15;
        PyObject *tmp_kwargs_value_3;
        PyObject *tmp_ass_subscribed_6;
        PyObject *tmp_expression_value_31;
        PyObject *tmp_ass_subscript_6;
        tmp_dict_key_4 = mod_consts[30];
        tmp_called_value_17 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_17 == NULL)) {
            tmp_called_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 59;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_30 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_30 == NULL)) {
            tmp_expression_value_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_30 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 59;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_15 = mod_consts[42];
        tmp_tuple_element_3 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_30, tmp_subscript_value_15);
        if (tmp_tuple_element_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 59;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_3 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_3, 0, tmp_tuple_element_3);
        tmp_tuple_element_3 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_3, 1, tmp_tuple_element_3);
        tmp_kwargs_value_3 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 59;
        tmp_dict_value_4 = CALL_FUNCTION(tstate, tmp_called_value_17, tmp_args_value_3, tmp_kwargs_value_3);
        Py_DECREF(tmp_args_value_3);
        Py_DECREF(tmp_kwargs_value_3);
        if (tmp_dict_value_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 59;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_6 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_6, tmp_dict_key_4, tmp_dict_value_4);
        Py_DECREF(tmp_dict_value_4);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_31 = par_self;
        tmp_ass_subscribed_6 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_31, mod_consts[15]);
        if (tmp_ass_subscribed_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_6);

            exception_lineno = 58;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_6 = mod_consts[42];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_6, tmp_ass_subscript_6, tmp_ass_subvalue_6);
        Py_DECREF(tmp_ass_subscribed_6);
        Py_DECREF(tmp_ass_subvalue_6);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 58;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_18;
        PyObject *tmp_expression_value_32;
        PyObject *tmp_call_result_10;
        PyObject *tmp_args_element_value_28;
        PyObject *tmp_expression_value_33;
        PyObject *tmp_expression_value_34;
        PyObject *tmp_expression_value_35;
        PyObject *tmp_subscript_value_16;
        PyObject *tmp_subscript_value_17;
        PyObject *tmp_args_element_value_29;
        PyObject *tmp_args_element_value_30;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_32 = var_tab_layout;
        tmp_called_value_18 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_32, mod_consts[7]);
        if (tmp_called_value_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 61;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_35 = par_self;
        tmp_expression_value_34 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_35, mod_consts[15]);
        if (tmp_expression_value_34 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_18);

            exception_lineno = 61;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_16 = mod_consts[42];
        tmp_expression_value_33 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_34, tmp_subscript_value_16);
        Py_DECREF(tmp_expression_value_34);
        if (tmp_expression_value_33 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_18);

            exception_lineno = 61;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_17 = mod_consts[30];
        tmp_args_element_value_28 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_33, tmp_subscript_value_17);
        Py_DECREF(tmp_expression_value_33);
        if (tmp_args_element_value_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_18);

            exception_lineno = 61;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_29 = mod_consts[33];
        tmp_args_element_value_30 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 61;
        {
            PyObject *call_args[] = {tmp_args_element_value_28, tmp_args_element_value_29, tmp_args_element_value_30};
            tmp_call_result_10 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_18, call_args);
        }

        Py_DECREF(tmp_called_value_18);
        Py_DECREF(tmp_args_element_value_28);
        if (tmp_call_result_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 61;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_10);
    }
    {
        PyObject *tmp_ass_subvalue_7;
        PyObject *tmp_dict_key_5;
        PyObject *tmp_dict_value_5;
        PyObject *tmp_called_value_19;
        PyObject *tmp_args_value_4;
        PyObject *tmp_tuple_element_4;
        PyObject *tmp_expression_value_36;
        PyObject *tmp_subscript_value_18;
        PyObject *tmp_kwargs_value_4;
        PyObject *tmp_ass_subscribed_7;
        PyObject *tmp_expression_value_37;
        PyObject *tmp_ass_subscript_7;
        tmp_dict_key_5 = mod_consts[25];
        tmp_called_value_19 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_19 == NULL)) {
            tmp_called_value_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_36 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_36 == NULL)) {
            tmp_expression_value_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_36 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_18 = mod_consts[43];
        tmp_tuple_element_4 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_36, tmp_subscript_value_18);
        if (tmp_tuple_element_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_4 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_4, 0, tmp_tuple_element_4);
        tmp_tuple_element_4 = mod_consts[27];
        PyTuple_SET_ITEM0(tmp_args_value_4, 1, tmp_tuple_element_4);
        tmp_kwargs_value_4 = DICT_COPY(mod_consts[44]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 64;
        tmp_dict_value_5 = CALL_FUNCTION(tstate, tmp_called_value_19, tmp_args_value_4, tmp_kwargs_value_4);
        Py_DECREF(tmp_args_value_4);
        Py_DECREF(tmp_kwargs_value_4);
        if (tmp_dict_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_7 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_7, tmp_dict_key_5, tmp_dict_value_5);
        Py_DECREF(tmp_dict_value_5);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_37 = par_self;
        tmp_ass_subscribed_7 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_37, mod_consts[15]);
        if (tmp_ass_subscribed_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_7);

            exception_lineno = 63;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_7 = mod_consts[43];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_7, tmp_ass_subscript_7, tmp_ass_subvalue_7);
        Py_DECREF(tmp_ass_subscribed_7);
        Py_DECREF(tmp_ass_subvalue_7);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 63;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_20;
        PyObject *tmp_expression_value_38;
        PyObject *tmp_call_result_11;
        PyObject *tmp_args_element_value_31;
        PyObject *tmp_expression_value_39;
        PyObject *tmp_expression_value_40;
        PyObject *tmp_expression_value_41;
        PyObject *tmp_subscript_value_19;
        PyObject *tmp_subscript_value_20;
        PyObject *tmp_args_element_value_32;
        PyObject *tmp_args_element_value_33;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_38 = var_tab_layout;
        tmp_called_value_20 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_38, mod_consts[7]);
        if (tmp_called_value_20 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 66;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_41 = par_self;
        tmp_expression_value_40 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_41, mod_consts[15]);
        if (tmp_expression_value_40 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_20);

            exception_lineno = 66;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_19 = mod_consts[43];
        tmp_expression_value_39 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_40, tmp_subscript_value_19);
        Py_DECREF(tmp_expression_value_40);
        if (tmp_expression_value_39 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_20);

            exception_lineno = 66;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_20 = mod_consts[25];
        tmp_args_element_value_31 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_39, tmp_subscript_value_20);
        Py_DECREF(tmp_expression_value_39);
        if (tmp_args_element_value_31 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_20);

            exception_lineno = 66;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_32 = mod_consts[45];
        tmp_args_element_value_33 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 66;
        {
            PyObject *call_args[] = {tmp_args_element_value_31, tmp_args_element_value_32, tmp_args_element_value_33};
            tmp_call_result_11 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_20, call_args);
        }

        Py_DECREF(tmp_called_value_20);
        Py_DECREF(tmp_args_element_value_31);
        if (tmp_call_result_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 66;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_11);
    }
    {
        PyObject *tmp_ass_subvalue_8;
        PyObject *tmp_dict_key_6;
        PyObject *tmp_dict_value_6;
        PyObject *tmp_called_value_21;
        PyObject *tmp_args_value_5;
        PyObject *tmp_tuple_element_5;
        PyObject *tmp_expression_value_42;
        PyObject *tmp_subscript_value_21;
        PyObject *tmp_kwargs_value_5;
        PyObject *tmp_ass_subscribed_8;
        PyObject *tmp_expression_value_43;
        PyObject *tmp_ass_subscript_8;
        tmp_dict_key_6 = mod_consts[30];
        tmp_called_value_21 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_21 == NULL)) {
            tmp_called_value_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 69;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_42 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_42 == NULL)) {
            tmp_expression_value_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_42 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 69;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_21 = mod_consts[46];
        tmp_tuple_element_5 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_42, tmp_subscript_value_21);
        if (tmp_tuple_element_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 69;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_5 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_5, 0, tmp_tuple_element_5);
        tmp_tuple_element_5 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_5, 1, tmp_tuple_element_5);
        tmp_kwargs_value_5 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 69;
        tmp_dict_value_6 = CALL_FUNCTION(tstate, tmp_called_value_21, tmp_args_value_5, tmp_kwargs_value_5);
        Py_DECREF(tmp_args_value_5);
        Py_DECREF(tmp_kwargs_value_5);
        if (tmp_dict_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 69;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_8 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_8, tmp_dict_key_6, tmp_dict_value_6);
        Py_DECREF(tmp_dict_value_6);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_43 = par_self;
        tmp_ass_subscribed_8 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_43, mod_consts[15]);
        if (tmp_ass_subscribed_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_8);

            exception_lineno = 68;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_8 = mod_consts[46];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_8, tmp_ass_subscript_8, tmp_ass_subvalue_8);
        Py_DECREF(tmp_ass_subscribed_8);
        Py_DECREF(tmp_ass_subvalue_8);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 68;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_22;
        PyObject *tmp_expression_value_44;
        PyObject *tmp_call_result_12;
        PyObject *tmp_args_element_value_34;
        PyObject *tmp_expression_value_45;
        PyObject *tmp_expression_value_46;
        PyObject *tmp_expression_value_47;
        PyObject *tmp_subscript_value_22;
        PyObject *tmp_subscript_value_23;
        PyObject *tmp_args_element_value_35;
        PyObject *tmp_args_element_value_36;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_44 = var_tab_layout;
        tmp_called_value_22 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_44, mod_consts[7]);
        if (tmp_called_value_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_47 = par_self;
        tmp_expression_value_46 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_47, mod_consts[15]);
        if (tmp_expression_value_46 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_22);

            exception_lineno = 71;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_22 = mod_consts[46];
        tmp_expression_value_45 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_46, tmp_subscript_value_22);
        Py_DECREF(tmp_expression_value_46);
        if (tmp_expression_value_45 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_22);

            exception_lineno = 71;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_23 = mod_consts[30];
        tmp_args_element_value_34 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_45, tmp_subscript_value_23);
        Py_DECREF(tmp_expression_value_45);
        if (tmp_args_element_value_34 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_22);

            exception_lineno = 71;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_35 = mod_consts[47];
        tmp_args_element_value_36 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 71;
        {
            PyObject *call_args[] = {tmp_args_element_value_34, tmp_args_element_value_35, tmp_args_element_value_36};
            tmp_call_result_12 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_22, call_args);
        }

        Py_DECREF(tmp_called_value_22);
        Py_DECREF(tmp_args_element_value_34);
        if (tmp_call_result_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_12);
    }
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_called_value_23;
        tmp_called_value_23 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_23 == NULL)) {
            tmp_called_value_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_23 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 73;
        tmp_assign_source_7 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_23);
        if (tmp_assign_source_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_7;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_8;
        PyObject *tmp_called_value_24;
        PyObject *tmp_args_element_value_37;
        tmp_called_value_24 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_24 == NULL)) {
            tmp_called_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 74;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_37 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 74;
        tmp_assign_source_8 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_24, tmp_args_element_value_37);
        if (tmp_assign_source_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 74;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_8;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_5;
        PyObject *tmp_call_result_13;
        PyObject *tmp_args_element_value_38;
        PyObject *tmp_args_element_value_39;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_5 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_38 = var_tab;
        tmp_args_element_value_39 = mod_consts[48];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 75;
        {
            PyObject *call_args[] = {tmp_args_element_value_38, tmp_args_element_value_39};
            tmp_call_result_13 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_5,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 75;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_13);
    }
    {
        PyObject *tmp_ass_subvalue_9;
        PyObject *tmp_dict_key_7;
        PyObject *tmp_dict_value_7;
        PyObject *tmp_called_value_25;
        PyObject *tmp_args_value_6;
        PyObject *tmp_tuple_element_6;
        PyObject *tmp_expression_value_48;
        PyObject *tmp_subscript_value_24;
        PyObject *tmp_kwargs_value_6;
        PyObject *tmp_ass_subscribed_9;
        PyObject *tmp_expression_value_49;
        PyObject *tmp_ass_subscript_9;
        tmp_dict_key_7 = mod_consts[30];
        tmp_called_value_25 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_25 == NULL)) {
            tmp_called_value_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_48 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_48 == NULL)) {
            tmp_expression_value_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_48 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_24 = mod_consts[49];
        tmp_tuple_element_6 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_48, tmp_subscript_value_24);
        if (tmp_tuple_element_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_6 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_6, 0, tmp_tuple_element_6);
        tmp_tuple_element_6 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_6, 1, tmp_tuple_element_6);
        tmp_kwargs_value_6 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 78;
        tmp_dict_value_7 = CALL_FUNCTION(tstate, tmp_called_value_25, tmp_args_value_6, tmp_kwargs_value_6);
        Py_DECREF(tmp_args_value_6);
        Py_DECREF(tmp_kwargs_value_6);
        if (tmp_dict_value_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_9 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_9, tmp_dict_key_7, tmp_dict_value_7);
        Py_DECREF(tmp_dict_value_7);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_49 = par_self;
        tmp_ass_subscribed_9 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_49, mod_consts[15]);
        if (tmp_ass_subscribed_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_9);

            exception_lineno = 77;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_9 = mod_consts[49];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_9, tmp_ass_subscript_9, tmp_ass_subvalue_9);
        Py_DECREF(tmp_ass_subscribed_9);
        Py_DECREF(tmp_ass_subvalue_9);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 77;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_26;
        PyObject *tmp_expression_value_50;
        PyObject *tmp_call_result_14;
        PyObject *tmp_args_element_value_40;
        PyObject *tmp_expression_value_51;
        PyObject *tmp_expression_value_52;
        PyObject *tmp_expression_value_53;
        PyObject *tmp_subscript_value_25;
        PyObject *tmp_subscript_value_26;
        PyObject *tmp_args_element_value_41;
        PyObject *tmp_args_element_value_42;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_50 = var_tab_layout;
        tmp_called_value_26 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_50, mod_consts[7]);
        if (tmp_called_value_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 80;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_53 = par_self;
        tmp_expression_value_52 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_53, mod_consts[15]);
        if (tmp_expression_value_52 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_26);

            exception_lineno = 80;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_25 = mod_consts[49];
        tmp_expression_value_51 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_52, tmp_subscript_value_25);
        Py_DECREF(tmp_expression_value_52);
        if (tmp_expression_value_51 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_26);

            exception_lineno = 80;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_26 = mod_consts[30];
        tmp_args_element_value_40 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_51, tmp_subscript_value_26);
        Py_DECREF(tmp_expression_value_51);
        if (tmp_args_element_value_40 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_26);

            exception_lineno = 80;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_41 = mod_consts[24];
        tmp_args_element_value_42 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 80;
        {
            PyObject *call_args[] = {tmp_args_element_value_40, tmp_args_element_value_41, tmp_args_element_value_42};
            tmp_call_result_14 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_26, call_args);
        }

        Py_DECREF(tmp_called_value_26);
        Py_DECREF(tmp_args_element_value_40);
        if (tmp_call_result_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 80;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_14);
    }
    {
        PyObject *tmp_ass_subvalue_10;
        PyObject *tmp_dict_key_8;
        PyObject *tmp_dict_value_8;
        PyObject *tmp_called_value_27;
        PyObject *tmp_args_value_7;
        PyObject *tmp_tuple_element_7;
        PyObject *tmp_expression_value_54;
        PyObject *tmp_subscript_value_27;
        PyObject *tmp_kwargs_value_7;
        PyObject *tmp_ass_subscribed_10;
        PyObject *tmp_expression_value_56;
        PyObject *tmp_ass_subscript_10;
        tmp_dict_key_8 = mod_consts[25];
        tmp_called_value_27 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_27 == NULL)) {
            tmp_called_value_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_54 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_54 == NULL)) {
            tmp_expression_value_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_54 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_27 = mod_consts[50];
        tmp_tuple_element_7 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_54, tmp_subscript_value_27);
        if (tmp_tuple_element_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_7 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_7, 0, tmp_tuple_element_7);
        tmp_tuple_element_7 = mod_consts[27];
        PyTuple_SET_ITEM0(tmp_args_value_7, 1, tmp_tuple_element_7);
        tmp_kwargs_value_7 = DICT_COPY(mod_consts[51]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 83;
        tmp_dict_value_8 = CALL_FUNCTION(tstate, tmp_called_value_27, tmp_args_value_7, tmp_kwargs_value_7);
        Py_DECREF(tmp_args_value_7);
        Py_DECREF(tmp_kwargs_value_7);
        if (tmp_dict_value_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 83;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_10 = _PyDict_NewPresized( 2 );
        {
            PyObject *tmp_called_value_28;
            PyObject *tmp_args_value_8;
            PyObject *tmp_tuple_element_8;
            PyObject *tmp_expression_value_55;
            PyObject *tmp_subscript_value_28;
            PyObject *tmp_kwargs_value_8;
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_10, tmp_dict_key_8, tmp_dict_value_8);
            Py_DECREF(tmp_dict_value_8);
            assert(!(tmp_res != 0));
            tmp_dict_key_8 = mod_consts[30];
            tmp_called_value_28 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

            if (unlikely(tmp_called_value_28 == NULL)) {
                tmp_called_value_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
            }

            if (tmp_called_value_28 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 84;
                type_description_1 = "oooooc";
                goto dict_build_exception_1;
            }
            tmp_expression_value_55 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_55 == NULL)) {
                tmp_expression_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_55 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 84;
                type_description_1 = "oooooc";
                goto dict_build_exception_1;
            }
            tmp_subscript_value_28 = mod_consts[50];
            tmp_tuple_element_8 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_55, tmp_subscript_value_28);
            if (tmp_tuple_element_8 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 84;
                type_description_1 = "oooooc";
                goto dict_build_exception_1;
            }
            tmp_args_value_8 = MAKE_TUPLE_EMPTY(2);
            PyTuple_SET_ITEM(tmp_args_value_8, 0, tmp_tuple_element_8);
            tmp_tuple_element_8 = mod_consts[32];
            PyTuple_SET_ITEM0(tmp_args_value_8, 1, tmp_tuple_element_8);
            tmp_kwargs_value_8 = DICT_COPY(mod_consts[28]);
            frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 84;
            tmp_dict_value_8 = CALL_FUNCTION(tstate, tmp_called_value_28, tmp_args_value_8, tmp_kwargs_value_8);
            Py_DECREF(tmp_args_value_8);
            Py_DECREF(tmp_kwargs_value_8);
            if (tmp_dict_value_8 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 84;
                type_description_1 = "oooooc";
                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_10, tmp_dict_key_8, tmp_dict_value_8);
            Py_DECREF(tmp_dict_value_8);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_1;
        // Exception handling pass through code for dict_build:
        dict_build_exception_1:;
        Py_DECREF(tmp_ass_subvalue_10);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_1:;
        CHECK_OBJECT(par_self);
        tmp_expression_value_56 = par_self;
        tmp_ass_subscribed_10 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_56, mod_consts[15]);
        if (tmp_ass_subscribed_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_10);

            exception_lineno = 82;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_10 = mod_consts[50];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_10, tmp_ass_subscript_10, tmp_ass_subvalue_10);
        Py_DECREF(tmp_ass_subscribed_10);
        Py_DECREF(tmp_ass_subvalue_10);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_29;
        PyObject *tmp_expression_value_57;
        PyObject *tmp_call_result_15;
        PyObject *tmp_args_element_value_43;
        PyObject *tmp_expression_value_58;
        PyObject *tmp_expression_value_59;
        PyObject *tmp_expression_value_60;
        PyObject *tmp_subscript_value_29;
        PyObject *tmp_subscript_value_30;
        PyObject *tmp_args_element_value_44;
        PyObject *tmp_args_element_value_45;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_57 = var_tab_layout;
        tmp_called_value_29 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_57, mod_consts[7]);
        if (tmp_called_value_29 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 86;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_60 = par_self;
        tmp_expression_value_59 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_60, mod_consts[15]);
        if (tmp_expression_value_59 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_29);

            exception_lineno = 86;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_29 = mod_consts[50];
        tmp_expression_value_58 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_59, tmp_subscript_value_29);
        Py_DECREF(tmp_expression_value_59);
        if (tmp_expression_value_58 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_29);

            exception_lineno = 86;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_30 = mod_consts[25];
        tmp_args_element_value_43 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_58, tmp_subscript_value_30);
        Py_DECREF(tmp_expression_value_58);
        if (tmp_args_element_value_43 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_29);

            exception_lineno = 86;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_44 = mod_consts[29];
        tmp_args_element_value_45 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 86;
        {
            PyObject *call_args[] = {tmp_args_element_value_43, tmp_args_element_value_44, tmp_args_element_value_45};
            tmp_call_result_15 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_29, call_args);
        }

        Py_DECREF(tmp_called_value_29);
        Py_DECREF(tmp_args_element_value_43);
        if (tmp_call_result_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 86;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_15);
    }
    {
        PyObject *tmp_called_value_30;
        PyObject *tmp_expression_value_61;
        PyObject *tmp_call_result_16;
        PyObject *tmp_args_element_value_46;
        PyObject *tmp_expression_value_62;
        PyObject *tmp_expression_value_63;
        PyObject *tmp_expression_value_64;
        PyObject *tmp_subscript_value_31;
        PyObject *tmp_subscript_value_32;
        PyObject *tmp_args_element_value_47;
        PyObject *tmp_args_element_value_48;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_61 = var_tab_layout;
        tmp_called_value_30 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_61, mod_consts[7]);
        if (tmp_called_value_30 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 87;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_64 = par_self;
        tmp_expression_value_63 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_64, mod_consts[15]);
        if (tmp_expression_value_63 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_30);

            exception_lineno = 87;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_31 = mod_consts[50];
        tmp_expression_value_62 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_63, tmp_subscript_value_31);
        Py_DECREF(tmp_expression_value_63);
        if (tmp_expression_value_62 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_30);

            exception_lineno = 87;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_32 = mod_consts[30];
        tmp_args_element_value_46 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_62, tmp_subscript_value_32);
        Py_DECREF(tmp_expression_value_62);
        if (tmp_args_element_value_46 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_30);

            exception_lineno = 87;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_47 = mod_consts[29];
        tmp_args_element_value_48 = mod_consts[29];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 87;
        {
            PyObject *call_args[] = {tmp_args_element_value_46, tmp_args_element_value_47, tmp_args_element_value_48};
            tmp_call_result_16 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_30, call_args);
        }

        Py_DECREF(tmp_called_value_30);
        Py_DECREF(tmp_args_element_value_46);
        if (tmp_call_result_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 87;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_16);
    }
    {
        PyObject *tmp_assign_source_9;
        PyObject *tmp_called_value_31;
        tmp_called_value_31 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_31 == NULL)) {
            tmp_called_value_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_31 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 89;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 89;
        tmp_assign_source_9 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_31);
        if (tmp_assign_source_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 89;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_9;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_10;
        PyObject *tmp_called_value_32;
        PyObject *tmp_args_element_value_49;
        tmp_called_value_32 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_32 == NULL)) {
            tmp_called_value_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_32 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 90;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_49 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 90;
        tmp_assign_source_10 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_32, tmp_args_element_value_49);
        if (tmp_assign_source_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 90;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_10;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_6;
        PyObject *tmp_call_result_17;
        PyObject *tmp_args_element_value_50;
        PyObject *tmp_args_element_value_51;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_6 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_50 = var_tab;
        tmp_args_element_value_51 = mod_consts[52];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 91;
        {
            PyObject *call_args[] = {tmp_args_element_value_50, tmp_args_element_value_51};
            tmp_call_result_17 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_6,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 91;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_17);
    }
    {
        PyObject *tmp_ass_subvalue_11;
        PyObject *tmp_called_value_33;
        PyObject *tmp_args_element_value_52;
        PyObject *tmp_args_element_value_53;
        PyObject *tmp_expression_value_65;
        PyObject *tmp_subscript_value_33;
        PyObject *tmp_ass_subscribed_11;
        PyObject *tmp_expression_value_66;
        PyObject *tmp_ass_subscript_11;
        tmp_called_value_33 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_33 == NULL)) {
            tmp_called_value_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_33 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_52 = mod_consts[53];
        tmp_expression_value_65 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_65 == NULL)) {
            tmp_expression_value_65 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_65 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_33 = mod_consts[53];
        tmp_args_element_value_53 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_65, tmp_subscript_value_33);
        if (tmp_args_element_value_53 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 93;
        {
            PyObject *call_args[] = {tmp_args_element_value_52, tmp_args_element_value_53};
            tmp_ass_subvalue_11 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_33, call_args);
        }

        Py_DECREF(tmp_args_element_value_53);
        if (tmp_ass_subvalue_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_66 = par_self;
        tmp_ass_subscribed_11 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_66, mod_consts[15]);
        if (tmp_ass_subscribed_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_11);

            exception_lineno = 93;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_11 = mod_consts[53];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_11, tmp_ass_subscript_11, tmp_ass_subvalue_11);
        Py_DECREF(tmp_ass_subscribed_11);
        Py_DECREF(tmp_ass_subvalue_11);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 93;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_34;
        PyObject *tmp_expression_value_67;
        PyObject *tmp_call_result_18;
        PyObject *tmp_args_element_value_54;
        PyObject *tmp_expression_value_68;
        PyObject *tmp_expression_value_69;
        PyObject *tmp_subscript_value_34;
        PyObject *tmp_args_element_value_55;
        PyObject *tmp_args_element_value_56;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_67 = var_tab_layout;
        tmp_called_value_34 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_67, mod_consts[7]);
        if (tmp_called_value_34 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 94;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_69 = par_self;
        tmp_expression_value_68 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_69, mod_consts[15]);
        if (tmp_expression_value_68 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_34);

            exception_lineno = 94;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_34 = mod_consts[53];
        tmp_args_element_value_54 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_68, tmp_subscript_value_34);
        Py_DECREF(tmp_expression_value_68);
        if (tmp_args_element_value_54 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_34);

            exception_lineno = 94;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_55 = mod_consts[24];
        tmp_args_element_value_56 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 94;
        {
            PyObject *call_args[] = {tmp_args_element_value_54, tmp_args_element_value_55, tmp_args_element_value_56};
            tmp_call_result_18 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_34, call_args);
        }

        Py_DECREF(tmp_called_value_34);
        Py_DECREF(tmp_args_element_value_54);
        if (tmp_call_result_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 94;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_18);
    }
    {
        PyObject *tmp_ass_subvalue_12;
        PyObject *tmp_dict_key_9;
        PyObject *tmp_dict_value_9;
        PyObject *tmp_called_value_35;
        PyObject *tmp_args_value_9;
        PyObject *tmp_tuple_element_9;
        PyObject *tmp_expression_value_70;
        PyObject *tmp_subscript_value_35;
        PyObject *tmp_kwargs_value_9;
        PyObject *tmp_ass_subscribed_12;
        PyObject *tmp_expression_value_71;
        PyObject *tmp_ass_subscript_12;
        tmp_dict_key_9 = mod_consts[30];
        tmp_called_value_35 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_35 == NULL)) {
            tmp_called_value_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_35 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 97;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_70 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_70 == NULL)) {
            tmp_expression_value_70 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_70 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 97;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_35 = mod_consts[54];
        tmp_tuple_element_9 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_70, tmp_subscript_value_35);
        if (tmp_tuple_element_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 97;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_9 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_9, 0, tmp_tuple_element_9);
        tmp_tuple_element_9 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_9, 1, tmp_tuple_element_9);
        tmp_kwargs_value_9 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 97;
        tmp_dict_value_9 = CALL_FUNCTION(tstate, tmp_called_value_35, tmp_args_value_9, tmp_kwargs_value_9);
        Py_DECREF(tmp_args_value_9);
        Py_DECREF(tmp_kwargs_value_9);
        if (tmp_dict_value_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 97;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_12 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_12, tmp_dict_key_9, tmp_dict_value_9);
        Py_DECREF(tmp_dict_value_9);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_71 = par_self;
        tmp_ass_subscribed_12 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_71, mod_consts[15]);
        if (tmp_ass_subscribed_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_12);

            exception_lineno = 96;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_12 = mod_consts[54];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_12, tmp_ass_subscript_12, tmp_ass_subvalue_12);
        Py_DECREF(tmp_ass_subscribed_12);
        Py_DECREF(tmp_ass_subvalue_12);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 96;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_36;
        PyObject *tmp_expression_value_72;
        PyObject *tmp_call_result_19;
        PyObject *tmp_args_element_value_57;
        PyObject *tmp_expression_value_73;
        PyObject *tmp_expression_value_74;
        PyObject *tmp_expression_value_75;
        PyObject *tmp_subscript_value_36;
        PyObject *tmp_subscript_value_37;
        PyObject *tmp_args_element_value_58;
        PyObject *tmp_args_element_value_59;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_72 = var_tab_layout;
        tmp_called_value_36 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_72, mod_consts[7]);
        if (tmp_called_value_36 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 99;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_75 = par_self;
        tmp_expression_value_74 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_75, mod_consts[15]);
        if (tmp_expression_value_74 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_36);

            exception_lineno = 99;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_36 = mod_consts[54];
        tmp_expression_value_73 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_74, tmp_subscript_value_36);
        Py_DECREF(tmp_expression_value_74);
        if (tmp_expression_value_73 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_36);

            exception_lineno = 99;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_37 = mod_consts[30];
        tmp_args_element_value_57 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_73, tmp_subscript_value_37);
        Py_DECREF(tmp_expression_value_73);
        if (tmp_args_element_value_57 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_36);

            exception_lineno = 99;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_58 = mod_consts[29];
        tmp_args_element_value_59 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 99;
        {
            PyObject *call_args[] = {tmp_args_element_value_57, tmp_args_element_value_58, tmp_args_element_value_59};
            tmp_call_result_19 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_36, call_args);
        }

        Py_DECREF(tmp_called_value_36);
        Py_DECREF(tmp_args_element_value_57);
        if (tmp_call_result_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 99;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_19);
    }
    {
        PyObject *tmp_assign_source_11;
        PyObject *tmp_called_value_37;
        tmp_called_value_37 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_37 == NULL)) {
            tmp_called_value_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_37 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 101;
        tmp_assign_source_11 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_37);
        if (tmp_assign_source_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_11;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_12;
        PyObject *tmp_called_value_38;
        PyObject *tmp_args_element_value_60;
        tmp_called_value_38 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_38 == NULL)) {
            tmp_called_value_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_38 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_60 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 102;
        tmp_assign_source_12 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_38, tmp_args_element_value_60);
        if (tmp_assign_source_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_12;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_7;
        PyObject *tmp_call_result_20;
        PyObject *tmp_args_element_value_61;
        PyObject *tmp_args_element_value_62;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_7 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_61 = var_tab;
        tmp_args_element_value_62 = mod_consts[55];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 103;
        {
            PyObject *call_args[] = {tmp_args_element_value_61, tmp_args_element_value_62};
            tmp_call_result_20 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_7,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_20 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 103;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_20);
    }
    {
        PyObject *tmp_ass_subvalue_13;
        PyObject *tmp_called_value_39;
        PyObject *tmp_args_element_value_63;
        PyObject *tmp_args_element_value_64;
        PyObject *tmp_expression_value_76;
        PyObject *tmp_subscript_value_38;
        PyObject *tmp_ass_subscribed_13;
        PyObject *tmp_expression_value_77;
        PyObject *tmp_ass_subscript_13;
        tmp_called_value_39 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_39 == NULL)) {
            tmp_called_value_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_39 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 105;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_63 = mod_consts[56];
        tmp_expression_value_76 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_76 == NULL)) {
            tmp_expression_value_76 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_76 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 105;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_38 = mod_consts[56];
        tmp_args_element_value_64 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_76, tmp_subscript_value_38);
        if (tmp_args_element_value_64 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 105;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 105;
        {
            PyObject *call_args[] = {tmp_args_element_value_63, tmp_args_element_value_64};
            tmp_ass_subvalue_13 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_39, call_args);
        }

        Py_DECREF(tmp_args_element_value_64);
        if (tmp_ass_subvalue_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 105;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_77 = par_self;
        tmp_ass_subscribed_13 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_77, mod_consts[15]);
        if (tmp_ass_subscribed_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_13);

            exception_lineno = 105;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_13 = mod_consts[56];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_13, tmp_ass_subscript_13, tmp_ass_subvalue_13);
        Py_DECREF(tmp_ass_subscribed_13);
        Py_DECREF(tmp_ass_subvalue_13);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 105;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_40;
        PyObject *tmp_expression_value_78;
        PyObject *tmp_call_result_21;
        PyObject *tmp_args_element_value_65;
        PyObject *tmp_expression_value_79;
        PyObject *tmp_expression_value_80;
        PyObject *tmp_subscript_value_39;
        PyObject *tmp_args_element_value_66;
        PyObject *tmp_args_element_value_67;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_78 = var_tab_layout;
        tmp_called_value_40 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_78, mod_consts[7]);
        if (tmp_called_value_40 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 106;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_80 = par_self;
        tmp_expression_value_79 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_80, mod_consts[15]);
        if (tmp_expression_value_79 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_40);

            exception_lineno = 106;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_39 = mod_consts[56];
        tmp_args_element_value_65 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_79, tmp_subscript_value_39);
        Py_DECREF(tmp_expression_value_79);
        if (tmp_args_element_value_65 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_40);

            exception_lineno = 106;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_66 = mod_consts[24];
        tmp_args_element_value_67 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 106;
        {
            PyObject *call_args[] = {tmp_args_element_value_65, tmp_args_element_value_66, tmp_args_element_value_67};
            tmp_call_result_21 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_40, call_args);
        }

        Py_DECREF(tmp_called_value_40);
        Py_DECREF(tmp_args_element_value_65);
        if (tmp_call_result_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 106;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_21);
    }
    {
        PyObject *tmp_ass_subvalue_14;
        PyObject *tmp_called_value_41;
        PyObject *tmp_args_element_value_68;
        PyObject *tmp_args_element_value_69;
        PyObject *tmp_expression_value_81;
        PyObject *tmp_subscript_value_40;
        PyObject *tmp_ass_subscribed_14;
        PyObject *tmp_expression_value_82;
        PyObject *tmp_ass_subscript_14;
        tmp_called_value_41 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_41 == NULL)) {
            tmp_called_value_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_41 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 108;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_68 = mod_consts[57];
        tmp_expression_value_81 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_81 == NULL)) {
            tmp_expression_value_81 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_81 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 108;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_40 = mod_consts[57];
        tmp_args_element_value_69 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_81, tmp_subscript_value_40);
        if (tmp_args_element_value_69 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 108;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 108;
        {
            PyObject *call_args[] = {tmp_args_element_value_68, tmp_args_element_value_69};
            tmp_ass_subvalue_14 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_41, call_args);
        }

        Py_DECREF(tmp_args_element_value_69);
        if (tmp_ass_subvalue_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 108;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_82 = par_self;
        tmp_ass_subscribed_14 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_82, mod_consts[15]);
        if (tmp_ass_subscribed_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_14);

            exception_lineno = 108;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_14 = mod_consts[57];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_14, tmp_ass_subscript_14, tmp_ass_subvalue_14);
        Py_DECREF(tmp_ass_subscribed_14);
        Py_DECREF(tmp_ass_subvalue_14);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 108;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_42;
        PyObject *tmp_expression_value_83;
        PyObject *tmp_call_result_22;
        PyObject *tmp_args_element_value_70;
        PyObject *tmp_expression_value_84;
        PyObject *tmp_expression_value_85;
        PyObject *tmp_subscript_value_41;
        PyObject *tmp_args_element_value_71;
        PyObject *tmp_args_element_value_72;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_83 = var_tab_layout;
        tmp_called_value_42 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_83, mod_consts[7]);
        if (tmp_called_value_42 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 109;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_85 = par_self;
        tmp_expression_value_84 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_85, mod_consts[15]);
        if (tmp_expression_value_84 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_42);

            exception_lineno = 109;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_41 = mod_consts[57];
        tmp_args_element_value_70 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_84, tmp_subscript_value_41);
        Py_DECREF(tmp_expression_value_84);
        if (tmp_args_element_value_70 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_42);

            exception_lineno = 109;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_71 = mod_consts[29];
        tmp_args_element_value_72 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 109;
        {
            PyObject *call_args[] = {tmp_args_element_value_70, tmp_args_element_value_71, tmp_args_element_value_72};
            tmp_call_result_22 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_42, call_args);
        }

        Py_DECREF(tmp_called_value_42);
        Py_DECREF(tmp_args_element_value_70);
        if (tmp_call_result_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 109;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_22);
    }
    {
        PyObject *tmp_assign_source_13;
        PyObject *tmp_called_value_43;
        tmp_called_value_43 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_43 == NULL)) {
            tmp_called_value_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_43 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 111;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 111;
        tmp_assign_source_13 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_43);
        if (tmp_assign_source_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 111;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_13;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_called_value_44;
        PyObject *tmp_args_element_value_73;
        tmp_called_value_44 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_44 == NULL)) {
            tmp_called_value_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_44 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 112;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_73 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 112;
        tmp_assign_source_14 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_44, tmp_args_element_value_73);
        if (tmp_assign_source_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 112;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_14;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_8;
        PyObject *tmp_call_result_23;
        PyObject *tmp_args_element_value_74;
        PyObject *tmp_args_element_value_75;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_8 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_74 = var_tab;
        tmp_args_element_value_75 = mod_consts[58];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 113;
        {
            PyObject *call_args[] = {tmp_args_element_value_74, tmp_args_element_value_75};
            tmp_call_result_23 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_8,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_23 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 113;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_23);
    }
    {
        PyObject *tmp_ass_subvalue_15;
        PyObject *tmp_dict_key_10;
        PyObject *tmp_dict_value_10;
        PyObject *tmp_called_value_45;
        PyObject *tmp_args_value_10;
        PyObject *tmp_tuple_element_10;
        PyObject *tmp_expression_value_86;
        PyObject *tmp_subscript_value_42;
        PyObject *tmp_kwargs_value_10;
        PyObject *tmp_ass_subscribed_15;
        PyObject *tmp_expression_value_87;
        PyObject *tmp_ass_subscript_15;
        tmp_dict_key_10 = mod_consts[30];
        tmp_called_value_45 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_45 == NULL)) {
            tmp_called_value_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_45 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 116;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_86 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_86 == NULL)) {
            tmp_expression_value_86 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_86 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 116;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_42 = mod_consts[59];
        tmp_tuple_element_10 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_86, tmp_subscript_value_42);
        if (tmp_tuple_element_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 116;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_10 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_10, 0, tmp_tuple_element_10);
        tmp_tuple_element_10 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_10, 1, tmp_tuple_element_10);
        tmp_kwargs_value_10 = DICT_COPY(mod_consts[60]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 116;
        tmp_dict_value_10 = CALL_FUNCTION(tstate, tmp_called_value_45, tmp_args_value_10, tmp_kwargs_value_10);
        Py_DECREF(tmp_args_value_10);
        Py_DECREF(tmp_kwargs_value_10);
        if (tmp_dict_value_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 116;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_15 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_15, tmp_dict_key_10, tmp_dict_value_10);
        Py_DECREF(tmp_dict_value_10);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_87 = par_self;
        tmp_ass_subscribed_15 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_87, mod_consts[15]);
        if (tmp_ass_subscribed_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_15);

            exception_lineno = 115;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_15 = mod_consts[59];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_15, tmp_ass_subscript_15, tmp_ass_subvalue_15);
        Py_DECREF(tmp_ass_subscribed_15);
        Py_DECREF(tmp_ass_subvalue_15);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 115;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_46;
        PyObject *tmp_expression_value_88;
        PyObject *tmp_call_result_24;
        PyObject *tmp_args_element_value_76;
        PyObject *tmp_expression_value_89;
        PyObject *tmp_expression_value_90;
        PyObject *tmp_expression_value_91;
        PyObject *tmp_subscript_value_43;
        PyObject *tmp_subscript_value_44;
        PyObject *tmp_args_element_value_77;
        PyObject *tmp_args_element_value_78;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_88 = var_tab_layout;
        tmp_called_value_46 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_88, mod_consts[7]);
        if (tmp_called_value_46 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 118;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_91 = par_self;
        tmp_expression_value_90 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_91, mod_consts[15]);
        if (tmp_expression_value_90 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_46);

            exception_lineno = 118;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_43 = mod_consts[59];
        tmp_expression_value_89 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_90, tmp_subscript_value_43);
        Py_DECREF(tmp_expression_value_90);
        if (tmp_expression_value_89 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_46);

            exception_lineno = 118;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_44 = mod_consts[30];
        tmp_args_element_value_76 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_89, tmp_subscript_value_44);
        Py_DECREF(tmp_expression_value_89);
        if (tmp_args_element_value_76 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_46);

            exception_lineno = 118;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_77 = mod_consts[24];
        tmp_args_element_value_78 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 118;
        {
            PyObject *call_args[] = {tmp_args_element_value_76, tmp_args_element_value_77, tmp_args_element_value_78};
            tmp_call_result_24 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_46, call_args);
        }

        Py_DECREF(tmp_called_value_46);
        Py_DECREF(tmp_args_element_value_76);
        if (tmp_call_result_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 118;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_24);
    }
    {
        PyObject *tmp_assign_source_15;
        PyObject *tmp_called_value_47;
        tmp_called_value_47 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_47 == NULL)) {
            tmp_called_value_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_47 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 120;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 120;
        tmp_assign_source_15 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_47);
        if (tmp_assign_source_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 120;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_15;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_16;
        PyObject *tmp_called_value_48;
        PyObject *tmp_args_element_value_79;
        tmp_called_value_48 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_48 == NULL)) {
            tmp_called_value_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_48 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 121;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_79 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 121;
        tmp_assign_source_16 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_48, tmp_args_element_value_79);
        if (tmp_assign_source_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 121;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_16;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_9;
        PyObject *tmp_call_result_25;
        PyObject *tmp_args_element_value_80;
        PyObject *tmp_args_element_value_81;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_9 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_80 = var_tab;
        tmp_args_element_value_81 = mod_consts[61];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 122;
        {
            PyObject *call_args[] = {tmp_args_element_value_80, tmp_args_element_value_81};
            tmp_call_result_25 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_9,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 122;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_25);
    }
    {
        PyObject *tmp_ass_subvalue_16;
        PyObject *tmp_called_value_49;
        PyObject *tmp_args_element_value_82;
        PyObject *tmp_args_element_value_83;
        PyObject *tmp_expression_value_92;
        PyObject *tmp_subscript_value_45;
        PyObject *tmp_ass_subscribed_16;
        PyObject *tmp_expression_value_93;
        PyObject *tmp_ass_subscript_16;
        tmp_called_value_49 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_49 == NULL)) {
            tmp_called_value_49 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_49 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 124;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_82 = mod_consts[62];
        tmp_expression_value_92 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_92 == NULL)) {
            tmp_expression_value_92 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_92 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 124;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_45 = mod_consts[62];
        tmp_args_element_value_83 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_92, tmp_subscript_value_45);
        if (tmp_args_element_value_83 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 124;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 124;
        {
            PyObject *call_args[] = {tmp_args_element_value_82, tmp_args_element_value_83};
            tmp_ass_subvalue_16 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_49, call_args);
        }

        Py_DECREF(tmp_args_element_value_83);
        if (tmp_ass_subvalue_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 124;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_93 = par_self;
        tmp_ass_subscribed_16 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_93, mod_consts[15]);
        if (tmp_ass_subscribed_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_16);

            exception_lineno = 124;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_16 = mod_consts[62];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_16, tmp_ass_subscript_16, tmp_ass_subvalue_16);
        Py_DECREF(tmp_ass_subscribed_16);
        Py_DECREF(tmp_ass_subvalue_16);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 124;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_50;
        PyObject *tmp_expression_value_94;
        PyObject *tmp_call_result_26;
        PyObject *tmp_args_element_value_84;
        PyObject *tmp_expression_value_95;
        PyObject *tmp_expression_value_96;
        PyObject *tmp_subscript_value_46;
        PyObject *tmp_args_element_value_85;
        PyObject *tmp_args_element_value_86;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_94 = var_tab_layout;
        tmp_called_value_50 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_94, mod_consts[7]);
        if (tmp_called_value_50 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 125;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_96 = par_self;
        tmp_expression_value_95 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_96, mod_consts[15]);
        if (tmp_expression_value_95 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_50);

            exception_lineno = 125;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_46 = mod_consts[62];
        tmp_args_element_value_84 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_95, tmp_subscript_value_46);
        Py_DECREF(tmp_expression_value_95);
        if (tmp_args_element_value_84 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_50);

            exception_lineno = 125;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_85 = mod_consts[24];
        tmp_args_element_value_86 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 125;
        {
            PyObject *call_args[] = {tmp_args_element_value_84, tmp_args_element_value_85, tmp_args_element_value_86};
            tmp_call_result_26 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_50, call_args);
        }

        Py_DECREF(tmp_called_value_50);
        Py_DECREF(tmp_args_element_value_84);
        if (tmp_call_result_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 125;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_26);
    }
    {
        PyObject *tmp_ass_subvalue_17;
        PyObject *tmp_dict_key_11;
        PyObject *tmp_dict_value_11;
        PyObject *tmp_called_value_51;
        PyObject *tmp_args_value_11;
        PyObject *tmp_tuple_element_11;
        PyObject *tmp_expression_value_97;
        PyObject *tmp_subscript_value_47;
        PyObject *tmp_kwargs_value_11;
        PyObject *tmp_ass_subscribed_17;
        PyObject *tmp_expression_value_98;
        PyObject *tmp_ass_subscript_17;
        tmp_dict_key_11 = mod_consts[30];
        tmp_called_value_51 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_51 == NULL)) {
            tmp_called_value_51 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_51 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 128;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_97 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_97 == NULL)) {
            tmp_expression_value_97 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_97 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 128;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_47 = mod_consts[63];
        tmp_tuple_element_11 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_97, tmp_subscript_value_47);
        if (tmp_tuple_element_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 128;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_11 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_11, 0, tmp_tuple_element_11);
        tmp_tuple_element_11 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_11, 1, tmp_tuple_element_11);
        tmp_kwargs_value_11 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 128;
        tmp_dict_value_11 = CALL_FUNCTION(tstate, tmp_called_value_51, tmp_args_value_11, tmp_kwargs_value_11);
        Py_DECREF(tmp_args_value_11);
        Py_DECREF(tmp_kwargs_value_11);
        if (tmp_dict_value_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 128;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_17 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_17, tmp_dict_key_11, tmp_dict_value_11);
        Py_DECREF(tmp_dict_value_11);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_98 = par_self;
        tmp_ass_subscribed_17 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_98, mod_consts[15]);
        if (tmp_ass_subscribed_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_17);

            exception_lineno = 127;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_17 = mod_consts[63];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_17, tmp_ass_subscript_17, tmp_ass_subvalue_17);
        Py_DECREF(tmp_ass_subscribed_17);
        Py_DECREF(tmp_ass_subvalue_17);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 127;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_52;
        PyObject *tmp_expression_value_99;
        PyObject *tmp_call_result_27;
        PyObject *tmp_args_element_value_87;
        PyObject *tmp_expression_value_100;
        PyObject *tmp_expression_value_101;
        PyObject *tmp_expression_value_102;
        PyObject *tmp_subscript_value_48;
        PyObject *tmp_subscript_value_49;
        PyObject *tmp_args_element_value_88;
        PyObject *tmp_args_element_value_89;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_99 = var_tab_layout;
        tmp_called_value_52 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_99, mod_consts[7]);
        if (tmp_called_value_52 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 130;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_102 = par_self;
        tmp_expression_value_101 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_102, mod_consts[15]);
        if (tmp_expression_value_101 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_52);

            exception_lineno = 130;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_48 = mod_consts[63];
        tmp_expression_value_100 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_101, tmp_subscript_value_48);
        Py_DECREF(tmp_expression_value_101);
        if (tmp_expression_value_100 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_52);

            exception_lineno = 130;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_49 = mod_consts[30];
        tmp_args_element_value_87 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_100, tmp_subscript_value_49);
        Py_DECREF(tmp_expression_value_100);
        if (tmp_args_element_value_87 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_52);

            exception_lineno = 130;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_88 = mod_consts[29];
        tmp_args_element_value_89 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 130;
        {
            PyObject *call_args[] = {tmp_args_element_value_87, tmp_args_element_value_88, tmp_args_element_value_89};
            tmp_call_result_27 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_52, call_args);
        }

        Py_DECREF(tmp_called_value_52);
        Py_DECREF(tmp_args_element_value_87);
        if (tmp_call_result_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 130;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_27);
    }
    {
        PyObject *tmp_assign_source_17;
        PyObject *tmp_called_value_53;
        tmp_called_value_53 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_53 == NULL)) {
            tmp_called_value_53 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_53 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 132;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 132;
        tmp_assign_source_17 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_53);
        if (tmp_assign_source_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 132;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_17;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_18;
        PyObject *tmp_called_value_54;
        PyObject *tmp_args_element_value_90;
        tmp_called_value_54 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_54 == NULL)) {
            tmp_called_value_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_54 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 133;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_90 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 133;
        tmp_assign_source_18 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_54, tmp_args_element_value_90);
        if (tmp_assign_source_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 133;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_18;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_10;
        PyObject *tmp_call_result_28;
        PyObject *tmp_args_element_value_91;
        PyObject *tmp_args_element_value_92;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_10 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_91 = var_tab;
        tmp_args_element_value_92 = mod_consts[64];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 134;
        {
            PyObject *call_args[] = {tmp_args_element_value_91, tmp_args_element_value_92};
            tmp_call_result_28 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_10,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_28);
    }
    {
        PyObject *tmp_ass_subvalue_18;
        PyObject *tmp_called_value_55;
        PyObject *tmp_args_element_value_93;
        PyObject *tmp_args_element_value_94;
        PyObject *tmp_expression_value_103;
        PyObject *tmp_subscript_value_50;
        PyObject *tmp_ass_subscribed_18;
        PyObject *tmp_expression_value_104;
        PyObject *tmp_ass_subscript_18;
        tmp_called_value_55 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_55 == NULL)) {
            tmp_called_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_55 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 136;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_93 = mod_consts[65];
        tmp_expression_value_103 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_103 == NULL)) {
            tmp_expression_value_103 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_103 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 136;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_50 = mod_consts[65];
        tmp_args_element_value_94 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_103, tmp_subscript_value_50);
        if (tmp_args_element_value_94 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 136;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 136;
        {
            PyObject *call_args[] = {tmp_args_element_value_93, tmp_args_element_value_94};
            tmp_ass_subvalue_18 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_55, call_args);
        }

        Py_DECREF(tmp_args_element_value_94);
        if (tmp_ass_subvalue_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 136;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_104 = par_self;
        tmp_ass_subscribed_18 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_104, mod_consts[15]);
        if (tmp_ass_subscribed_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_18);

            exception_lineno = 136;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_18 = mod_consts[65];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_18, tmp_ass_subscript_18, tmp_ass_subvalue_18);
        Py_DECREF(tmp_ass_subscribed_18);
        Py_DECREF(tmp_ass_subvalue_18);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 136;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_56;
        PyObject *tmp_expression_value_105;
        PyObject *tmp_call_result_29;
        PyObject *tmp_args_element_value_95;
        PyObject *tmp_expression_value_106;
        PyObject *tmp_expression_value_107;
        PyObject *tmp_subscript_value_51;
        PyObject *tmp_args_element_value_96;
        PyObject *tmp_args_element_value_97;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_105 = var_tab_layout;
        tmp_called_value_56 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_105, mod_consts[7]);
        if (tmp_called_value_56 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 137;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_107 = par_self;
        tmp_expression_value_106 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_107, mod_consts[15]);
        if (tmp_expression_value_106 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_56);

            exception_lineno = 137;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_51 = mod_consts[65];
        tmp_args_element_value_95 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_106, tmp_subscript_value_51);
        Py_DECREF(tmp_expression_value_106);
        if (tmp_args_element_value_95 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_56);

            exception_lineno = 137;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_96 = mod_consts[24];
        tmp_args_element_value_97 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 137;
        {
            PyObject *call_args[] = {tmp_args_element_value_95, tmp_args_element_value_96, tmp_args_element_value_97};
            tmp_call_result_29 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_56, call_args);
        }

        Py_DECREF(tmp_called_value_56);
        Py_DECREF(tmp_args_element_value_95);
        if (tmp_call_result_29 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 137;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_29);
    }
    {
        PyObject *tmp_ass_subvalue_19;
        PyObject *tmp_called_value_57;
        PyObject *tmp_args_element_value_98;
        PyObject *tmp_args_element_value_99;
        PyObject *tmp_expression_value_108;
        PyObject *tmp_subscript_value_52;
        PyObject *tmp_ass_subscribed_19;
        PyObject *tmp_expression_value_109;
        PyObject *tmp_ass_subscript_19;
        tmp_called_value_57 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_57 == NULL)) {
            tmp_called_value_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_57 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 139;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_98 = mod_consts[66];
        tmp_expression_value_108 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_108 == NULL)) {
            tmp_expression_value_108 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_108 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 139;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_52 = mod_consts[66];
        tmp_args_element_value_99 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_108, tmp_subscript_value_52);
        if (tmp_args_element_value_99 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 139;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 139;
        {
            PyObject *call_args[] = {tmp_args_element_value_98, tmp_args_element_value_99};
            tmp_ass_subvalue_19 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_57, call_args);
        }

        Py_DECREF(tmp_args_element_value_99);
        if (tmp_ass_subvalue_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 139;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_109 = par_self;
        tmp_ass_subscribed_19 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_109, mod_consts[15]);
        if (tmp_ass_subscribed_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_19);

            exception_lineno = 139;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_19 = mod_consts[66];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_19, tmp_ass_subscript_19, tmp_ass_subvalue_19);
        Py_DECREF(tmp_ass_subscribed_19);
        Py_DECREF(tmp_ass_subvalue_19);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 139;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_58;
        PyObject *tmp_expression_value_110;
        PyObject *tmp_call_result_30;
        PyObject *tmp_args_element_value_100;
        PyObject *tmp_expression_value_111;
        PyObject *tmp_expression_value_112;
        PyObject *tmp_subscript_value_53;
        PyObject *tmp_args_element_value_101;
        PyObject *tmp_args_element_value_102;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_110 = var_tab_layout;
        tmp_called_value_58 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_110, mod_consts[7]);
        if (tmp_called_value_58 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 140;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_112 = par_self;
        tmp_expression_value_111 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_112, mod_consts[15]);
        if (tmp_expression_value_111 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_58);

            exception_lineno = 140;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_53 = mod_consts[66];
        tmp_args_element_value_100 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_111, tmp_subscript_value_53);
        Py_DECREF(tmp_expression_value_111);
        if (tmp_args_element_value_100 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_58);

            exception_lineno = 140;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_101 = mod_consts[29];
        tmp_args_element_value_102 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 140;
        {
            PyObject *call_args[] = {tmp_args_element_value_100, tmp_args_element_value_101, tmp_args_element_value_102};
            tmp_call_result_30 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_58, call_args);
        }

        Py_DECREF(tmp_called_value_58);
        Py_DECREF(tmp_args_element_value_100);
        if (tmp_call_result_30 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 140;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_30);
    }
    {
        PyObject *tmp_ass_subvalue_20;
        PyObject *tmp_dict_key_12;
        PyObject *tmp_dict_value_12;
        PyObject *tmp_called_value_59;
        PyObject *tmp_kw_call_value_0_2;
        PyObject *tmp_list_element_2;
        PyObject *tmp_ass_subscribed_20;
        PyObject *tmp_expression_value_115;
        PyObject *tmp_ass_subscript_20;
        tmp_dict_key_12 = mod_consts[36];
        tmp_called_value_59 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[4]);

        if (unlikely(tmp_called_value_59 == NULL)) {
            tmp_called_value_59 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[4]);
        }

        if (tmp_called_value_59 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 143;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_list_element_2 = mod_consts[37];
        tmp_kw_call_value_0_2 = MAKE_LIST_EMPTY(3);
        {
            PyObject *tmp_expression_value_113;
            PyObject *tmp_subscript_value_54;
            PyObject *tmp_expression_value_114;
            PyObject *tmp_subscript_value_55;
            PyList_SET_ITEM0(tmp_kw_call_value_0_2, 0, tmp_list_element_2);
            tmp_expression_value_113 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_113 == NULL)) {
                tmp_expression_value_113 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_113 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 143;
                type_description_1 = "oooooc";
                goto list_build_exception_2;
            }
            tmp_subscript_value_54 = mod_consts[67];
            tmp_list_element_2 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_113, tmp_subscript_value_54);
            if (tmp_list_element_2 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 143;
                type_description_1 = "oooooc";
                goto list_build_exception_2;
            }
            PyList_SET_ITEM(tmp_kw_call_value_0_2, 1, tmp_list_element_2);
            tmp_expression_value_114 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_114 == NULL)) {
                tmp_expression_value_114 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_114 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 143;
                type_description_1 = "oooooc";
                goto list_build_exception_2;
            }
            tmp_subscript_value_55 = mod_consts[68];
            tmp_list_element_2 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_114, tmp_subscript_value_55);
            if (tmp_list_element_2 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 143;
                type_description_1 = "oooooc";
                goto list_build_exception_2;
            }
            PyList_SET_ITEM(tmp_kw_call_value_0_2, 2, tmp_list_element_2);
        }
        goto list_build_noexception_2;
        // Exception handling pass through code for list_build:
        list_build_exception_2:;
        Py_DECREF(tmp_kw_call_value_0_2);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_2:;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 143;
        {
            PyObject *kw_values[1] = {tmp_kw_call_value_0_2};
            tmp_dict_value_12 = CALL_FUNCTION_WITH_POSARGS2_KWSPLIT(tstate, tmp_called_value_59, mod_consts[69], kw_values, mod_consts[41]);
        }

        Py_DECREF(tmp_kw_call_value_0_2);
        if (tmp_dict_value_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 143;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_20 = _PyDict_NewPresized( 3 );
        {
            PyObject *tmp_called_value_60;
            PyObject *tmp_called_value_61;
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_20, tmp_dict_key_12, tmp_dict_value_12);
            Py_DECREF(tmp_dict_value_12);
            assert(!(tmp_res != 0));
            tmp_dict_key_12 = mod_consts[25];
            tmp_called_value_60 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

            if (unlikely(tmp_called_value_60 == NULL)) {
                tmp_called_value_60 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
            }

            if (tmp_called_value_60 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 144;
                type_description_1 = "oooooc";
                goto dict_build_exception_2;
            }
            frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 144;
            tmp_dict_value_12 = CALL_FUNCTION_WITH_ARGS2_VECTORCALL(tstate, tmp_called_value_60, &PyTuple_GET_ITEM(mod_consts[70], 0), mod_consts[10]);
            if (tmp_dict_value_12 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 144;
                type_description_1 = "oooooc";
                goto dict_build_exception_2;
            }
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_20, tmp_dict_key_12, tmp_dict_value_12);
            Py_DECREF(tmp_dict_value_12);
            assert(!(tmp_res != 0));
            tmp_dict_key_12 = mod_consts[30];
            tmp_called_value_61 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

            if (unlikely(tmp_called_value_61 == NULL)) {
                tmp_called_value_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
            }

            if (tmp_called_value_61 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 145;
                type_description_1 = "oooooc";
                goto dict_build_exception_2;
            }
            frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 145;
            tmp_dict_value_12 = CALL_FUNCTION_WITH_ARGS2_VECTORCALL(tstate, tmp_called_value_61, &PyTuple_GET_ITEM(mod_consts[71], 0), mod_consts[10]);
            if (tmp_dict_value_12 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 145;
                type_description_1 = "oooooc";
                goto dict_build_exception_2;
            }
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_20, tmp_dict_key_12, tmp_dict_value_12);
            Py_DECREF(tmp_dict_value_12);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_2;
        // Exception handling pass through code for dict_build:
        dict_build_exception_2:;
        Py_DECREF(tmp_ass_subvalue_20);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_2:;
        CHECK_OBJECT(par_self);
        tmp_expression_value_115 = par_self;
        tmp_ass_subscribed_20 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_115, mod_consts[15]);
        if (tmp_ass_subscribed_20 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_20);

            exception_lineno = 142;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_20 = mod_consts[67];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_20, tmp_ass_subscript_20, tmp_ass_subvalue_20);
        Py_DECREF(tmp_ass_subscribed_20);
        Py_DECREF(tmp_ass_subvalue_20);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 142;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_62;
        PyObject *tmp_expression_value_116;
        PyObject *tmp_call_result_31;
        PyObject *tmp_args_element_value_103;
        PyObject *tmp_expression_value_117;
        PyObject *tmp_expression_value_118;
        PyObject *tmp_expression_value_119;
        PyObject *tmp_subscript_value_56;
        PyObject *tmp_subscript_value_57;
        PyObject *tmp_args_element_value_104;
        PyObject *tmp_args_element_value_105;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_116 = var_tab_layout;
        tmp_called_value_62 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_116, mod_consts[7]);
        if (tmp_called_value_62 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 147;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_119 = par_self;
        tmp_expression_value_118 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_119, mod_consts[15]);
        if (tmp_expression_value_118 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_62);

            exception_lineno = 147;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_56 = mod_consts[67];
        tmp_expression_value_117 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_118, tmp_subscript_value_56);
        Py_DECREF(tmp_expression_value_118);
        if (tmp_expression_value_117 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_62);

            exception_lineno = 147;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_57 = mod_consts[36];
        tmp_args_element_value_103 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_117, tmp_subscript_value_57);
        Py_DECREF(tmp_expression_value_117);
        if (tmp_args_element_value_103 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_62);

            exception_lineno = 147;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_104 = mod_consts[33];
        tmp_args_element_value_105 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 147;
        {
            PyObject *call_args[] = {tmp_args_element_value_103, tmp_args_element_value_104, tmp_args_element_value_105};
            tmp_call_result_31 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_62, call_args);
        }

        Py_DECREF(tmp_called_value_62);
        Py_DECREF(tmp_args_element_value_103);
        if (tmp_call_result_31 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 147;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_31);
    }
    {
        PyObject *tmp_called_value_63;
        PyObject *tmp_expression_value_120;
        PyObject *tmp_call_result_32;
        PyObject *tmp_args_element_value_106;
        PyObject *tmp_expression_value_121;
        PyObject *tmp_expression_value_122;
        PyObject *tmp_expression_value_123;
        PyObject *tmp_subscript_value_58;
        PyObject *tmp_subscript_value_59;
        PyObject *tmp_args_element_value_107;
        PyObject *tmp_args_element_value_108;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_120 = var_tab_layout;
        tmp_called_value_63 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_120, mod_consts[7]);
        if (tmp_called_value_63 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_123 = par_self;
        tmp_expression_value_122 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_123, mod_consts[15]);
        if (tmp_expression_value_122 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_63);

            exception_lineno = 148;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_58 = mod_consts[67];
        tmp_expression_value_121 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_122, tmp_subscript_value_58);
        Py_DECREF(tmp_expression_value_122);
        if (tmp_expression_value_121 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_63);

            exception_lineno = 148;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_59 = mod_consts[25];
        tmp_args_element_value_106 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_121, tmp_subscript_value_59);
        Py_DECREF(tmp_expression_value_121);
        if (tmp_args_element_value_106 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_63);

            exception_lineno = 148;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_107 = mod_consts[33];
        tmp_args_element_value_108 = mod_consts[29];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 148;
        {
            PyObject *call_args[] = {tmp_args_element_value_106, tmp_args_element_value_107, tmp_args_element_value_108};
            tmp_call_result_32 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_63, call_args);
        }

        Py_DECREF(tmp_called_value_63);
        Py_DECREF(tmp_args_element_value_106);
        if (tmp_call_result_32 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_32);
    }
    {
        PyObject *tmp_called_value_64;
        PyObject *tmp_expression_value_124;
        PyObject *tmp_call_result_33;
        PyObject *tmp_args_element_value_109;
        PyObject *tmp_expression_value_125;
        PyObject *tmp_expression_value_126;
        PyObject *tmp_expression_value_127;
        PyObject *tmp_subscript_value_60;
        PyObject *tmp_subscript_value_61;
        PyObject *tmp_args_element_value_110;
        PyObject *tmp_args_element_value_111;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_124 = var_tab_layout;
        tmp_called_value_64 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_124, mod_consts[7]);
        if (tmp_called_value_64 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 149;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_127 = par_self;
        tmp_expression_value_126 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_127, mod_consts[15]);
        if (tmp_expression_value_126 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_64);

            exception_lineno = 149;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_60 = mod_consts[67];
        tmp_expression_value_125 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_126, tmp_subscript_value_60);
        Py_DECREF(tmp_expression_value_126);
        if (tmp_expression_value_125 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_64);

            exception_lineno = 149;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_61 = mod_consts[30];
        tmp_args_element_value_109 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_125, tmp_subscript_value_61);
        Py_DECREF(tmp_expression_value_125);
        if (tmp_args_element_value_109 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_64);

            exception_lineno = 149;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_110 = mod_consts[33];
        tmp_args_element_value_111 = mod_consts[33];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 149;
        {
            PyObject *call_args[] = {tmp_args_element_value_109, tmp_args_element_value_110, tmp_args_element_value_111};
            tmp_call_result_33 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_64, call_args);
        }

        Py_DECREF(tmp_called_value_64);
        Py_DECREF(tmp_args_element_value_109);
        if (tmp_call_result_33 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 149;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_33);
    }
    {
        PyObject *tmp_assign_source_19;
        PyObject *tmp_called_value_65;
        tmp_called_value_65 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_65 == NULL)) {
            tmp_called_value_65 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_65 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 151;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 151;
        tmp_assign_source_19 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_65);
        if (tmp_assign_source_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 151;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_19;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_20;
        PyObject *tmp_called_value_66;
        PyObject *tmp_args_element_value_112;
        tmp_called_value_66 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_66 == NULL)) {
            tmp_called_value_66 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_66 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 152;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_112 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 152;
        tmp_assign_source_20 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_66, tmp_args_element_value_112);
        if (tmp_assign_source_20 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 152;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_20;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_11;
        PyObject *tmp_call_result_34;
        PyObject *tmp_args_element_value_113;
        PyObject *tmp_args_element_value_114;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_11 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_113 = var_tab;
        tmp_args_element_value_114 = mod_consts[72];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 153;
        {
            PyObject *call_args[] = {tmp_args_element_value_113, tmp_args_element_value_114};
            tmp_call_result_34 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_11,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_34 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 153;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_34);
    }
    {
        PyObject *tmp_ass_subvalue_21;
        PyObject *tmp_called_value_67;
        PyObject *tmp_args_element_value_115;
        PyObject *tmp_args_element_value_116;
        PyObject *tmp_expression_value_128;
        PyObject *tmp_subscript_value_62;
        PyObject *tmp_ass_subscribed_21;
        PyObject *tmp_expression_value_129;
        PyObject *tmp_ass_subscript_21;
        tmp_called_value_67 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_67 == NULL)) {
            tmp_called_value_67 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_67 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 155;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_115 = mod_consts[73];
        tmp_expression_value_128 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_128 == NULL)) {
            tmp_expression_value_128 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_128 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 155;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_62 = mod_consts[73];
        tmp_args_element_value_116 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_128, tmp_subscript_value_62);
        if (tmp_args_element_value_116 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 155;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 155;
        {
            PyObject *call_args[] = {tmp_args_element_value_115, tmp_args_element_value_116};
            tmp_ass_subvalue_21 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_67, call_args);
        }

        Py_DECREF(tmp_args_element_value_116);
        if (tmp_ass_subvalue_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 155;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_129 = par_self;
        tmp_ass_subscribed_21 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_129, mod_consts[15]);
        if (tmp_ass_subscribed_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_21);

            exception_lineno = 155;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_21 = mod_consts[73];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_21, tmp_ass_subscript_21, tmp_ass_subvalue_21);
        Py_DECREF(tmp_ass_subscribed_21);
        Py_DECREF(tmp_ass_subvalue_21);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 155;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_68;
        PyObject *tmp_expression_value_130;
        PyObject *tmp_call_result_35;
        PyObject *tmp_args_element_value_117;
        PyObject *tmp_expression_value_131;
        PyObject *tmp_expression_value_132;
        PyObject *tmp_subscript_value_63;
        PyObject *tmp_args_element_value_118;
        PyObject *tmp_args_element_value_119;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_130 = var_tab_layout;
        tmp_called_value_68 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_130, mod_consts[7]);
        if (tmp_called_value_68 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 156;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_132 = par_self;
        tmp_expression_value_131 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_132, mod_consts[15]);
        if (tmp_expression_value_131 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_68);

            exception_lineno = 156;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_63 = mod_consts[73];
        tmp_args_element_value_117 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_131, tmp_subscript_value_63);
        Py_DECREF(tmp_expression_value_131);
        if (tmp_args_element_value_117 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_68);

            exception_lineno = 156;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_118 = mod_consts[24];
        tmp_args_element_value_119 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 156;
        {
            PyObject *call_args[] = {tmp_args_element_value_117, tmp_args_element_value_118, tmp_args_element_value_119};
            tmp_call_result_35 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_68, call_args);
        }

        Py_DECREF(tmp_called_value_68);
        Py_DECREF(tmp_args_element_value_117);
        if (tmp_call_result_35 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 156;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_35);
    }
    {
        PyObject *tmp_assign_source_21;
        PyObject *tmp_called_value_69;
        tmp_called_value_69 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_69 == NULL)) {
            tmp_called_value_69 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_69 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 158;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 158;
        tmp_assign_source_21 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_69);
        if (tmp_assign_source_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 158;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_21;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_22;
        PyObject *tmp_called_value_70;
        PyObject *tmp_args_element_value_120;
        tmp_called_value_70 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_70 == NULL)) {
            tmp_called_value_70 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_70 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 159;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_120 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 159;
        tmp_assign_source_22 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_70, tmp_args_element_value_120);
        if (tmp_assign_source_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 159;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_22;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_12;
        PyObject *tmp_call_result_36;
        PyObject *tmp_args_element_value_121;
        PyObject *tmp_args_element_value_122;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_12 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_121 = var_tab;
        tmp_args_element_value_122 = mod_consts[74];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 160;
        {
            PyObject *call_args[] = {tmp_args_element_value_121, tmp_args_element_value_122};
            tmp_call_result_36 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_12,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_36 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 160;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_36);
    }
    {
        PyObject *tmp_ass_subvalue_22;
        PyObject *tmp_called_value_71;
        PyObject *tmp_args_element_value_123;
        PyObject *tmp_args_element_value_124;
        PyObject *tmp_expression_value_133;
        PyObject *tmp_subscript_value_64;
        PyObject *tmp_ass_subscribed_22;
        PyObject *tmp_expression_value_134;
        PyObject *tmp_ass_subscript_22;
        tmp_called_value_71 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_called_value_71 == NULL)) {
            tmp_called_value_71 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
        }

        if (tmp_called_value_71 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 162;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_123 = mod_consts[75];
        tmp_expression_value_133 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_133 == NULL)) {
            tmp_expression_value_133 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_133 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 162;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_64 = mod_consts[75];
        tmp_args_element_value_124 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_133, tmp_subscript_value_64);
        if (tmp_args_element_value_124 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 162;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 162;
        {
            PyObject *call_args[] = {tmp_args_element_value_123, tmp_args_element_value_124};
            tmp_ass_subvalue_22 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_71, call_args);
        }

        Py_DECREF(tmp_args_element_value_124);
        if (tmp_ass_subvalue_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 162;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_134 = par_self;
        tmp_ass_subscribed_22 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_134, mod_consts[15]);
        if (tmp_ass_subscribed_22 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_22);

            exception_lineno = 162;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_22 = mod_consts[75];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_22, tmp_ass_subscript_22, tmp_ass_subvalue_22);
        Py_DECREF(tmp_ass_subscribed_22);
        Py_DECREF(tmp_ass_subvalue_22);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 162;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_72;
        PyObject *tmp_expression_value_135;
        PyObject *tmp_call_result_37;
        PyObject *tmp_args_element_value_125;
        PyObject *tmp_expression_value_136;
        PyObject *tmp_expression_value_137;
        PyObject *tmp_subscript_value_65;
        PyObject *tmp_args_element_value_126;
        PyObject *tmp_args_element_value_127;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_135 = var_tab_layout;
        tmp_called_value_72 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_135, mod_consts[7]);
        if (tmp_called_value_72 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 163;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_137 = par_self;
        tmp_expression_value_136 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_137, mod_consts[15]);
        if (tmp_expression_value_136 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_72);

            exception_lineno = 163;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_65 = mod_consts[75];
        tmp_args_element_value_125 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_136, tmp_subscript_value_65);
        Py_DECREF(tmp_expression_value_136);
        if (tmp_args_element_value_125 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_72);

            exception_lineno = 163;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_126 = mod_consts[24];
        tmp_args_element_value_127 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 163;
        {
            PyObject *call_args[] = {tmp_args_element_value_125, tmp_args_element_value_126, tmp_args_element_value_127};
            tmp_call_result_37 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_72, call_args);
        }

        Py_DECREF(tmp_called_value_72);
        Py_DECREF(tmp_args_element_value_125);
        if (tmp_call_result_37 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 163;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_37);
    }
    {
        PyObject *tmp_ass_subvalue_23;
        PyObject *tmp_dict_key_13;
        PyObject *tmp_dict_value_13;
        PyObject *tmp_called_value_73;
        PyObject *tmp_args_value_12;
        PyObject *tmp_tuple_element_12;
        PyObject *tmp_expression_value_138;
        PyObject *tmp_subscript_value_66;
        PyObject *tmp_kwargs_value_12;
        PyObject *tmp_ass_subscribed_23;
        PyObject *tmp_expression_value_139;
        PyObject *tmp_ass_subscript_23;
        tmp_dict_key_13 = mod_consts[30];
        tmp_called_value_73 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_73 == NULL)) {
            tmp_called_value_73 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_73 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_138 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_138 == NULL)) {
            tmp_expression_value_138 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_138 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_66 = mod_consts[76];
        tmp_tuple_element_12 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_138, tmp_subscript_value_66);
        if (tmp_tuple_element_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_12 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_12, 0, tmp_tuple_element_12);
        tmp_tuple_element_12 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_12, 1, tmp_tuple_element_12);
        tmp_kwargs_value_12 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 166;
        tmp_dict_value_13 = CALL_FUNCTION(tstate, tmp_called_value_73, tmp_args_value_12, tmp_kwargs_value_12);
        Py_DECREF(tmp_args_value_12);
        Py_DECREF(tmp_kwargs_value_12);
        if (tmp_dict_value_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 166;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_23 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_23, tmp_dict_key_13, tmp_dict_value_13);
        Py_DECREF(tmp_dict_value_13);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_139 = par_self;
        tmp_ass_subscribed_23 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_139, mod_consts[15]);
        if (tmp_ass_subscribed_23 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_23);

            exception_lineno = 165;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_23 = mod_consts[76];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_23, tmp_ass_subscript_23, tmp_ass_subvalue_23);
        Py_DECREF(tmp_ass_subscribed_23);
        Py_DECREF(tmp_ass_subvalue_23);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 165;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_74;
        PyObject *tmp_expression_value_140;
        PyObject *tmp_call_result_38;
        PyObject *tmp_args_element_value_128;
        PyObject *tmp_expression_value_141;
        PyObject *tmp_expression_value_142;
        PyObject *tmp_expression_value_143;
        PyObject *tmp_subscript_value_67;
        PyObject *tmp_subscript_value_68;
        PyObject *tmp_args_element_value_129;
        PyObject *tmp_args_element_value_130;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_140 = var_tab_layout;
        tmp_called_value_74 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_140, mod_consts[7]);
        if (tmp_called_value_74 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 168;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_143 = par_self;
        tmp_expression_value_142 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_143, mod_consts[15]);
        if (tmp_expression_value_142 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_74);

            exception_lineno = 168;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_67 = mod_consts[76];
        tmp_expression_value_141 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_142, tmp_subscript_value_67);
        Py_DECREF(tmp_expression_value_142);
        if (tmp_expression_value_141 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_74);

            exception_lineno = 168;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_68 = mod_consts[30];
        tmp_args_element_value_128 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_141, tmp_subscript_value_68);
        Py_DECREF(tmp_expression_value_141);
        if (tmp_args_element_value_128 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_74);

            exception_lineno = 168;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_129 = mod_consts[29];
        tmp_args_element_value_130 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 168;
        {
            PyObject *call_args[] = {tmp_args_element_value_128, tmp_args_element_value_129, tmp_args_element_value_130};
            tmp_call_result_38 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_74, call_args);
        }

        Py_DECREF(tmp_called_value_74);
        Py_DECREF(tmp_args_element_value_128);
        if (tmp_call_result_38 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 168;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_38);
    }
    {
        PyObject *tmp_ass_subvalue_24;
        PyObject *tmp_dict_key_14;
        PyObject *tmp_dict_value_14;
        PyObject *tmp_called_value_75;
        PyObject *tmp_args_element_value_131;
        PyObject *tmp_expression_value_144;
        PyObject *tmp_subscript_value_69;
        PyObject *tmp_args_element_value_132;
        PyObject *tmp_ass_subscribed_24;
        PyObject *tmp_expression_value_146;
        PyObject *tmp_ass_subscript_24;
        tmp_dict_key_14 = mod_consts[25];
        tmp_called_value_75 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_75 == NULL)) {
            tmp_called_value_75 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_75 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 171;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_144 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_144 == NULL)) {
            tmp_expression_value_144 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_144 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 171;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_69 = mod_consts[77];
        tmp_args_element_value_131 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_144, tmp_subscript_value_69);
        if (tmp_args_element_value_131 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 171;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_132 = mod_consts[27];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 171;
        {
            PyObject *call_args[] = {tmp_args_element_value_131, tmp_args_element_value_132};
            tmp_dict_value_14 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_75, call_args);
        }

        Py_DECREF(tmp_args_element_value_131);
        if (tmp_dict_value_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 171;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_24 = _PyDict_NewPresized( 2 );
        {
            PyObject *tmp_called_value_76;
            PyObject *tmp_args_value_13;
            PyObject *tmp_tuple_element_13;
            PyObject *tmp_expression_value_145;
            PyObject *tmp_subscript_value_70;
            PyObject *tmp_kwargs_value_13;
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_24, tmp_dict_key_14, tmp_dict_value_14);
            Py_DECREF(tmp_dict_value_14);
            assert(!(tmp_res != 0));
            tmp_dict_key_14 = mod_consts[30];
            tmp_called_value_76 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

            if (unlikely(tmp_called_value_76 == NULL)) {
                tmp_called_value_76 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
            }

            if (tmp_called_value_76 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 172;
                type_description_1 = "oooooc";
                goto dict_build_exception_3;
            }
            tmp_expression_value_145 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_145 == NULL)) {
                tmp_expression_value_145 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_145 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 172;
                type_description_1 = "oooooc";
                goto dict_build_exception_3;
            }
            tmp_subscript_value_70 = mod_consts[77];
            tmp_tuple_element_13 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_145, tmp_subscript_value_70);
            if (tmp_tuple_element_13 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 172;
                type_description_1 = "oooooc";
                goto dict_build_exception_3;
            }
            tmp_args_value_13 = MAKE_TUPLE_EMPTY(2);
            PyTuple_SET_ITEM(tmp_args_value_13, 0, tmp_tuple_element_13);
            tmp_tuple_element_13 = mod_consts[32];
            PyTuple_SET_ITEM0(tmp_args_value_13, 1, tmp_tuple_element_13);
            tmp_kwargs_value_13 = DICT_COPY(mod_consts[28]);
            frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 172;
            tmp_dict_value_14 = CALL_FUNCTION(tstate, tmp_called_value_76, tmp_args_value_13, tmp_kwargs_value_13);
            Py_DECREF(tmp_args_value_13);
            Py_DECREF(tmp_kwargs_value_13);
            if (tmp_dict_value_14 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 172;
                type_description_1 = "oooooc";
                goto dict_build_exception_3;
            }
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_24, tmp_dict_key_14, tmp_dict_value_14);
            Py_DECREF(tmp_dict_value_14);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_3;
        // Exception handling pass through code for dict_build:
        dict_build_exception_3:;
        Py_DECREF(tmp_ass_subvalue_24);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_3:;
        CHECK_OBJECT(par_self);
        tmp_expression_value_146 = par_self;
        tmp_ass_subscribed_24 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_146, mod_consts[15]);
        if (tmp_ass_subscribed_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_24);

            exception_lineno = 170;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_24 = mod_consts[77];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_24, tmp_ass_subscript_24, tmp_ass_subvalue_24);
        Py_DECREF(tmp_ass_subscribed_24);
        Py_DECREF(tmp_ass_subvalue_24);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 170;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_77;
        PyObject *tmp_expression_value_147;
        PyObject *tmp_call_result_39;
        PyObject *tmp_args_element_value_133;
        PyObject *tmp_expression_value_148;
        PyObject *tmp_expression_value_149;
        PyObject *tmp_expression_value_150;
        PyObject *tmp_subscript_value_71;
        PyObject *tmp_subscript_value_72;
        PyObject *tmp_args_element_value_134;
        PyObject *tmp_args_element_value_135;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_147 = var_tab_layout;
        tmp_called_value_77 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_147, mod_consts[7]);
        if (tmp_called_value_77 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 174;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_150 = par_self;
        tmp_expression_value_149 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_150, mod_consts[15]);
        if (tmp_expression_value_149 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_77);

            exception_lineno = 174;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_71 = mod_consts[77];
        tmp_expression_value_148 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_149, tmp_subscript_value_71);
        Py_DECREF(tmp_expression_value_149);
        if (tmp_expression_value_148 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_77);

            exception_lineno = 174;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_72 = mod_consts[25];
        tmp_args_element_value_133 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_148, tmp_subscript_value_72);
        Py_DECREF(tmp_expression_value_148);
        if (tmp_args_element_value_133 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_77);

            exception_lineno = 174;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_134 = mod_consts[33];
        tmp_args_element_value_135 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 174;
        {
            PyObject *call_args[] = {tmp_args_element_value_133, tmp_args_element_value_134, tmp_args_element_value_135};
            tmp_call_result_39 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_77, call_args);
        }

        Py_DECREF(tmp_called_value_77);
        Py_DECREF(tmp_args_element_value_133);
        if (tmp_call_result_39 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 174;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_39);
    }
    {
        PyObject *tmp_called_value_78;
        PyObject *tmp_expression_value_151;
        PyObject *tmp_call_result_40;
        PyObject *tmp_args_element_value_136;
        PyObject *tmp_expression_value_152;
        PyObject *tmp_expression_value_153;
        PyObject *tmp_expression_value_154;
        PyObject *tmp_subscript_value_73;
        PyObject *tmp_subscript_value_74;
        PyObject *tmp_args_element_value_137;
        PyObject *tmp_args_element_value_138;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_151 = var_tab_layout;
        tmp_called_value_78 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_151, mod_consts[7]);
        if (tmp_called_value_78 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 175;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_154 = par_self;
        tmp_expression_value_153 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_154, mod_consts[15]);
        if (tmp_expression_value_153 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_78);

            exception_lineno = 175;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_73 = mod_consts[77];
        tmp_expression_value_152 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_153, tmp_subscript_value_73);
        Py_DECREF(tmp_expression_value_153);
        if (tmp_expression_value_152 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_78);

            exception_lineno = 175;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_74 = mod_consts[30];
        tmp_args_element_value_136 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_152, tmp_subscript_value_74);
        Py_DECREF(tmp_expression_value_152);
        if (tmp_args_element_value_136 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_78);

            exception_lineno = 175;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_137 = mod_consts[33];
        tmp_args_element_value_138 = mod_consts[29];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 175;
        {
            PyObject *call_args[] = {tmp_args_element_value_136, tmp_args_element_value_137, tmp_args_element_value_138};
            tmp_call_result_40 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_78, call_args);
        }

        Py_DECREF(tmp_called_value_78);
        Py_DECREF(tmp_args_element_value_136);
        if (tmp_call_result_40 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 175;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_40);
    }
    {
        PyObject *tmp_assign_source_23;
        PyObject *tmp_called_value_79;
        tmp_called_value_79 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_79 == NULL)) {
            tmp_called_value_79 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_79 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 177;
        tmp_assign_source_23 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_79);
        if (tmp_assign_source_23 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_23;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_24;
        PyObject *tmp_called_value_80;
        PyObject *tmp_args_element_value_139;
        tmp_called_value_80 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_80 == NULL)) {
            tmp_called_value_80 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_80 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 178;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_139 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 178;
        tmp_assign_source_24 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_80, tmp_args_element_value_139);
        if (tmp_assign_source_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 178;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_24;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_13;
        PyObject *tmp_call_result_41;
        PyObject *tmp_args_element_value_140;
        PyObject *tmp_args_element_value_141;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_13 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_140 = var_tab;
        tmp_args_element_value_141 = mod_consts[78];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 179;
        {
            PyObject *call_args[] = {tmp_args_element_value_140, tmp_args_element_value_141};
            tmp_call_result_41 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_13,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_41 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 179;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_41);
    }
    {
        PyObject *tmp_ass_subvalue_25;
        PyObject *tmp_dict_key_15;
        PyObject *tmp_dict_value_15;
        PyObject *tmp_called_value_81;
        PyObject *tmp_args_element_value_142;
        PyObject *tmp_expression_value_155;
        PyObject *tmp_subscript_value_75;
        PyObject *tmp_args_element_value_143;
        PyObject *tmp_ass_subscribed_25;
        PyObject *tmp_expression_value_157;
        PyObject *tmp_ass_subscript_25;
        tmp_dict_key_15 = mod_consts[25];
        tmp_called_value_81 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_81 == NULL)) {
            tmp_called_value_81 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_81 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 182;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_155 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_155 == NULL)) {
            tmp_expression_value_155 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_155 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 182;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_75 = mod_consts[79];
        tmp_args_element_value_142 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_155, tmp_subscript_value_75);
        if (tmp_args_element_value_142 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 182;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_143 = mod_consts[27];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 182;
        {
            PyObject *call_args[] = {tmp_args_element_value_142, tmp_args_element_value_143};
            tmp_dict_value_15 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_81, call_args);
        }

        Py_DECREF(tmp_args_element_value_142);
        if (tmp_dict_value_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 182;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_25 = _PyDict_NewPresized( 2 );
        {
            PyObject *tmp_called_value_82;
            PyObject *tmp_args_value_14;
            PyObject *tmp_tuple_element_14;
            PyObject *tmp_expression_value_156;
            PyObject *tmp_subscript_value_76;
            PyObject *tmp_kwargs_value_14;
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_25, tmp_dict_key_15, tmp_dict_value_15);
            Py_DECREF(tmp_dict_value_15);
            assert(!(tmp_res != 0));
            tmp_dict_key_15 = mod_consts[30];
            tmp_called_value_82 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

            if (unlikely(tmp_called_value_82 == NULL)) {
                tmp_called_value_82 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
            }

            if (tmp_called_value_82 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 183;
                type_description_1 = "oooooc";
                goto dict_build_exception_4;
            }
            tmp_expression_value_156 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_expression_value_156 == NULL)) {
                tmp_expression_value_156 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_expression_value_156 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 183;
                type_description_1 = "oooooc";
                goto dict_build_exception_4;
            }
            tmp_subscript_value_76 = mod_consts[79];
            tmp_tuple_element_14 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_156, tmp_subscript_value_76);
            if (tmp_tuple_element_14 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 183;
                type_description_1 = "oooooc";
                goto dict_build_exception_4;
            }
            tmp_args_value_14 = MAKE_TUPLE_EMPTY(2);
            PyTuple_SET_ITEM(tmp_args_value_14, 0, tmp_tuple_element_14);
            tmp_tuple_element_14 = mod_consts[32];
            PyTuple_SET_ITEM0(tmp_args_value_14, 1, tmp_tuple_element_14);
            tmp_kwargs_value_14 = DICT_COPY(mod_consts[28]);
            frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 183;
            tmp_dict_value_15 = CALL_FUNCTION(tstate, tmp_called_value_82, tmp_args_value_14, tmp_kwargs_value_14);
            Py_DECREF(tmp_args_value_14);
            Py_DECREF(tmp_kwargs_value_14);
            if (tmp_dict_value_15 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 183;
                type_description_1 = "oooooc";
                goto dict_build_exception_4;
            }
            tmp_res = PyDict_SetItem(tmp_ass_subvalue_25, tmp_dict_key_15, tmp_dict_value_15);
            Py_DECREF(tmp_dict_value_15);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_4;
        // Exception handling pass through code for dict_build:
        dict_build_exception_4:;
        Py_DECREF(tmp_ass_subvalue_25);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_4:;
        CHECK_OBJECT(par_self);
        tmp_expression_value_157 = par_self;
        tmp_ass_subscribed_25 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_157, mod_consts[15]);
        if (tmp_ass_subscribed_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_25);

            exception_lineno = 181;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_25 = mod_consts[79];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_25, tmp_ass_subscript_25, tmp_ass_subvalue_25);
        Py_DECREF(tmp_ass_subscribed_25);
        Py_DECREF(tmp_ass_subvalue_25);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 181;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_83;
        PyObject *tmp_expression_value_158;
        PyObject *tmp_call_result_42;
        PyObject *tmp_args_element_value_144;
        PyObject *tmp_expression_value_159;
        PyObject *tmp_expression_value_160;
        PyObject *tmp_expression_value_161;
        PyObject *tmp_subscript_value_77;
        PyObject *tmp_subscript_value_78;
        PyObject *tmp_args_element_value_145;
        PyObject *tmp_args_element_value_146;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_158 = var_tab_layout;
        tmp_called_value_83 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_158, mod_consts[7]);
        if (tmp_called_value_83 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 185;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_161 = par_self;
        tmp_expression_value_160 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_161, mod_consts[15]);
        if (tmp_expression_value_160 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_83);

            exception_lineno = 185;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_77 = mod_consts[79];
        tmp_expression_value_159 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_160, tmp_subscript_value_77);
        Py_DECREF(tmp_expression_value_160);
        if (tmp_expression_value_159 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_83);

            exception_lineno = 185;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_78 = mod_consts[25];
        tmp_args_element_value_144 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_159, tmp_subscript_value_78);
        Py_DECREF(tmp_expression_value_159);
        if (tmp_args_element_value_144 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_83);

            exception_lineno = 185;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_145 = mod_consts[24];
        tmp_args_element_value_146 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 185;
        {
            PyObject *call_args[] = {tmp_args_element_value_144, tmp_args_element_value_145, tmp_args_element_value_146};
            tmp_call_result_42 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_83, call_args);
        }

        Py_DECREF(tmp_called_value_83);
        Py_DECREF(tmp_args_element_value_144);
        if (tmp_call_result_42 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 185;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_42);
    }
    {
        PyObject *tmp_called_value_84;
        PyObject *tmp_expression_value_162;
        PyObject *tmp_call_result_43;
        PyObject *tmp_args_element_value_147;
        PyObject *tmp_expression_value_163;
        PyObject *tmp_expression_value_164;
        PyObject *tmp_expression_value_165;
        PyObject *tmp_subscript_value_79;
        PyObject *tmp_subscript_value_80;
        PyObject *tmp_args_element_value_148;
        PyObject *tmp_args_element_value_149;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_162 = var_tab_layout;
        tmp_called_value_84 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_162, mod_consts[7]);
        if (tmp_called_value_84 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 186;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_165 = par_self;
        tmp_expression_value_164 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_165, mod_consts[15]);
        if (tmp_expression_value_164 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_84);

            exception_lineno = 186;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_79 = mod_consts[79];
        tmp_expression_value_163 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_164, tmp_subscript_value_79);
        Py_DECREF(tmp_expression_value_164);
        if (tmp_expression_value_163 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_84);

            exception_lineno = 186;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_80 = mod_consts[30];
        tmp_args_element_value_147 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_163, tmp_subscript_value_80);
        Py_DECREF(tmp_expression_value_163);
        if (tmp_args_element_value_147 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_84);

            exception_lineno = 186;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_148 = mod_consts[24];
        tmp_args_element_value_149 = mod_consts[29];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 186;
        {
            PyObject *call_args[] = {tmp_args_element_value_147, tmp_args_element_value_148, tmp_args_element_value_149};
            tmp_call_result_43 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_84, call_args);
        }

        Py_DECREF(tmp_called_value_84);
        Py_DECREF(tmp_args_element_value_147);
        if (tmp_call_result_43 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 186;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_43);
    }
    {
        PyObject *tmp_assign_source_25;
        PyObject *tmp_called_value_85;
        tmp_called_value_85 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_85 == NULL)) {
            tmp_called_value_85 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_85 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 188;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 188;
        tmp_assign_source_25 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_85);
        if (tmp_assign_source_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 188;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_25;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_26;
        PyObject *tmp_called_value_86;
        PyObject *tmp_args_element_value_150;
        tmp_called_value_86 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_86 == NULL)) {
            tmp_called_value_86 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_86 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 189;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_150 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 189;
        tmp_assign_source_26 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_86, tmp_args_element_value_150);
        if (tmp_assign_source_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 189;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_26;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_14;
        PyObject *tmp_call_result_44;
        PyObject *tmp_args_element_value_151;
        PyObject *tmp_args_element_value_152;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_14 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_151 = var_tab;
        tmp_args_element_value_152 = mod_consts[80];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 190;
        {
            PyObject *call_args[] = {tmp_args_element_value_151, tmp_args_element_value_152};
            tmp_call_result_44 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_14,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_44 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 190;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_44);
    }
    {
        PyObject *tmp_ass_subvalue_26;
        PyObject *tmp_dict_key_16;
        PyObject *tmp_dict_value_16;
        PyObject *tmp_called_value_87;
        PyObject *tmp_args_value_15;
        PyObject *tmp_tuple_element_15;
        PyObject *tmp_expression_value_166;
        PyObject *tmp_subscript_value_81;
        PyObject *tmp_kwargs_value_15;
        PyObject *tmp_ass_subscribed_26;
        PyObject *tmp_expression_value_167;
        PyObject *tmp_ass_subscript_26;
        tmp_dict_key_16 = mod_consts[30];
        tmp_called_value_87 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_87 == NULL)) {
            tmp_called_value_87 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_87 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 193;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_166 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_166 == NULL)) {
            tmp_expression_value_166 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_166 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 193;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_81 = mod_consts[81];
        tmp_tuple_element_15 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_166, tmp_subscript_value_81);
        if (tmp_tuple_element_15 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 193;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_15 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_15, 0, tmp_tuple_element_15);
        tmp_tuple_element_15 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_15, 1, tmp_tuple_element_15);
        tmp_kwargs_value_15 = DICT_COPY(mod_consts[28]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 193;
        tmp_dict_value_16 = CALL_FUNCTION(tstate, tmp_called_value_87, tmp_args_value_15, tmp_kwargs_value_15);
        Py_DECREF(tmp_args_value_15);
        Py_DECREF(tmp_kwargs_value_15);
        if (tmp_dict_value_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 193;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_26 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_26, tmp_dict_key_16, tmp_dict_value_16);
        Py_DECREF(tmp_dict_value_16);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_167 = par_self;
        tmp_ass_subscribed_26 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_167, mod_consts[15]);
        if (tmp_ass_subscribed_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_26);

            exception_lineno = 192;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_26 = mod_consts[81];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_26, tmp_ass_subscript_26, tmp_ass_subvalue_26);
        Py_DECREF(tmp_ass_subscribed_26);
        Py_DECREF(tmp_ass_subvalue_26);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 192;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_88;
        PyObject *tmp_expression_value_168;
        PyObject *tmp_call_result_45;
        PyObject *tmp_args_element_value_153;
        PyObject *tmp_expression_value_169;
        PyObject *tmp_expression_value_170;
        PyObject *tmp_expression_value_171;
        PyObject *tmp_subscript_value_82;
        PyObject *tmp_subscript_value_83;
        PyObject *tmp_args_element_value_154;
        PyObject *tmp_args_element_value_155;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_168 = var_tab_layout;
        tmp_called_value_88 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_168, mod_consts[7]);
        if (tmp_called_value_88 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 195;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_171 = par_self;
        tmp_expression_value_170 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_171, mod_consts[15]);
        if (tmp_expression_value_170 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_88);

            exception_lineno = 195;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_82 = mod_consts[81];
        tmp_expression_value_169 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_170, tmp_subscript_value_82);
        Py_DECREF(tmp_expression_value_170);
        if (tmp_expression_value_169 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_88);

            exception_lineno = 195;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_83 = mod_consts[30];
        tmp_args_element_value_153 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_169, tmp_subscript_value_83);
        Py_DECREF(tmp_expression_value_169);
        if (tmp_args_element_value_153 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_88);

            exception_lineno = 195;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_154 = mod_consts[24];
        tmp_args_element_value_155 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 195;
        {
            PyObject *call_args[] = {tmp_args_element_value_153, tmp_args_element_value_154, tmp_args_element_value_155};
            tmp_call_result_45 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_88, call_args);
        }

        Py_DECREF(tmp_called_value_88);
        Py_DECREF(tmp_args_element_value_153);
        if (tmp_call_result_45 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 195;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_45);
    }
    {
        PyObject *tmp_assign_source_27;
        PyObject *tmp_called_value_89;
        tmp_called_value_89 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_called_value_89 == NULL)) {
            tmp_called_value_89 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_called_value_89 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 197;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 197;
        tmp_assign_source_27 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_89);
        if (tmp_assign_source_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 197;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab;
            assert(old != NULL);
            var_tab = tmp_assign_source_27;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_assign_source_28;
        PyObject *tmp_called_value_90;
        PyObject *tmp_args_element_value_156;
        tmp_called_value_90 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_90 == NULL)) {
            tmp_called_value_90 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        if (tmp_called_value_90 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 198;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_156 = var_tab;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 198;
        tmp_assign_source_28 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_90, tmp_args_element_value_156);
        if (tmp_assign_source_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 198;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        {
            PyObject *old = var_tab_layout;
            assert(old != NULL);
            var_tab_layout = tmp_assign_source_28;
            Py_DECREF(old);
        }

    }
    {
        PyObject *tmp_called_instance_15;
        PyObject *tmp_call_result_46;
        PyObject *tmp_args_element_value_157;
        PyObject *tmp_args_element_value_158;
        CHECK_OBJECT(var_tabs);
        tmp_called_instance_15 = var_tabs;
        CHECK_OBJECT(var_tab);
        tmp_args_element_value_157 = var_tab;
        tmp_args_element_value_158 = mod_consts[82];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 199;
        {
            PyObject *call_args[] = {tmp_args_element_value_157, tmp_args_element_value_158};
            tmp_call_result_46 = CALL_METHOD_WITH_ARGS2(
                tstate,
                tmp_called_instance_15,
                mod_consts[19],
                call_args
            );
        }

        if (tmp_call_result_46 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 199;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_46);
    }
    {
        PyObject *tmp_ass_subvalue_27;
        PyObject *tmp_dict_key_17;
        PyObject *tmp_dict_value_17;
        PyObject *tmp_called_value_91;
        PyObject *tmp_args_value_16;
        PyObject *tmp_tuple_element_16;
        PyObject *tmp_expression_value_172;
        PyObject *tmp_subscript_value_84;
        PyObject *tmp_kwargs_value_16;
        PyObject *tmp_ass_subscribed_27;
        PyObject *tmp_expression_value_173;
        PyObject *tmp_ass_subscript_27;
        tmp_dict_key_17 = mod_consts[30];
        tmp_called_value_91 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_91 == NULL)) {
            tmp_called_value_91 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_91 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 202;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_172 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_172 == NULL)) {
            tmp_expression_value_172 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_172 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 202;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_84 = mod_consts[83];
        tmp_tuple_element_16 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_172, tmp_subscript_value_84);
        if (tmp_tuple_element_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 202;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_16 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_16, 0, tmp_tuple_element_16);
        tmp_tuple_element_16 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_16, 1, tmp_tuple_element_16);
        tmp_kwargs_value_16 = DICT_COPY(mod_consts[60]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 202;
        tmp_dict_value_17 = CALL_FUNCTION(tstate, tmp_called_value_91, tmp_args_value_16, tmp_kwargs_value_16);
        Py_DECREF(tmp_args_value_16);
        Py_DECREF(tmp_kwargs_value_16);
        if (tmp_dict_value_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 202;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_27 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_27, tmp_dict_key_17, tmp_dict_value_17);
        Py_DECREF(tmp_dict_value_17);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_173 = par_self;
        tmp_ass_subscribed_27 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_173, mod_consts[15]);
        if (tmp_ass_subscribed_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_27);

            exception_lineno = 201;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_27 = mod_consts[83];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_27, tmp_ass_subscript_27, tmp_ass_subvalue_27);
        Py_DECREF(tmp_ass_subscribed_27);
        Py_DECREF(tmp_ass_subvalue_27);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 201;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_92;
        PyObject *tmp_expression_value_174;
        PyObject *tmp_call_result_47;
        PyObject *tmp_args_element_value_159;
        PyObject *tmp_expression_value_175;
        PyObject *tmp_expression_value_176;
        PyObject *tmp_expression_value_177;
        PyObject *tmp_subscript_value_85;
        PyObject *tmp_subscript_value_86;
        PyObject *tmp_args_element_value_160;
        PyObject *tmp_args_element_value_161;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_174 = var_tab_layout;
        tmp_called_value_92 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_174, mod_consts[7]);
        if (tmp_called_value_92 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 204;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_177 = par_self;
        tmp_expression_value_176 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_177, mod_consts[15]);
        if (tmp_expression_value_176 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);

            exception_lineno = 204;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_85 = mod_consts[83];
        tmp_expression_value_175 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_176, tmp_subscript_value_85);
        Py_DECREF(tmp_expression_value_176);
        if (tmp_expression_value_175 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);

            exception_lineno = 204;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_86 = mod_consts[30];
        tmp_args_element_value_159 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_175, tmp_subscript_value_86);
        Py_DECREF(tmp_expression_value_175);
        if (tmp_args_element_value_159 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);

            exception_lineno = 204;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_160 = mod_consts[24];
        tmp_args_element_value_161 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 204;
        {
            PyObject *call_args[] = {tmp_args_element_value_159, tmp_args_element_value_160, tmp_args_element_value_161};
            tmp_call_result_47 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_92, call_args);
        }

        Py_DECREF(tmp_called_value_92);
        Py_DECREF(tmp_args_element_value_159);
        if (tmp_call_result_47 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 204;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_47);
    }
    {
        PyObject *tmp_ass_subvalue_28;
        PyObject *tmp_dict_key_18;
        PyObject *tmp_dict_value_18;
        PyObject *tmp_called_value_93;
        PyObject *tmp_args_value_17;
        PyObject *tmp_tuple_element_17;
        PyObject *tmp_expression_value_178;
        PyObject *tmp_subscript_value_87;
        PyObject *tmp_kwargs_value_17;
        PyObject *tmp_ass_subscribed_28;
        PyObject *tmp_expression_value_179;
        PyObject *tmp_ass_subscript_28;
        tmp_dict_key_18 = mod_consts[30];
        tmp_called_value_93 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_called_value_93 == NULL)) {
            tmp_called_value_93 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_called_value_93 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 207;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_expression_value_178 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23]);

        if (unlikely(tmp_expression_value_178 == NULL)) {
            tmp_expression_value_178 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
        }

        if (tmp_expression_value_178 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 207;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_87 = mod_consts[84];
        tmp_tuple_element_17 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_178, tmp_subscript_value_87);
        if (tmp_tuple_element_17 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 207;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_value_17 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM(tmp_args_value_17, 0, tmp_tuple_element_17);
        tmp_tuple_element_17 = mod_consts[32];
        PyTuple_SET_ITEM0(tmp_args_value_17, 1, tmp_tuple_element_17);
        tmp_kwargs_value_17 = DICT_COPY(mod_consts[60]);
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 207;
        tmp_dict_value_18 = CALL_FUNCTION(tstate, tmp_called_value_93, tmp_args_value_17, tmp_kwargs_value_17);
        Py_DECREF(tmp_args_value_17);
        Py_DECREF(tmp_kwargs_value_17);
        if (tmp_dict_value_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 207;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subvalue_28 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_ass_subvalue_28, tmp_dict_key_18, tmp_dict_value_18);
        Py_DECREF(tmp_dict_value_18);
        assert(!(tmp_res != 0));
        CHECK_OBJECT(par_self);
        tmp_expression_value_179 = par_self;
        tmp_ass_subscribed_28 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_179, mod_consts[15]);
        if (tmp_ass_subscribed_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_ass_subvalue_28);

            exception_lineno = 206;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_ass_subscript_28 = mod_consts[84];
        tmp_result = SET_SUBSCRIPT(tstate, tmp_ass_subscribed_28, tmp_ass_subscript_28, tmp_ass_subvalue_28);
        Py_DECREF(tmp_ass_subscribed_28);
        Py_DECREF(tmp_ass_subvalue_28);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 206;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_94;
        PyObject *tmp_expression_value_180;
        PyObject *tmp_call_result_48;
        PyObject *tmp_args_element_value_162;
        PyObject *tmp_expression_value_181;
        PyObject *tmp_expression_value_182;
        PyObject *tmp_expression_value_183;
        PyObject *tmp_subscript_value_88;
        PyObject *tmp_subscript_value_89;
        PyObject *tmp_args_element_value_163;
        PyObject *tmp_args_element_value_164;
        CHECK_OBJECT(var_tab_layout);
        tmp_expression_value_180 = var_tab_layout;
        tmp_called_value_94 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_180, mod_consts[7]);
        if (tmp_called_value_94 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 209;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_183 = par_self;
        tmp_expression_value_182 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_183, mod_consts[15]);
        if (tmp_expression_value_182 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_94);

            exception_lineno = 209;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_88 = mod_consts[84];
        tmp_expression_value_181 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_182, tmp_subscript_value_88);
        Py_DECREF(tmp_expression_value_182);
        if (tmp_expression_value_181 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_94);

            exception_lineno = 209;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_subscript_value_89 = mod_consts[30];
        tmp_args_element_value_162 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_181, tmp_subscript_value_89);
        Py_DECREF(tmp_expression_value_181);
        if (tmp_args_element_value_162 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_94);

            exception_lineno = 209;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_163 = mod_consts[29];
        tmp_args_element_value_164 = mod_consts[24];
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 209;
        {
            PyObject *call_args[] = {tmp_args_element_value_162, tmp_args_element_value_163, tmp_args_element_value_164};
            tmp_call_result_48 = CALL_FUNCTION_WITH_ARGS3(tstate, tmp_called_value_94, call_args);
        }

        Py_DECREF(tmp_called_value_94);
        Py_DECREF(tmp_args_element_value_162);
        if (tmp_call_result_48 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 209;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_48);
    }
    {
        PyObject *tmp_called_instance_16;
        PyObject *tmp_call_result_49;
        CHECK_OBJECT(var_layout);
        tmp_called_instance_16 = var_layout;
        frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame.f_lineno = 211;
        tmp_call_result_49 = CALL_METHOD_NO_ARGS(tstate, tmp_called_instance_16, mod_consts[85]);
        if (tmp_call_result_49 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 211;
            type_description_1 = "oooooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_49);
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_a59296a7f8c550f17b41865cc1aa23c7, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_a59296a7f8c550f17b41865cc1aa23c7->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_a59296a7f8c550f17b41865cc1aa23c7, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_a59296a7f8c550f17b41865cc1aa23c7,
        type_description_1,
        par_self,
        var_layout,
        var_tabs,
        var_tab,
        var_tab_layout,
        self->m_closure[0]
    );


    // Release cached frame if used for exception.
    if (frame_a59296a7f8c550f17b41865cc1aa23c7 == cache_frame_a59296a7f8c550f17b41865cc1aa23c7) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_a59296a7f8c550f17b41865cc1aa23c7);
        cache_frame_a59296a7f8c550f17b41865cc1aa23c7 = NULL;
    }

    assertFrameObject(frame_a59296a7f8c550f17b41865cc1aa23c7);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto try_except_handler_1;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_layout);
    Py_DECREF(var_layout);
    var_layout = NULL;
    CHECK_OBJECT(var_tabs);
    Py_DECREF(var_tabs);
    var_tabs = NULL;
    CHECK_OBJECT(var_tab);
    Py_DECREF(var_tab);
    var_tab = NULL;
    CHECK_OBJECT(var_tab_layout);
    Py_DECREF(var_tab_layout);
    var_tab_layout = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_layout);
    var_layout = NULL;
    Py_XDECREF(var_tabs);
    var_tabs = NULL;
    Py_XDECREF(var_tab);
    var_tab = NULL;
    Py_XDECREF(var_tab_layout);
    var_tab_layout = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_qt$components$bonuses$$$function__3___getitem__(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[0];
    PyObject *par_item = python_pars[1];
    struct Nuitka_FrameObject *frame_314a5deb612b7e8d61fb4a2a255bbf78;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_314a5deb612b7e8d61fb4a2a255bbf78 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_314a5deb612b7e8d61fb4a2a255bbf78)) {
        Py_XDECREF(cache_frame_314a5deb612b7e8d61fb4a2a255bbf78);

#if _DEBUG_REFCOUNTS
        if (cache_frame_314a5deb612b7e8d61fb4a2a255bbf78 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_314a5deb612b7e8d61fb4a2a255bbf78 = MAKE_FUNCTION_FRAME(tstate, codeobj_314a5deb612b7e8d61fb4a2a255bbf78, module_qt$components$bonuses, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_314a5deb612b7e8d61fb4a2a255bbf78->m_type_description == NULL);
    frame_314a5deb612b7e8d61fb4a2a255bbf78 = cache_frame_314a5deb612b7e8d61fb4a2a255bbf78;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_314a5deb612b7e8d61fb4a2a255bbf78);
    assert(Py_REFCNT(frame_314a5deb612b7e8d61fb4a2a255bbf78) == 2);

    // Framed code:
    {
        PyObject *tmp_expression_value_1;
        PyObject *tmp_expression_value_2;
        PyObject *tmp_subscript_value_1;
        CHECK_OBJECT(par_self);
        tmp_expression_value_2 = par_self;
        tmp_expression_value_1 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_2, mod_consts[15]);
        if (tmp_expression_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 214;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_item);
        tmp_subscript_value_1 = par_item;
        tmp_return_value = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_1, tmp_subscript_value_1);
        Py_DECREF(tmp_expression_value_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 214;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_314a5deb612b7e8d61fb4a2a255bbf78, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_314a5deb612b7e8d61fb4a2a255bbf78->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_314a5deb612b7e8d61fb4a2a255bbf78, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_314a5deb612b7e8d61fb4a2a255bbf78,
        type_description_1,
        par_self,
        par_item
    );


    // Release cached frame if used for exception.
    if (frame_314a5deb612b7e8d61fb4a2a255bbf78 == cache_frame_314a5deb612b7e8d61fb4a2a255bbf78) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_314a5deb612b7e8d61fb4a2a255bbf78);
        cache_frame_314a5deb612b7e8d61fb4a2a255bbf78 = NULL;
    }

    assertFrameObject(frame_314a5deb612b7e8d61fb4a2a255bbf78);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);
    CHECK_OBJECT(par_item);
    Py_DECREF(par_item);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);
    CHECK_OBJECT(par_item);
    Py_DECREF(par_item);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_qt$components$bonuses$$$function__4_items(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[0];
    struct Nuitka_FrameObject *frame_41196fb28ed1cff61af2ccc3c6c2ae89;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89)) {
        Py_XDECREF(cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89);

#if _DEBUG_REFCOUNTS
        if (cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89 = MAKE_FUNCTION_FRAME(tstate, codeobj_41196fb28ed1cff61af2ccc3c6c2ae89, module_qt$components$bonuses, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89->m_type_description == NULL);
    frame_41196fb28ed1cff61af2ccc3c6c2ae89 = cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_41196fb28ed1cff61af2ccc3c6c2ae89);
    assert(Py_REFCNT(frame_41196fb28ed1cff61af2ccc3c6c2ae89) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_expression_value_2;
        CHECK_OBJECT(par_self);
        tmp_expression_value_2 = par_self;
        tmp_expression_value_1 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_2, mod_consts[15]);
        if (tmp_expression_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 217;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_1, mod_consts[86]);
        Py_DECREF(tmp_expression_value_1);
        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 217;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        frame_41196fb28ed1cff61af2ccc3c6c2ae89->m_frame.f_lineno = 217;
        tmp_return_value = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_1);
        Py_DECREF(tmp_called_value_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 217;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_41196fb28ed1cff61af2ccc3c6c2ae89, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_41196fb28ed1cff61af2ccc3c6c2ae89->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_41196fb28ed1cff61af2ccc3c6c2ae89, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_41196fb28ed1cff61af2ccc3c6c2ae89,
        type_description_1,
        par_self
    );


    // Release cached frame if used for exception.
    if (frame_41196fb28ed1cff61af2ccc3c6c2ae89 == cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89);
        cache_frame_41196fb28ed1cff61af2ccc3c6c2ae89 = NULL;
    }

    assertFrameObject(frame_41196fb28ed1cff61af2ccc3c6c2ae89);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_qt$components$bonuses$$$function__5___init__(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[0];
    PyObject *var_layout = NULL;
    struct Nuitka_FrameObject *frame_bed27f74d7af26fbf540226f0e111d85;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    bool tmp_result;
    static struct Nuitka_FrameObject *cache_frame_bed27f74d7af26fbf540226f0e111d85 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_bed27f74d7af26fbf540226f0e111d85)) {
        Py_XDECREF(cache_frame_bed27f74d7af26fbf540226f0e111d85);

#if _DEBUG_REFCOUNTS
        if (cache_frame_bed27f74d7af26fbf540226f0e111d85 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_bed27f74d7af26fbf540226f0e111d85 = MAKE_FUNCTION_FRAME(tstate, codeobj_bed27f74d7af26fbf540226f0e111d85, module_qt$components$bonuses, sizeof(void *)+sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_bed27f74d7af26fbf540226f0e111d85->m_type_description == NULL);
    frame_bed27f74d7af26fbf540226f0e111d85 = cache_frame_bed27f74d7af26fbf540226f0e111d85;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_bed27f74d7af26fbf540226f0e111d85);
    assert(Py_REFCNT(frame_bed27f74d7af26fbf540226f0e111d85) == 2);

    // Framed code:
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_type_arg_value_1;
        PyObject *tmp_object_arg_value_1;
        PyObject *tmp_call_result_1;
        if (Nuitka_Cell_GET(self->m_closure[0]) == NULL) {

            FORMAT_UNBOUND_CLOSURE_ERROR(&exception_type, &exception_value, mod_consts[0]);
            exception_tb = NULL;
            NORMALIZE_EXCEPTION(tstate, &exception_type, &exception_value, &exception_tb);
            CHAIN_EXCEPTION(tstate, exception_value);

            exception_lineno = 222;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }

        tmp_type_arg_value_1 = Nuitka_Cell_GET(self->m_closure[0]);
        CHECK_OBJECT(par_self);
        tmp_object_arg_value_1 = par_self;
        tmp_called_instance_1 = BUILTIN_SUPER0(tstate, moduledict_qt$components$bonuses, tmp_type_arg_value_1, tmp_object_arg_value_1);
        if (tmp_called_instance_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 222;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 222;
        tmp_call_result_1 = CALL_METHOD_NO_ARGS(tstate, tmp_called_instance_1, mod_consts[1]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_call_result_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 222;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_called_value_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[14]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 223;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 223;
        tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_1);
        if (tmp_assign_source_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 223;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        assert(var_layout == NULL);
        var_layout = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_instance_2;
        PyObject *tmp_call_result_2;
        PyObject *tmp_args_element_value_1;
        CHECK_OBJECT(par_self);
        tmp_called_instance_2 = par_self;
        CHECK_OBJECT(var_layout);
        tmp_args_element_value_1 = var_layout;
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 224;
        tmp_call_result_2 = CALL_METHOD_WITH_SINGLE_ARG(tstate, tmp_called_instance_2, mod_consts[3], tmp_args_element_value_1);
        if (tmp_call_result_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 224;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_called_value_2;
        PyObject *tmp_assattr_target_1;
        tmp_called_value_2 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[16]);

        if (unlikely(tmp_called_value_2 == NULL)) {
            tmp_called_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[16]);
        }

        if (tmp_called_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 226;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 226;
        tmp_assattr_value_1 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_2);
        if (tmp_assattr_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 226;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_assattr_target_1 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_1, mod_consts[87], tmp_assattr_value_1);
        Py_DECREF(tmp_assattr_value_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 226;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_3;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_3;
        PyObject *tmp_args_element_value_2;
        PyObject *tmp_expression_value_2;
        CHECK_OBJECT(var_layout);
        tmp_expression_value_1 = var_layout;
        tmp_called_value_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_1, mod_consts[7]);
        if (tmp_called_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 227;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_2 = par_self;
        tmp_args_element_value_2 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_2, mod_consts[87]);
        if (tmp_args_element_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_3);

            exception_lineno = 227;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 227;
        tmp_call_result_3 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_3, tmp_args_element_value_2);
        Py_DECREF(tmp_called_value_3);
        Py_DECREF(tmp_args_element_value_2);
        if (tmp_call_result_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 227;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_3);
    }
    {
        PyObject *tmp_assattr_value_2;
        PyObject *tmp_called_value_4;
        PyObject *tmp_assattr_target_2;
        tmp_called_value_4 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[88]);

        if (unlikely(tmp_called_value_4 == NULL)) {
            tmp_called_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[88]);
        }

        if (tmp_called_value_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 228;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 228;
        tmp_assattr_value_2 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_4);
        if (tmp_assattr_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 228;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_assattr_target_2 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_2, mod_consts[6], tmp_assattr_value_2);
        Py_DECREF(tmp_assattr_value_2);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 228;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_5;
        PyObject *tmp_expression_value_3;
        PyObject *tmp_expression_value_4;
        PyObject *tmp_call_result_4;
        PyObject *tmp_args_element_value_3;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_args_element_value_4;
        CHECK_OBJECT(par_self);
        tmp_expression_value_4 = par_self;
        tmp_expression_value_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_4, mod_consts[87]);
        if (tmp_expression_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 229;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        tmp_called_value_5 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_3, mod_consts[19]);
        Py_DECREF(tmp_expression_value_3);
        if (tmp_called_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 229;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_5 = par_self;
        tmp_args_element_value_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_5, mod_consts[6]);
        if (tmp_args_element_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_5);

            exception_lineno = 229;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_4 = mod_consts[89];
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 229;
        {
            PyObject *call_args[] = {tmp_args_element_value_3, tmp_args_element_value_4};
            tmp_call_result_4 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_5, call_args);
        }

        Py_DECREF(tmp_called_value_5);
        Py_DECREF(tmp_args_element_value_3);
        if (tmp_call_result_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 229;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_4);
    }
    {
        PyObject *tmp_assattr_value_3;
        PyObject *tmp_called_value_6;
        PyObject *tmp_assattr_target_3;
        tmp_called_value_6 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[90]);

        if (unlikely(tmp_called_value_6 == NULL)) {
            tmp_called_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[90]);
        }

        if (tmp_called_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 230;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 230;
        tmp_assattr_value_3 = CALL_FUNCTION_NO_ARGS(tstate, tmp_called_value_6);
        if (tmp_assattr_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 230;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_assattr_target_3 = par_self;
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_3, mod_consts[15], tmp_assattr_value_3);
        Py_DECREF(tmp_assattr_value_3);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 230;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_called_value_7;
        PyObject *tmp_expression_value_6;
        PyObject *tmp_expression_value_7;
        PyObject *tmp_call_result_5;
        PyObject *tmp_args_element_value_5;
        PyObject *tmp_expression_value_8;
        PyObject *tmp_args_element_value_6;
        CHECK_OBJECT(par_self);
        tmp_expression_value_7 = par_self;
        tmp_expression_value_6 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_7, mod_consts[87]);
        if (tmp_expression_value_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 231;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        tmp_called_value_7 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_6, mod_consts[19]);
        Py_DECREF(tmp_expression_value_6);
        if (tmp_called_value_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 231;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_self);
        tmp_expression_value_8 = par_self;
        tmp_args_element_value_5 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_8, mod_consts[15]);
        if (tmp_args_element_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_7);

            exception_lineno = 231;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_6 = mod_consts[91];
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 231;
        {
            PyObject *call_args[] = {tmp_args_element_value_5, tmp_args_element_value_6};
            tmp_call_result_5 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_7, call_args);
        }

        Py_DECREF(tmp_called_value_7);
        Py_DECREF(tmp_args_element_value_5);
        if (tmp_call_result_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 231;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_5);
    }
    {
        PyObject *tmp_called_instance_3;
        PyObject *tmp_call_result_6;
        CHECK_OBJECT(var_layout);
        tmp_called_instance_3 = var_layout;
        frame_bed27f74d7af26fbf540226f0e111d85->m_frame.f_lineno = 233;
        tmp_call_result_6 = CALL_METHOD_NO_ARGS(tstate, tmp_called_instance_3, mod_consts[85]);
        if (tmp_call_result_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 233;
            type_description_1 = "ooc";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_6);
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_bed27f74d7af26fbf540226f0e111d85, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_bed27f74d7af26fbf540226f0e111d85->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_bed27f74d7af26fbf540226f0e111d85, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_bed27f74d7af26fbf540226f0e111d85,
        type_description_1,
        par_self,
        var_layout,
        self->m_closure[0]
    );


    // Release cached frame if used for exception.
    if (frame_bed27f74d7af26fbf540226f0e111d85 == cache_frame_bed27f74d7af26fbf540226f0e111d85) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_bed27f74d7af26fbf540226f0e111d85);
        cache_frame_bed27f74d7af26fbf540226f0e111d85 = NULL;
    }

    assertFrameObject(frame_bed27f74d7af26fbf540226f0e111d85);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto try_except_handler_1;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_layout);
    Py_DECREF(var_layout);
    var_layout = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_layout);
    var_layout = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_self);
    Py_DECREF(par_self);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}



static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__1___init__(struct Nuitka_CellObject **closure) {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_qt$components$bonuses$$$function__1___init__,
        mod_consts[1],
#if PYTHON_VERSION >= 0x300
        mod_consts[112],
#endif
        codeobj_68ce670cce80fe3ce987e15cd74f3c85,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_qt$components$bonuses,
        NULL,
        closure,
        1
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__2___init__(struct Nuitka_CellObject **closure) {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_qt$components$bonuses$$$function__2___init__,
        mod_consts[1],
#if PYTHON_VERSION >= 0x300
        mod_consts[114],
#endif
        codeobj_a59296a7f8c550f17b41865cc1aa23c7,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_qt$components$bonuses,
        NULL,
        closure,
        1
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__3___getitem__() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_qt$components$bonuses$$$function__3___getitem__,
        mod_consts[105],
#if PYTHON_VERSION >= 0x300
        mod_consts[115],
#endif
        codeobj_314a5deb612b7e8d61fb4a2a255bbf78,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_qt$components$bonuses,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__4_items() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_qt$components$bonuses$$$function__4_items,
        mod_consts[86],
#if PYTHON_VERSION >= 0x300
        mod_consts[116],
#endif
        codeobj_41196fb28ed1cff61af2ccc3c6c2ae89,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_qt$components$bonuses,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_qt$components$bonuses$$$function__5___init__(struct Nuitka_CellObject **closure) {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_qt$components$bonuses$$$function__5___init__,
        mod_consts[1],
#if PYTHON_VERSION >= 0x300
        mod_consts[118],
#endif
        codeobj_bed27f74d7af26fbf540226f0e111d85,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_qt$components$bonuses,
        NULL,
        closure,
        1
    );


    return (PyObject *)result;
}


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill
extern void registerDillPluginTables(PyThreadState *tstate, char const *module_name, PyMethodDef *reduce_compiled_function, PyMethodDef *create_compiled_function);

static function_impl_code const function_table_qt$components$bonuses[] = {
    impl_qt$components$bonuses$$$function__1___init__,
    impl_qt$components$bonuses$$$function__2___init__,
    impl_qt$components$bonuses$$$function__3___getitem__,
    impl_qt$components$bonuses$$$function__4_items,
    impl_qt$components$bonuses$$$function__5___init__,
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTuple(args, "O:reduce_compiled_function", &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        PyThreadState *tstate = PyThreadState_GET();

        SET_CURRENT_EXCEPTION_TYPE0_STR(tstate, PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    int offset = Nuitka_Function_GetFunctionCodeIndex(function, function_table_qt$components$bonuses);

    if (unlikely(offset == -1)) {
        PyThreadState *tstate = PyThreadState_GET();
#if 0
        PRINT_STRING("Looking for:");
        PRINT_ITEM(func);
        PRINT_NEW_LINE();
#endif
        SET_CURRENT_EXCEPTION_TYPE0_STR(tstate, PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = MAKE_TUPLE_EMPTY(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);


    PyObject *result = MAKE_TUPLE_EMPTY(6);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
#if PYTHON_VERSION >= 0x300
    PyTuple_SET_ITEM0(result, 3, function->m_kwdefaults ? function->m_kwdefaults : Py_None);
#else
    PyTuple_SET_ITEM0(result, 3, Py_None);
#endif
    PyTuple_SET_ITEM0(result, 4, function->m_doc != NULL ? function->m_doc : Py_None);

    if (offset == -5) {
        CHECK_OBJECT(function->m_constant_return_value);
        PyTuple_SET_ITEM0(result, 5, function->m_constant_return_value);
    } else {
        PyTuple_SET_ITEM0(result, 5, Py_None);
    }

#if PYTHON_VERSION >= 0x300
    PyTuple_SET_ITEM0(result, 6, function->m_qualname);
#else
    PyTuple_SET_ITEM0(result, 6, Py_None);
#endif

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS, NULL};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *function_index;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *kw_defaults;
    PyObject *doc;
    PyObject *constant_return_value;
    PyObject *function_qualname;

    if (!PyArg_ParseTuple(args, "OOOOOO:create_compiled_function", &function_index, &code_object_desc, &defaults, &kw_defaults, &doc, &constant_return_value, &function_qualname, NULL)) {
        return NULL;
    }

#if PYTHON_VERSION >= 0x300
    if (kw_defaults == Py_None) {
        kw_defaults = NULL;
    }
#endif

    return (PyObject *)Nuitka_Function_CreateFunctionViaCodeIndex(
        module_qt$components$bonuses,
        function_qualname,
        function_index,
        code_object_desc,
        constant_return_value,
        defaults,
        kw_defaults,
        doc,
        function_table_qt$components$bonuses,
        sizeof(function_table_qt$components$bonuses) / sizeof(function_impl_code)
    );
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_qt$components$bonuses(PyThreadState *tstate, PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("qt$components$bonuses");

    // Store the module for future use.
    module_qt$components$bonuses = module;

    // Modules can be loaded again in case of errors, avoid the init being done again.
    static bool init_done = false;

    if (init_done == false) {
#if defined(_NUITKA_MODULE) && 0
        // In case of an extension module loaded into a process, we need to call
        // initialization here because that's the first and potentially only time
        // we are going called.

        // Initialize the constant values used.
        _initBuiltinModule();
        createGlobalConstants(tstate);

        /* Initialize the compiled types of Nuitka. */
        _initCompiledCellType();
        _initCompiledGeneratorType();
        _initCompiledFunctionType();
        _initCompiledMethodType();
        _initCompiledFrameType();

        _initSlotCompare();
#if PYTHON_VERSION >= 0x270
        _initSlotIterNext();
#endif

        patchTypeComparison();

        // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
        PRINT_STRING("qt$components$bonuses: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader(tstate);

#if PYTHON_VERSION >= 0x300
        patchInspectModule(tstate);
#endif

#endif

        /* The constants only used by this module are created now. */
        NUITKA_PRINT_TRACE("qt$components$bonuses: Calling createModuleConstants().\n");
        createModuleConstants(tstate);

        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initqt$components$bonuses\n");

    moduledict_qt$components$bonuses = MODULE_DICT(module_qt$components$bonuses);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    {
        char const *module_name_c;
        if (loader_entry != NULL) {
            module_name_c = loader_entry->name;
        } else {
            PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___name__);
            module_name_c = Nuitka_String_AsString(module_name);
        }

        registerDillPluginTables(tstate, module_name_c, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
    }




#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_qt$components$bonuses,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_qt$components$bonuses,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[37]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_qt$components$bonuses,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_qt$components$bonuses,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_qt$components$bonuses,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_qt$components$bonuses);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

    UPDATE_STRING_DICT0(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, _spec_from_module, module_qt$components$bonuses);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(tstate, spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_CellObject *outline_0_var___class__ = NULL;
    struct Nuitka_CellObject *outline_1_var___class__ = NULL;
    struct Nuitka_CellObject *outline_2_var___class__ = NULL;
    PyObject *tmp_class_creation_1__bases = NULL;
    PyObject *tmp_class_creation_1__bases_orig = NULL;
    PyObject *tmp_class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_class_creation_1__metaclass = NULL;
    PyObject *tmp_class_creation_1__prepared = NULL;
    PyObject *tmp_class_creation_2__bases = NULL;
    PyObject *tmp_class_creation_2__bases_orig = NULL;
    PyObject *tmp_class_creation_2__class_decl_dict = NULL;
    PyObject *tmp_class_creation_2__metaclass = NULL;
    PyObject *tmp_class_creation_2__prepared = NULL;
    PyObject *tmp_class_creation_3__bases = NULL;
    PyObject *tmp_class_creation_3__bases_orig = NULL;
    PyObject *tmp_class_creation_3__class_decl_dict = NULL;
    PyObject *tmp_class_creation_3__metaclass = NULL;
    PyObject *tmp_class_creation_3__prepared = NULL;
    PyObject *tmp_import_from_1__module = NULL;
    PyObject *tmp_import_from_2__module = NULL;
    struct Nuitka_FrameObject *frame_6bf2c041525e6e64362c99311da263cd;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    int tmp_res;
    PyObject *locals_qt$components$bonuses$$$class__1_FormationWidget_6 = NULL;
    PyObject *tmp_dictset_value;
    struct Nuitka_FrameObject *frame_aefc3212dc3c30828b9bdb225a7b2afa_2;
    NUITKA_MAY_BE_UNUSED char const *type_description_2 = NULL;
    PyObject *exception_keeper_type_3;
    PyObject *exception_keeper_value_3;
    PyTracebackObject *exception_keeper_tb_3;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_3;
    PyObject *exception_keeper_type_4;
    PyObject *exception_keeper_value_4;
    PyTracebackObject *exception_keeper_tb_4;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_4;
    PyObject *exception_keeper_type_5;
    PyObject *exception_keeper_value_5;
    PyTracebackObject *exception_keeper_tb_5;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_5;
    PyObject *locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20 = NULL;
    struct Nuitka_FrameObject *frame_c6d31f9da8bc34e06ddad249a420ba82_3;
    NUITKA_MAY_BE_UNUSED char const *type_description_3 = NULL;
    PyObject *exception_keeper_type_6;
    PyObject *exception_keeper_value_6;
    PyTracebackObject *exception_keeper_tb_6;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_6;
    PyObject *exception_keeper_type_7;
    PyObject *exception_keeper_value_7;
    PyTracebackObject *exception_keeper_tb_7;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_7;
    PyObject *exception_keeper_type_8;
    PyObject *exception_keeper_value_8;
    PyTracebackObject *exception_keeper_tb_8;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_8;
    PyObject *locals_qt$components$bonuses$$$class__3_BonusesWidget_220 = NULL;
    struct Nuitka_FrameObject *frame_2c75e018e9ac1b4024c4dde109bbdf2c_4;
    NUITKA_MAY_BE_UNUSED char const *type_description_4 = NULL;
    PyObject *exception_keeper_type_9;
    PyObject *exception_keeper_value_9;
    PyTracebackObject *exception_keeper_tb_9;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_9;
    PyObject *exception_keeper_type_10;
    PyObject *exception_keeper_value_10;
    PyTracebackObject *exception_keeper_tb_10;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_10;
    PyObject *exception_keeper_type_11;
    PyObject *exception_keeper_value_11;
    PyTracebackObject *exception_keeper_tb_11;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_11;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[92], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[93], tmp_assign_source_2);
    }
    frame_6bf2c041525e6e64362c99311da263cd = MAKE_MODULE_FRAME(codeobj_6bf2c041525e6e64362c99311da263cd, module_qt$components$bonuses);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_6bf2c041525e6e64362c99311da263cd);
    assert(Py_REFCNT(frame_6bf2c041525e6e64362c99311da263cd) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[94]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[94]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_1, mod_consts[95], tmp_assattr_value_1);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_value_2;
        PyObject *tmp_assattr_target_2;
        tmp_assattr_value_2 = Py_True;
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[94]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[94]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_2, mod_consts[96], tmp_assattr_value_2);
        if (tmp_result == false) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[97], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[98];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_qt$components$bonuses;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[99];
        tmp_level_value_1 = mod_consts[24];
        frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 1;
        tmp_assign_source_4 = IMPORT_MODULE5(tstate, tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_4 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        assert(tmp_import_from_1__module == NULL);
        tmp_import_from_1__module = tmp_assign_source_4;
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_import_name_from_1;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_1 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_5 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_1,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[4],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_5 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_1, mod_consts[4]);
        }

        if (tmp_assign_source_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[4], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_import_name_from_2;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_2 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_2)) {
            tmp_assign_source_6 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_2,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[8],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_6 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_2, mod_consts[8]);
        }

        if (tmp_assign_source_6 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[8], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_import_name_from_3;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_3 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_3)) {
            tmp_assign_source_7 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_3,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[21],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_7 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_3, mod_consts[21]);
        }

        if (tmp_assign_source_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[21], tmp_assign_source_7);
    }
    goto try_end_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    {
        PyObject *tmp_assign_source_8;
        PyObject *tmp_name_value_2;
        PyObject *tmp_globals_arg_value_2;
        PyObject *tmp_locals_arg_value_2;
        PyObject *tmp_fromlist_value_2;
        PyObject *tmp_level_value_2;
        tmp_name_value_2 = mod_consts[100];
        tmp_globals_arg_value_2 = (PyObject *)moduledict_qt$components$bonuses;
        tmp_locals_arg_value_2 = Py_None;
        tmp_fromlist_value_2 = mod_consts[101];
        tmp_level_value_2 = mod_consts[24];
        frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 2;
        tmp_assign_source_8 = IMPORT_MODULE5(tstate, tmp_name_value_2, tmp_globals_arg_value_2, tmp_locals_arg_value_2, tmp_fromlist_value_2, tmp_level_value_2);
        if (tmp_assign_source_8 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;

            goto frame_exception_exit_1;
        }
        assert(tmp_import_from_2__module == NULL);
        tmp_import_from_2__module = tmp_assign_source_8;
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_9;
        PyObject *tmp_import_name_from_4;
        CHECK_OBJECT(tmp_import_from_2__module);
        tmp_import_name_from_4 = tmp_import_from_2__module;
        if (PyModule_Check(tmp_import_name_from_4)) {
            tmp_assign_source_9 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_4,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[17],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_9 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_4, mod_consts[17]);
        }

        if (tmp_assign_source_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;

            goto try_except_handler_2;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;
        PyObject *tmp_import_name_from_5;
        CHECK_OBJECT(tmp_import_from_2__module);
        tmp_import_name_from_5 = tmp_import_from_2__module;
        if (PyModule_Check(tmp_import_name_from_5)) {
            tmp_assign_source_10 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_5,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[14],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_10 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_5, mod_consts[14]);
        }

        if (tmp_assign_source_10 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;

            goto try_except_handler_2;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;
        PyObject *tmp_import_name_from_6;
        CHECK_OBJECT(tmp_import_from_2__module);
        tmp_import_name_from_6 = tmp_import_from_2__module;
        if (PyModule_Check(tmp_import_name_from_6)) {
            tmp_assign_source_11 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_6,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[2],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_11 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_6, mod_consts[2]);
        }

        if (tmp_assign_source_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;

            goto try_except_handler_2;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[2], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;
        PyObject *tmp_import_name_from_7;
        CHECK_OBJECT(tmp_import_from_2__module);
        tmp_import_name_from_7 = tmp_import_from_2__module;
        if (PyModule_Check(tmp_import_name_from_7)) {
            tmp_assign_source_12 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_7,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[18],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_12 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_7, mod_consts[18]);
        }

        if (tmp_assign_source_12 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;

            goto try_except_handler_2;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[18], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;
        PyObject *tmp_import_name_from_8;
        CHECK_OBJECT(tmp_import_from_2__module);
        tmp_import_name_from_8 = tmp_import_from_2__module;
        if (PyModule_Check(tmp_import_name_from_8)) {
            tmp_assign_source_13 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_8,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[16],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_13 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_8, mod_consts[16]);
        }

        if (tmp_assign_source_13 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 2;

            goto try_except_handler_2;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[16], tmp_assign_source_13);
    }
    goto try_end_2;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    CHECK_OBJECT(tmp_import_from_2__module);
    Py_DECREF(tmp_import_from_2__module);
    tmp_import_from_2__module = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto frame_exception_exit_1;
    // End of try:
    try_end_2:;
    CHECK_OBJECT(tmp_import_from_2__module);
    Py_DECREF(tmp_import_from_2__module);
    tmp_import_from_2__module = NULL;
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_import_name_from_9;
        PyObject *tmp_name_value_3;
        PyObject *tmp_globals_arg_value_3;
        PyObject *tmp_locals_arg_value_3;
        PyObject *tmp_fromlist_value_3;
        PyObject *tmp_level_value_3;
        tmp_name_value_3 = mod_consts[102];
        tmp_globals_arg_value_3 = (PyObject *)moduledict_qt$components$bonuses;
        tmp_locals_arg_value_3 = Py_None;
        tmp_fromlist_value_3 = mod_consts[103];
        tmp_level_value_3 = mod_consts[24];
        frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 3;
        tmp_import_name_from_9 = IMPORT_MODULE5(tstate, tmp_name_value_3, tmp_globals_arg_value_3, tmp_locals_arg_value_3, tmp_fromlist_value_3, tmp_level_value_3);
        if (tmp_import_name_from_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 3;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_9)) {
            tmp_assign_source_14 = IMPORT_NAME_OR_MODULE(
                tstate,
                tmp_import_name_from_9,
                (PyObject *)moduledict_qt$components$bonuses,
                mod_consts[23],
                mod_consts[24]
            );
        } else {
            tmp_assign_source_14 = IMPORT_NAME_FROM_MODULE(tstate, tmp_import_name_from_9, mod_consts[23]);
        }

        Py_DECREF(tmp_import_name_from_9);
        if (tmp_assign_source_14 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 3;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[23], tmp_assign_source_14);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_15;
        PyObject *tmp_tuple_element_1;
        tmp_tuple_element_1 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_tuple_element_1 == NULL)) {
            tmp_tuple_element_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_tuple_element_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_assign_source_15 = MAKE_TUPLE_EMPTY(1);
        PyTuple_SET_ITEM0(tmp_assign_source_15, 0, tmp_tuple_element_1);
        assert(tmp_class_creation_1__bases_orig == NULL);
        tmp_class_creation_1__bases_orig = tmp_assign_source_15;
    }
    {
        PyObject *tmp_assign_source_16;
        PyObject *tmp_dircall_arg1_1;
        CHECK_OBJECT(tmp_class_creation_1__bases_orig);
        tmp_dircall_arg1_1 = tmp_class_creation_1__bases_orig;
        Py_INCREF(tmp_dircall_arg1_1);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_1};
            tmp_assign_source_16 = impl___main__$$$function__1__mro_entries_conversion(tstate, dir_call_args);
        }
        if (tmp_assign_source_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        assert(tmp_class_creation_1__bases == NULL);
        tmp_class_creation_1__bases = tmp_assign_source_16;
    }
    {
        PyObject *tmp_assign_source_17;
        tmp_assign_source_17 = MAKE_DICT_EMPTY();
        assert(tmp_class_creation_1__class_decl_dict == NULL);
        tmp_class_creation_1__class_decl_dict = tmp_assign_source_17;
    }
    {
        PyObject *tmp_assign_source_18;
        PyObject *tmp_metaclass_value_1;
        nuitka_bool tmp_condition_result_1;
        int tmp_truth_name_1;
        PyObject *tmp_type_arg_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_subscript_value_1;
        PyObject *tmp_bases_value_1;
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_truth_name_1 = CHECK_IF_TRUE(tmp_class_creation_1__bases);
        if (tmp_truth_name_1 == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_condition_result_1 = tmp_truth_name_1 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_1 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_1;
        } else {
            goto condexpr_false_1;
        }
        condexpr_true_1:;
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_expression_value_1 = tmp_class_creation_1__bases;
        tmp_subscript_value_1 = mod_consts[24];
        tmp_type_arg_1 = LOOKUP_SUBSCRIPT_CONST(tstate, tmp_expression_value_1, tmp_subscript_value_1, 0);
        if (tmp_type_arg_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_metaclass_value_1 = BUILTIN_TYPE1(tmp_type_arg_1);
        Py_DECREF(tmp_type_arg_1);
        if (tmp_metaclass_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        goto condexpr_end_1;
        condexpr_false_1:;
        tmp_metaclass_value_1 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_1);
        condexpr_end_1:;
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_bases_value_1 = tmp_class_creation_1__bases;
        tmp_assign_source_18 = SELECT_METACLASS(tstate, tmp_metaclass_value_1, tmp_bases_value_1);
        Py_DECREF(tmp_metaclass_value_1);
        if (tmp_assign_source_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        assert(tmp_class_creation_1__metaclass == NULL);
        tmp_class_creation_1__metaclass = tmp_assign_source_18;
    }
    {
        bool tmp_condition_result_2;
        PyObject *tmp_expression_value_2;
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_2 = tmp_class_creation_1__metaclass;
        tmp_res = HAS_ATTR_BOOL2(tstate, tmp_expression_value_2, mod_consts[104]);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_condition_result_2 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_2 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    {
        PyObject *tmp_assign_source_19;
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_3;
        PyObject *tmp_args_value_1;
        PyObject *tmp_tuple_element_2;
        PyObject *tmp_kwargs_value_1;
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_3 = tmp_class_creation_1__metaclass;
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_3, mod_consts[104]);
        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_tuple_element_2 = mod_consts[88];
        tmp_args_value_1 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM0(tmp_args_value_1, 0, tmp_tuple_element_2);
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_tuple_element_2 = tmp_class_creation_1__bases;
        PyTuple_SET_ITEM0(tmp_args_value_1, 1, tmp_tuple_element_2);
        CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
        tmp_kwargs_value_1 = tmp_class_creation_1__class_decl_dict;
        frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 6;
        tmp_assign_source_19 = CALL_FUNCTION(tstate, tmp_called_value_1, tmp_args_value_1, tmp_kwargs_value_1);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_args_value_1);
        if (tmp_assign_source_19 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        assert(tmp_class_creation_1__prepared == NULL);
        tmp_class_creation_1__prepared = tmp_assign_source_19;
    }
    {
        bool tmp_condition_result_3;
        PyObject *tmp_operand_value_1;
        PyObject *tmp_expression_value_4;
        CHECK_OBJECT(tmp_class_creation_1__prepared);
        tmp_expression_value_4 = tmp_class_creation_1__prepared;
        tmp_res = HAS_ATTR_BOOL2(tstate, tmp_expression_value_4, mod_consts[105]);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_operand_value_1 = (tmp_res != 0) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        assert(!(tmp_res == -1));
        tmp_condition_result_3 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_3 != false) {
            goto branch_yes_2;
        } else {
            goto branch_no_2;
        }
    }
    branch_yes_2:;
    {
        PyObject *tmp_raise_type_1;
        PyObject *tmp_raise_value_1;
        PyObject *tmp_mod_expr_left_1;
        PyObject *tmp_mod_expr_right_1;
        PyObject *tmp_tuple_element_3;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_name_value_4;
        PyObject *tmp_default_value_1;
        tmp_raise_type_1 = PyExc_TypeError;
        tmp_mod_expr_left_1 = mod_consts[106];
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_5 = tmp_class_creation_1__metaclass;
        tmp_name_value_4 = mod_consts[107];
        tmp_default_value_1 = mod_consts[108];
        tmp_tuple_element_3 = BUILTIN_GETATTR(tstate, tmp_expression_value_5, tmp_name_value_4, tmp_default_value_1);
        if (tmp_tuple_element_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        tmp_mod_expr_right_1 = MAKE_TUPLE_EMPTY(2);
        {
            PyObject *tmp_expression_value_6;
            PyObject *tmp_type_arg_2;
            PyTuple_SET_ITEM(tmp_mod_expr_right_1, 0, tmp_tuple_element_3);
            CHECK_OBJECT(tmp_class_creation_1__prepared);
            tmp_type_arg_2 = tmp_class_creation_1__prepared;
            tmp_expression_value_6 = BUILTIN_TYPE1(tmp_type_arg_2);
            assert(!(tmp_expression_value_6 == NULL));
            tmp_tuple_element_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_6, mod_consts[107]);
            Py_DECREF(tmp_expression_value_6);
            if (tmp_tuple_element_3 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 6;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_1, 1, tmp_tuple_element_3);
        }
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_mod_expr_right_1);
        goto try_except_handler_3;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        tmp_raise_value_1 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_1, tmp_mod_expr_right_1);
        Py_DECREF(tmp_mod_expr_right_1);
        if (tmp_raise_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_3;
        }
        exception_type = tmp_raise_type_1;
        Py_INCREF(tmp_raise_type_1);
        exception_value = tmp_raise_value_1;
        exception_lineno = 6;
        RAISE_EXCEPTION_IMPLICIT(tstate, &exception_type, &exception_value, &exception_tb);

        goto try_except_handler_3;
    }
    branch_no_2:;
    goto branch_end_1;
    branch_no_1:;
    {
        PyObject *tmp_assign_source_20;
        tmp_assign_source_20 = MAKE_DICT_EMPTY();
        assert(tmp_class_creation_1__prepared == NULL);
        tmp_class_creation_1__prepared = tmp_assign_source_20;
    }
    branch_end_1:;
    {
        PyObject *tmp_assign_source_21;
        outline_0_var___class__ = Nuitka_Cell_Empty();
        {
            PyObject *tmp_set_locals_1;
            CHECK_OBJECT(tmp_class_creation_1__prepared);
            tmp_set_locals_1 = tmp_class_creation_1__prepared;
            locals_qt$components$bonuses$$$class__1_FormationWidget_6 = tmp_set_locals_1;
            Py_INCREF(tmp_set_locals_1);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[109];
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__1_FormationWidget_6, mod_consts[110], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_5;
        }
        tmp_dictset_value = mod_consts[88];
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__1_FormationWidget_6, mod_consts[111], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_5;
        }
        frame_aefc3212dc3c30828b9bdb225a7b2afa_2 = MAKE_CLASS_FRAME(tstate, codeobj_aefc3212dc3c30828b9bdb225a7b2afa, module_qt$components$bonuses, NULL, sizeof(void *));

        // Push the new frame as the currently active one, and we should be exclusively
        // owning it.
        pushFrameStackCompiledFrame(tstate, frame_aefc3212dc3c30828b9bdb225a7b2afa_2);
        assert(Py_REFCNT(frame_aefc3212dc3c30828b9bdb225a7b2afa_2) == 2);

        // Framed code:
        {
            struct Nuitka_CellObject *tmp_closure_1[1];

            tmp_closure_1[0] = outline_0_var___class__;
            Py_INCREF(tmp_closure_1[0]);

            tmp_dictset_value = MAKE_FUNCTION_qt$components$bonuses$$$function__1___init__(tmp_closure_1);

            tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__1_FormationWidget_6, mod_consts[1], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 7;
                type_description_2 = "c";
                goto frame_exception_exit_2;
            }
        }


        // Put the previous frame back on top.
        popFrameStack(tstate);

        goto frame_no_exception_1;
        frame_exception_exit_2:


        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_aefc3212dc3c30828b9bdb225a7b2afa_2, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_aefc3212dc3c30828b9bdb225a7b2afa_2->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_aefc3212dc3c30828b9bdb225a7b2afa_2, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_aefc3212dc3c30828b9bdb225a7b2afa_2,
            type_description_2,
            outline_0_var___class__
        );



        assertFrameObject(frame_aefc3212dc3c30828b9bdb225a7b2afa_2);

        // Put the previous frame back on top.
        popFrameStack(tstate);

        // Return the error.
        goto nested_frame_exit_1;
        frame_no_exception_1:;
        goto skip_nested_handling_1;
        nested_frame_exit_1:;

        goto try_except_handler_5;
        skip_nested_handling_1:;
        {
            nuitka_bool tmp_condition_result_4;
            PyObject *tmp_cmp_expr_left_1;
            PyObject *tmp_cmp_expr_right_1;
            CHECK_OBJECT(tmp_class_creation_1__bases);
            tmp_cmp_expr_left_1 = tmp_class_creation_1__bases;
            CHECK_OBJECT(tmp_class_creation_1__bases_orig);
            tmp_cmp_expr_right_1 = tmp_class_creation_1__bases_orig;
            tmp_condition_result_4 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
            if (tmp_condition_result_4 == NUITKA_BOOL_EXCEPTION) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 6;

                goto try_except_handler_5;
            }
            if (tmp_condition_result_4 == NUITKA_BOOL_TRUE) {
                goto branch_yes_3;
            } else {
                goto branch_no_3;
            }
        }
        branch_yes_3:;
        CHECK_OBJECT(tmp_class_creation_1__bases_orig);
        tmp_dictset_value = tmp_class_creation_1__bases_orig;
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__1_FormationWidget_6, mod_consts[113], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 6;

            goto try_except_handler_5;
        }
        branch_no_3:;
        {
            PyObject *tmp_assign_source_22;
            PyObject *tmp_called_value_2;
            PyObject *tmp_args_value_2;
            PyObject *tmp_tuple_element_4;
            PyObject *tmp_kwargs_value_2;
            CHECK_OBJECT(tmp_class_creation_1__metaclass);
            tmp_called_value_2 = tmp_class_creation_1__metaclass;
            tmp_tuple_element_4 = mod_consts[88];
            tmp_args_value_2 = MAKE_TUPLE_EMPTY(3);
            PyTuple_SET_ITEM0(tmp_args_value_2, 0, tmp_tuple_element_4);
            CHECK_OBJECT(tmp_class_creation_1__bases);
            tmp_tuple_element_4 = tmp_class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_2, 1, tmp_tuple_element_4);
            tmp_tuple_element_4 = locals_qt$components$bonuses$$$class__1_FormationWidget_6;
            PyTuple_SET_ITEM0(tmp_args_value_2, 2, tmp_tuple_element_4);
            CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
            tmp_kwargs_value_2 = tmp_class_creation_1__class_decl_dict;
            frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 6;
            tmp_assign_source_22 = CALL_FUNCTION(tstate, tmp_called_value_2, tmp_args_value_2, tmp_kwargs_value_2);
            Py_DECREF(tmp_args_value_2);
            if (tmp_assign_source_22 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 6;

                goto try_except_handler_5;
            }
            assert(Nuitka_Cell_GET(outline_0_var___class__) == NULL);
            PyCell_SET(outline_0_var___class__, tmp_assign_source_22);

        }
        CHECK_OBJECT(Nuitka_Cell_GET(outline_0_var___class__));
        tmp_assign_source_21 = Nuitka_Cell_GET(outline_0_var___class__);
        Py_INCREF(tmp_assign_source_21);
        goto try_return_handler_5;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_5:;
        Py_DECREF(locals_qt$components$bonuses$$$class__1_FormationWidget_6);
        locals_qt$components$bonuses$$$class__1_FormationWidget_6 = NULL;
        goto try_return_handler_4;
        // Exception handler code:
        try_except_handler_5:;
        exception_keeper_type_3 = exception_type;
        exception_keeper_value_3 = exception_value;
        exception_keeper_tb_3 = exception_tb;
        exception_keeper_lineno_3 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_qt$components$bonuses$$$class__1_FormationWidget_6);
        locals_qt$components$bonuses$$$class__1_FormationWidget_6 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_3;
        exception_value = exception_keeper_value_3;
        exception_tb = exception_keeper_tb_3;
        exception_lineno = exception_keeper_lineno_3;

        goto try_except_handler_4;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_4:;
        CHECK_OBJECT(outline_0_var___class__);
        Py_DECREF(outline_0_var___class__);
        outline_0_var___class__ = NULL;
        goto outline_result_1;
        // Exception handler code:
        try_except_handler_4:;
        exception_keeper_type_4 = exception_type;
        exception_keeper_value_4 = exception_value;
        exception_keeper_tb_4 = exception_tb;
        exception_keeper_lineno_4 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_4;
        exception_value = exception_keeper_value_4;
        exception_tb = exception_keeper_tb_4;
        exception_lineno = exception_keeper_lineno_4;

        goto outline_exception_1;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_1:;
        exception_lineno = 6;
        goto try_except_handler_3;
        outline_result_1:;
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[88], tmp_assign_source_21);
    }
    goto try_end_3;
    // Exception handler code:
    try_except_handler_3:;
    exception_keeper_type_5 = exception_type;
    exception_keeper_value_5 = exception_value;
    exception_keeper_tb_5 = exception_tb;
    exception_keeper_lineno_5 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_1__bases_orig);
    tmp_class_creation_1__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_1__bases);
    tmp_class_creation_1__bases = NULL;
    Py_XDECREF(tmp_class_creation_1__class_decl_dict);
    tmp_class_creation_1__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_1__metaclass);
    tmp_class_creation_1__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_1__prepared);
    tmp_class_creation_1__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_5;
    exception_value = exception_keeper_value_5;
    exception_tb = exception_keeper_tb_5;
    exception_lineno = exception_keeper_lineno_5;

    goto frame_exception_exit_1;
    // End of try:
    try_end_3:;
    CHECK_OBJECT(tmp_class_creation_1__bases_orig);
    Py_DECREF(tmp_class_creation_1__bases_orig);
    tmp_class_creation_1__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_1__bases);
    Py_DECREF(tmp_class_creation_1__bases);
    tmp_class_creation_1__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
    Py_DECREF(tmp_class_creation_1__class_decl_dict);
    tmp_class_creation_1__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_1__metaclass);
    Py_DECREF(tmp_class_creation_1__metaclass);
    tmp_class_creation_1__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_1__prepared);
    Py_DECREF(tmp_class_creation_1__prepared);
    tmp_class_creation_1__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_23;
        PyObject *tmp_tuple_element_5;
        tmp_tuple_element_5 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_tuple_element_5 == NULL)) {
            tmp_tuple_element_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_tuple_element_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_assign_source_23 = MAKE_TUPLE_EMPTY(1);
        PyTuple_SET_ITEM0(tmp_assign_source_23, 0, tmp_tuple_element_5);
        assert(tmp_class_creation_2__bases_orig == NULL);
        tmp_class_creation_2__bases_orig = tmp_assign_source_23;
    }
    {
        PyObject *tmp_assign_source_24;
        PyObject *tmp_dircall_arg1_2;
        CHECK_OBJECT(tmp_class_creation_2__bases_orig);
        tmp_dircall_arg1_2 = tmp_class_creation_2__bases_orig;
        Py_INCREF(tmp_dircall_arg1_2);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_2};
            tmp_assign_source_24 = impl___main__$$$function__1__mro_entries_conversion(tstate, dir_call_args);
        }
        if (tmp_assign_source_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        assert(tmp_class_creation_2__bases == NULL);
        tmp_class_creation_2__bases = tmp_assign_source_24;
    }
    {
        PyObject *tmp_assign_source_25;
        tmp_assign_source_25 = MAKE_DICT_EMPTY();
        assert(tmp_class_creation_2__class_decl_dict == NULL);
        tmp_class_creation_2__class_decl_dict = tmp_assign_source_25;
    }
    {
        PyObject *tmp_assign_source_26;
        PyObject *tmp_metaclass_value_2;
        nuitka_bool tmp_condition_result_5;
        int tmp_truth_name_2;
        PyObject *tmp_type_arg_3;
        PyObject *tmp_expression_value_7;
        PyObject *tmp_subscript_value_2;
        PyObject *tmp_bases_value_2;
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_truth_name_2 = CHECK_IF_TRUE(tmp_class_creation_2__bases);
        if (tmp_truth_name_2 == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_condition_result_5 = tmp_truth_name_2 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_5 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_2;
        } else {
            goto condexpr_false_2;
        }
        condexpr_true_2:;
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_expression_value_7 = tmp_class_creation_2__bases;
        tmp_subscript_value_2 = mod_consts[24];
        tmp_type_arg_3 = LOOKUP_SUBSCRIPT_CONST(tstate, tmp_expression_value_7, tmp_subscript_value_2, 0);
        if (tmp_type_arg_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_metaclass_value_2 = BUILTIN_TYPE1(tmp_type_arg_3);
        Py_DECREF(tmp_type_arg_3);
        if (tmp_metaclass_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        goto condexpr_end_2;
        condexpr_false_2:;
        tmp_metaclass_value_2 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_2);
        condexpr_end_2:;
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_bases_value_2 = tmp_class_creation_2__bases;
        tmp_assign_source_26 = SELECT_METACLASS(tstate, tmp_metaclass_value_2, tmp_bases_value_2);
        Py_DECREF(tmp_metaclass_value_2);
        if (tmp_assign_source_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        assert(tmp_class_creation_2__metaclass == NULL);
        tmp_class_creation_2__metaclass = tmp_assign_source_26;
    }
    {
        bool tmp_condition_result_6;
        PyObject *tmp_expression_value_8;
        CHECK_OBJECT(tmp_class_creation_2__metaclass);
        tmp_expression_value_8 = tmp_class_creation_2__metaclass;
        tmp_res = HAS_ATTR_BOOL2(tstate, tmp_expression_value_8, mod_consts[104]);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_condition_result_6 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_6 != false) {
            goto branch_yes_4;
        } else {
            goto branch_no_4;
        }
    }
    branch_yes_4:;
    {
        PyObject *tmp_assign_source_27;
        PyObject *tmp_called_value_3;
        PyObject *tmp_expression_value_9;
        PyObject *tmp_args_value_3;
        PyObject *tmp_tuple_element_6;
        PyObject *tmp_kwargs_value_3;
        CHECK_OBJECT(tmp_class_creation_2__metaclass);
        tmp_expression_value_9 = tmp_class_creation_2__metaclass;
        tmp_called_value_3 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_9, mod_consts[104]);
        if (tmp_called_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_tuple_element_6 = mod_consts[90];
        tmp_args_value_3 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM0(tmp_args_value_3, 0, tmp_tuple_element_6);
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_tuple_element_6 = tmp_class_creation_2__bases;
        PyTuple_SET_ITEM0(tmp_args_value_3, 1, tmp_tuple_element_6);
        CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
        tmp_kwargs_value_3 = tmp_class_creation_2__class_decl_dict;
        frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 20;
        tmp_assign_source_27 = CALL_FUNCTION(tstate, tmp_called_value_3, tmp_args_value_3, tmp_kwargs_value_3);
        Py_DECREF(tmp_called_value_3);
        Py_DECREF(tmp_args_value_3);
        if (tmp_assign_source_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        assert(tmp_class_creation_2__prepared == NULL);
        tmp_class_creation_2__prepared = tmp_assign_source_27;
    }
    {
        bool tmp_condition_result_7;
        PyObject *tmp_operand_value_2;
        PyObject *tmp_expression_value_10;
        CHECK_OBJECT(tmp_class_creation_2__prepared);
        tmp_expression_value_10 = tmp_class_creation_2__prepared;
        tmp_res = HAS_ATTR_BOOL2(tstate, tmp_expression_value_10, mod_consts[105]);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_operand_value_2 = (tmp_res != 0) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_2);
        assert(!(tmp_res == -1));
        tmp_condition_result_7 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_7 != false) {
            goto branch_yes_5;
        } else {
            goto branch_no_5;
        }
    }
    branch_yes_5:;
    {
        PyObject *tmp_raise_type_2;
        PyObject *tmp_raise_value_2;
        PyObject *tmp_mod_expr_left_2;
        PyObject *tmp_mod_expr_right_2;
        PyObject *tmp_tuple_element_7;
        PyObject *tmp_expression_value_11;
        PyObject *tmp_name_value_5;
        PyObject *tmp_default_value_2;
        tmp_raise_type_2 = PyExc_TypeError;
        tmp_mod_expr_left_2 = mod_consts[106];
        CHECK_OBJECT(tmp_class_creation_2__metaclass);
        tmp_expression_value_11 = tmp_class_creation_2__metaclass;
        tmp_name_value_5 = mod_consts[107];
        tmp_default_value_2 = mod_consts[108];
        tmp_tuple_element_7 = BUILTIN_GETATTR(tstate, tmp_expression_value_11, tmp_name_value_5, tmp_default_value_2);
        if (tmp_tuple_element_7 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        tmp_mod_expr_right_2 = MAKE_TUPLE_EMPTY(2);
        {
            PyObject *tmp_expression_value_12;
            PyObject *tmp_type_arg_4;
            PyTuple_SET_ITEM(tmp_mod_expr_right_2, 0, tmp_tuple_element_7);
            CHECK_OBJECT(tmp_class_creation_2__prepared);
            tmp_type_arg_4 = tmp_class_creation_2__prepared;
            tmp_expression_value_12 = BUILTIN_TYPE1(tmp_type_arg_4);
            assert(!(tmp_expression_value_12 == NULL));
            tmp_tuple_element_7 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_12, mod_consts[107]);
            Py_DECREF(tmp_expression_value_12);
            if (tmp_tuple_element_7 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 20;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_2, 1, tmp_tuple_element_7);
        }
        goto tuple_build_noexception_2;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_2:;
        Py_DECREF(tmp_mod_expr_right_2);
        goto try_except_handler_6;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_2:;
        tmp_raise_value_2 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_2, tmp_mod_expr_right_2);
        Py_DECREF(tmp_mod_expr_right_2);
        if (tmp_raise_value_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_6;
        }
        exception_type = tmp_raise_type_2;
        Py_INCREF(tmp_raise_type_2);
        exception_value = tmp_raise_value_2;
        exception_lineno = 20;
        RAISE_EXCEPTION_IMPLICIT(tstate, &exception_type, &exception_value, &exception_tb);

        goto try_except_handler_6;
    }
    branch_no_5:;
    goto branch_end_4;
    branch_no_4:;
    {
        PyObject *tmp_assign_source_28;
        tmp_assign_source_28 = MAKE_DICT_EMPTY();
        assert(tmp_class_creation_2__prepared == NULL);
        tmp_class_creation_2__prepared = tmp_assign_source_28;
    }
    branch_end_4:;
    {
        PyObject *tmp_assign_source_29;
        outline_1_var___class__ = Nuitka_Cell_Empty();
        {
            PyObject *tmp_set_locals_2;
            CHECK_OBJECT(tmp_class_creation_2__prepared);
            tmp_set_locals_2 = tmp_class_creation_2__prepared;
            locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20 = tmp_set_locals_2;
            Py_INCREF(tmp_set_locals_2);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[109];
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20, mod_consts[110], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_8;
        }
        tmp_dictset_value = mod_consts[90];
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20, mod_consts[111], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_8;
        }
        frame_c6d31f9da8bc34e06ddad249a420ba82_3 = MAKE_CLASS_FRAME(tstate, codeobj_c6d31f9da8bc34e06ddad249a420ba82, module_qt$components$bonuses, NULL, sizeof(void *));

        // Push the new frame as the currently active one, and we should be exclusively
        // owning it.
        pushFrameStackCompiledFrame(tstate, frame_c6d31f9da8bc34e06ddad249a420ba82_3);
        assert(Py_REFCNT(frame_c6d31f9da8bc34e06ddad249a420ba82_3) == 2);

        // Framed code:
        {
            struct Nuitka_CellObject *tmp_closure_2[1];

            tmp_closure_2[0] = outline_1_var___class__;
            Py_INCREF(tmp_closure_2[0]);

            tmp_dictset_value = MAKE_FUNCTION_qt$components$bonuses$$$function__2___init__(tmp_closure_2);

            tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20, mod_consts[1], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 21;
                type_description_2 = "c";
                goto frame_exception_exit_3;
            }
        }


        tmp_dictset_value = MAKE_FUNCTION_qt$components$bonuses$$$function__3___getitem__();

        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20, mod_consts[105], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 213;
            type_description_2 = "c";
            goto frame_exception_exit_3;
        }


        tmp_dictset_value = MAKE_FUNCTION_qt$components$bonuses$$$function__4_items();

        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20, mod_consts[86], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 216;
            type_description_2 = "c";
            goto frame_exception_exit_3;
        }


        // Put the previous frame back on top.
        popFrameStack(tstate);

        goto frame_no_exception_2;
        frame_exception_exit_3:


        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_c6d31f9da8bc34e06ddad249a420ba82_3, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_c6d31f9da8bc34e06ddad249a420ba82_3->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_c6d31f9da8bc34e06ddad249a420ba82_3, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_c6d31f9da8bc34e06ddad249a420ba82_3,
            type_description_2,
            outline_1_var___class__
        );



        assertFrameObject(frame_c6d31f9da8bc34e06ddad249a420ba82_3);

        // Put the previous frame back on top.
        popFrameStack(tstate);

        // Return the error.
        goto nested_frame_exit_2;
        frame_no_exception_2:;
        goto skip_nested_handling_2;
        nested_frame_exit_2:;

        goto try_except_handler_8;
        skip_nested_handling_2:;
        {
            nuitka_bool tmp_condition_result_8;
            PyObject *tmp_cmp_expr_left_2;
            PyObject *tmp_cmp_expr_right_2;
            CHECK_OBJECT(tmp_class_creation_2__bases);
            tmp_cmp_expr_left_2 = tmp_class_creation_2__bases;
            CHECK_OBJECT(tmp_class_creation_2__bases_orig);
            tmp_cmp_expr_right_2 = tmp_class_creation_2__bases_orig;
            tmp_condition_result_8 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_2, tmp_cmp_expr_right_2);
            if (tmp_condition_result_8 == NUITKA_BOOL_EXCEPTION) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 20;

                goto try_except_handler_8;
            }
            if (tmp_condition_result_8 == NUITKA_BOOL_TRUE) {
                goto branch_yes_6;
            } else {
                goto branch_no_6;
            }
        }
        branch_yes_6:;
        CHECK_OBJECT(tmp_class_creation_2__bases_orig);
        tmp_dictset_value = tmp_class_creation_2__bases_orig;
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20, mod_consts[113], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto try_except_handler_8;
        }
        branch_no_6:;
        {
            PyObject *tmp_assign_source_30;
            PyObject *tmp_called_value_4;
            PyObject *tmp_args_value_4;
            PyObject *tmp_tuple_element_8;
            PyObject *tmp_kwargs_value_4;
            CHECK_OBJECT(tmp_class_creation_2__metaclass);
            tmp_called_value_4 = tmp_class_creation_2__metaclass;
            tmp_tuple_element_8 = mod_consts[90];
            tmp_args_value_4 = MAKE_TUPLE_EMPTY(3);
            PyTuple_SET_ITEM0(tmp_args_value_4, 0, tmp_tuple_element_8);
            CHECK_OBJECT(tmp_class_creation_2__bases);
            tmp_tuple_element_8 = tmp_class_creation_2__bases;
            PyTuple_SET_ITEM0(tmp_args_value_4, 1, tmp_tuple_element_8);
            tmp_tuple_element_8 = locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20;
            PyTuple_SET_ITEM0(tmp_args_value_4, 2, tmp_tuple_element_8);
            CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
            tmp_kwargs_value_4 = tmp_class_creation_2__class_decl_dict;
            frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 20;
            tmp_assign_source_30 = CALL_FUNCTION(tstate, tmp_called_value_4, tmp_args_value_4, tmp_kwargs_value_4);
            Py_DECREF(tmp_args_value_4);
            if (tmp_assign_source_30 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 20;

                goto try_except_handler_8;
            }
            assert(Nuitka_Cell_GET(outline_1_var___class__) == NULL);
            PyCell_SET(outline_1_var___class__, tmp_assign_source_30);

        }
        CHECK_OBJECT(Nuitka_Cell_GET(outline_1_var___class__));
        tmp_assign_source_29 = Nuitka_Cell_GET(outline_1_var___class__);
        Py_INCREF(tmp_assign_source_29);
        goto try_return_handler_8;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_8:;
        Py_DECREF(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20);
        locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20 = NULL;
        goto try_return_handler_7;
        // Exception handler code:
        try_except_handler_8:;
        exception_keeper_type_6 = exception_type;
        exception_keeper_value_6 = exception_value;
        exception_keeper_tb_6 = exception_tb;
        exception_keeper_lineno_6 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20);
        locals_qt$components$bonuses$$$class__2_TeamGainsWidget_20 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_6;
        exception_value = exception_keeper_value_6;
        exception_tb = exception_keeper_tb_6;
        exception_lineno = exception_keeper_lineno_6;

        goto try_except_handler_7;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_7:;
        CHECK_OBJECT(outline_1_var___class__);
        Py_DECREF(outline_1_var___class__);
        outline_1_var___class__ = NULL;
        goto outline_result_2;
        // Exception handler code:
        try_except_handler_7:;
        exception_keeper_type_7 = exception_type;
        exception_keeper_value_7 = exception_value;
        exception_keeper_tb_7 = exception_tb;
        exception_keeper_lineno_7 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_7;
        exception_value = exception_keeper_value_7;
        exception_tb = exception_keeper_tb_7;
        exception_lineno = exception_keeper_lineno_7;

        goto outline_exception_2;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_2:;
        exception_lineno = 20;
        goto try_except_handler_6;
        outline_result_2:;
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[90], tmp_assign_source_29);
    }
    goto try_end_4;
    // Exception handler code:
    try_except_handler_6:;
    exception_keeper_type_8 = exception_type;
    exception_keeper_value_8 = exception_value;
    exception_keeper_tb_8 = exception_tb;
    exception_keeper_lineno_8 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_2__bases_orig);
    tmp_class_creation_2__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_2__bases);
    tmp_class_creation_2__bases = NULL;
    Py_XDECREF(tmp_class_creation_2__class_decl_dict);
    tmp_class_creation_2__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_2__metaclass);
    tmp_class_creation_2__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_2__prepared);
    tmp_class_creation_2__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_8;
    exception_value = exception_keeper_value_8;
    exception_tb = exception_keeper_tb_8;
    exception_lineno = exception_keeper_lineno_8;

    goto frame_exception_exit_1;
    // End of try:
    try_end_4:;
    CHECK_OBJECT(tmp_class_creation_2__bases_orig);
    Py_DECREF(tmp_class_creation_2__bases_orig);
    tmp_class_creation_2__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_2__bases);
    Py_DECREF(tmp_class_creation_2__bases);
    tmp_class_creation_2__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
    Py_DECREF(tmp_class_creation_2__class_decl_dict);
    tmp_class_creation_2__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_2__metaclass);
    Py_DECREF(tmp_class_creation_2__metaclass);
    tmp_class_creation_2__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_2__prepared);
    Py_DECREF(tmp_class_creation_2__prepared);
    tmp_class_creation_2__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_31;
        PyObject *tmp_tuple_element_9;
        tmp_tuple_element_9 = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[17]);

        if (unlikely(tmp_tuple_element_9 == NULL)) {
            tmp_tuple_element_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[17]);
        }

        if (tmp_tuple_element_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_assign_source_31 = MAKE_TUPLE_EMPTY(1);
        PyTuple_SET_ITEM0(tmp_assign_source_31, 0, tmp_tuple_element_9);
        assert(tmp_class_creation_3__bases_orig == NULL);
        tmp_class_creation_3__bases_orig = tmp_assign_source_31;
    }
    {
        PyObject *tmp_assign_source_32;
        PyObject *tmp_dircall_arg1_3;
        CHECK_OBJECT(tmp_class_creation_3__bases_orig);
        tmp_dircall_arg1_3 = tmp_class_creation_3__bases_orig;
        Py_INCREF(tmp_dircall_arg1_3);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_3};
            tmp_assign_source_32 = impl___main__$$$function__1__mro_entries_conversion(tstate, dir_call_args);
        }
        if (tmp_assign_source_32 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        assert(tmp_class_creation_3__bases == NULL);
        tmp_class_creation_3__bases = tmp_assign_source_32;
    }
    {
        PyObject *tmp_assign_source_33;
        tmp_assign_source_33 = MAKE_DICT_EMPTY();
        assert(tmp_class_creation_3__class_decl_dict == NULL);
        tmp_class_creation_3__class_decl_dict = tmp_assign_source_33;
    }
    {
        PyObject *tmp_assign_source_34;
        PyObject *tmp_metaclass_value_3;
        nuitka_bool tmp_condition_result_9;
        int tmp_truth_name_3;
        PyObject *tmp_type_arg_5;
        PyObject *tmp_expression_value_13;
        PyObject *tmp_subscript_value_3;
        PyObject *tmp_bases_value_3;
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_truth_name_3 = CHECK_IF_TRUE(tmp_class_creation_3__bases);
        if (tmp_truth_name_3 == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_condition_result_9 = tmp_truth_name_3 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_9 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_3;
        } else {
            goto condexpr_false_3;
        }
        condexpr_true_3:;
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_expression_value_13 = tmp_class_creation_3__bases;
        tmp_subscript_value_3 = mod_consts[24];
        tmp_type_arg_5 = LOOKUP_SUBSCRIPT_CONST(tstate, tmp_expression_value_13, tmp_subscript_value_3, 0);
        if (tmp_type_arg_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_metaclass_value_3 = BUILTIN_TYPE1(tmp_type_arg_5);
        Py_DECREF(tmp_type_arg_5);
        if (tmp_metaclass_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        goto condexpr_end_3;
        condexpr_false_3:;
        tmp_metaclass_value_3 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_3);
        condexpr_end_3:;
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_bases_value_3 = tmp_class_creation_3__bases;
        tmp_assign_source_34 = SELECT_METACLASS(tstate, tmp_metaclass_value_3, tmp_bases_value_3);
        Py_DECREF(tmp_metaclass_value_3);
        if (tmp_assign_source_34 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        assert(tmp_class_creation_3__metaclass == NULL);
        tmp_class_creation_3__metaclass = tmp_assign_source_34;
    }
    {
        bool tmp_condition_result_10;
        PyObject *tmp_expression_value_14;
        CHECK_OBJECT(tmp_class_creation_3__metaclass);
        tmp_expression_value_14 = tmp_class_creation_3__metaclass;
        tmp_res = HAS_ATTR_BOOL2(tstate, tmp_expression_value_14, mod_consts[104]);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_condition_result_10 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_10 != false) {
            goto branch_yes_7;
        } else {
            goto branch_no_7;
        }
    }
    branch_yes_7:;
    {
        PyObject *tmp_assign_source_35;
        PyObject *tmp_called_value_5;
        PyObject *tmp_expression_value_15;
        PyObject *tmp_args_value_5;
        PyObject *tmp_tuple_element_10;
        PyObject *tmp_kwargs_value_5;
        CHECK_OBJECT(tmp_class_creation_3__metaclass);
        tmp_expression_value_15 = tmp_class_creation_3__metaclass;
        tmp_called_value_5 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_15, mod_consts[104]);
        if (tmp_called_value_5 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_tuple_element_10 = mod_consts[117];
        tmp_args_value_5 = MAKE_TUPLE_EMPTY(2);
        PyTuple_SET_ITEM0(tmp_args_value_5, 0, tmp_tuple_element_10);
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_tuple_element_10 = tmp_class_creation_3__bases;
        PyTuple_SET_ITEM0(tmp_args_value_5, 1, tmp_tuple_element_10);
        CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
        tmp_kwargs_value_5 = tmp_class_creation_3__class_decl_dict;
        frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 220;
        tmp_assign_source_35 = CALL_FUNCTION(tstate, tmp_called_value_5, tmp_args_value_5, tmp_kwargs_value_5);
        Py_DECREF(tmp_called_value_5);
        Py_DECREF(tmp_args_value_5);
        if (tmp_assign_source_35 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        assert(tmp_class_creation_3__prepared == NULL);
        tmp_class_creation_3__prepared = tmp_assign_source_35;
    }
    {
        bool tmp_condition_result_11;
        PyObject *tmp_operand_value_3;
        PyObject *tmp_expression_value_16;
        CHECK_OBJECT(tmp_class_creation_3__prepared);
        tmp_expression_value_16 = tmp_class_creation_3__prepared;
        tmp_res = HAS_ATTR_BOOL2(tstate, tmp_expression_value_16, mod_consts[105]);
        if (tmp_res == -1) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_operand_value_3 = (tmp_res != 0) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_3);
        assert(!(tmp_res == -1));
        tmp_condition_result_11 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_11 != false) {
            goto branch_yes_8;
        } else {
            goto branch_no_8;
        }
    }
    branch_yes_8:;
    {
        PyObject *tmp_raise_type_3;
        PyObject *tmp_raise_value_3;
        PyObject *tmp_mod_expr_left_3;
        PyObject *tmp_mod_expr_right_3;
        PyObject *tmp_tuple_element_11;
        PyObject *tmp_expression_value_17;
        PyObject *tmp_name_value_6;
        PyObject *tmp_default_value_3;
        tmp_raise_type_3 = PyExc_TypeError;
        tmp_mod_expr_left_3 = mod_consts[106];
        CHECK_OBJECT(tmp_class_creation_3__metaclass);
        tmp_expression_value_17 = tmp_class_creation_3__metaclass;
        tmp_name_value_6 = mod_consts[107];
        tmp_default_value_3 = mod_consts[108];
        tmp_tuple_element_11 = BUILTIN_GETATTR(tstate, tmp_expression_value_17, tmp_name_value_6, tmp_default_value_3);
        if (tmp_tuple_element_11 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        tmp_mod_expr_right_3 = MAKE_TUPLE_EMPTY(2);
        {
            PyObject *tmp_expression_value_18;
            PyObject *tmp_type_arg_6;
            PyTuple_SET_ITEM(tmp_mod_expr_right_3, 0, tmp_tuple_element_11);
            CHECK_OBJECT(tmp_class_creation_3__prepared);
            tmp_type_arg_6 = tmp_class_creation_3__prepared;
            tmp_expression_value_18 = BUILTIN_TYPE1(tmp_type_arg_6);
            assert(!(tmp_expression_value_18 == NULL));
            tmp_tuple_element_11 = LOOKUP_ATTRIBUTE(tstate, tmp_expression_value_18, mod_consts[107]);
            Py_DECREF(tmp_expression_value_18);
            if (tmp_tuple_element_11 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 220;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_3, 1, tmp_tuple_element_11);
        }
        goto tuple_build_noexception_3;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_3:;
        Py_DECREF(tmp_mod_expr_right_3);
        goto try_except_handler_9;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_3:;
        tmp_raise_value_3 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_3, tmp_mod_expr_right_3);
        Py_DECREF(tmp_mod_expr_right_3);
        if (tmp_raise_value_3 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_9;
        }
        exception_type = tmp_raise_type_3;
        Py_INCREF(tmp_raise_type_3);
        exception_value = tmp_raise_value_3;
        exception_lineno = 220;
        RAISE_EXCEPTION_IMPLICIT(tstate, &exception_type, &exception_value, &exception_tb);

        goto try_except_handler_9;
    }
    branch_no_8:;
    goto branch_end_7;
    branch_no_7:;
    {
        PyObject *tmp_assign_source_36;
        tmp_assign_source_36 = MAKE_DICT_EMPTY();
        assert(tmp_class_creation_3__prepared == NULL);
        tmp_class_creation_3__prepared = tmp_assign_source_36;
    }
    branch_end_7:;
    {
        PyObject *tmp_assign_source_37;
        outline_2_var___class__ = Nuitka_Cell_Empty();
        {
            PyObject *tmp_set_locals_3;
            CHECK_OBJECT(tmp_class_creation_3__prepared);
            tmp_set_locals_3 = tmp_class_creation_3__prepared;
            locals_qt$components$bonuses$$$class__3_BonusesWidget_220 = tmp_set_locals_3;
            Py_INCREF(tmp_set_locals_3);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[109];
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__3_BonusesWidget_220, mod_consts[110], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_11;
        }
        tmp_dictset_value = mod_consts[117];
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__3_BonusesWidget_220, mod_consts[111], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_11;
        }
        frame_2c75e018e9ac1b4024c4dde109bbdf2c_4 = MAKE_CLASS_FRAME(tstate, codeobj_2c75e018e9ac1b4024c4dde109bbdf2c, module_qt$components$bonuses, NULL, sizeof(void *));

        // Push the new frame as the currently active one, and we should be exclusively
        // owning it.
        pushFrameStackCompiledFrame(tstate, frame_2c75e018e9ac1b4024c4dde109bbdf2c_4);
        assert(Py_REFCNT(frame_2c75e018e9ac1b4024c4dde109bbdf2c_4) == 2);

        // Framed code:
        {
            struct Nuitka_CellObject *tmp_closure_3[1];

            tmp_closure_3[0] = outline_2_var___class__;
            Py_INCREF(tmp_closure_3[0]);

            tmp_dictset_value = MAKE_FUNCTION_qt$components$bonuses$$$function__5___init__(tmp_closure_3);

            tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__3_BonusesWidget_220, mod_consts[1], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 221;
                type_description_2 = "c";
                goto frame_exception_exit_4;
            }
        }


        // Put the previous frame back on top.
        popFrameStack(tstate);

        goto frame_no_exception_3;
        frame_exception_exit_4:


        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_2c75e018e9ac1b4024c4dde109bbdf2c_4, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_2c75e018e9ac1b4024c4dde109bbdf2c_4->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_2c75e018e9ac1b4024c4dde109bbdf2c_4, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_2c75e018e9ac1b4024c4dde109bbdf2c_4,
            type_description_2,
            outline_2_var___class__
        );



        assertFrameObject(frame_2c75e018e9ac1b4024c4dde109bbdf2c_4);

        // Put the previous frame back on top.
        popFrameStack(tstate);

        // Return the error.
        goto nested_frame_exit_3;
        frame_no_exception_3:;
        goto skip_nested_handling_3;
        nested_frame_exit_3:;

        goto try_except_handler_11;
        skip_nested_handling_3:;
        {
            nuitka_bool tmp_condition_result_12;
            PyObject *tmp_cmp_expr_left_3;
            PyObject *tmp_cmp_expr_right_3;
            CHECK_OBJECT(tmp_class_creation_3__bases);
            tmp_cmp_expr_left_3 = tmp_class_creation_3__bases;
            CHECK_OBJECT(tmp_class_creation_3__bases_orig);
            tmp_cmp_expr_right_3 = tmp_class_creation_3__bases_orig;
            tmp_condition_result_12 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_3, tmp_cmp_expr_right_3);
            if (tmp_condition_result_12 == NUITKA_BOOL_EXCEPTION) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 220;

                goto try_except_handler_11;
            }
            if (tmp_condition_result_12 == NUITKA_BOOL_TRUE) {
                goto branch_yes_9;
            } else {
                goto branch_no_9;
            }
        }
        branch_yes_9:;
        CHECK_OBJECT(tmp_class_creation_3__bases_orig);
        tmp_dictset_value = tmp_class_creation_3__bases_orig;
        tmp_res = PyObject_SetItem(locals_qt$components$bonuses$$$class__3_BonusesWidget_220, mod_consts[113], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 220;

            goto try_except_handler_11;
        }
        branch_no_9:;
        {
            PyObject *tmp_assign_source_38;
            PyObject *tmp_called_value_6;
            PyObject *tmp_args_value_6;
            PyObject *tmp_tuple_element_12;
            PyObject *tmp_kwargs_value_6;
            CHECK_OBJECT(tmp_class_creation_3__metaclass);
            tmp_called_value_6 = tmp_class_creation_3__metaclass;
            tmp_tuple_element_12 = mod_consts[117];
            tmp_args_value_6 = MAKE_TUPLE_EMPTY(3);
            PyTuple_SET_ITEM0(tmp_args_value_6, 0, tmp_tuple_element_12);
            CHECK_OBJECT(tmp_class_creation_3__bases);
            tmp_tuple_element_12 = tmp_class_creation_3__bases;
            PyTuple_SET_ITEM0(tmp_args_value_6, 1, tmp_tuple_element_12);
            tmp_tuple_element_12 = locals_qt$components$bonuses$$$class__3_BonusesWidget_220;
            PyTuple_SET_ITEM0(tmp_args_value_6, 2, tmp_tuple_element_12);
            CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
            tmp_kwargs_value_6 = tmp_class_creation_3__class_decl_dict;
            frame_6bf2c041525e6e64362c99311da263cd->m_frame.f_lineno = 220;
            tmp_assign_source_38 = CALL_FUNCTION(tstate, tmp_called_value_6, tmp_args_value_6, tmp_kwargs_value_6);
            Py_DECREF(tmp_args_value_6);
            if (tmp_assign_source_38 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 220;

                goto try_except_handler_11;
            }
            assert(Nuitka_Cell_GET(outline_2_var___class__) == NULL);
            PyCell_SET(outline_2_var___class__, tmp_assign_source_38);

        }
        CHECK_OBJECT(Nuitka_Cell_GET(outline_2_var___class__));
        tmp_assign_source_37 = Nuitka_Cell_GET(outline_2_var___class__);
        Py_INCREF(tmp_assign_source_37);
        goto try_return_handler_11;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_11:;
        Py_DECREF(locals_qt$components$bonuses$$$class__3_BonusesWidget_220);
        locals_qt$components$bonuses$$$class__3_BonusesWidget_220 = NULL;
        goto try_return_handler_10;
        // Exception handler code:
        try_except_handler_11:;
        exception_keeper_type_9 = exception_type;
        exception_keeper_value_9 = exception_value;
        exception_keeper_tb_9 = exception_tb;
        exception_keeper_lineno_9 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_qt$components$bonuses$$$class__3_BonusesWidget_220);
        locals_qt$components$bonuses$$$class__3_BonusesWidget_220 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_9;
        exception_value = exception_keeper_value_9;
        exception_tb = exception_keeper_tb_9;
        exception_lineno = exception_keeper_lineno_9;

        goto try_except_handler_10;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_10:;
        CHECK_OBJECT(outline_2_var___class__);
        Py_DECREF(outline_2_var___class__);
        outline_2_var___class__ = NULL;
        goto outline_result_3;
        // Exception handler code:
        try_except_handler_10:;
        exception_keeper_type_10 = exception_type;
        exception_keeper_value_10 = exception_value;
        exception_keeper_tb_10 = exception_tb;
        exception_keeper_lineno_10 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_10;
        exception_value = exception_keeper_value_10;
        exception_tb = exception_keeper_tb_10;
        exception_lineno = exception_keeper_lineno_10;

        goto outline_exception_3;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_3:;
        exception_lineno = 220;
        goto try_except_handler_9;
        outline_result_3:;
        UPDATE_STRING_DICT1(moduledict_qt$components$bonuses, (Nuitka_StringObject *)mod_consts[117], tmp_assign_source_37);
    }
    goto try_end_5;
    // Exception handler code:
    try_except_handler_9:;
    exception_keeper_type_11 = exception_type;
    exception_keeper_value_11 = exception_value;
    exception_keeper_tb_11 = exception_tb;
    exception_keeper_lineno_11 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_3__bases_orig);
    tmp_class_creation_3__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_3__bases);
    tmp_class_creation_3__bases = NULL;
    Py_XDECREF(tmp_class_creation_3__class_decl_dict);
    tmp_class_creation_3__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_3__metaclass);
    tmp_class_creation_3__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_3__prepared);
    tmp_class_creation_3__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_11;
    exception_value = exception_keeper_value_11;
    exception_tb = exception_keeper_tb_11;
    exception_lineno = exception_keeper_lineno_11;

    goto frame_exception_exit_1;
    // End of try:
    try_end_5:;


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_4;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_6bf2c041525e6e64362c99311da263cd, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_6bf2c041525e6e64362c99311da263cd->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_6bf2c041525e6e64362c99311da263cd, exception_lineno);
    }



    assertFrameObject(frame_6bf2c041525e6e64362c99311da263cd);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_4:;
    CHECK_OBJECT(tmp_class_creation_3__bases_orig);
    Py_DECREF(tmp_class_creation_3__bases_orig);
    tmp_class_creation_3__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_3__bases);
    Py_DECREF(tmp_class_creation_3__bases);
    tmp_class_creation_3__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
    Py_DECREF(tmp_class_creation_3__class_decl_dict);
    tmp_class_creation_3__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_3__metaclass);
    Py_DECREF(tmp_class_creation_3__metaclass);
    tmp_class_creation_3__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_3__prepared);
    Py_DECREF(tmp_class_creation_3__prepared);
    tmp_class_creation_3__prepared = NULL;

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("qt$components$bonuses", false);

    Py_INCREF(module_qt$components$bonuses);
    return module_qt$components$bonuses;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_qt$components$bonuses, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(tstate, module_name);
        }
    }
#endif
    PGO_onModuleExit("qt$components$bonuses", false);

    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);
    return NULL;
}
