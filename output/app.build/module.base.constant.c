/* Generated code for Python module 'base$constant'
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

/* The "module_base$constant" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_base$constant;
PyDictObject *moduledict_base$constant;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[77];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[77];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(PyThreadState *tstate) {
    if (constants_created == false) {
        loadConstantsBlob(tstate, &mod_consts[0], UNTRANSLATE("base.constant"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 77; i++) {
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
void checkModuleConstants_base$constant(PyThreadState *tstate) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 77; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(tstate, mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_6788ba1ae737446e4c049b14b00919e9;
static PyCodeObject *codeobj_bc238783b14422bc6b8a8477e29996fa;
static PyCodeObject *codeobj_6e366a4aa886166102dfea59e5f4cb81;
static PyCodeObject *codeobj_5ff212778e89cd38a404e600d79280e6;
static PyCodeObject *codeobj_8dfd58ee1ded31ac573e0c35fead28a2;
static PyCodeObject *codeobj_ea279ac63e3e532e56c66f20179feae3;
static PyCodeObject *codeobj_8fc1fc7d73097e7d1e8566fd2c8e5d9f;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[72]); CHECK_OBJECT(module_filename_obj);
    codeobj_6788ba1ae737446e4c049b14b00919e9 = MAKE_CODE_OBJECT(module_filename_obj, 1, 0, mod_consts[73], mod_consts[73], NULL, NULL, 0, 0, 0);
    codeobj_bc238783b14422bc6b8a8477e29996fa = MAKE_CODE_OBJECT(module_filename_obj, 60, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[5], mod_consts[5], mod_consts[74], NULL, 1, 0, 0);
    codeobj_6e366a4aa886166102dfea59e5f4cb81 = MAKE_CODE_OBJECT(module_filename_obj, 64, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[69], mod_consts[69], mod_consts[75], NULL, 2, 0, 0);
    codeobj_5ff212778e89cd38a404e600d79280e6 = MAKE_CODE_OBJECT(module_filename_obj, 52, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[2], mod_consts[2], mod_consts[74], NULL, 1, 0, 0);
    codeobj_8dfd58ee1ded31ac573e0c35fead28a2 = MAKE_CODE_OBJECT(module_filename_obj, 56, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[68], mod_consts[68], mod_consts[75], NULL, 2, 0, 0);
    codeobj_ea279ac63e3e532e56c66f20179feae3 = MAKE_CODE_OBJECT(module_filename_obj, 72, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[71], mod_consts[71], mod_consts[74], NULL, 1, 0, 0);
    codeobj_8fc1fc7d73097e7d1e8566fd2c8e5d9f = MAKE_CODE_OBJECT(module_filename_obj, 68, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[70], mod_consts[70], mod_consts[74], NULL, 1, 0, 0);
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_base$constant$$$function__1_PHYSICAL_ATTACK_POWER_COF();


static PyObject *MAKE_FUNCTION_base$constant$$$function__2_PHYSICAL_DOT_ATTACK_POWER_COF();


static PyObject *MAKE_FUNCTION_base$constant$$$function__3_MAGICAL_ATTACK_POWER_COF();


static PyObject *MAKE_FUNCTION_base$constant$$$function__4_MAGICAL_DOT_ATTACK_POWER_COF();


static PyObject *MAKE_FUNCTION_base$constant$$$function__5_WEAPON_DAMAGE_COF();


static PyObject *MAKE_FUNCTION_base$constant$$$function__6_SURPLUS_COF();


// The module function definitions.
static PyObject *impl_base$constant$$$function__1_PHYSICAL_ATTACK_POWER_COF(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_cof = python_pars[0];
    struct Nuitka_FrameObject *frame_5ff212778e89cd38a404e600d79280e6;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_5ff212778e89cd38a404e600d79280e6 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_5ff212778e89cd38a404e600d79280e6)) {
        Py_XDECREF(cache_frame_5ff212778e89cd38a404e600d79280e6);

#if _DEBUG_REFCOUNTS
        if (cache_frame_5ff212778e89cd38a404e600d79280e6 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_5ff212778e89cd38a404e600d79280e6 = MAKE_FUNCTION_FRAME(tstate, codeobj_5ff212778e89cd38a404e600d79280e6, module_base$constant, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_5ff212778e89cd38a404e600d79280e6->m_type_description == NULL);
    frame_5ff212778e89cd38a404e600d79280e6 = cache_frame_5ff212778e89cd38a404e600d79280e6;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_5ff212778e89cd38a404e600d79280e6);
    assert(Py_REFCNT(frame_5ff212778e89cd38a404e600d79280e6) == 2);

    // Framed code:
    {
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        PyObject *tmp_truediv_expr_left_2;
        PyObject *tmp_truediv_expr_right_2;
        CHECK_OBJECT(par_cof);
        tmp_truediv_expr_left_2 = par_cof;
        tmp_truediv_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[0]);

        if (unlikely(tmp_truediv_expr_right_2 == NULL)) {
            tmp_truediv_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[0]);
        }

        if (tmp_truediv_expr_right_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 53;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_left_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_2, tmp_truediv_expr_right_2);
        if (tmp_truediv_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 53;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[1]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[1]);
        }

        if (tmp_truediv_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_1);

            exception_lineno = 53;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_return_value = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        Py_DECREF(tmp_truediv_expr_left_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 53;
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
        exception_tb = MAKE_TRACEBACK(frame_5ff212778e89cd38a404e600d79280e6, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_5ff212778e89cd38a404e600d79280e6->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_5ff212778e89cd38a404e600d79280e6, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_5ff212778e89cd38a404e600d79280e6,
        type_description_1,
        par_cof
    );


    // Release cached frame if used for exception.
    if (frame_5ff212778e89cd38a404e600d79280e6 == cache_frame_5ff212778e89cd38a404e600d79280e6) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_5ff212778e89cd38a404e600d79280e6);
        cache_frame_5ff212778e89cd38a404e600d79280e6 = NULL;
    }

    assertFrameObject(frame_5ff212778e89cd38a404e600d79280e6);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_base$constant$$$function__2_PHYSICAL_DOT_ATTACK_POWER_COF(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_cof = python_pars[0];
    PyObject *par_interval = python_pars[1];
    struct Nuitka_FrameObject *frame_8dfd58ee1ded31ac573e0c35fead28a2;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_8dfd58ee1ded31ac573e0c35fead28a2 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_8dfd58ee1ded31ac573e0c35fead28a2)) {
        Py_XDECREF(cache_frame_8dfd58ee1ded31ac573e0c35fead28a2);

#if _DEBUG_REFCOUNTS
        if (cache_frame_8dfd58ee1ded31ac573e0c35fead28a2 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_8dfd58ee1ded31ac573e0c35fead28a2 = MAKE_FUNCTION_FRAME(tstate, codeobj_8dfd58ee1ded31ac573e0c35fead28a2, module_base$constant, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_8dfd58ee1ded31ac573e0c35fead28a2->m_type_description == NULL);
    frame_8dfd58ee1ded31ac573e0c35fead28a2 = cache_frame_8dfd58ee1ded31ac573e0c35fead28a2;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_8dfd58ee1ded31ac573e0c35fead28a2);
    assert(Py_REFCNT(frame_8dfd58ee1ded31ac573e0c35fead28a2) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        PyObject *tmp_truediv_expr_left_2;
        PyObject *tmp_truediv_expr_right_2;
        PyObject *tmp_mult_expr_left_1;
        PyObject *tmp_mult_expr_right_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[2]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[2]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 57;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_cof);
        tmp_mult_expr_left_1 = par_cof;
        CHECK_OBJECT(par_interval);
        tmp_mult_expr_right_1 = par_interval;
        tmp_truediv_expr_left_2 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_left_1, tmp_mult_expr_right_1);
        if (tmp_truediv_expr_left_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 57;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[0]);

        if (unlikely(tmp_truediv_expr_right_2 == NULL)) {
            tmp_truediv_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[0]);
        }

        if (tmp_truediv_expr_right_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_2);

            exception_lineno = 57;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_left_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_2, tmp_truediv_expr_right_2);
        Py_DECREF(tmp_truediv_expr_left_2);
        if (tmp_truediv_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 57;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[3]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[3]);
        }

        if (tmp_truediv_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_1);

            exception_lineno = 57;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        Py_DECREF(tmp_truediv_expr_left_1);
        if (tmp_args_element_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 57;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        frame_8dfd58ee1ded31ac573e0c35fead28a2->m_frame.f_lineno = 57;
        tmp_return_value = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 57;
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
        exception_tb = MAKE_TRACEBACK(frame_8dfd58ee1ded31ac573e0c35fead28a2, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_8dfd58ee1ded31ac573e0c35fead28a2->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_8dfd58ee1ded31ac573e0c35fead28a2, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_8dfd58ee1ded31ac573e0c35fead28a2,
        type_description_1,
        par_cof,
        par_interval
    );


    // Release cached frame if used for exception.
    if (frame_8dfd58ee1ded31ac573e0c35fead28a2 == cache_frame_8dfd58ee1ded31ac573e0c35fead28a2) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_8dfd58ee1ded31ac573e0c35fead28a2);
        cache_frame_8dfd58ee1ded31ac573e0c35fead28a2 = NULL;
    }

    assertFrameObject(frame_8dfd58ee1ded31ac573e0c35fead28a2);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    CHECK_OBJECT(par_interval);
    Py_DECREF(par_interval);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    CHECK_OBJECT(par_interval);
    Py_DECREF(par_interval);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_base$constant$$$function__3_MAGICAL_ATTACK_POWER_COF(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_cof = python_pars[0];
    struct Nuitka_FrameObject *frame_bc238783b14422bc6b8a8477e29996fa;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_bc238783b14422bc6b8a8477e29996fa = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_bc238783b14422bc6b8a8477e29996fa)) {
        Py_XDECREF(cache_frame_bc238783b14422bc6b8a8477e29996fa);

#if _DEBUG_REFCOUNTS
        if (cache_frame_bc238783b14422bc6b8a8477e29996fa == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_bc238783b14422bc6b8a8477e29996fa = MAKE_FUNCTION_FRAME(tstate, codeobj_bc238783b14422bc6b8a8477e29996fa, module_base$constant, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_bc238783b14422bc6b8a8477e29996fa->m_type_description == NULL);
    frame_bc238783b14422bc6b8a8477e29996fa = cache_frame_bc238783b14422bc6b8a8477e29996fa;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_bc238783b14422bc6b8a8477e29996fa);
    assert(Py_REFCNT(frame_bc238783b14422bc6b8a8477e29996fa) == 2);

    // Framed code:
    {
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        PyObject *tmp_truediv_expr_left_2;
        PyObject *tmp_truediv_expr_right_2;
        CHECK_OBJECT(par_cof);
        tmp_truediv_expr_left_2 = par_cof;
        tmp_truediv_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[0]);

        if (unlikely(tmp_truediv_expr_right_2 == NULL)) {
            tmp_truediv_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[0]);
        }

        if (tmp_truediv_expr_right_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 61;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_left_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_2, tmp_truediv_expr_right_2);
        if (tmp_truediv_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 61;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[4]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[4]);
        }

        if (tmp_truediv_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_1);

            exception_lineno = 61;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_return_value = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        Py_DECREF(tmp_truediv_expr_left_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 61;
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
        exception_tb = MAKE_TRACEBACK(frame_bc238783b14422bc6b8a8477e29996fa, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_bc238783b14422bc6b8a8477e29996fa->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_bc238783b14422bc6b8a8477e29996fa, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_bc238783b14422bc6b8a8477e29996fa,
        type_description_1,
        par_cof
    );


    // Release cached frame if used for exception.
    if (frame_bc238783b14422bc6b8a8477e29996fa == cache_frame_bc238783b14422bc6b8a8477e29996fa) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_bc238783b14422bc6b8a8477e29996fa);
        cache_frame_bc238783b14422bc6b8a8477e29996fa = NULL;
    }

    assertFrameObject(frame_bc238783b14422bc6b8a8477e29996fa);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_base$constant$$$function__4_MAGICAL_DOT_ATTACK_POWER_COF(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_cof = python_pars[0];
    PyObject *par_interval = python_pars[1];
    struct Nuitka_FrameObject *frame_6e366a4aa886166102dfea59e5f4cb81;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_6e366a4aa886166102dfea59e5f4cb81 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_6e366a4aa886166102dfea59e5f4cb81)) {
        Py_XDECREF(cache_frame_6e366a4aa886166102dfea59e5f4cb81);

#if _DEBUG_REFCOUNTS
        if (cache_frame_6e366a4aa886166102dfea59e5f4cb81 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_6e366a4aa886166102dfea59e5f4cb81 = MAKE_FUNCTION_FRAME(tstate, codeobj_6e366a4aa886166102dfea59e5f4cb81, module_base$constant, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_6e366a4aa886166102dfea59e5f4cb81->m_type_description == NULL);
    frame_6e366a4aa886166102dfea59e5f4cb81 = cache_frame_6e366a4aa886166102dfea59e5f4cb81;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_6e366a4aa886166102dfea59e5f4cb81);
    assert(Py_REFCNT(frame_6e366a4aa886166102dfea59e5f4cb81) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        PyObject *tmp_truediv_expr_left_2;
        PyObject *tmp_truediv_expr_right_2;
        PyObject *tmp_mult_expr_left_1;
        PyObject *tmp_mult_expr_right_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[5]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_cof);
        tmp_mult_expr_left_1 = par_cof;
        CHECK_OBJECT(par_interval);
        tmp_mult_expr_right_1 = par_interval;
        tmp_truediv_expr_left_2 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_left_1, tmp_mult_expr_right_1);
        if (tmp_truediv_expr_left_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[0]);

        if (unlikely(tmp_truediv_expr_right_2 == NULL)) {
            tmp_truediv_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[0]);
        }

        if (tmp_truediv_expr_right_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_2);

            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_left_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_2, tmp_truediv_expr_right_2);
        Py_DECREF(tmp_truediv_expr_left_2);
        if (tmp_truediv_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[3]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[3]);
        }

        if (tmp_truediv_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_1);

            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_args_element_value_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        Py_DECREF(tmp_truediv_expr_left_1);
        if (tmp_args_element_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        frame_6e366a4aa886166102dfea59e5f4cb81->m_frame.f_lineno = 65;
        tmp_return_value = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
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
        exception_tb = MAKE_TRACEBACK(frame_6e366a4aa886166102dfea59e5f4cb81, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_6e366a4aa886166102dfea59e5f4cb81->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_6e366a4aa886166102dfea59e5f4cb81, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_6e366a4aa886166102dfea59e5f4cb81,
        type_description_1,
        par_cof,
        par_interval
    );


    // Release cached frame if used for exception.
    if (frame_6e366a4aa886166102dfea59e5f4cb81 == cache_frame_6e366a4aa886166102dfea59e5f4cb81) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_6e366a4aa886166102dfea59e5f4cb81);
        cache_frame_6e366a4aa886166102dfea59e5f4cb81 = NULL;
    }

    assertFrameObject(frame_6e366a4aa886166102dfea59e5f4cb81);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    CHECK_OBJECT(par_interval);
    Py_DECREF(par_interval);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    CHECK_OBJECT(par_interval);
    Py_DECREF(par_interval);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_base$constant$$$function__5_WEAPON_DAMAGE_COF(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_cof = python_pars[0];
    struct Nuitka_FrameObject *frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f)) {
        Py_XDECREF(cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f);

#if _DEBUG_REFCOUNTS
        if (cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f = MAKE_FUNCTION_FRAME(tstate, codeobj_8fc1fc7d73097e7d1e8566fd2c8e5d9f, module_base$constant, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f->m_type_description == NULL);
    frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f = cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f);
    assert(Py_REFCNT(frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f) == 2);

    // Framed code:
    {
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        CHECK_OBJECT(par_cof);
        tmp_truediv_expr_left_1 = par_cof;
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        if (tmp_truediv_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 69;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_return_value = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 69;
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
        exception_tb = MAKE_TRACEBACK(frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f,
        type_description_1,
        par_cof
    );


    // Release cached frame if used for exception.
    if (frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f == cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f);
        cache_frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f = NULL;
    }

    assertFrameObject(frame_8fc1fc7d73097e7d1e8566fd2c8e5d9f);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_base$constant$$$function__6_SURPLUS_COF(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_cof = python_pars[0];
    struct Nuitka_FrameObject *frame_ea279ac63e3e532e56c66f20179feae3;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_ea279ac63e3e532e56c66f20179feae3 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_ea279ac63e3e532e56c66f20179feae3)) {
        Py_XDECREF(cache_frame_ea279ac63e3e532e56c66f20179feae3);

#if _DEBUG_REFCOUNTS
        if (cache_frame_ea279ac63e3e532e56c66f20179feae3 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_ea279ac63e3e532e56c66f20179feae3 = MAKE_FUNCTION_FRAME(tstate, codeobj_ea279ac63e3e532e56c66f20179feae3, module_base$constant, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_ea279ac63e3e532e56c66f20179feae3->m_type_description == NULL);
    frame_ea279ac63e3e532e56c66f20179feae3 = cache_frame_ea279ac63e3e532e56c66f20179feae3;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_ea279ac63e3e532e56c66f20179feae3);
    assert(Py_REFCNT(frame_ea279ac63e3e532e56c66f20179feae3) == 2);

    // Framed code:
    {
        PyObject *tmp_mult_expr_left_1;
        PyObject *tmp_mult_expr_right_1;
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        PyObject *tmp_add_expr_left_1;
        PyObject *tmp_add_expr_right_1;
        PyObject *tmp_truediv_expr_left_2;
        PyObject *tmp_truediv_expr_right_2;
        PyObject *tmp_add_expr_left_2;
        PyObject *tmp_add_expr_right_2;
        PyObject *tmp_int_arg_1;
        PyObject *tmp_cmp_expr_left_1;
        PyObject *tmp_cmp_expr_right_1;
        CHECK_OBJECT(par_cof);
        tmp_add_expr_left_2 = par_cof;
        CHECK_OBJECT(par_cof);
        tmp_cmp_expr_left_1 = par_cof;
        tmp_cmp_expr_right_1 = mod_consts[7];
        tmp_int_arg_1 = RICH_COMPARE_LT_OBJECT_OBJECT_LONG(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
        if (tmp_int_arg_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_add_expr_right_2 = PyNumber_Int(tmp_int_arg_1);
        Py_DECREF(tmp_int_arg_1);
        if (tmp_add_expr_right_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_left_2 = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_add_expr_left_2, tmp_add_expr_right_2);
        Py_DECREF(tmp_add_expr_right_2);
        if (tmp_truediv_expr_left_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_2 == NULL)) {
            tmp_truediv_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        if (tmp_truediv_expr_right_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_2);

            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_add_expr_left_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_2, tmp_truediv_expr_right_2);
        Py_DECREF(tmp_truediv_expr_left_2);
        if (tmp_add_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_add_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_add_expr_right_1 == NULL)) {
            tmp_add_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        if (tmp_add_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_add_expr_left_1);

            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_left_1 = BINARY_OPERATION_ADD_OBJECT_OBJECT_OBJECT(tmp_add_expr_left_1, tmp_add_expr_right_1);
        Py_DECREF(tmp_add_expr_left_1);
        if (tmp_truediv_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        if (tmp_truediv_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_truediv_expr_left_1);

            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_mult_expr_left_1 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        Py_DECREF(tmp_truediv_expr_left_1);
        if (tmp_mult_expr_left_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_mult_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[8]);

        if (unlikely(tmp_mult_expr_right_1 == NULL)) {
            tmp_mult_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[8]);
        }

        if (tmp_mult_expr_right_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_mult_expr_left_1);

            exception_lineno = 73;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_return_value = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_left_1, tmp_mult_expr_right_1);
        Py_DECREF(tmp_mult_expr_left_1);
        if (tmp_return_value == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 73;
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
        exception_tb = MAKE_TRACEBACK(frame_ea279ac63e3e532e56c66f20179feae3, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_ea279ac63e3e532e56c66f20179feae3->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_ea279ac63e3e532e56c66f20179feae3, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_ea279ac63e3e532e56c66f20179feae3,
        type_description_1,
        par_cof
    );


    // Release cached frame if used for exception.
    if (frame_ea279ac63e3e532e56c66f20179feae3 == cache_frame_ea279ac63e3e532e56c66f20179feae3) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_ea279ac63e3e532e56c66f20179feae3);
        cache_frame_ea279ac63e3e532e56c66f20179feae3 = NULL;
    }

    assertFrameObject(frame_ea279ac63e3e532e56c66f20179feae3);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_cof);
    Py_DECREF(par_cof);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}



static PyObject *MAKE_FUNCTION_base$constant$$$function__1_PHYSICAL_ATTACK_POWER_COF() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_base$constant$$$function__1_PHYSICAL_ATTACK_POWER_COF,
        mod_consts[2],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_5ff212778e89cd38a404e600d79280e6,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_base$constant,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_base$constant$$$function__2_PHYSICAL_DOT_ATTACK_POWER_COF() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_base$constant$$$function__2_PHYSICAL_DOT_ATTACK_POWER_COF,
        mod_consts[68],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_8dfd58ee1ded31ac573e0c35fead28a2,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_base$constant,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_base$constant$$$function__3_MAGICAL_ATTACK_POWER_COF() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_base$constant$$$function__3_MAGICAL_ATTACK_POWER_COF,
        mod_consts[5],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_bc238783b14422bc6b8a8477e29996fa,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_base$constant,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_base$constant$$$function__4_MAGICAL_DOT_ATTACK_POWER_COF() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_base$constant$$$function__4_MAGICAL_DOT_ATTACK_POWER_COF,
        mod_consts[69],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_6e366a4aa886166102dfea59e5f4cb81,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_base$constant,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_base$constant$$$function__5_WEAPON_DAMAGE_COF() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_base$constant$$$function__5_WEAPON_DAMAGE_COF,
        mod_consts[70],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_8fc1fc7d73097e7d1e8566fd2c8e5d9f,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_base$constant,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_base$constant$$$function__6_SURPLUS_COF() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_base$constant$$$function__6_SURPLUS_COF,
        mod_consts[71],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_ea279ac63e3e532e56c66f20179feae3,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_base$constant,
        NULL,
        NULL,
        0
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

static function_impl_code const function_table_base$constant[] = {
    impl_base$constant$$$function__1_PHYSICAL_ATTACK_POWER_COF,
    impl_base$constant$$$function__2_PHYSICAL_DOT_ATTACK_POWER_COF,
    impl_base$constant$$$function__3_MAGICAL_ATTACK_POWER_COF,
    impl_base$constant$$$function__4_MAGICAL_DOT_ATTACK_POWER_COF,
    impl_base$constant$$$function__5_WEAPON_DAMAGE_COF,
    impl_base$constant$$$function__6_SURPLUS_COF,
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

    int offset = Nuitka_Function_GetFunctionCodeIndex(function, function_table_base$constant);

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
        module_base$constant,
        function_qualname,
        function_index,
        code_object_desc,
        constant_return_value,
        defaults,
        kw_defaults,
        doc,
        function_table_base$constant,
        sizeof(function_table_base$constant) / sizeof(function_impl_code)
    );
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_base$constant(PyThreadState *tstate, PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("base$constant");

    // Store the module for future use.
    module_base$constant = module;

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
        PRINT_STRING("base$constant: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader(tstate);

#if PYTHON_VERSION >= 0x300
        patchInspectModule(tstate);
#endif

#endif

        /* The constants only used by this module are created now. */
        NUITKA_PRINT_TRACE("base$constant: Calling createModuleConstants().\n");
        createModuleConstants(tstate);

        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initbase$constant\n");

    moduledict_base$constant = MODULE_DICT(module_base$constant);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    {
        char const *module_name_c;
        if (loader_entry != NULL) {
            module_name_c = loader_entry->name;
        } else {
            PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___name__);
            module_name_c = Nuitka_String_AsString(module_name);
        }

        registerDillPluginTables(tstate, module_name_c, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
    }




#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_base$constant,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_base$constant,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[76]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_base$constant,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_base$constant,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_base$constant,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_base$constant);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

    UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, _spec_from_module, module_base$constant);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(tstate, spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_FrameObject *frame_6788ba1ae737446e4c049b14b00919e9;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[9], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[10], tmp_assign_source_2);
    }
    frame_6788ba1ae737446e4c049b14b00919e9 = MAKE_MODULE_FRAME(codeobj_6788ba1ae737446e4c049b14b00919e9, module_base$constant);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_6788ba1ae737446e4c049b14b00919e9);
    assert(Py_REFCNT(frame_6788ba1ae737446e4c049b14b00919e9) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[11]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[11]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_1, mod_consts[12], tmp_assattr_value_1);
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
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[11]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[11]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_2, mod_consts[13], tmp_assattr_value_2);
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
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = mod_consts[15];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        tmp_assign_source_5 = mod_consts[16];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        tmp_assign_source_6 = mod_consts[17];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[18], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        tmp_assign_source_7 = mod_consts[19];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[20], tmp_assign_source_7);
    }
    {
        PyObject *tmp_assign_source_8;
        tmp_assign_source_8 = mod_consts[21];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[22], tmp_assign_source_8);
    }
    {
        PyObject *tmp_assign_source_9;
        tmp_assign_source_9 = mod_consts[23];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[24], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;
        tmp_assign_source_10 = mod_consts[25];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[3], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;
        tmp_assign_source_11 = mod_consts[26];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;
        tmp_assign_source_12 = mod_consts[25];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[4], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;
        tmp_assign_source_13 = mod_consts[26];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[27], tmp_assign_source_13);
    }
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_mult_expr_left_1;
        PyObject *tmp_mult_expr_right_1;
        PyObject *tmp_sub_expr_left_1;
        PyObject *tmp_sub_expr_right_1;
        PyObject *tmp_mult_expr_left_2;
        PyObject *tmp_mult_expr_right_2;
        tmp_mult_expr_left_1 = mod_consts[28];
        tmp_mult_expr_left_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[20]);

        if (unlikely(tmp_mult_expr_left_2 == NULL)) {
            tmp_mult_expr_left_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
        }

        assert(!(tmp_mult_expr_left_2 == NULL));
        tmp_mult_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_mult_expr_right_2 == NULL)) {
            tmp_mult_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        assert(!(tmp_mult_expr_right_2 == NULL));
        tmp_sub_expr_left_1 = BINARY_OPERATION_MULT_OBJECT_LONG_LONG(tmp_mult_expr_left_2, tmp_mult_expr_right_2);
        assert(!(tmp_sub_expr_left_1 == NULL));
        tmp_sub_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[22]);

        if (unlikely(tmp_sub_expr_right_1 == NULL)) {
            tmp_sub_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[22]);
        }

        assert(!(tmp_sub_expr_right_1 == NULL));
        tmp_mult_expr_right_1 = BINARY_OPERATION_SUB_OBJECT_LONG_LONG(tmp_sub_expr_left_1, tmp_sub_expr_right_1);
        Py_DECREF(tmp_sub_expr_left_1);
        assert(!(tmp_mult_expr_right_1 == NULL));
        tmp_assign_source_14 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_right_1, tmp_mult_expr_left_1);
        Py_DECREF(tmp_mult_expr_right_1);
        assert(!(tmp_assign_source_14 == NULL));
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[29], tmp_assign_source_14);
    }
    {
        PyObject *tmp_assign_source_15;
        PyObject *tmp_mult_expr_left_3;
        PyObject *tmp_mult_expr_right_3;
        PyObject *tmp_sub_expr_left_2;
        PyObject *tmp_sub_expr_right_2;
        PyObject *tmp_mult_expr_left_4;
        PyObject *tmp_mult_expr_right_4;
        tmp_mult_expr_left_3 = mod_consts[30];
        tmp_mult_expr_left_4 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[20]);

        if (unlikely(tmp_mult_expr_left_4 == NULL)) {
            tmp_mult_expr_left_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
        }

        assert(!(tmp_mult_expr_left_4 == NULL));
        tmp_mult_expr_right_4 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_mult_expr_right_4 == NULL)) {
            tmp_mult_expr_right_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        assert(!(tmp_mult_expr_right_4 == NULL));
        tmp_sub_expr_left_2 = BINARY_OPERATION_MULT_OBJECT_LONG_LONG(tmp_mult_expr_left_4, tmp_mult_expr_right_4);
        assert(!(tmp_sub_expr_left_2 == NULL));
        tmp_sub_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[22]);

        if (unlikely(tmp_sub_expr_right_2 == NULL)) {
            tmp_sub_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[22]);
        }

        assert(!(tmp_sub_expr_right_2 == NULL));
        tmp_mult_expr_right_3 = BINARY_OPERATION_SUB_OBJECT_LONG_LONG(tmp_sub_expr_left_2, tmp_sub_expr_right_2);
        Py_DECREF(tmp_sub_expr_left_2);
        assert(!(tmp_mult_expr_right_3 == NULL));
        tmp_assign_source_15 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_right_3, tmp_mult_expr_left_3);
        Py_DECREF(tmp_mult_expr_right_3);
        assert(!(tmp_assign_source_15 == NULL));
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[31], tmp_assign_source_15);
    }
    {
        PyObject *tmp_assign_source_16;
        PyObject *tmp_mult_expr_left_5;
        PyObject *tmp_mult_expr_right_5;
        PyObject *tmp_sub_expr_left_3;
        PyObject *tmp_sub_expr_right_3;
        PyObject *tmp_mult_expr_left_6;
        PyObject *tmp_mult_expr_right_6;
        tmp_mult_expr_left_5 = mod_consts[28];
        tmp_mult_expr_left_6 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[20]);

        if (unlikely(tmp_mult_expr_left_6 == NULL)) {
            tmp_mult_expr_left_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
        }

        assert(!(tmp_mult_expr_left_6 == NULL));
        tmp_mult_expr_right_6 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_mult_expr_right_6 == NULL)) {
            tmp_mult_expr_right_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        assert(!(tmp_mult_expr_right_6 == NULL));
        tmp_sub_expr_left_3 = BINARY_OPERATION_MULT_OBJECT_LONG_LONG(tmp_mult_expr_left_6, tmp_mult_expr_right_6);
        assert(!(tmp_sub_expr_left_3 == NULL));
        tmp_sub_expr_right_3 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[22]);

        if (unlikely(tmp_sub_expr_right_3 == NULL)) {
            tmp_sub_expr_right_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[22]);
        }

        assert(!(tmp_sub_expr_right_3 == NULL));
        tmp_mult_expr_right_5 = BINARY_OPERATION_SUB_OBJECT_LONG_LONG(tmp_sub_expr_left_3, tmp_sub_expr_right_3);
        Py_DECREF(tmp_sub_expr_left_3);
        assert(!(tmp_mult_expr_right_5 == NULL));
        tmp_assign_source_16 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_right_5, tmp_mult_expr_left_5);
        Py_DECREF(tmp_mult_expr_right_5);
        assert(!(tmp_assign_source_16 == NULL));
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[32], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;
        PyObject *tmp_mult_expr_left_7;
        PyObject *tmp_mult_expr_right_7;
        PyObject *tmp_sub_expr_left_4;
        PyObject *tmp_sub_expr_right_4;
        PyObject *tmp_mult_expr_left_8;
        PyObject *tmp_mult_expr_right_8;
        tmp_mult_expr_left_7 = mod_consts[33];
        tmp_mult_expr_left_8 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[20]);

        if (unlikely(tmp_mult_expr_left_8 == NULL)) {
            tmp_mult_expr_left_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
        }

        assert(!(tmp_mult_expr_left_8 == NULL));
        tmp_mult_expr_right_8 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_mult_expr_right_8 == NULL)) {
            tmp_mult_expr_right_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        assert(!(tmp_mult_expr_right_8 == NULL));
        tmp_sub_expr_left_4 = BINARY_OPERATION_MULT_OBJECT_LONG_LONG(tmp_mult_expr_left_8, tmp_mult_expr_right_8);
        assert(!(tmp_sub_expr_left_4 == NULL));
        tmp_sub_expr_right_4 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[22]);

        if (unlikely(tmp_sub_expr_right_4 == NULL)) {
            tmp_sub_expr_right_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[22]);
        }

        assert(!(tmp_sub_expr_right_4 == NULL));
        tmp_mult_expr_right_7 = BINARY_OPERATION_SUB_OBJECT_LONG_LONG(tmp_sub_expr_left_4, tmp_sub_expr_right_4);
        Py_DECREF(tmp_sub_expr_left_4);
        assert(!(tmp_mult_expr_right_7 == NULL));
        tmp_assign_source_17 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_right_7, tmp_mult_expr_left_7);
        Py_DECREF(tmp_mult_expr_right_7);
        assert(!(tmp_assign_source_17 == NULL));
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[34], tmp_assign_source_17);
    }
    {
        PyObject *tmp_assign_source_18;
        PyObject *tmp_mult_expr_left_9;
        PyObject *tmp_mult_expr_right_9;
        PyObject *tmp_sub_expr_left_5;
        PyObject *tmp_sub_expr_right_5;
        PyObject *tmp_mult_expr_left_10;
        PyObject *tmp_mult_expr_right_10;
        tmp_mult_expr_left_9 = mod_consts[35];
        tmp_mult_expr_left_10 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[20]);

        if (unlikely(tmp_mult_expr_left_10 == NULL)) {
            tmp_mult_expr_left_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
        }

        assert(!(tmp_mult_expr_left_10 == NULL));
        tmp_mult_expr_right_10 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_mult_expr_right_10 == NULL)) {
            tmp_mult_expr_right_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[18]);
        }

        assert(!(tmp_mult_expr_right_10 == NULL));
        tmp_sub_expr_left_5 = BINARY_OPERATION_MULT_OBJECT_LONG_LONG(tmp_mult_expr_left_10, tmp_mult_expr_right_10);
        assert(!(tmp_sub_expr_left_5 == NULL));
        tmp_sub_expr_right_5 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[22]);

        if (unlikely(tmp_sub_expr_right_5 == NULL)) {
            tmp_sub_expr_right_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[22]);
        }

        assert(!(tmp_sub_expr_right_5 == NULL));
        tmp_mult_expr_right_9 = BINARY_OPERATION_SUB_OBJECT_LONG_LONG(tmp_sub_expr_left_5, tmp_sub_expr_right_5);
        Py_DECREF(tmp_sub_expr_left_5);
        assert(!(tmp_mult_expr_right_9 == NULL));
        tmp_assign_source_18 = BINARY_OPERATION_MULT_OBJECT_OBJECT_OBJECT(tmp_mult_expr_right_9, tmp_mult_expr_left_9);
        Py_DECREF(tmp_mult_expr_right_9);
        assert(!(tmp_assign_source_18 == NULL));
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[36], tmp_assign_source_18);
    }
    {
        PyObject *tmp_assign_source_19;
        tmp_assign_source_19 = mod_consts[37];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[8], tmp_assign_source_19);
    }
    {
        PyObject *tmp_assign_source_20;
        tmp_assign_source_20 = mod_consts[38];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[39], tmp_assign_source_20);
    }
    {
        PyObject *tmp_assign_source_21;
        tmp_assign_source_21 = DICT_COPY(mod_consts[40]);
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[41], tmp_assign_source_21);
    }
    {
        PyObject *tmp_assign_source_22;
        tmp_assign_source_22 = mod_consts[42];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[43], tmp_assign_source_22);
    }
    {
        PyObject *tmp_assign_source_23;
        tmp_assign_source_23 = mod_consts[44];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[45], tmp_assign_source_23);
    }
    {
        PyObject *tmp_assign_source_24;
        PyObject *tmp_truediv_expr_left_1;
        PyObject *tmp_truediv_expr_right_1;
        tmp_truediv_expr_left_1 = mod_consts[46];
        tmp_truediv_expr_right_1 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_1 == NULL)) {
            tmp_truediv_expr_right_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        assert(!(tmp_truediv_expr_right_1 == NULL));
        tmp_assign_source_24 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_1, tmp_truediv_expr_right_1);
        if (tmp_assign_source_24 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 35;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[47], tmp_assign_source_24);
    }
    {
        PyObject *tmp_assign_source_25;
        PyObject *tmp_truediv_expr_left_2;
        PyObject *tmp_truediv_expr_right_2;
        tmp_truediv_expr_left_2 = mod_consts[48];
        tmp_truediv_expr_right_2 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_2 == NULL)) {
            tmp_truediv_expr_right_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        assert(!(tmp_truediv_expr_right_2 == NULL));
        tmp_assign_source_25 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_2, tmp_truediv_expr_right_2);
        if (tmp_assign_source_25 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 36;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[49], tmp_assign_source_25);
    }
    {
        PyObject *tmp_assign_source_26;
        PyObject *tmp_truediv_expr_left_3;
        PyObject *tmp_truediv_expr_right_3;
        tmp_truediv_expr_left_3 = mod_consts[50];
        tmp_truediv_expr_right_3 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_3 == NULL)) {
            tmp_truediv_expr_right_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        assert(!(tmp_truediv_expr_right_3 == NULL));
        tmp_assign_source_26 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_3, tmp_truediv_expr_right_3);
        if (tmp_assign_source_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[51], tmp_assign_source_26);
    }
    {
        PyObject *tmp_assign_source_27;
        PyObject *tmp_truediv_expr_left_4;
        PyObject *tmp_truediv_expr_right_4;
        tmp_truediv_expr_left_4 = mod_consts[46];
        tmp_truediv_expr_right_4 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_4 == NULL)) {
            tmp_truediv_expr_right_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        assert(!(tmp_truediv_expr_right_4 == NULL));
        tmp_assign_source_27 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_4, tmp_truediv_expr_right_4);
        if (tmp_assign_source_27 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 40;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[52], tmp_assign_source_27);
    }
    {
        PyObject *tmp_assign_source_28;
        PyObject *tmp_truediv_expr_left_5;
        PyObject *tmp_truediv_expr_right_5;
        tmp_truediv_expr_left_5 = mod_consts[53];
        tmp_truediv_expr_right_5 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_5 == NULL)) {
            tmp_truediv_expr_right_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        assert(!(tmp_truediv_expr_right_5 == NULL));
        tmp_assign_source_28 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_5, tmp_truediv_expr_right_5);
        if (tmp_assign_source_28 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 41;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[54], tmp_assign_source_28);
    }
    {
        PyObject *tmp_assign_source_29;
        PyObject *tmp_truediv_expr_left_6;
        PyObject *tmp_truediv_expr_right_6;
        tmp_truediv_expr_left_6 = mod_consts[50];
        tmp_truediv_expr_right_6 = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_truediv_expr_right_6 == NULL)) {
            tmp_truediv_expr_right_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[6]);
        }

        assert(!(tmp_truediv_expr_right_6 == NULL));
        tmp_assign_source_29 = BINARY_OPERATION_TRUEDIV_OBJECT_OBJECT_OBJECT(tmp_truediv_expr_left_6, tmp_truediv_expr_right_6);
        if (tmp_assign_source_29 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 42;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[55], tmp_assign_source_29);
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_6788ba1ae737446e4c049b14b00919e9, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_6788ba1ae737446e4c049b14b00919e9->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_6788ba1ae737446e4c049b14b00919e9, exception_lineno);
    }



    assertFrameObject(frame_6788ba1ae737446e4c049b14b00919e9);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;
    {
        PyObject *tmp_assign_source_30;
        tmp_assign_source_30 = mod_consts[56];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[57], tmp_assign_source_30);
    }
    {
        PyObject *tmp_assign_source_31;
        tmp_assign_source_31 = mod_consts[58];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[59], tmp_assign_source_31);
    }
    {
        PyObject *tmp_assign_source_32;
        tmp_assign_source_32 = mod_consts[60];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[61], tmp_assign_source_32);
    }
    {
        PyObject *tmp_assign_source_33;
        tmp_assign_source_33 = mod_consts[62];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[63], tmp_assign_source_33);
    }
    {
        PyObject *tmp_assign_source_34;
        tmp_assign_source_34 = mod_consts[64];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[65], tmp_assign_source_34);
    }
    {
        PyObject *tmp_assign_source_35;
        tmp_assign_source_35 = mod_consts[66];
        UPDATE_STRING_DICT0(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[67], tmp_assign_source_35);
    }
    {
        PyObject *tmp_assign_source_36;


        tmp_assign_source_36 = MAKE_FUNCTION_base$constant$$$function__1_PHYSICAL_ATTACK_POWER_COF();

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[2], tmp_assign_source_36);
    }
    {
        PyObject *tmp_assign_source_37;


        tmp_assign_source_37 = MAKE_FUNCTION_base$constant$$$function__2_PHYSICAL_DOT_ATTACK_POWER_COF();

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[68], tmp_assign_source_37);
    }
    {
        PyObject *tmp_assign_source_38;


        tmp_assign_source_38 = MAKE_FUNCTION_base$constant$$$function__3_MAGICAL_ATTACK_POWER_COF();

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_38);
    }
    {
        PyObject *tmp_assign_source_39;


        tmp_assign_source_39 = MAKE_FUNCTION_base$constant$$$function__4_MAGICAL_DOT_ATTACK_POWER_COF();

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[69], tmp_assign_source_39);
    }
    {
        PyObject *tmp_assign_source_40;


        tmp_assign_source_40 = MAKE_FUNCTION_base$constant$$$function__5_WEAPON_DAMAGE_COF();

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[70], tmp_assign_source_40);
    }
    {
        PyObject *tmp_assign_source_41;


        tmp_assign_source_41 = MAKE_FUNCTION_base$constant$$$function__6_SURPLUS_COF();

        UPDATE_STRING_DICT1(moduledict_base$constant, (Nuitka_StringObject *)mod_consts[71], tmp_assign_source_41);
    }

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("base$constant", false);

    Py_INCREF(module_base$constant);
    return module_base$constant;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_base$constant, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(tstate, module_name);
        }
    }
#endif
    PGO_onModuleExit("base$constant", false);

    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);
    return NULL;
}
