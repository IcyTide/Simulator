/* Generated code for Python module 'general$consumables'
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

/* The "module_general$consumables" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_general$consumables;
PyDictObject *moduledict_general$consumables;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[183];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[183];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(PyThreadState *tstate) {
    if (constants_created == false) {
        loadConstantsBlob(tstate, &mod_consts[0], UNTRANSLATE("general.consumables"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 183; i++) {
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
void checkModuleConstants_general$consumables(PyThreadState *tstate) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 183; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(tstate, mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_c882f4f0f7cca0ca41864096797f6688;
static PyCodeObject *codeobj_1169514ad861b3cf2de794e31cbb26c0;
static PyCodeObject *codeobj_e94a74512cc228f25e3343fa1439d927;
static PyCodeObject *codeobj_0e407133af10331c20b0e76cc9d9a0a1;
static PyCodeObject *codeobj_880c6a08f9fff6ff921999676bced6d2;
static PyCodeObject *codeobj_3be29d4f434620146409244b200048f2;
static PyCodeObject *codeobj_bc69608fc706b7d97c68667b852945d4;
static PyCodeObject *codeobj_bc9e4b980e63f4fe120bb151ec8bcce7;
static PyCodeObject *codeobj_761ac7d338b483e06d15a13a9cc8efed;
static PyCodeObject *codeobj_2d964f9ea2281fcbc78d6637b41b10b4;
static PyCodeObject *codeobj_feb81ece12dd1bdc3461dabfa36e4fbf;
static PyCodeObject *codeobj_3c77d3d28955a07bf8478d679df7b694;
static PyCodeObject *codeobj_7c6ee4065215a71ac3609ec688769de4;
static PyCodeObject *codeobj_b0df215bdb123893b3c70b212fe9bccb;
static PyCodeObject *codeobj_55829651d111e38e199999b1eaa96201;
static PyCodeObject *codeobj_be7b08e1396dd416500e22c3903a27d3;
static PyCodeObject *codeobj_e8db72b4548ff0b5e6a831be86241d32;
static PyCodeObject *codeobj_c32478bcff6af44edff00a87e368e6d7;
static PyCodeObject *codeobj_b365139fb97d25576846d889c4d022c6;
static PyCodeObject *codeobj_59d887266b48af293b82614553acd6fa;
static PyCodeObject *codeobj_e55847e3b45a5e54cdeac8437d8b74f0;
static PyCodeObject *codeobj_4520fb9be7f73bc17013223f5c96f80f;
static PyCodeObject *codeobj_8a14fb7192a2abe6bf6b2116561cc16b;
static PyCodeObject *codeobj_7af5a8e6f08109f75abb02a62b36c006;
static PyCodeObject *codeobj_ad70b2d72ded525a8dd218ffe92d7e2c;
static PyCodeObject *codeobj_49a61b3e1ae9509bf333db6e92d558c9;
static PyCodeObject *codeobj_182c892eb30ddde0d66b80c5c729552f;
static PyCodeObject *codeobj_2908e31858b4caa48edb3686cbef0273;
static PyCodeObject *codeobj_9fc3ccf1159f371709112b2066a3c81d;
static PyCodeObject *codeobj_57fa061eb3de049bc50b71312be9b077;
static PyCodeObject *codeobj_e9fa428c0755b1f44a9d1c11580bb77b;
static PyCodeObject *codeobj_f0f59773c22184729b6ff686be7e3693;
static PyCodeObject *codeobj_2e82ba0253cd42b92fc9a39a1cc21dda;
static PyCodeObject *codeobj_edb4f666f32b3302b343095186bcfa94;
static PyCodeObject *codeobj_73100602d3c37514771855fdc1496741;
static PyCodeObject *codeobj_74bb33b1843ad1ccd1b6421712908d21;
static PyCodeObject *codeobj_8e851050db72deb68cfe22128e92451b;
static PyCodeObject *codeobj_781cfd9b2a50395e86d9e69451c6cfb9;
static PyCodeObject *codeobj_17b93562b4c94ce1c68f8cd611f34694;
static PyCodeObject *codeobj_1881c47ea39f67ee5ef81303441dbcfe;
static PyCodeObject *codeobj_41b0937ef481d2fc3f5adb35960603ef;
static PyCodeObject *codeobj_ced346e6f194625165a5ed52efcf68e1;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[179]); CHECK_OBJECT(module_filename_obj);
    codeobj_c882f4f0f7cca0ca41864096797f6688 = MAKE_CODE_OBJECT(module_filename_obj, 1, 0, mod_consts[180], mod_consts[180], NULL, NULL, 0, 0, 0);
    codeobj_1169514ad861b3cf2de794e31cbb26c0 = MAKE_CODE_OBJECT(module_filename_obj, 58, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[30], mod_consts[30], mod_consts[181], NULL, 1, 0, 0);
    codeobj_e94a74512cc228f25e3343fa1439d927 = MAKE_CODE_OBJECT(module_filename_obj, 104, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[40], mod_consts[40], mod_consts[181], NULL, 1, 0, 0);
    codeobj_0e407133af10331c20b0e76cc9d9a0a1 = MAKE_CODE_OBJECT(module_filename_obj, 15, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[21], mod_consts[21], mod_consts[181], NULL, 1, 0, 0);
    codeobj_880c6a08f9fff6ff921999676bced6d2 = MAKE_CODE_OBJECT(module_filename_obj, 150, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[50], mod_consts[50], mod_consts[181], NULL, 1, 0, 0);
    codeobj_3be29d4f434620146409244b200048f2 = MAKE_CODE_OBJECT(module_filename_obj, 97, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[39], mod_consts[39], mod_consts[181], NULL, 1, 0, 0);
    codeobj_bc69608fc706b7d97c68667b852945d4 = MAKE_CODE_OBJECT(module_filename_obj, 143, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[49], mod_consts[49], mod_consts[181], NULL, 1, 0, 0);
    codeobj_bc9e4b980e63f4fe120bb151ec8bcce7 = MAKE_CODE_OBJECT(module_filename_obj, 93, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[38], mod_consts[38], mod_consts[181], NULL, 1, 0, 0);
    codeobj_761ac7d338b483e06d15a13a9cc8efed = MAKE_CODE_OBJECT(module_filename_obj, 139, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[48], mod_consts[48], mod_consts[181], NULL, 1, 0, 0);
    codeobj_2d964f9ea2281fcbc78d6637b41b10b4 = MAKE_CODE_OBJECT(module_filename_obj, 47, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[28], mod_consts[28], mod_consts[181], NULL, 1, 0, 0);
    codeobj_feb81ece12dd1bdc3461dabfa36e4fbf = MAKE_CODE_OBJECT(module_filename_obj, 185, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[58], mod_consts[58], mod_consts[181], NULL, 1, 0, 0);
    codeobj_3c77d3d28955a07bf8478d679df7b694 = MAKE_CODE_OBJECT(module_filename_obj, 51, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[29], mod_consts[29], mod_consts[181], NULL, 1, 0, 0);
    codeobj_7c6ee4065215a71ac3609ec688769de4 = MAKE_CODE_OBJECT(module_filename_obj, 43, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[27], mod_consts[27], mod_consts[181], NULL, 1, 0, 0);
    codeobj_b0df215bdb123893b3c70b212fe9bccb = MAKE_CODE_OBJECT(module_filename_obj, 89, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[37], mod_consts[37], mod_consts[181], NULL, 1, 0, 0);
    codeobj_55829651d111e38e199999b1eaa96201 = MAKE_CODE_OBJECT(module_filename_obj, 135, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[47], mod_consts[47], mod_consts[181], NULL, 1, 0, 0);
    codeobj_be7b08e1396dd416500e22c3903a27d3 = MAKE_CODE_OBJECT(module_filename_obj, 166, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[54], mod_consts[54], mod_consts[181], NULL, 1, 0, 0);
    codeobj_e8db72b4548ff0b5e6a831be86241d32 = MAKE_CODE_OBJECT(module_filename_obj, 8, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[20], mod_consts[20], mod_consts[181], NULL, 1, 0, 0);
    codeobj_c32478bcff6af44edff00a87e368e6d7 = MAKE_CODE_OBJECT(module_filename_obj, 81, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[35], mod_consts[35], mod_consts[181], NULL, 1, 0, 0);
    codeobj_b365139fb97d25576846d889c4d022c6 = MAKE_CODE_OBJECT(module_filename_obj, 127, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[45], mod_consts[45], mod_consts[181], NULL, 1, 0, 0);
    codeobj_59d887266b48af293b82614553acd6fa = MAKE_CODE_OBJECT(module_filename_obj, 177, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[56], mod_consts[56], mod_consts[181], NULL, 1, 0, 0);
    codeobj_e55847e3b45a5e54cdeac8437d8b74f0 = MAKE_CODE_OBJECT(module_filename_obj, 37, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[26], mod_consts[26], mod_consts[182], NULL, 2, 0, 0);
    codeobj_4520fb9be7f73bc17013223f5c96f80f = MAKE_CODE_OBJECT(module_filename_obj, 189, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[59], mod_consts[59], mod_consts[181], NULL, 1, 0, 0);
    codeobj_8a14fb7192a2abe6bf6b2116561cc16b = MAKE_CODE_OBJECT(module_filename_obj, 4, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[19], mod_consts[19], mod_consts[181], NULL, 1, 0, 0);
    codeobj_7af5a8e6f08109f75abb02a62b36c006 = MAKE_CODE_OBJECT(module_filename_obj, 77, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[34], mod_consts[34], mod_consts[181], NULL, 1, 0, 0);
    codeobj_ad70b2d72ded525a8dd218ffe92d7e2c = MAKE_CODE_OBJECT(module_filename_obj, 123, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[44], mod_consts[44], mod_consts[181], NULL, 1, 0, 0);
    codeobj_49a61b3e1ae9509bf333db6e92d558c9 = MAKE_CODE_OBJECT(module_filename_obj, 173, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[55], mod_consts[55], mod_consts[181], NULL, 1, 0, 0);
    codeobj_182c892eb30ddde0d66b80c5c729552f = MAKE_CODE_OBJECT(module_filename_obj, 31, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[25], mod_consts[25], mod_consts[182], NULL, 2, 0, 0);
    codeobj_2908e31858b4caa48edb3686cbef0273 = MAKE_CODE_OBJECT(module_filename_obj, 66, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[32], mod_consts[32], mod_consts[181], NULL, 1, 0, 0);
    codeobj_9fc3ccf1159f371709112b2066a3c81d = MAKE_CODE_OBJECT(module_filename_obj, 112, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[42], mod_consts[42], mod_consts[181], NULL, 1, 0, 0);
    codeobj_57fa061eb3de049bc50b71312be9b077 = MAKE_CODE_OBJECT(module_filename_obj, 23, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[23], mod_consts[23], mod_consts[181], NULL, 1, 0, 0);
    codeobj_e9fa428c0755b1f44a9d1c11580bb77b = MAKE_CODE_OBJECT(module_filename_obj, 158, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[52], mod_consts[52], mod_consts[181], NULL, 1, 0, 0);
    codeobj_f0f59773c22184729b6ff686be7e3693 = MAKE_CODE_OBJECT(module_filename_obj, 70, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[33], mod_consts[33], mod_consts[181], NULL, 1, 0, 0);
    codeobj_2e82ba0253cd42b92fc9a39a1cc21dda = MAKE_CODE_OBJECT(module_filename_obj, 116, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[43], mod_consts[43], mod_consts[181], NULL, 1, 0, 0);
    codeobj_edb4f666f32b3302b343095186bcfa94 = MAKE_CODE_OBJECT(module_filename_obj, 27, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[24], mod_consts[24], mod_consts[181], NULL, 1, 0, 0);
    codeobj_73100602d3c37514771855fdc1496741 = MAKE_CODE_OBJECT(module_filename_obj, 162, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[53], mod_consts[53], mod_consts[181], NULL, 1, 0, 0);
    codeobj_74bb33b1843ad1ccd1b6421712908d21 = MAKE_CODE_OBJECT(module_filename_obj, 181, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[57], mod_consts[57], mod_consts[181], NULL, 1, 0, 0);
    codeobj_8e851050db72deb68cfe22128e92451b = MAKE_CODE_OBJECT(module_filename_obj, 62, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[31], mod_consts[31], mod_consts[181], NULL, 1, 0, 0);
    codeobj_781cfd9b2a50395e86d9e69451c6cfb9 = MAKE_CODE_OBJECT(module_filename_obj, 108, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[41], mod_consts[41], mod_consts[181], NULL, 1, 0, 0);
    codeobj_17b93562b4c94ce1c68f8cd611f34694 = MAKE_CODE_OBJECT(module_filename_obj, 19, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[22], mod_consts[22], mod_consts[181], NULL, 1, 0, 0);
    codeobj_1881c47ea39f67ee5ef81303441dbcfe = MAKE_CODE_OBJECT(module_filename_obj, 154, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[51], mod_consts[51], mod_consts[181], NULL, 1, 0, 0);
    codeobj_41b0937ef481d2fc3f5adb35960603ef = MAKE_CODE_OBJECT(module_filename_obj, 85, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[36], mod_consts[36], mod_consts[181], NULL, 1, 0, 0);
    codeobj_ced346e6f194625165a5ed52efcf68e1 = MAKE_CODE_OBJECT(module_filename_obj, 131, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[46], mod_consts[46], mod_consts[181], NULL, 1, 0, 0);
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_general$consumables$$$function__10_boiled_fish_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__11_guild_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__12_agility_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__13_strength_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__14_spirit_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__15_spunk_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__16_physical_attack_power_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__17_magical_attack_power_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__18_surplus_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__19_haste_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__1_physical_attack_power_enchant();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__20_all_overcome_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__21_all_critical_strike_food();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__22_agility_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__23_strength_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__24_spirit_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__25_spunk_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__26_physical_attack_power_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__27_magical_attack_power_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__28_surplus_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__29_haste_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__2_magical_attack_power_enchant();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__30_all_overcome_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__31_all_critical_strike_potion();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__32_agility_wine();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__33_strength_wine();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__34_spirit_wine();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__35_spunk_wine();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__36_haste_wine();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__37_physical_attack_power_snack();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__38_magical_attack_power_snack();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__39_strain_snack();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__3_agility_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__40_critical_snack();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__41_overcome_snack();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__4_strength_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__5_spirit_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__6_spunk_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__7_physical_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__8_magical_spread();


static PyObject *MAKE_FUNCTION_general$consumables$$$function__9_guild_spread();


// The module function definitions.
static PyObject *impl_general$consumables$$$function__1_physical_attack_power_enchant(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[0];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__2_magical_attack_power_enchant(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[1];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__3_agility_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[2];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__4_strength_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[3];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__5_spirit_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[4];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__6_spunk_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[5];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__7_physical_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value1 = python_pars[0];
    PyObject *par_value2 = python_pars[1];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[0];
        CHECK_OBJECT(par_value1);
        tmp_dict_value_1 = par_value1;
        tmp_return_value = _PyDict_NewPresized( 3 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[6];
        CHECK_OBJECT(par_value2);
        tmp_dict_value_1 = par_value2;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[7];
        CHECK_OBJECT(par_value2);
        tmp_dict_value_1 = par_value2;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value1);
    Py_DECREF(par_value1);
    CHECK_OBJECT(par_value2);
    Py_DECREF(par_value2);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__8_magical_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value1 = python_pars[0];
    PyObject *par_value2 = python_pars[1];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[1];
        CHECK_OBJECT(par_value1);
        tmp_dict_value_1 = par_value1;
        tmp_return_value = _PyDict_NewPresized( 3 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[6];
        CHECK_OBJECT(par_value2);
        tmp_dict_value_1 = par_value2;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[7];
        CHECK_OBJECT(par_value2);
        tmp_dict_value_1 = par_value2;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value1);
    Py_DECREF(par_value1);
    CHECK_OBJECT(par_value2);
    Py_DECREF(par_value2);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__9_guild_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[7];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 2 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[8];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__10_boiled_fish_spread(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[7];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 2 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[8];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__11_guild_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[8];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__12_agility_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[2];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__13_strength_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[3];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__14_spirit_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[4];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__15_spunk_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[5];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__16_physical_attack_power_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[0];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__17_magical_attack_power_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[1];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__18_surplus_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[7];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__19_haste_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[9];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__20_all_overcome_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[10];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 2 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[11];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__21_all_critical_strike_food(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[6];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__22_agility_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[2];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__23_strength_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[3];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__24_spirit_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[4];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__25_spunk_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[5];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__26_physical_attack_power_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[0];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__27_magical_attack_power_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[1];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__28_surplus_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[7];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__29_haste_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[9];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__30_all_overcome_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[10];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 2 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[11];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__31_all_critical_strike_potion(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[6];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__32_agility_wine(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[2];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__33_strength_wine(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[3];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__34_spirit_wine(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[4];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__35_spunk_wine(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[5];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__36_haste_wine(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[9];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__37_physical_attack_power_snack(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[0];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__38_magical_attack_power_snack(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[1];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__39_strain_snack(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[8];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__40_critical_snack(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[6];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}


static PyObject *impl_general$consumables$$$function__41_overcome_snack(PyThreadState *tstate, struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = HAS_ERROR_OCCURRED(tstate);
#endif

    // Local variable declarations.
    PyObject *par_value = python_pars[0];
    PyObject *tmp_return_value = NULL;
    int tmp_res;

    // Actual function body.
    {
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[10];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_return_value = _PyDict_NewPresized( 2 );
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        tmp_dict_key_1 = mod_consts[11];
        CHECK_OBJECT(par_value);
        tmp_dict_value_1 = par_value;
        tmp_res = PyDict_SetItem(tmp_return_value, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));
        goto function_return_exit;
    }

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_value);
    Py_DECREF(par_value);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !HAS_ERROR_OCCURRED(tstate));
   return tmp_return_value;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__10_boiled_fish_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__10_boiled_fish_spread,
        mod_consts[28],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_2d964f9ea2281fcbc78d6637b41b10b4,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__11_guild_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__11_guild_food,
        mod_consts[29],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_3c77d3d28955a07bf8478d679df7b694,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__12_agility_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__12_agility_food,
        mod_consts[30],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_1169514ad861b3cf2de794e31cbb26c0,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__13_strength_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__13_strength_food,
        mod_consts[31],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_8e851050db72deb68cfe22128e92451b,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__14_spirit_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__14_spirit_food,
        mod_consts[32],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_2908e31858b4caa48edb3686cbef0273,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__15_spunk_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__15_spunk_food,
        mod_consts[33],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_f0f59773c22184729b6ff686be7e3693,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__16_physical_attack_power_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__16_physical_attack_power_food,
        mod_consts[34],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_7af5a8e6f08109f75abb02a62b36c006,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__17_magical_attack_power_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__17_magical_attack_power_food,
        mod_consts[35],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_c32478bcff6af44edff00a87e368e6d7,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__18_surplus_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__18_surplus_food,
        mod_consts[36],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_41b0937ef481d2fc3f5adb35960603ef,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__19_haste_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__19_haste_food,
        mod_consts[37],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_b0df215bdb123893b3c70b212fe9bccb,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__1_physical_attack_power_enchant() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__1_physical_attack_power_enchant,
        mod_consts[19],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_8a14fb7192a2abe6bf6b2116561cc16b,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__20_all_overcome_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__20_all_overcome_food,
        mod_consts[38],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_bc9e4b980e63f4fe120bb151ec8bcce7,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__21_all_critical_strike_food() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__21_all_critical_strike_food,
        mod_consts[39],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_3be29d4f434620146409244b200048f2,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__22_agility_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__22_agility_potion,
        mod_consts[40],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_e94a74512cc228f25e3343fa1439d927,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__23_strength_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__23_strength_potion,
        mod_consts[41],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_781cfd9b2a50395e86d9e69451c6cfb9,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__24_spirit_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__24_spirit_potion,
        mod_consts[42],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_9fc3ccf1159f371709112b2066a3c81d,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__25_spunk_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__25_spunk_potion,
        mod_consts[43],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_2e82ba0253cd42b92fc9a39a1cc21dda,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__26_physical_attack_power_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__26_physical_attack_power_potion,
        mod_consts[44],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_ad70b2d72ded525a8dd218ffe92d7e2c,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__27_magical_attack_power_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__27_magical_attack_power_potion,
        mod_consts[45],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_b365139fb97d25576846d889c4d022c6,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__28_surplus_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__28_surplus_potion,
        mod_consts[46],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_ced346e6f194625165a5ed52efcf68e1,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__29_haste_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__29_haste_potion,
        mod_consts[47],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_55829651d111e38e199999b1eaa96201,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__2_magical_attack_power_enchant() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__2_magical_attack_power_enchant,
        mod_consts[20],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_e8db72b4548ff0b5e6a831be86241d32,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__30_all_overcome_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__30_all_overcome_potion,
        mod_consts[48],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_761ac7d338b483e06d15a13a9cc8efed,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__31_all_critical_strike_potion() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__31_all_critical_strike_potion,
        mod_consts[49],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_bc69608fc706b7d97c68667b852945d4,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__32_agility_wine() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__32_agility_wine,
        mod_consts[50],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_880c6a08f9fff6ff921999676bced6d2,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__33_strength_wine() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__33_strength_wine,
        mod_consts[51],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_1881c47ea39f67ee5ef81303441dbcfe,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__34_spirit_wine() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__34_spirit_wine,
        mod_consts[52],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_e9fa428c0755b1f44a9d1c11580bb77b,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__35_spunk_wine() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__35_spunk_wine,
        mod_consts[53],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_73100602d3c37514771855fdc1496741,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__36_haste_wine() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__36_haste_wine,
        mod_consts[54],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_be7b08e1396dd416500e22c3903a27d3,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__37_physical_attack_power_snack() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__37_physical_attack_power_snack,
        mod_consts[55],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_49a61b3e1ae9509bf333db6e92d558c9,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__38_magical_attack_power_snack() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__38_magical_attack_power_snack,
        mod_consts[56],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_59d887266b48af293b82614553acd6fa,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__39_strain_snack() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__39_strain_snack,
        mod_consts[57],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_74bb33b1843ad1ccd1b6421712908d21,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__3_agility_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__3_agility_spread,
        mod_consts[21],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_0e407133af10331c20b0e76cc9d9a0a1,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__40_critical_snack() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__40_critical_snack,
        mod_consts[58],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_feb81ece12dd1bdc3461dabfa36e4fbf,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__41_overcome_snack() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__41_overcome_snack,
        mod_consts[59],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_4520fb9be7f73bc17013223f5c96f80f,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__4_strength_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__4_strength_spread,
        mod_consts[22],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_17b93562b4c94ce1c68f8cd611f34694,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__5_spirit_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__5_spirit_spread,
        mod_consts[23],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_57fa061eb3de049bc50b71312be9b077,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__6_spunk_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__6_spunk_spread,
        mod_consts[24],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_edb4f666f32b3302b343095186bcfa94,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__7_physical_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__7_physical_spread,
        mod_consts[25],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_182c892eb30ddde0d66b80c5c729552f,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__8_magical_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__8_magical_spread,
        mod_consts[26],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_e55847e3b45a5e54cdeac8437d8b74f0,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_general$consumables$$$function__9_guild_spread() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_general$consumables$$$function__9_guild_spread,
        mod_consts[27],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_7c6ee4065215a71ac3609ec688769de4,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_general$consumables,
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

static function_impl_code const function_table_general$consumables[] = {
    impl_general$consumables$$$function__1_physical_attack_power_enchant,
    impl_general$consumables$$$function__2_magical_attack_power_enchant,
    impl_general$consumables$$$function__3_agility_spread,
    impl_general$consumables$$$function__4_strength_spread,
    impl_general$consumables$$$function__5_spirit_spread,
    impl_general$consumables$$$function__6_spunk_spread,
    impl_general$consumables$$$function__7_physical_spread,
    impl_general$consumables$$$function__8_magical_spread,
    impl_general$consumables$$$function__9_guild_spread,
    impl_general$consumables$$$function__10_boiled_fish_spread,
    impl_general$consumables$$$function__11_guild_food,
    impl_general$consumables$$$function__12_agility_food,
    impl_general$consumables$$$function__13_strength_food,
    impl_general$consumables$$$function__14_spirit_food,
    impl_general$consumables$$$function__15_spunk_food,
    impl_general$consumables$$$function__16_physical_attack_power_food,
    impl_general$consumables$$$function__17_magical_attack_power_food,
    impl_general$consumables$$$function__18_surplus_food,
    impl_general$consumables$$$function__19_haste_food,
    impl_general$consumables$$$function__20_all_overcome_food,
    impl_general$consumables$$$function__21_all_critical_strike_food,
    impl_general$consumables$$$function__22_agility_potion,
    impl_general$consumables$$$function__23_strength_potion,
    impl_general$consumables$$$function__24_spirit_potion,
    impl_general$consumables$$$function__25_spunk_potion,
    impl_general$consumables$$$function__26_physical_attack_power_potion,
    impl_general$consumables$$$function__27_magical_attack_power_potion,
    impl_general$consumables$$$function__28_surplus_potion,
    impl_general$consumables$$$function__29_haste_potion,
    impl_general$consumables$$$function__30_all_overcome_potion,
    impl_general$consumables$$$function__31_all_critical_strike_potion,
    impl_general$consumables$$$function__32_agility_wine,
    impl_general$consumables$$$function__33_strength_wine,
    impl_general$consumables$$$function__34_spirit_wine,
    impl_general$consumables$$$function__35_spunk_wine,
    impl_general$consumables$$$function__36_haste_wine,
    impl_general$consumables$$$function__37_physical_attack_power_snack,
    impl_general$consumables$$$function__38_magical_attack_power_snack,
    impl_general$consumables$$$function__39_strain_snack,
    impl_general$consumables$$$function__40_critical_snack,
    impl_general$consumables$$$function__41_overcome_snack,
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

    int offset = Nuitka_Function_GetFunctionCodeIndex(function, function_table_general$consumables);

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
        module_general$consumables,
        function_qualname,
        function_index,
        code_object_desc,
        constant_return_value,
        defaults,
        kw_defaults,
        doc,
        function_table_general$consumables,
        sizeof(function_table_general$consumables) / sizeof(function_impl_code)
    );
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_general$consumables(PyThreadState *tstate, PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("general$consumables");

    // Store the module for future use.
    module_general$consumables = module;

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
        PRINT_STRING("general$consumables: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader(tstate);

#if PYTHON_VERSION >= 0x300
        patchInspectModule(tstate);
#endif

#endif

        /* The constants only used by this module are created now. */
        NUITKA_PRINT_TRACE("general$consumables: Calling createModuleConstants().\n");
        createModuleConstants(tstate);

        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initgeneral$consumables\n");

    moduledict_general$consumables = MODULE_DICT(module_general$consumables);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    {
        char const *module_name_c;
        if (loader_entry != NULL) {
            module_name_c = loader_entry->name;
        } else {
            PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___name__);
            module_name_c = Nuitka_String_AsString(module_name);
        }

        registerDillPluginTables(tstate, module_name_c, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
    }




#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_general$consumables,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_general$consumables,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[64]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_general$consumables,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_general$consumables,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_general$consumables,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_general$consumables);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

    UPDATE_STRING_DICT0(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, _spec_from_module, module_general$consumables);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(tstate, spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_FrameObject *frame_c882f4f0f7cca0ca41864096797f6688;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = mod_consts[12];
        UPDATE_STRING_DICT0(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[13], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_2);
    }
    frame_c882f4f0f7cca0ca41864096797f6688 = MAKE_MODULE_FRAME(codeobj_c882f4f0f7cca0ca41864096797f6688, module_general$consumables);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(tstate, frame_c882f4f0f7cca0ca41864096797f6688);
    assert(Py_REFCNT(frame_c882f4f0f7cca0ca41864096797f6688) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[15]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[15]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_1, mod_consts[16], tmp_assattr_value_1);
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
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[15]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[15]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tstate, tmp_assattr_target_2, mod_consts[17], tmp_assattr_value_2);
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
        UPDATE_STRING_DICT0(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[18], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;


        tmp_assign_source_4 = MAKE_FUNCTION_general$consumables$$$function__1_physical_attack_power_enchant();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[19], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;


        tmp_assign_source_5 = MAKE_FUNCTION_general$consumables$$$function__2_magical_attack_power_enchant();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[20], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;


        tmp_assign_source_6 = MAKE_FUNCTION_general$consumables$$$function__3_agility_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[21], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;


        tmp_assign_source_7 = MAKE_FUNCTION_general$consumables$$$function__4_strength_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[22], tmp_assign_source_7);
    }
    {
        PyObject *tmp_assign_source_8;


        tmp_assign_source_8 = MAKE_FUNCTION_general$consumables$$$function__5_spirit_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[23], tmp_assign_source_8);
    }
    {
        PyObject *tmp_assign_source_9;


        tmp_assign_source_9 = MAKE_FUNCTION_general$consumables$$$function__6_spunk_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[24], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;


        tmp_assign_source_10 = MAKE_FUNCTION_general$consumables$$$function__7_physical_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[25], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;


        tmp_assign_source_11 = MAKE_FUNCTION_general$consumables$$$function__8_magical_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[26], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;


        tmp_assign_source_12 = MAKE_FUNCTION_general$consumables$$$function__9_guild_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[27], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;


        tmp_assign_source_13 = MAKE_FUNCTION_general$consumables$$$function__10_boiled_fish_spread();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[28], tmp_assign_source_13);
    }
    {
        PyObject *tmp_assign_source_14;


        tmp_assign_source_14 = MAKE_FUNCTION_general$consumables$$$function__11_guild_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[29], tmp_assign_source_14);
    }
    {
        PyObject *tmp_assign_source_15;


        tmp_assign_source_15 = MAKE_FUNCTION_general$consumables$$$function__12_agility_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[30], tmp_assign_source_15);
    }
    {
        PyObject *tmp_assign_source_16;


        tmp_assign_source_16 = MAKE_FUNCTION_general$consumables$$$function__13_strength_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[31], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;


        tmp_assign_source_17 = MAKE_FUNCTION_general$consumables$$$function__14_spirit_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[32], tmp_assign_source_17);
    }
    {
        PyObject *tmp_assign_source_18;


        tmp_assign_source_18 = MAKE_FUNCTION_general$consumables$$$function__15_spunk_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[33], tmp_assign_source_18);
    }
    {
        PyObject *tmp_assign_source_19;


        tmp_assign_source_19 = MAKE_FUNCTION_general$consumables$$$function__16_physical_attack_power_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[34], tmp_assign_source_19);
    }
    {
        PyObject *tmp_assign_source_20;


        tmp_assign_source_20 = MAKE_FUNCTION_general$consumables$$$function__17_magical_attack_power_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[35], tmp_assign_source_20);
    }
    {
        PyObject *tmp_assign_source_21;


        tmp_assign_source_21 = MAKE_FUNCTION_general$consumables$$$function__18_surplus_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[36], tmp_assign_source_21);
    }
    {
        PyObject *tmp_assign_source_22;


        tmp_assign_source_22 = MAKE_FUNCTION_general$consumables$$$function__19_haste_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[37], tmp_assign_source_22);
    }
    {
        PyObject *tmp_assign_source_23;


        tmp_assign_source_23 = MAKE_FUNCTION_general$consumables$$$function__20_all_overcome_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[38], tmp_assign_source_23);
    }
    {
        PyObject *tmp_assign_source_24;


        tmp_assign_source_24 = MAKE_FUNCTION_general$consumables$$$function__21_all_critical_strike_food();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[39], tmp_assign_source_24);
    }
    {
        PyObject *tmp_assign_source_25;


        tmp_assign_source_25 = MAKE_FUNCTION_general$consumables$$$function__22_agility_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[40], tmp_assign_source_25);
    }
    {
        PyObject *tmp_assign_source_26;


        tmp_assign_source_26 = MAKE_FUNCTION_general$consumables$$$function__23_strength_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[41], tmp_assign_source_26);
    }
    {
        PyObject *tmp_assign_source_27;


        tmp_assign_source_27 = MAKE_FUNCTION_general$consumables$$$function__24_spirit_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[42], tmp_assign_source_27);
    }
    {
        PyObject *tmp_assign_source_28;


        tmp_assign_source_28 = MAKE_FUNCTION_general$consumables$$$function__25_spunk_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[43], tmp_assign_source_28);
    }
    {
        PyObject *tmp_assign_source_29;


        tmp_assign_source_29 = MAKE_FUNCTION_general$consumables$$$function__26_physical_attack_power_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[44], tmp_assign_source_29);
    }
    {
        PyObject *tmp_assign_source_30;


        tmp_assign_source_30 = MAKE_FUNCTION_general$consumables$$$function__27_magical_attack_power_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[45], tmp_assign_source_30);
    }
    {
        PyObject *tmp_assign_source_31;


        tmp_assign_source_31 = MAKE_FUNCTION_general$consumables$$$function__28_surplus_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[46], tmp_assign_source_31);
    }
    {
        PyObject *tmp_assign_source_32;


        tmp_assign_source_32 = MAKE_FUNCTION_general$consumables$$$function__29_haste_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[47], tmp_assign_source_32);
    }
    {
        PyObject *tmp_assign_source_33;


        tmp_assign_source_33 = MAKE_FUNCTION_general$consumables$$$function__30_all_overcome_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[48], tmp_assign_source_33);
    }
    {
        PyObject *tmp_assign_source_34;


        tmp_assign_source_34 = MAKE_FUNCTION_general$consumables$$$function__31_all_critical_strike_potion();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[49], tmp_assign_source_34);
    }
    {
        PyObject *tmp_assign_source_35;


        tmp_assign_source_35 = MAKE_FUNCTION_general$consumables$$$function__32_agility_wine();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[50], tmp_assign_source_35);
    }
    {
        PyObject *tmp_assign_source_36;


        tmp_assign_source_36 = MAKE_FUNCTION_general$consumables$$$function__33_strength_wine();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[51], tmp_assign_source_36);
    }
    {
        PyObject *tmp_assign_source_37;


        tmp_assign_source_37 = MAKE_FUNCTION_general$consumables$$$function__34_spirit_wine();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[52], tmp_assign_source_37);
    }
    {
        PyObject *tmp_assign_source_38;


        tmp_assign_source_38 = MAKE_FUNCTION_general$consumables$$$function__35_spunk_wine();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[53], tmp_assign_source_38);
    }
    {
        PyObject *tmp_assign_source_39;


        tmp_assign_source_39 = MAKE_FUNCTION_general$consumables$$$function__36_haste_wine();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[54], tmp_assign_source_39);
    }
    {
        PyObject *tmp_assign_source_40;


        tmp_assign_source_40 = MAKE_FUNCTION_general$consumables$$$function__37_physical_attack_power_snack();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[55], tmp_assign_source_40);
    }
    {
        PyObject *tmp_assign_source_41;


        tmp_assign_source_41 = MAKE_FUNCTION_general$consumables$$$function__38_magical_attack_power_snack();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[56], tmp_assign_source_41);
    }
    {
        PyObject *tmp_assign_source_42;


        tmp_assign_source_42 = MAKE_FUNCTION_general$consumables$$$function__39_strain_snack();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[57], tmp_assign_source_42);
    }
    {
        PyObject *tmp_assign_source_43;


        tmp_assign_source_43 = MAKE_FUNCTION_general$consumables$$$function__40_critical_snack();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[58], tmp_assign_source_43);
    }
    {
        PyObject *tmp_assign_source_44;


        tmp_assign_source_44 = MAKE_FUNCTION_general$consumables$$$function__41_overcome_snack();

        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[59], tmp_assign_source_44);
    }
    {
        PyObject *tmp_assign_source_45;
        tmp_assign_source_45 = DICT_COPY(mod_consts[60]);
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61], tmp_assign_source_45);
    }
    {
        PyObject *tmp_assign_source_46;
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        PyObject *tmp_string_concat_values_1;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_called_value_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_subscript_value_1;
        tmp_tuple_element_1 = mod_consts[62];
        tmp_string_concat_values_1 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_1;
            PyObject *tmp_dict_arg_value_1;
            PyObject *tmp_key_value_1;
            PyObject *tmp_format_spec_1;
            PyTuple_SET_ITEM0(tmp_string_concat_values_1, 0, tmp_tuple_element_1);
            tmp_dict_arg_value_1 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_dict_arg_value_1 == NULL)) {
                tmp_dict_arg_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            assert(!(tmp_dict_arg_value_1 == NULL));
            tmp_key_value_1 = mod_consts[63];
            tmp_format_value_1 = DICT_GET_ITEM_WITH_ERROR(tstate, tmp_dict_arg_value_1, tmp_key_value_1);
            if (tmp_format_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 241;

                goto tuple_build_exception_1;
            }
            tmp_format_spec_1 = mod_consts[64];
            tmp_tuple_element_1 = BUILTIN_FORMAT(tstate, tmp_format_value_1, tmp_format_spec_1);
            Py_DECREF(tmp_format_value_1);
            if (tmp_tuple_element_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 241;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_1, 1, tmp_tuple_element_1);
            tmp_tuple_element_1 = mod_consts[65];
            PyTuple_SET_ITEM0(tmp_string_concat_values_1, 2, tmp_tuple_element_1);
        }
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_string_concat_values_1);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_1);
        Py_DECREF(tmp_string_concat_values_1);
        if (tmp_dict_key_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 241;

            goto frame_exception_exit_1;
        }
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[30]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[30]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_dict_key_1);

            exception_lineno = 242;

            goto frame_exception_exit_1;
        }
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_dict_key_1);

            exception_lineno = 242;

            goto frame_exception_exit_1;
        }
        tmp_subscript_value_1 = mod_consts[63];
        tmp_args_element_value_1 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_1, tmp_subscript_value_1);
        if (tmp_args_element_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_dict_key_1);

            exception_lineno = 242;

            goto frame_exception_exit_1;
        }
        frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 242;
        tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_dict_value_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_dict_key_1);

            exception_lineno = 242;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_46 = _PyDict_NewPresized( 64 );
        {
            PyObject *tmp_string_concat_values_2;
            PyObject *tmp_tuple_element_2;
            PyObject *tmp_called_value_2;
            PyObject *tmp_args_element_value_2;
            PyObject *tmp_expression_value_3;
            PyObject *tmp_subscript_value_3;
            PyObject *tmp_string_concat_values_3;
            PyObject *tmp_tuple_element_3;
            PyObject *tmp_called_value_3;
            PyObject *tmp_args_element_value_3;
            PyObject *tmp_expression_value_5;
            PyObject *tmp_subscript_value_5;
            PyObject *tmp_string_concat_values_4;
            PyObject *tmp_tuple_element_4;
            PyObject *tmp_called_value_4;
            PyObject *tmp_args_element_value_4;
            PyObject *tmp_expression_value_7;
            PyObject *tmp_subscript_value_7;
            PyObject *tmp_string_concat_values_5;
            PyObject *tmp_tuple_element_5;
            PyObject *tmp_called_value_5;
            PyObject *tmp_args_element_value_5;
            PyObject *tmp_expression_value_9;
            PyObject *tmp_subscript_value_9;
            PyObject *tmp_string_concat_values_6;
            PyObject *tmp_tuple_element_6;
            PyObject *tmp_called_value_6;
            PyObject *tmp_args_element_value_6;
            PyObject *tmp_expression_value_11;
            PyObject *tmp_subscript_value_11;
            PyObject *tmp_string_concat_values_7;
            PyObject *tmp_tuple_element_7;
            PyObject *tmp_called_value_7;
            PyObject *tmp_args_element_value_7;
            PyObject *tmp_expression_value_13;
            PyObject *tmp_subscript_value_13;
            PyObject *tmp_string_concat_values_8;
            PyObject *tmp_tuple_element_8;
            PyObject *tmp_called_value_8;
            PyObject *tmp_args_element_value_8;
            PyObject *tmp_expression_value_15;
            PyObject *tmp_subscript_value_15;
            PyObject *tmp_string_concat_values_9;
            PyObject *tmp_tuple_element_9;
            PyObject *tmp_called_value_9;
            PyObject *tmp_args_element_value_9;
            PyObject *tmp_expression_value_17;
            PyObject *tmp_subscript_value_17;
            PyObject *tmp_string_concat_values_10;
            PyObject *tmp_tuple_element_10;
            PyObject *tmp_called_value_10;
            PyObject *tmp_args_element_value_10;
            PyObject *tmp_expression_value_19;
            PyObject *tmp_subscript_value_19;
            PyObject *tmp_string_concat_values_11;
            PyObject *tmp_tuple_element_11;
            PyObject *tmp_called_value_11;
            PyObject *tmp_args_element_value_11;
            PyObject *tmp_expression_value_21;
            PyObject *tmp_subscript_value_21;
            PyObject *tmp_string_concat_values_12;
            PyObject *tmp_tuple_element_12;
            PyObject *tmp_called_value_12;
            PyObject *tmp_args_element_value_12;
            PyObject *tmp_expression_value_23;
            PyObject *tmp_subscript_value_23;
            PyObject *tmp_string_concat_values_13;
            PyObject *tmp_tuple_element_13;
            PyObject *tmp_called_value_13;
            PyObject *tmp_args_element_value_13;
            PyObject *tmp_expression_value_25;
            PyObject *tmp_subscript_value_25;
            PyObject *tmp_string_concat_values_14;
            PyObject *tmp_tuple_element_14;
            PyObject *tmp_called_value_14;
            PyObject *tmp_args_element_value_14;
            PyObject *tmp_expression_value_27;
            PyObject *tmp_subscript_value_27;
            PyObject *tmp_string_concat_values_15;
            PyObject *tmp_tuple_element_15;
            PyObject *tmp_called_value_15;
            PyObject *tmp_args_element_value_15;
            PyObject *tmp_expression_value_29;
            PyObject *tmp_subscript_value_29;
            PyObject *tmp_string_concat_values_16;
            PyObject *tmp_tuple_element_16;
            PyObject *tmp_called_value_16;
            PyObject *tmp_args_element_value_16;
            PyObject *tmp_expression_value_31;
            PyObject *tmp_subscript_value_31;
            PyObject *tmp_string_concat_values_17;
            PyObject *tmp_tuple_element_17;
            PyObject *tmp_called_value_17;
            PyObject *tmp_args_element_value_17;
            PyObject *tmp_expression_value_33;
            PyObject *tmp_subscript_value_33;
            PyObject *tmp_string_concat_values_18;
            PyObject *tmp_tuple_element_18;
            PyObject *tmp_called_value_18;
            PyObject *tmp_args_element_value_18;
            PyObject *tmp_expression_value_35;
            PyObject *tmp_subscript_value_35;
            PyObject *tmp_string_concat_values_19;
            PyObject *tmp_tuple_element_19;
            PyObject *tmp_called_value_19;
            PyObject *tmp_args_element_value_19;
            PyObject *tmp_expression_value_37;
            PyObject *tmp_subscript_value_37;
            PyObject *tmp_string_concat_values_20;
            PyObject *tmp_tuple_element_20;
            PyObject *tmp_called_value_20;
            PyObject *tmp_args_element_value_20;
            PyObject *tmp_expression_value_39;
            PyObject *tmp_subscript_value_39;
            PyObject *tmp_string_concat_values_21;
            PyObject *tmp_tuple_element_21;
            PyObject *tmp_called_value_21;
            PyObject *tmp_args_element_value_21;
            PyObject *tmp_expression_value_41;
            PyObject *tmp_subscript_value_41;
            PyObject *tmp_string_concat_values_22;
            PyObject *tmp_tuple_element_22;
            PyObject *tmp_called_value_22;
            PyObject *tmp_args_element_value_22;
            PyObject *tmp_expression_value_43;
            PyObject *tmp_subscript_value_43;
            PyObject *tmp_string_concat_values_23;
            PyObject *tmp_tuple_element_23;
            PyObject *tmp_called_value_23;
            PyObject *tmp_args_element_value_23;
            PyObject *tmp_expression_value_45;
            PyObject *tmp_subscript_value_45;
            PyObject *tmp_string_concat_values_24;
            PyObject *tmp_tuple_element_24;
            PyObject *tmp_called_value_24;
            PyObject *tmp_args_element_value_24;
            PyObject *tmp_expression_value_47;
            PyObject *tmp_subscript_value_47;
            PyObject *tmp_string_concat_values_25;
            PyObject *tmp_tuple_element_25;
            PyObject *tmp_called_value_25;
            PyObject *tmp_args_element_value_25;
            PyObject *tmp_expression_value_49;
            PyObject *tmp_subscript_value_49;
            PyObject *tmp_string_concat_values_26;
            PyObject *tmp_tuple_element_26;
            PyObject *tmp_called_value_26;
            PyObject *tmp_args_element_value_26;
            PyObject *tmp_expression_value_51;
            PyObject *tmp_subscript_value_51;
            PyObject *tmp_string_concat_values_27;
            PyObject *tmp_tuple_element_27;
            PyObject *tmp_called_value_27;
            PyObject *tmp_args_element_value_27;
            PyObject *tmp_expression_value_53;
            PyObject *tmp_subscript_value_53;
            PyObject *tmp_string_concat_values_28;
            PyObject *tmp_tuple_element_28;
            PyObject *tmp_called_value_28;
            PyObject *tmp_args_element_value_28;
            PyObject *tmp_expression_value_55;
            PyObject *tmp_subscript_value_55;
            PyObject *tmp_string_concat_values_29;
            PyObject *tmp_tuple_element_29;
            PyObject *tmp_called_value_29;
            PyObject *tmp_args_element_value_29;
            PyObject *tmp_expression_value_57;
            PyObject *tmp_subscript_value_57;
            PyObject *tmp_string_concat_values_30;
            PyObject *tmp_tuple_element_30;
            PyObject *tmp_called_value_30;
            PyObject *tmp_args_element_value_30;
            PyObject *tmp_expression_value_59;
            PyObject *tmp_subscript_value_59;
            PyObject *tmp_string_concat_values_31;
            PyObject *tmp_tuple_element_31;
            PyObject *tmp_called_value_31;
            PyObject *tmp_args_element_value_31;
            PyObject *tmp_expression_value_61;
            PyObject *tmp_subscript_value_61;
            PyObject *tmp_string_concat_values_32;
            PyObject *tmp_tuple_element_32;
            PyObject *tmp_called_value_32;
            PyObject *tmp_args_element_value_32;
            PyObject *tmp_expression_value_63;
            PyObject *tmp_subscript_value_63;
            PyObject *tmp_string_concat_values_33;
            PyObject *tmp_tuple_element_33;
            PyObject *tmp_called_value_33;
            PyObject *tmp_args_element_value_33;
            PyObject *tmp_expression_value_65;
            PyObject *tmp_subscript_value_65;
            PyObject *tmp_string_concat_values_34;
            PyObject *tmp_tuple_element_34;
            PyObject *tmp_called_value_34;
            PyObject *tmp_args_element_value_34;
            PyObject *tmp_expression_value_67;
            PyObject *tmp_subscript_value_67;
            PyObject *tmp_string_concat_values_35;
            PyObject *tmp_tuple_element_35;
            PyObject *tmp_called_value_35;
            PyObject *tmp_args_element_value_35;
            PyObject *tmp_expression_value_69;
            PyObject *tmp_subscript_value_69;
            PyObject *tmp_string_concat_values_36;
            PyObject *tmp_tuple_element_36;
            PyObject *tmp_called_value_36;
            PyObject *tmp_args_element_value_36;
            PyObject *tmp_expression_value_71;
            PyObject *tmp_subscript_value_71;
            PyObject *tmp_string_concat_values_37;
            PyObject *tmp_tuple_element_37;
            PyObject *tmp_called_value_37;
            PyObject *tmp_args_element_value_37;
            PyObject *tmp_expression_value_73;
            PyObject *tmp_subscript_value_73;
            PyObject *tmp_string_concat_values_38;
            PyObject *tmp_tuple_element_38;
            PyObject *tmp_called_value_38;
            PyObject *tmp_args_element_value_38;
            PyObject *tmp_expression_value_75;
            PyObject *tmp_subscript_value_75;
            PyObject *tmp_string_concat_values_39;
            PyObject *tmp_tuple_element_39;
            PyObject *tmp_called_value_39;
            PyObject *tmp_args_element_value_39;
            PyObject *tmp_expression_value_77;
            PyObject *tmp_subscript_value_77;
            PyObject *tmp_string_concat_values_40;
            PyObject *tmp_tuple_element_40;
            PyObject *tmp_called_value_40;
            PyObject *tmp_args_element_value_40;
            PyObject *tmp_expression_value_79;
            PyObject *tmp_subscript_value_79;
            PyObject *tmp_string_concat_values_41;
            PyObject *tmp_tuple_element_41;
            PyObject *tmp_called_value_41;
            PyObject *tmp_args_element_value_41;
            PyObject *tmp_expression_value_81;
            PyObject *tmp_subscript_value_81;
            PyObject *tmp_string_concat_values_42;
            PyObject *tmp_tuple_element_42;
            PyObject *tmp_called_value_42;
            PyObject *tmp_args_element_value_42;
            PyObject *tmp_expression_value_83;
            PyObject *tmp_subscript_value_83;
            PyObject *tmp_string_concat_values_43;
            PyObject *tmp_tuple_element_43;
            PyObject *tmp_called_value_43;
            PyObject *tmp_args_element_value_43;
            PyObject *tmp_expression_value_85;
            PyObject *tmp_subscript_value_85;
            PyObject *tmp_string_concat_values_44;
            PyObject *tmp_tuple_element_44;
            PyObject *tmp_called_value_44;
            PyObject *tmp_args_element_value_44;
            PyObject *tmp_expression_value_87;
            PyObject *tmp_subscript_value_87;
            PyObject *tmp_string_concat_values_45;
            PyObject *tmp_tuple_element_45;
            PyObject *tmp_called_value_45;
            PyObject *tmp_args_element_value_45;
            PyObject *tmp_expression_value_89;
            PyObject *tmp_subscript_value_89;
            PyObject *tmp_string_concat_values_46;
            PyObject *tmp_tuple_element_46;
            PyObject *tmp_called_value_46;
            PyObject *tmp_args_element_value_46;
            PyObject *tmp_expression_value_91;
            PyObject *tmp_subscript_value_91;
            PyObject *tmp_string_concat_values_47;
            PyObject *tmp_tuple_element_47;
            PyObject *tmp_called_value_47;
            PyObject *tmp_args_element_value_47;
            PyObject *tmp_expression_value_93;
            PyObject *tmp_subscript_value_93;
            PyObject *tmp_string_concat_values_48;
            PyObject *tmp_tuple_element_48;
            PyObject *tmp_called_value_48;
            PyObject *tmp_args_element_value_48;
            PyObject *tmp_expression_value_95;
            PyObject *tmp_subscript_value_95;
            PyObject *tmp_string_concat_values_49;
            PyObject *tmp_tuple_element_49;
            PyObject *tmp_called_value_49;
            PyObject *tmp_args_element_value_49;
            PyObject *tmp_expression_value_97;
            PyObject *tmp_subscript_value_97;
            PyObject *tmp_string_concat_values_50;
            PyObject *tmp_tuple_element_50;
            PyObject *tmp_called_value_50;
            PyObject *tmp_args_element_value_50;
            PyObject *tmp_expression_value_99;
            PyObject *tmp_subscript_value_99;
            PyObject *tmp_string_concat_values_51;
            PyObject *tmp_tuple_element_51;
            PyObject *tmp_called_value_51;
            PyObject *tmp_args_element_value_51;
            PyObject *tmp_expression_value_101;
            PyObject *tmp_subscript_value_101;
            PyObject *tmp_string_concat_values_52;
            PyObject *tmp_tuple_element_52;
            PyObject *tmp_called_value_52;
            PyObject *tmp_args_element_value_52;
            PyObject *tmp_expression_value_103;
            PyObject *tmp_subscript_value_103;
            PyObject *tmp_string_concat_values_53;
            PyObject *tmp_tuple_element_53;
            PyObject *tmp_called_value_53;
            PyObject *tmp_args_element_value_53;
            PyObject *tmp_expression_value_105;
            PyObject *tmp_subscript_value_105;
            PyObject *tmp_string_concat_values_54;
            PyObject *tmp_tuple_element_54;
            PyObject *tmp_called_value_54;
            PyObject *tmp_args_element_value_54;
            PyObject *tmp_expression_value_107;
            PyObject *tmp_subscript_value_107;
            PyObject *tmp_called_value_55;
            PyObject *tmp_args_element_value_55;
            PyObject *tmp_expression_value_108;
            PyObject *tmp_subscript_value_108;
            PyObject *tmp_called_value_56;
            PyObject *tmp_args_element_value_56;
            PyObject *tmp_expression_value_109;
            PyObject *tmp_subscript_value_109;
            PyObject *tmp_string_concat_values_55;
            PyObject *tmp_tuple_element_55;
            PyObject *tmp_called_value_57;
            PyObject *tmp_args_element_value_57;
            PyObject *tmp_expression_value_111;
            PyObject *tmp_subscript_value_111;
            PyObject *tmp_string_concat_values_56;
            PyObject *tmp_tuple_element_56;
            PyObject *tmp_called_value_58;
            PyObject *tmp_args_element_value_58;
            PyObject *tmp_expression_value_113;
            PyObject *tmp_subscript_value_113;
            PyObject *tmp_string_concat_values_57;
            PyObject *tmp_tuple_element_57;
            PyObject *tmp_called_value_59;
            PyObject *tmp_args_element_value_59;
            PyObject *tmp_expression_value_115;
            PyObject *tmp_subscript_value_115;
            PyObject *tmp_string_concat_values_58;
            PyObject *tmp_tuple_element_58;
            PyObject *tmp_called_value_60;
            PyObject *tmp_args_element_value_60;
            PyObject *tmp_expression_value_117;
            PyObject *tmp_subscript_value_117;
            PyObject *tmp_string_concat_values_59;
            PyObject *tmp_tuple_element_59;
            PyObject *tmp_called_value_61;
            PyObject *tmp_args_element_value_61;
            PyObject *tmp_expression_value_120;
            PyObject *tmp_subscript_value_120;
            PyObject *tmp_args_element_value_62;
            PyObject *tmp_expression_value_121;
            PyObject *tmp_subscript_value_121;
            PyObject *tmp_string_concat_values_60;
            PyObject *tmp_tuple_element_60;
            PyObject *tmp_called_value_62;
            PyObject *tmp_args_element_value_63;
            PyObject *tmp_expression_value_124;
            PyObject *tmp_subscript_value_124;
            PyObject *tmp_args_element_value_64;
            PyObject *tmp_expression_value_125;
            PyObject *tmp_subscript_value_125;
            PyObject *tmp_string_concat_values_61;
            PyObject *tmp_tuple_element_61;
            PyObject *tmp_called_value_63;
            PyObject *tmp_args_element_value_65;
            PyObject *tmp_expression_value_127;
            PyObject *tmp_subscript_value_127;
            PyObject *tmp_string_concat_values_62;
            PyObject *tmp_tuple_element_62;
            PyObject *tmp_called_value_64;
            PyObject *tmp_args_element_value_66;
            PyObject *tmp_expression_value_129;
            PyObject *tmp_subscript_value_129;
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_2 = mod_consts[66];
            tmp_string_concat_values_2 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_2;
                PyObject *tmp_expression_value_2;
                PyObject *tmp_subscript_value_2;
                PyObject *tmp_format_spec_2;
                PyTuple_SET_ITEM0(tmp_string_concat_values_2, 0, tmp_tuple_element_2);
                tmp_expression_value_2 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_2 == NULL)) {
                    tmp_expression_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_2 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 243;

                    goto tuple_build_exception_2;
                }
                tmp_subscript_value_2 = mod_consts[67];
                tmp_format_value_2 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_2, tmp_subscript_value_2);
                if (tmp_format_value_2 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 243;

                    goto tuple_build_exception_2;
                }
                tmp_format_spec_2 = mod_consts[64];
                tmp_tuple_element_2 = BUILTIN_FORMAT(tstate, tmp_format_value_2, tmp_format_spec_2);
                Py_DECREF(tmp_format_value_2);
                if (tmp_tuple_element_2 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 243;

                    goto tuple_build_exception_2;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_2, 1, tmp_tuple_element_2);
                tmp_tuple_element_2 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_2, 2, tmp_tuple_element_2);
            }
            goto tuple_build_noexception_2;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_2:;
            Py_DECREF(tmp_string_concat_values_2);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_2:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_2);
            Py_DECREF(tmp_string_concat_values_2);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 243;

                goto dict_build_exception_1;
            }
            tmp_called_value_2 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[30]);

            if (unlikely(tmp_called_value_2 == NULL)) {
                tmp_called_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[30]);
            }

            if (tmp_called_value_2 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 244;

                goto dict_build_exception_1;
            }
            tmp_expression_value_3 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_3 == NULL)) {
                tmp_expression_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_3 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 244;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_3 = mod_consts[67];
            tmp_args_element_value_2 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_3, tmp_subscript_value_3);
            if (tmp_args_element_value_2 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 244;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 244;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_2, tmp_args_element_value_2);
            Py_DECREF(tmp_args_element_value_2);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 244;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_3 = mod_consts[68];
            tmp_string_concat_values_3 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_3;
                PyObject *tmp_expression_value_4;
                PyObject *tmp_subscript_value_4;
                PyObject *tmp_format_spec_3;
                PyTuple_SET_ITEM0(tmp_string_concat_values_3, 0, tmp_tuple_element_3);
                tmp_expression_value_4 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_4 == NULL)) {
                    tmp_expression_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_4 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 246;

                    goto tuple_build_exception_3;
                }
                tmp_subscript_value_4 = mod_consts[63];
                tmp_format_value_3 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_4, tmp_subscript_value_4);
                if (tmp_format_value_3 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 246;

                    goto tuple_build_exception_3;
                }
                tmp_format_spec_3 = mod_consts[64];
                tmp_tuple_element_3 = BUILTIN_FORMAT(tstate, tmp_format_value_3, tmp_format_spec_3);
                Py_DECREF(tmp_format_value_3);
                if (tmp_tuple_element_3 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 246;

                    goto tuple_build_exception_3;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_3, 1, tmp_tuple_element_3);
                tmp_tuple_element_3 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_3, 2, tmp_tuple_element_3);
            }
            goto tuple_build_noexception_3;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_3:;
            Py_DECREF(tmp_string_concat_values_3);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_3:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_3);
            Py_DECREF(tmp_string_concat_values_3);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 246;

                goto dict_build_exception_1;
            }
            tmp_called_value_3 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[31]);

            if (unlikely(tmp_called_value_3 == NULL)) {
                tmp_called_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[31]);
            }

            if (tmp_called_value_3 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 247;

                goto dict_build_exception_1;
            }
            tmp_expression_value_5 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_5 == NULL)) {
                tmp_expression_value_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_5 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 247;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_5 = mod_consts[63];
            tmp_args_element_value_3 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_5, tmp_subscript_value_5);
            if (tmp_args_element_value_3 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 247;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 247;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_3, tmp_args_element_value_3);
            Py_DECREF(tmp_args_element_value_3);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 247;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_4 = mod_consts[70];
            tmp_string_concat_values_4 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_4;
                PyObject *tmp_expression_value_6;
                PyObject *tmp_subscript_value_6;
                PyObject *tmp_format_spec_4;
                PyTuple_SET_ITEM0(tmp_string_concat_values_4, 0, tmp_tuple_element_4);
                tmp_expression_value_6 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_6 == NULL)) {
                    tmp_expression_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 248;

                    goto tuple_build_exception_4;
                }
                tmp_subscript_value_6 = mod_consts[67];
                tmp_format_value_4 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_6, tmp_subscript_value_6);
                if (tmp_format_value_4 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 248;

                    goto tuple_build_exception_4;
                }
                tmp_format_spec_4 = mod_consts[64];
                tmp_tuple_element_4 = BUILTIN_FORMAT(tstate, tmp_format_value_4, tmp_format_spec_4);
                Py_DECREF(tmp_format_value_4);
                if (tmp_tuple_element_4 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 248;

                    goto tuple_build_exception_4;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_4, 1, tmp_tuple_element_4);
                tmp_tuple_element_4 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_4, 2, tmp_tuple_element_4);
            }
            goto tuple_build_noexception_4;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_4:;
            Py_DECREF(tmp_string_concat_values_4);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_4:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_4);
            Py_DECREF(tmp_string_concat_values_4);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 248;

                goto dict_build_exception_1;
            }
            tmp_called_value_4 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[31]);

            if (unlikely(tmp_called_value_4 == NULL)) {
                tmp_called_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[31]);
            }

            if (tmp_called_value_4 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 249;

                goto dict_build_exception_1;
            }
            tmp_expression_value_7 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_7 == NULL)) {
                tmp_expression_value_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_7 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 249;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_7 = mod_consts[67];
            tmp_args_element_value_4 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_7, tmp_subscript_value_7);
            if (tmp_args_element_value_4 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 249;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 249;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_4, tmp_args_element_value_4);
            Py_DECREF(tmp_args_element_value_4);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 249;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_5 = mod_consts[71];
            tmp_string_concat_values_5 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_5;
                PyObject *tmp_expression_value_8;
                PyObject *tmp_subscript_value_8;
                PyObject *tmp_format_spec_5;
                PyTuple_SET_ITEM0(tmp_string_concat_values_5, 0, tmp_tuple_element_5);
                tmp_expression_value_8 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_8 == NULL)) {
                    tmp_expression_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_8 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 251;

                    goto tuple_build_exception_5;
                }
                tmp_subscript_value_8 = mod_consts[63];
                tmp_format_value_5 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_8, tmp_subscript_value_8);
                if (tmp_format_value_5 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 251;

                    goto tuple_build_exception_5;
                }
                tmp_format_spec_5 = mod_consts[64];
                tmp_tuple_element_5 = BUILTIN_FORMAT(tstate, tmp_format_value_5, tmp_format_spec_5);
                Py_DECREF(tmp_format_value_5);
                if (tmp_tuple_element_5 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 251;

                    goto tuple_build_exception_5;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_5, 1, tmp_tuple_element_5);
                tmp_tuple_element_5 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_5, 2, tmp_tuple_element_5);
            }
            goto tuple_build_noexception_5;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_5:;
            Py_DECREF(tmp_string_concat_values_5);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_5:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_5);
            Py_DECREF(tmp_string_concat_values_5);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 251;

                goto dict_build_exception_1;
            }
            tmp_called_value_5 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[32]);

            if (unlikely(tmp_called_value_5 == NULL)) {
                tmp_called_value_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[32]);
            }

            if (tmp_called_value_5 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 252;

                goto dict_build_exception_1;
            }
            tmp_expression_value_9 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_9 == NULL)) {
                tmp_expression_value_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_9 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 252;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_9 = mod_consts[63];
            tmp_args_element_value_5 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_9, tmp_subscript_value_9);
            if (tmp_args_element_value_5 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 252;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 252;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_5, tmp_args_element_value_5);
            Py_DECREF(tmp_args_element_value_5);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 252;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_6 = mod_consts[73];
            tmp_string_concat_values_6 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_6;
                PyObject *tmp_expression_value_10;
                PyObject *tmp_subscript_value_10;
                PyObject *tmp_format_spec_6;
                PyTuple_SET_ITEM0(tmp_string_concat_values_6, 0, tmp_tuple_element_6);
                tmp_expression_value_10 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_10 == NULL)) {
                    tmp_expression_value_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_10 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 253;

                    goto tuple_build_exception_6;
                }
                tmp_subscript_value_10 = mod_consts[67];
                tmp_format_value_6 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_10, tmp_subscript_value_10);
                if (tmp_format_value_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 253;

                    goto tuple_build_exception_6;
                }
                tmp_format_spec_6 = mod_consts[64];
                tmp_tuple_element_6 = BUILTIN_FORMAT(tstate, tmp_format_value_6, tmp_format_spec_6);
                Py_DECREF(tmp_format_value_6);
                if (tmp_tuple_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 253;

                    goto tuple_build_exception_6;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_6, 1, tmp_tuple_element_6);
                tmp_tuple_element_6 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_6, 2, tmp_tuple_element_6);
            }
            goto tuple_build_noexception_6;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_6:;
            Py_DECREF(tmp_string_concat_values_6);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_6:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_6);
            Py_DECREF(tmp_string_concat_values_6);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 253;

                goto dict_build_exception_1;
            }
            tmp_called_value_6 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[32]);

            if (unlikely(tmp_called_value_6 == NULL)) {
                tmp_called_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[32]);
            }

            if (tmp_called_value_6 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 254;

                goto dict_build_exception_1;
            }
            tmp_expression_value_11 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_11 == NULL)) {
                tmp_expression_value_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_11 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 254;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_11 = mod_consts[67];
            tmp_args_element_value_6 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_11, tmp_subscript_value_11);
            if (tmp_args_element_value_6 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 254;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 254;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_6, tmp_args_element_value_6);
            Py_DECREF(tmp_args_element_value_6);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 254;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_7 = mod_consts[74];
            tmp_string_concat_values_7 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_7;
                PyObject *tmp_expression_value_12;
                PyObject *tmp_subscript_value_12;
                PyObject *tmp_format_spec_7;
                PyTuple_SET_ITEM0(tmp_string_concat_values_7, 0, tmp_tuple_element_7);
                tmp_expression_value_12 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_12 == NULL)) {
                    tmp_expression_value_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_12 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 256;

                    goto tuple_build_exception_7;
                }
                tmp_subscript_value_12 = mod_consts[63];
                tmp_format_value_7 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_12, tmp_subscript_value_12);
                if (tmp_format_value_7 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 256;

                    goto tuple_build_exception_7;
                }
                tmp_format_spec_7 = mod_consts[64];
                tmp_tuple_element_7 = BUILTIN_FORMAT(tstate, tmp_format_value_7, tmp_format_spec_7);
                Py_DECREF(tmp_format_value_7);
                if (tmp_tuple_element_7 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 256;

                    goto tuple_build_exception_7;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_7, 1, tmp_tuple_element_7);
                tmp_tuple_element_7 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_7, 2, tmp_tuple_element_7);
            }
            goto tuple_build_noexception_7;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_7:;
            Py_DECREF(tmp_string_concat_values_7);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_7:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_7);
            Py_DECREF(tmp_string_concat_values_7);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 256;

                goto dict_build_exception_1;
            }
            tmp_called_value_7 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[33]);

            if (unlikely(tmp_called_value_7 == NULL)) {
                tmp_called_value_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[33]);
            }

            if (tmp_called_value_7 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 257;

                goto dict_build_exception_1;
            }
            tmp_expression_value_13 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_13 == NULL)) {
                tmp_expression_value_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_13 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 257;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_13 = mod_consts[63];
            tmp_args_element_value_7 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_13, tmp_subscript_value_13);
            if (tmp_args_element_value_7 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 257;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 257;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_7, tmp_args_element_value_7);
            Py_DECREF(tmp_args_element_value_7);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 257;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_8 = mod_consts[76];
            tmp_string_concat_values_8 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_8;
                PyObject *tmp_expression_value_14;
                PyObject *tmp_subscript_value_14;
                PyObject *tmp_format_spec_8;
                PyTuple_SET_ITEM0(tmp_string_concat_values_8, 0, tmp_tuple_element_8);
                tmp_expression_value_14 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_14 == NULL)) {
                    tmp_expression_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_14 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 258;

                    goto tuple_build_exception_8;
                }
                tmp_subscript_value_14 = mod_consts[67];
                tmp_format_value_8 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_14, tmp_subscript_value_14);
                if (tmp_format_value_8 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 258;

                    goto tuple_build_exception_8;
                }
                tmp_format_spec_8 = mod_consts[64];
                tmp_tuple_element_8 = BUILTIN_FORMAT(tstate, tmp_format_value_8, tmp_format_spec_8);
                Py_DECREF(tmp_format_value_8);
                if (tmp_tuple_element_8 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 258;

                    goto tuple_build_exception_8;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_8, 1, tmp_tuple_element_8);
                tmp_tuple_element_8 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_8, 2, tmp_tuple_element_8);
            }
            goto tuple_build_noexception_8;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_8:;
            Py_DECREF(tmp_string_concat_values_8);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_8:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_8);
            Py_DECREF(tmp_string_concat_values_8);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 258;

                goto dict_build_exception_1;
            }
            tmp_called_value_8 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[33]);

            if (unlikely(tmp_called_value_8 == NULL)) {
                tmp_called_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[33]);
            }

            if (tmp_called_value_8 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 259;

                goto dict_build_exception_1;
            }
            tmp_expression_value_15 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_15 == NULL)) {
                tmp_expression_value_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_15 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 259;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_15 = mod_consts[67];
            tmp_args_element_value_8 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_15, tmp_subscript_value_15);
            if (tmp_args_element_value_8 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 259;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 259;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_8, tmp_args_element_value_8);
            Py_DECREF(tmp_args_element_value_8);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 259;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_9 = mod_consts[77];
            tmp_string_concat_values_9 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_9;
                PyObject *tmp_expression_value_16;
                PyObject *tmp_subscript_value_16;
                PyObject *tmp_format_spec_9;
                PyTuple_SET_ITEM0(tmp_string_concat_values_9, 0, tmp_tuple_element_9);
                tmp_expression_value_16 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_16 == NULL)) {
                    tmp_expression_value_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_16 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 261;

                    goto tuple_build_exception_9;
                }
                tmp_subscript_value_16 = mod_consts[78];
                tmp_format_value_9 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_16, tmp_subscript_value_16);
                if (tmp_format_value_9 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 261;

                    goto tuple_build_exception_9;
                }
                tmp_format_spec_9 = mod_consts[64];
                tmp_tuple_element_9 = BUILTIN_FORMAT(tstate, tmp_format_value_9, tmp_format_spec_9);
                Py_DECREF(tmp_format_value_9);
                if (tmp_tuple_element_9 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 261;

                    goto tuple_build_exception_9;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_9, 1, tmp_tuple_element_9);
                tmp_tuple_element_9 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_9, 2, tmp_tuple_element_9);
            }
            goto tuple_build_noexception_9;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_9:;
            Py_DECREF(tmp_string_concat_values_9);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_9:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_9);
            Py_DECREF(tmp_string_concat_values_9);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 261;

                goto dict_build_exception_1;
            }
            tmp_called_value_9 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[34]);

            if (unlikely(tmp_called_value_9 == NULL)) {
                tmp_called_value_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[34]);
            }

            if (tmp_called_value_9 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 262;

                goto dict_build_exception_1;
            }
            tmp_expression_value_17 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_17 == NULL)) {
                tmp_expression_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_17 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 262;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_17 = mod_consts[78];
            tmp_args_element_value_9 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_17, tmp_subscript_value_17);
            if (tmp_args_element_value_9 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 262;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 262;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_9, tmp_args_element_value_9);
            Py_DECREF(tmp_args_element_value_9);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 262;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_10 = mod_consts[80];
            tmp_string_concat_values_10 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_10;
                PyObject *tmp_expression_value_18;
                PyObject *tmp_subscript_value_18;
                PyObject *tmp_format_spec_10;
                PyTuple_SET_ITEM0(tmp_string_concat_values_10, 0, tmp_tuple_element_10);
                tmp_expression_value_18 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_18 == NULL)) {
                    tmp_expression_value_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_18 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 263;

                    goto tuple_build_exception_10;
                }
                tmp_subscript_value_18 = mod_consts[81];
                tmp_format_value_10 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_18, tmp_subscript_value_18);
                if (tmp_format_value_10 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 263;

                    goto tuple_build_exception_10;
                }
                tmp_format_spec_10 = mod_consts[64];
                tmp_tuple_element_10 = BUILTIN_FORMAT(tstate, tmp_format_value_10, tmp_format_spec_10);
                Py_DECREF(tmp_format_value_10);
                if (tmp_tuple_element_10 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 263;

                    goto tuple_build_exception_10;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_10, 1, tmp_tuple_element_10);
                tmp_tuple_element_10 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_10, 2, tmp_tuple_element_10);
            }
            goto tuple_build_noexception_10;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_10:;
            Py_DECREF(tmp_string_concat_values_10);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_10:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_10);
            Py_DECREF(tmp_string_concat_values_10);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 263;

                goto dict_build_exception_1;
            }
            tmp_called_value_10 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[34]);

            if (unlikely(tmp_called_value_10 == NULL)) {
                tmp_called_value_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[34]);
            }

            if (tmp_called_value_10 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 264;

                goto dict_build_exception_1;
            }
            tmp_expression_value_19 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_19 == NULL)) {
                tmp_expression_value_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_19 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 264;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_19 = mod_consts[81];
            tmp_args_element_value_10 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_19, tmp_subscript_value_19);
            if (tmp_args_element_value_10 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 264;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 264;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_10, tmp_args_element_value_10);
            Py_DECREF(tmp_args_element_value_10);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 264;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_11 = mod_consts[82];
            tmp_string_concat_values_11 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_11;
                PyObject *tmp_expression_value_20;
                PyObject *tmp_subscript_value_20;
                PyObject *tmp_format_spec_11;
                PyTuple_SET_ITEM0(tmp_string_concat_values_11, 0, tmp_tuple_element_11);
                tmp_expression_value_20 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_20 == NULL)) {
                    tmp_expression_value_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_20 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 266;

                    goto tuple_build_exception_11;
                }
                tmp_subscript_value_20 = mod_consts[83];
                tmp_format_value_11 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_20, tmp_subscript_value_20);
                if (tmp_format_value_11 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 266;

                    goto tuple_build_exception_11;
                }
                tmp_format_spec_11 = mod_consts[64];
                tmp_tuple_element_11 = BUILTIN_FORMAT(tstate, tmp_format_value_11, tmp_format_spec_11);
                Py_DECREF(tmp_format_value_11);
                if (tmp_tuple_element_11 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 266;

                    goto tuple_build_exception_11;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_11, 1, tmp_tuple_element_11);
                tmp_tuple_element_11 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_11, 2, tmp_tuple_element_11);
            }
            goto tuple_build_noexception_11;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_11:;
            Py_DECREF(tmp_string_concat_values_11);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_11:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_11);
            Py_DECREF(tmp_string_concat_values_11);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 266;

                goto dict_build_exception_1;
            }
            tmp_called_value_11 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[35]);

            if (unlikely(tmp_called_value_11 == NULL)) {
                tmp_called_value_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[35]);
            }

            if (tmp_called_value_11 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 267;

                goto dict_build_exception_1;
            }
            tmp_expression_value_21 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_21 == NULL)) {
                tmp_expression_value_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_21 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 267;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_21 = mod_consts[83];
            tmp_args_element_value_11 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_21, tmp_subscript_value_21);
            if (tmp_args_element_value_11 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 267;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 267;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_11, tmp_args_element_value_11);
            Py_DECREF(tmp_args_element_value_11);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 267;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_12 = mod_consts[85];
            tmp_string_concat_values_12 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_12;
                PyObject *tmp_expression_value_22;
                PyObject *tmp_subscript_value_22;
                PyObject *tmp_format_spec_12;
                PyTuple_SET_ITEM0(tmp_string_concat_values_12, 0, tmp_tuple_element_12);
                tmp_expression_value_22 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_22 == NULL)) {
                    tmp_expression_value_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_22 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 268;

                    goto tuple_build_exception_12;
                }
                tmp_subscript_value_22 = mod_consts[86];
                tmp_format_value_12 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_22, tmp_subscript_value_22);
                if (tmp_format_value_12 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 268;

                    goto tuple_build_exception_12;
                }
                tmp_format_spec_12 = mod_consts[64];
                tmp_tuple_element_12 = BUILTIN_FORMAT(tstate, tmp_format_value_12, tmp_format_spec_12);
                Py_DECREF(tmp_format_value_12);
                if (tmp_tuple_element_12 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 268;

                    goto tuple_build_exception_12;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_12, 1, tmp_tuple_element_12);
                tmp_tuple_element_12 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_12, 2, tmp_tuple_element_12);
            }
            goto tuple_build_noexception_12;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_12:;
            Py_DECREF(tmp_string_concat_values_12);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_12:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_12);
            Py_DECREF(tmp_string_concat_values_12);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 268;

                goto dict_build_exception_1;
            }
            tmp_called_value_12 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[35]);

            if (unlikely(tmp_called_value_12 == NULL)) {
                tmp_called_value_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[35]);
            }

            if (tmp_called_value_12 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 269;

                goto dict_build_exception_1;
            }
            tmp_expression_value_23 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_23 == NULL)) {
                tmp_expression_value_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_23 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 269;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_23 = mod_consts[86];
            tmp_args_element_value_12 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_23, tmp_subscript_value_23);
            if (tmp_args_element_value_12 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 269;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 269;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_12, tmp_args_element_value_12);
            Py_DECREF(tmp_args_element_value_12);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 269;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_13 = mod_consts[87];
            tmp_string_concat_values_13 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_13;
                PyObject *tmp_expression_value_24;
                PyObject *tmp_subscript_value_24;
                PyObject *tmp_format_spec_13;
                PyTuple_SET_ITEM0(tmp_string_concat_values_13, 0, tmp_tuple_element_13);
                tmp_expression_value_24 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_24 == NULL)) {
                    tmp_expression_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_24 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 271;

                    goto tuple_build_exception_13;
                }
                tmp_subscript_value_24 = mod_consts[88];
                tmp_format_value_13 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_24, tmp_subscript_value_24);
                if (tmp_format_value_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 271;

                    goto tuple_build_exception_13;
                }
                tmp_format_spec_13 = mod_consts[64];
                tmp_tuple_element_13 = BUILTIN_FORMAT(tstate, tmp_format_value_13, tmp_format_spec_13);
                Py_DECREF(tmp_format_value_13);
                if (tmp_tuple_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 271;

                    goto tuple_build_exception_13;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_13, 1, tmp_tuple_element_13);
                tmp_tuple_element_13 = mod_consts[89];
                PyTuple_SET_ITEM0(tmp_string_concat_values_13, 2, tmp_tuple_element_13);
            }
            goto tuple_build_noexception_13;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_13:;
            Py_DECREF(tmp_string_concat_values_13);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_13:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_13);
            Py_DECREF(tmp_string_concat_values_13);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 271;

                goto dict_build_exception_1;
            }
            tmp_called_value_13 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[36]);

            if (unlikely(tmp_called_value_13 == NULL)) {
                tmp_called_value_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[36]);
            }

            if (tmp_called_value_13 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 272;

                goto dict_build_exception_1;
            }
            tmp_expression_value_25 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_25 == NULL)) {
                tmp_expression_value_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_25 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 272;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_25 = mod_consts[88];
            tmp_args_element_value_13 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_25, tmp_subscript_value_25);
            if (tmp_args_element_value_13 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 272;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 272;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_13, tmp_args_element_value_13);
            Py_DECREF(tmp_args_element_value_13);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 272;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_14 = mod_consts[90];
            tmp_string_concat_values_14 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_14;
                PyObject *tmp_expression_value_26;
                PyObject *tmp_subscript_value_26;
                PyObject *tmp_format_spec_14;
                PyTuple_SET_ITEM0(tmp_string_concat_values_14, 0, tmp_tuple_element_14);
                tmp_expression_value_26 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_26 == NULL)) {
                    tmp_expression_value_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_26 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 273;

                    goto tuple_build_exception_14;
                }
                tmp_subscript_value_26 = mod_consts[88];
                tmp_format_value_14 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_26, tmp_subscript_value_26);
                if (tmp_format_value_14 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 273;

                    goto tuple_build_exception_14;
                }
                tmp_format_spec_14 = mod_consts[64];
                tmp_tuple_element_14 = BUILTIN_FORMAT(tstate, tmp_format_value_14, tmp_format_spec_14);
                Py_DECREF(tmp_format_value_14);
                if (tmp_tuple_element_14 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 273;

                    goto tuple_build_exception_14;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_14, 1, tmp_tuple_element_14);
                tmp_tuple_element_14 = mod_consts[91];
                PyTuple_SET_ITEM0(tmp_string_concat_values_14, 2, tmp_tuple_element_14);
            }
            goto tuple_build_noexception_14;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_14:;
            Py_DECREF(tmp_string_concat_values_14);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_14:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_14);
            Py_DECREF(tmp_string_concat_values_14);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 273;

                goto dict_build_exception_1;
            }
            tmp_called_value_14 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[37]);

            if (unlikely(tmp_called_value_14 == NULL)) {
                tmp_called_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[37]);
            }

            if (tmp_called_value_14 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 274;

                goto dict_build_exception_1;
            }
            tmp_expression_value_27 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_27 == NULL)) {
                tmp_expression_value_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_27 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 274;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_27 = mod_consts[88];
            tmp_args_element_value_14 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_27, tmp_subscript_value_27);
            if (tmp_args_element_value_14 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 274;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 274;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_14, tmp_args_element_value_14);
            Py_DECREF(tmp_args_element_value_14);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 274;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_15 = mod_consts[92];
            tmp_string_concat_values_15 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_15;
                PyObject *tmp_expression_value_28;
                PyObject *tmp_subscript_value_28;
                PyObject *tmp_format_spec_15;
                PyTuple_SET_ITEM0(tmp_string_concat_values_15, 0, tmp_tuple_element_15);
                tmp_expression_value_28 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_28 == NULL)) {
                    tmp_expression_value_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_28 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 275;

                    goto tuple_build_exception_15;
                }
                tmp_subscript_value_28 = mod_consts[88];
                tmp_format_value_15 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_28, tmp_subscript_value_28);
                if (tmp_format_value_15 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 275;

                    goto tuple_build_exception_15;
                }
                tmp_format_spec_15 = mod_consts[64];
                tmp_tuple_element_15 = BUILTIN_FORMAT(tstate, tmp_format_value_15, tmp_format_spec_15);
                Py_DECREF(tmp_format_value_15);
                if (tmp_tuple_element_15 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 275;

                    goto tuple_build_exception_15;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_15, 1, tmp_tuple_element_15);
                tmp_tuple_element_15 = mod_consts[93];
                PyTuple_SET_ITEM0(tmp_string_concat_values_15, 2, tmp_tuple_element_15);
            }
            goto tuple_build_noexception_15;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_15:;
            Py_DECREF(tmp_string_concat_values_15);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_15:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_15);
            Py_DECREF(tmp_string_concat_values_15);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 275;

                goto dict_build_exception_1;
            }
            tmp_called_value_15 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[38]);

            if (unlikely(tmp_called_value_15 == NULL)) {
                tmp_called_value_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[38]);
            }

            if (tmp_called_value_15 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 276;

                goto dict_build_exception_1;
            }
            tmp_expression_value_29 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_29 == NULL)) {
                tmp_expression_value_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_29 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 276;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_29 = mod_consts[88];
            tmp_args_element_value_15 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_29, tmp_subscript_value_29);
            if (tmp_args_element_value_15 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 276;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 276;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_15, tmp_args_element_value_15);
            Py_DECREF(tmp_args_element_value_15);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 276;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_16 = mod_consts[94];
            tmp_string_concat_values_16 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_16;
                PyObject *tmp_expression_value_30;
                PyObject *tmp_subscript_value_30;
                PyObject *tmp_format_spec_16;
                PyTuple_SET_ITEM0(tmp_string_concat_values_16, 0, tmp_tuple_element_16);
                tmp_expression_value_30 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_30 == NULL)) {
                    tmp_expression_value_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_30 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 277;

                    goto tuple_build_exception_16;
                }
                tmp_subscript_value_30 = mod_consts[88];
                tmp_format_value_16 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_30, tmp_subscript_value_30);
                if (tmp_format_value_16 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 277;

                    goto tuple_build_exception_16;
                }
                tmp_format_spec_16 = mod_consts[64];
                tmp_tuple_element_16 = BUILTIN_FORMAT(tstate, tmp_format_value_16, tmp_format_spec_16);
                Py_DECREF(tmp_format_value_16);
                if (tmp_tuple_element_16 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 277;

                    goto tuple_build_exception_16;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_16, 1, tmp_tuple_element_16);
                tmp_tuple_element_16 = mod_consts[95];
                PyTuple_SET_ITEM0(tmp_string_concat_values_16, 2, tmp_tuple_element_16);
            }
            goto tuple_build_noexception_16;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_16:;
            Py_DECREF(tmp_string_concat_values_16);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_16:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_16);
            Py_DECREF(tmp_string_concat_values_16);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 277;

                goto dict_build_exception_1;
            }
            tmp_called_value_16 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[39]);

            if (unlikely(tmp_called_value_16 == NULL)) {
                tmp_called_value_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[39]);
            }

            if (tmp_called_value_16 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 278;

                goto dict_build_exception_1;
            }
            tmp_expression_value_31 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_31 == NULL)) {
                tmp_expression_value_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_31 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 278;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_31 = mod_consts[88];
            tmp_args_element_value_16 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_31, tmp_subscript_value_31);
            if (tmp_args_element_value_16 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 278;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 278;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_16, tmp_args_element_value_16);
            Py_DECREF(tmp_args_element_value_16);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 278;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_17 = mod_consts[96];
            tmp_string_concat_values_17 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_17;
                PyObject *tmp_expression_value_32;
                PyObject *tmp_subscript_value_32;
                PyObject *tmp_format_spec_17;
                PyTuple_SET_ITEM0(tmp_string_concat_values_17, 0, tmp_tuple_element_17);
                tmp_expression_value_32 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_32 == NULL)) {
                    tmp_expression_value_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_32 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 279;

                    goto tuple_build_exception_17;
                }
                tmp_subscript_value_32 = mod_consts[97];
                tmp_format_value_17 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_32, tmp_subscript_value_32);
                if (tmp_format_value_17 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 279;

                    goto tuple_build_exception_17;
                }
                tmp_format_spec_17 = mod_consts[64];
                tmp_tuple_element_17 = BUILTIN_FORMAT(tstate, tmp_format_value_17, tmp_format_spec_17);
                Py_DECREF(tmp_format_value_17);
                if (tmp_tuple_element_17 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 279;

                    goto tuple_build_exception_17;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_17, 1, tmp_tuple_element_17);
                tmp_tuple_element_17 = mod_consts[89];
                PyTuple_SET_ITEM0(tmp_string_concat_values_17, 2, tmp_tuple_element_17);
            }
            goto tuple_build_noexception_17;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_17:;
            Py_DECREF(tmp_string_concat_values_17);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_17:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_17);
            Py_DECREF(tmp_string_concat_values_17);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 279;

                goto dict_build_exception_1;
            }
            tmp_called_value_17 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[36]);

            if (unlikely(tmp_called_value_17 == NULL)) {
                tmp_called_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[36]);
            }

            if (tmp_called_value_17 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 280;

                goto dict_build_exception_1;
            }
            tmp_expression_value_33 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_33 == NULL)) {
                tmp_expression_value_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_33 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 280;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_33 = mod_consts[97];
            tmp_args_element_value_17 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_33, tmp_subscript_value_33);
            if (tmp_args_element_value_17 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 280;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 280;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_17, tmp_args_element_value_17);
            Py_DECREF(tmp_args_element_value_17);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 280;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_18 = mod_consts[98];
            tmp_string_concat_values_18 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_18;
                PyObject *tmp_expression_value_34;
                PyObject *tmp_subscript_value_34;
                PyObject *tmp_format_spec_18;
                PyTuple_SET_ITEM0(tmp_string_concat_values_18, 0, tmp_tuple_element_18);
                tmp_expression_value_34 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_34 == NULL)) {
                    tmp_expression_value_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_34 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 281;

                    goto tuple_build_exception_18;
                }
                tmp_subscript_value_34 = mod_consts[97];
                tmp_format_value_18 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_34, tmp_subscript_value_34);
                if (tmp_format_value_18 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 281;

                    goto tuple_build_exception_18;
                }
                tmp_format_spec_18 = mod_consts[64];
                tmp_tuple_element_18 = BUILTIN_FORMAT(tstate, tmp_format_value_18, tmp_format_spec_18);
                Py_DECREF(tmp_format_value_18);
                if (tmp_tuple_element_18 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 281;

                    goto tuple_build_exception_18;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_18, 1, tmp_tuple_element_18);
                tmp_tuple_element_18 = mod_consts[91];
                PyTuple_SET_ITEM0(tmp_string_concat_values_18, 2, tmp_tuple_element_18);
            }
            goto tuple_build_noexception_18;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_18:;
            Py_DECREF(tmp_string_concat_values_18);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_18:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_18);
            Py_DECREF(tmp_string_concat_values_18);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 281;

                goto dict_build_exception_1;
            }
            tmp_called_value_18 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[37]);

            if (unlikely(tmp_called_value_18 == NULL)) {
                tmp_called_value_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[37]);
            }

            if (tmp_called_value_18 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 282;

                goto dict_build_exception_1;
            }
            tmp_expression_value_35 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_35 == NULL)) {
                tmp_expression_value_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_35 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 282;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_35 = mod_consts[97];
            tmp_args_element_value_18 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_35, tmp_subscript_value_35);
            if (tmp_args_element_value_18 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 282;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 282;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_18, tmp_args_element_value_18);
            Py_DECREF(tmp_args_element_value_18);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 282;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_19 = mod_consts[99];
            tmp_string_concat_values_19 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_19;
                PyObject *tmp_expression_value_36;
                PyObject *tmp_subscript_value_36;
                PyObject *tmp_format_spec_19;
                PyTuple_SET_ITEM0(tmp_string_concat_values_19, 0, tmp_tuple_element_19);
                tmp_expression_value_36 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_36 == NULL)) {
                    tmp_expression_value_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_36 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 283;

                    goto tuple_build_exception_19;
                }
                tmp_subscript_value_36 = mod_consts[97];
                tmp_format_value_19 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_36, tmp_subscript_value_36);
                if (tmp_format_value_19 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 283;

                    goto tuple_build_exception_19;
                }
                tmp_format_spec_19 = mod_consts[64];
                tmp_tuple_element_19 = BUILTIN_FORMAT(tstate, tmp_format_value_19, tmp_format_spec_19);
                Py_DECREF(tmp_format_value_19);
                if (tmp_tuple_element_19 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 283;

                    goto tuple_build_exception_19;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_19, 1, tmp_tuple_element_19);
                tmp_tuple_element_19 = mod_consts[93];
                PyTuple_SET_ITEM0(tmp_string_concat_values_19, 2, tmp_tuple_element_19);
            }
            goto tuple_build_noexception_19;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_19:;
            Py_DECREF(tmp_string_concat_values_19);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_19:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_19);
            Py_DECREF(tmp_string_concat_values_19);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 283;

                goto dict_build_exception_1;
            }
            tmp_called_value_19 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[38]);

            if (unlikely(tmp_called_value_19 == NULL)) {
                tmp_called_value_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[38]);
            }

            if (tmp_called_value_19 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 284;

                goto dict_build_exception_1;
            }
            tmp_expression_value_37 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_37 == NULL)) {
                tmp_expression_value_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_37 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 284;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_37 = mod_consts[97];
            tmp_args_element_value_19 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_37, tmp_subscript_value_37);
            if (tmp_args_element_value_19 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 284;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 284;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_19, tmp_args_element_value_19);
            Py_DECREF(tmp_args_element_value_19);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 284;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_20 = mod_consts[100];
            tmp_string_concat_values_20 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_20;
                PyObject *tmp_expression_value_38;
                PyObject *tmp_subscript_value_38;
                PyObject *tmp_format_spec_20;
                PyTuple_SET_ITEM0(tmp_string_concat_values_20, 0, tmp_tuple_element_20);
                tmp_expression_value_38 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_38 == NULL)) {
                    tmp_expression_value_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_38 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 285;

                    goto tuple_build_exception_20;
                }
                tmp_subscript_value_38 = mod_consts[97];
                tmp_format_value_20 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_38, tmp_subscript_value_38);
                if (tmp_format_value_20 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 285;

                    goto tuple_build_exception_20;
                }
                tmp_format_spec_20 = mod_consts[64];
                tmp_tuple_element_20 = BUILTIN_FORMAT(tstate, tmp_format_value_20, tmp_format_spec_20);
                Py_DECREF(tmp_format_value_20);
                if (tmp_tuple_element_20 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 285;

                    goto tuple_build_exception_20;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_20, 1, tmp_tuple_element_20);
                tmp_tuple_element_20 = mod_consts[95];
                PyTuple_SET_ITEM0(tmp_string_concat_values_20, 2, tmp_tuple_element_20);
            }
            goto tuple_build_noexception_20;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_20:;
            Py_DECREF(tmp_string_concat_values_20);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_20:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_20);
            Py_DECREF(tmp_string_concat_values_20);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 285;

                goto dict_build_exception_1;
            }
            tmp_called_value_20 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[39]);

            if (unlikely(tmp_called_value_20 == NULL)) {
                tmp_called_value_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[39]);
            }

            if (tmp_called_value_20 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 286;

                goto dict_build_exception_1;
            }
            tmp_expression_value_39 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_39 == NULL)) {
                tmp_expression_value_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_39 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 286;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_39 = mod_consts[97];
            tmp_args_element_value_20 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_39, tmp_subscript_value_39);
            if (tmp_args_element_value_20 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 286;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 286;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_20, tmp_args_element_value_20);
            Py_DECREF(tmp_args_element_value_20);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 286;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_21 = mod_consts[101];
            tmp_string_concat_values_21 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_21;
                PyObject *tmp_expression_value_40;
                PyObject *tmp_subscript_value_40;
                PyObject *tmp_format_spec_21;
                PyTuple_SET_ITEM0(tmp_string_concat_values_21, 0, tmp_tuple_element_21);
                tmp_expression_value_40 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_40 == NULL)) {
                    tmp_expression_value_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_40 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 288;

                    goto tuple_build_exception_21;
                }
                tmp_subscript_value_40 = mod_consts[102];
                tmp_format_value_21 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_40, tmp_subscript_value_40);
                if (tmp_format_value_21 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 288;

                    goto tuple_build_exception_21;
                }
                tmp_format_spec_21 = mod_consts[64];
                tmp_tuple_element_21 = BUILTIN_FORMAT(tstate, tmp_format_value_21, tmp_format_spec_21);
                Py_DECREF(tmp_format_value_21);
                if (tmp_tuple_element_21 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 288;

                    goto tuple_build_exception_21;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_21, 1, tmp_tuple_element_21);
                tmp_tuple_element_21 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_21, 2, tmp_tuple_element_21);
            }
            goto tuple_build_noexception_21;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_21:;
            Py_DECREF(tmp_string_concat_values_21);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_21:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_21);
            Py_DECREF(tmp_string_concat_values_21);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 288;

                goto dict_build_exception_1;
            }
            tmp_called_value_21 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[40]);

            if (unlikely(tmp_called_value_21 == NULL)) {
                tmp_called_value_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[40]);
            }

            if (tmp_called_value_21 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 289;

                goto dict_build_exception_1;
            }
            tmp_expression_value_41 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_41 == NULL)) {
                tmp_expression_value_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_41 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 289;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_41 = mod_consts[102];
            tmp_args_element_value_21 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_41, tmp_subscript_value_41);
            if (tmp_args_element_value_21 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 289;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 289;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_21, tmp_args_element_value_21);
            Py_DECREF(tmp_args_element_value_21);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 289;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_22 = mod_consts[103];
            tmp_string_concat_values_22 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_22;
                PyObject *tmp_expression_value_42;
                PyObject *tmp_subscript_value_42;
                PyObject *tmp_format_spec_22;
                PyTuple_SET_ITEM0(tmp_string_concat_values_22, 0, tmp_tuple_element_22);
                tmp_expression_value_42 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_42 == NULL)) {
                    tmp_expression_value_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_42 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 290;

                    goto tuple_build_exception_22;
                }
                tmp_subscript_value_42 = mod_consts[104];
                tmp_format_value_22 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_42, tmp_subscript_value_42);
                if (tmp_format_value_22 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 290;

                    goto tuple_build_exception_22;
                }
                tmp_format_spec_22 = mod_consts[64];
                tmp_tuple_element_22 = BUILTIN_FORMAT(tstate, tmp_format_value_22, tmp_format_spec_22);
                Py_DECREF(tmp_format_value_22);
                if (tmp_tuple_element_22 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 290;

                    goto tuple_build_exception_22;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_22, 1, tmp_tuple_element_22);
                tmp_tuple_element_22 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_22, 2, tmp_tuple_element_22);
            }
            goto tuple_build_noexception_22;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_22:;
            Py_DECREF(tmp_string_concat_values_22);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_22:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_22);
            Py_DECREF(tmp_string_concat_values_22);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 290;

                goto dict_build_exception_1;
            }
            tmp_called_value_22 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[40]);

            if (unlikely(tmp_called_value_22 == NULL)) {
                tmp_called_value_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[40]);
            }

            if (tmp_called_value_22 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 291;

                goto dict_build_exception_1;
            }
            tmp_expression_value_43 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_43 == NULL)) {
                tmp_expression_value_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_43 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 291;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_43 = mod_consts[104];
            tmp_args_element_value_22 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_43, tmp_subscript_value_43);
            if (tmp_args_element_value_22 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 291;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 291;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_22, tmp_args_element_value_22);
            Py_DECREF(tmp_args_element_value_22);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 291;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_23 = mod_consts[105];
            tmp_string_concat_values_23 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_23;
                PyObject *tmp_expression_value_44;
                PyObject *tmp_subscript_value_44;
                PyObject *tmp_format_spec_23;
                PyTuple_SET_ITEM0(tmp_string_concat_values_23, 0, tmp_tuple_element_23);
                tmp_expression_value_44 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_44 == NULL)) {
                    tmp_expression_value_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_44 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 293;

                    goto tuple_build_exception_23;
                }
                tmp_subscript_value_44 = mod_consts[102];
                tmp_format_value_23 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_44, tmp_subscript_value_44);
                if (tmp_format_value_23 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 293;

                    goto tuple_build_exception_23;
                }
                tmp_format_spec_23 = mod_consts[64];
                tmp_tuple_element_23 = BUILTIN_FORMAT(tstate, tmp_format_value_23, tmp_format_spec_23);
                Py_DECREF(tmp_format_value_23);
                if (tmp_tuple_element_23 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 293;

                    goto tuple_build_exception_23;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_23, 1, tmp_tuple_element_23);
                tmp_tuple_element_23 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_23, 2, tmp_tuple_element_23);
            }
            goto tuple_build_noexception_23;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_23:;
            Py_DECREF(tmp_string_concat_values_23);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_23:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_23);
            Py_DECREF(tmp_string_concat_values_23);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 293;

                goto dict_build_exception_1;
            }
            tmp_called_value_23 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[41]);

            if (unlikely(tmp_called_value_23 == NULL)) {
                tmp_called_value_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[41]);
            }

            if (tmp_called_value_23 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 294;

                goto dict_build_exception_1;
            }
            tmp_expression_value_45 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_45 == NULL)) {
                tmp_expression_value_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_45 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 294;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_45 = mod_consts[102];
            tmp_args_element_value_23 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_45, tmp_subscript_value_45);
            if (tmp_args_element_value_23 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 294;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 294;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_23, tmp_args_element_value_23);
            Py_DECREF(tmp_args_element_value_23);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 294;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_24 = mod_consts[106];
            tmp_string_concat_values_24 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_24;
                PyObject *tmp_expression_value_46;
                PyObject *tmp_subscript_value_46;
                PyObject *tmp_format_spec_24;
                PyTuple_SET_ITEM0(tmp_string_concat_values_24, 0, tmp_tuple_element_24);
                tmp_expression_value_46 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_46 == NULL)) {
                    tmp_expression_value_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_46 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 295;

                    goto tuple_build_exception_24;
                }
                tmp_subscript_value_46 = mod_consts[104];
                tmp_format_value_24 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_46, tmp_subscript_value_46);
                if (tmp_format_value_24 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 295;

                    goto tuple_build_exception_24;
                }
                tmp_format_spec_24 = mod_consts[64];
                tmp_tuple_element_24 = BUILTIN_FORMAT(tstate, tmp_format_value_24, tmp_format_spec_24);
                Py_DECREF(tmp_format_value_24);
                if (tmp_tuple_element_24 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 295;

                    goto tuple_build_exception_24;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_24, 1, tmp_tuple_element_24);
                tmp_tuple_element_24 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_24, 2, tmp_tuple_element_24);
            }
            goto tuple_build_noexception_24;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_24:;
            Py_DECREF(tmp_string_concat_values_24);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_24:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_24);
            Py_DECREF(tmp_string_concat_values_24);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 295;

                goto dict_build_exception_1;
            }
            tmp_called_value_24 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[41]);

            if (unlikely(tmp_called_value_24 == NULL)) {
                tmp_called_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[41]);
            }

            if (tmp_called_value_24 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 296;

                goto dict_build_exception_1;
            }
            tmp_expression_value_47 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_47 == NULL)) {
                tmp_expression_value_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_47 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 296;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_47 = mod_consts[104];
            tmp_args_element_value_24 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_47, tmp_subscript_value_47);
            if (tmp_args_element_value_24 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 296;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 296;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_24, tmp_args_element_value_24);
            Py_DECREF(tmp_args_element_value_24);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 296;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_25 = mod_consts[107];
            tmp_string_concat_values_25 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_25;
                PyObject *tmp_expression_value_48;
                PyObject *tmp_subscript_value_48;
                PyObject *tmp_format_spec_25;
                PyTuple_SET_ITEM0(tmp_string_concat_values_25, 0, tmp_tuple_element_25);
                tmp_expression_value_48 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_48 == NULL)) {
                    tmp_expression_value_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_48 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 298;

                    goto tuple_build_exception_25;
                }
                tmp_subscript_value_48 = mod_consts[102];
                tmp_format_value_25 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_48, tmp_subscript_value_48);
                if (tmp_format_value_25 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 298;

                    goto tuple_build_exception_25;
                }
                tmp_format_spec_25 = mod_consts[64];
                tmp_tuple_element_25 = BUILTIN_FORMAT(tstate, tmp_format_value_25, tmp_format_spec_25);
                Py_DECREF(tmp_format_value_25);
                if (tmp_tuple_element_25 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 298;

                    goto tuple_build_exception_25;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_25, 1, tmp_tuple_element_25);
                tmp_tuple_element_25 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_25, 2, tmp_tuple_element_25);
            }
            goto tuple_build_noexception_25;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_25:;
            Py_DECREF(tmp_string_concat_values_25);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_25:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_25);
            Py_DECREF(tmp_string_concat_values_25);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 298;

                goto dict_build_exception_1;
            }
            tmp_called_value_25 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[42]);

            if (unlikely(tmp_called_value_25 == NULL)) {
                tmp_called_value_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[42]);
            }

            if (tmp_called_value_25 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 299;

                goto dict_build_exception_1;
            }
            tmp_expression_value_49 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_49 == NULL)) {
                tmp_expression_value_49 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_49 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 299;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_49 = mod_consts[102];
            tmp_args_element_value_25 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_49, tmp_subscript_value_49);
            if (tmp_args_element_value_25 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 299;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 299;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_25, tmp_args_element_value_25);
            Py_DECREF(tmp_args_element_value_25);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 299;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_26 = mod_consts[108];
            tmp_string_concat_values_26 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_26;
                PyObject *tmp_expression_value_50;
                PyObject *tmp_subscript_value_50;
                PyObject *tmp_format_spec_26;
                PyTuple_SET_ITEM0(tmp_string_concat_values_26, 0, tmp_tuple_element_26);
                tmp_expression_value_50 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_50 == NULL)) {
                    tmp_expression_value_50 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_50 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 300;

                    goto tuple_build_exception_26;
                }
                tmp_subscript_value_50 = mod_consts[104];
                tmp_format_value_26 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_50, tmp_subscript_value_50);
                if (tmp_format_value_26 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 300;

                    goto tuple_build_exception_26;
                }
                tmp_format_spec_26 = mod_consts[64];
                tmp_tuple_element_26 = BUILTIN_FORMAT(tstate, tmp_format_value_26, tmp_format_spec_26);
                Py_DECREF(tmp_format_value_26);
                if (tmp_tuple_element_26 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 300;

                    goto tuple_build_exception_26;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_26, 1, tmp_tuple_element_26);
                tmp_tuple_element_26 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_26, 2, tmp_tuple_element_26);
            }
            goto tuple_build_noexception_26;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_26:;
            Py_DECREF(tmp_string_concat_values_26);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_26:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_26);
            Py_DECREF(tmp_string_concat_values_26);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 300;

                goto dict_build_exception_1;
            }
            tmp_called_value_26 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[42]);

            if (unlikely(tmp_called_value_26 == NULL)) {
                tmp_called_value_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[42]);
            }

            if (tmp_called_value_26 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 301;

                goto dict_build_exception_1;
            }
            tmp_expression_value_51 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_51 == NULL)) {
                tmp_expression_value_51 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_51 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 301;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_51 = mod_consts[104];
            tmp_args_element_value_26 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_51, tmp_subscript_value_51);
            if (tmp_args_element_value_26 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 301;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 301;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_26, tmp_args_element_value_26);
            Py_DECREF(tmp_args_element_value_26);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 301;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_27 = mod_consts[109];
            tmp_string_concat_values_27 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_27;
                PyObject *tmp_expression_value_52;
                PyObject *tmp_subscript_value_52;
                PyObject *tmp_format_spec_27;
                PyTuple_SET_ITEM0(tmp_string_concat_values_27, 0, tmp_tuple_element_27);
                tmp_expression_value_52 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_52 == NULL)) {
                    tmp_expression_value_52 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_52 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 303;

                    goto tuple_build_exception_27;
                }
                tmp_subscript_value_52 = mod_consts[102];
                tmp_format_value_27 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_52, tmp_subscript_value_52);
                if (tmp_format_value_27 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 303;

                    goto tuple_build_exception_27;
                }
                tmp_format_spec_27 = mod_consts[64];
                tmp_tuple_element_27 = BUILTIN_FORMAT(tstate, tmp_format_value_27, tmp_format_spec_27);
                Py_DECREF(tmp_format_value_27);
                if (tmp_tuple_element_27 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 303;

                    goto tuple_build_exception_27;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_27, 1, tmp_tuple_element_27);
                tmp_tuple_element_27 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_27, 2, tmp_tuple_element_27);
            }
            goto tuple_build_noexception_27;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_27:;
            Py_DECREF(tmp_string_concat_values_27);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_27:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_27);
            Py_DECREF(tmp_string_concat_values_27);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 303;

                goto dict_build_exception_1;
            }
            tmp_called_value_27 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[43]);

            if (unlikely(tmp_called_value_27 == NULL)) {
                tmp_called_value_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[43]);
            }

            if (tmp_called_value_27 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 304;

                goto dict_build_exception_1;
            }
            tmp_expression_value_53 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_53 == NULL)) {
                tmp_expression_value_53 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_53 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 304;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_53 = mod_consts[102];
            tmp_args_element_value_27 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_53, tmp_subscript_value_53);
            if (tmp_args_element_value_27 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 304;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 304;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_27, tmp_args_element_value_27);
            Py_DECREF(tmp_args_element_value_27);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 304;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_28 = mod_consts[110];
            tmp_string_concat_values_28 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_28;
                PyObject *tmp_expression_value_54;
                PyObject *tmp_subscript_value_54;
                PyObject *tmp_format_spec_28;
                PyTuple_SET_ITEM0(tmp_string_concat_values_28, 0, tmp_tuple_element_28);
                tmp_expression_value_54 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_54 == NULL)) {
                    tmp_expression_value_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_54 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 305;

                    goto tuple_build_exception_28;
                }
                tmp_subscript_value_54 = mod_consts[104];
                tmp_format_value_28 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_54, tmp_subscript_value_54);
                if (tmp_format_value_28 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 305;

                    goto tuple_build_exception_28;
                }
                tmp_format_spec_28 = mod_consts[64];
                tmp_tuple_element_28 = BUILTIN_FORMAT(tstate, tmp_format_value_28, tmp_format_spec_28);
                Py_DECREF(tmp_format_value_28);
                if (tmp_tuple_element_28 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 305;

                    goto tuple_build_exception_28;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_28, 1, tmp_tuple_element_28);
                tmp_tuple_element_28 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_28, 2, tmp_tuple_element_28);
            }
            goto tuple_build_noexception_28;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_28:;
            Py_DECREF(tmp_string_concat_values_28);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_28:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_28);
            Py_DECREF(tmp_string_concat_values_28);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 305;

                goto dict_build_exception_1;
            }
            tmp_called_value_28 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[43]);

            if (unlikely(tmp_called_value_28 == NULL)) {
                tmp_called_value_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[43]);
            }

            if (tmp_called_value_28 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 306;

                goto dict_build_exception_1;
            }
            tmp_expression_value_55 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_55 == NULL)) {
                tmp_expression_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_55 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 306;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_55 = mod_consts[104];
            tmp_args_element_value_28 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_55, tmp_subscript_value_55);
            if (tmp_args_element_value_28 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 306;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 306;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_28, tmp_args_element_value_28);
            Py_DECREF(tmp_args_element_value_28);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 306;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_29 = mod_consts[111];
            tmp_string_concat_values_29 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_29;
                PyObject *tmp_expression_value_56;
                PyObject *tmp_subscript_value_56;
                PyObject *tmp_format_spec_29;
                PyTuple_SET_ITEM0(tmp_string_concat_values_29, 0, tmp_tuple_element_29);
                tmp_expression_value_56 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_56 == NULL)) {
                    tmp_expression_value_56 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_56 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 308;

                    goto tuple_build_exception_29;
                }
                tmp_subscript_value_56 = mod_consts[112];
                tmp_format_value_29 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_56, tmp_subscript_value_56);
                if (tmp_format_value_29 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 308;

                    goto tuple_build_exception_29;
                }
                tmp_format_spec_29 = mod_consts[64];
                tmp_tuple_element_29 = BUILTIN_FORMAT(tstate, tmp_format_value_29, tmp_format_spec_29);
                Py_DECREF(tmp_format_value_29);
                if (tmp_tuple_element_29 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 308;

                    goto tuple_build_exception_29;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_29, 1, tmp_tuple_element_29);
                tmp_tuple_element_29 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_29, 2, tmp_tuple_element_29);
            }
            goto tuple_build_noexception_29;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_29:;
            Py_DECREF(tmp_string_concat_values_29);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_29:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_29);
            Py_DECREF(tmp_string_concat_values_29);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 308;

                goto dict_build_exception_1;
            }
            tmp_called_value_29 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[44]);

            if (unlikely(tmp_called_value_29 == NULL)) {
                tmp_called_value_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[44]);
            }

            if (tmp_called_value_29 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 309;

                goto dict_build_exception_1;
            }
            tmp_expression_value_57 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_57 == NULL)) {
                tmp_expression_value_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_57 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 309;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_57 = mod_consts[112];
            tmp_args_element_value_29 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_57, tmp_subscript_value_57);
            if (tmp_args_element_value_29 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 309;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 309;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_29, tmp_args_element_value_29);
            Py_DECREF(tmp_args_element_value_29);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 309;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_30 = mod_consts[113];
            tmp_string_concat_values_30 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_30;
                PyObject *tmp_expression_value_58;
                PyObject *tmp_subscript_value_58;
                PyObject *tmp_format_spec_30;
                PyTuple_SET_ITEM0(tmp_string_concat_values_30, 0, tmp_tuple_element_30);
                tmp_expression_value_58 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_58 == NULL)) {
                    tmp_expression_value_58 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_58 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 310;

                    goto tuple_build_exception_30;
                }
                tmp_subscript_value_58 = mod_consts[114];
                tmp_format_value_30 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_58, tmp_subscript_value_58);
                if (tmp_format_value_30 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 310;

                    goto tuple_build_exception_30;
                }
                tmp_format_spec_30 = mod_consts[64];
                tmp_tuple_element_30 = BUILTIN_FORMAT(tstate, tmp_format_value_30, tmp_format_spec_30);
                Py_DECREF(tmp_format_value_30);
                if (tmp_tuple_element_30 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 310;

                    goto tuple_build_exception_30;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_30, 1, tmp_tuple_element_30);
                tmp_tuple_element_30 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_30, 2, tmp_tuple_element_30);
            }
            goto tuple_build_noexception_30;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_30:;
            Py_DECREF(tmp_string_concat_values_30);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_30:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_30);
            Py_DECREF(tmp_string_concat_values_30);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 310;

                goto dict_build_exception_1;
            }
            tmp_called_value_30 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[44]);

            if (unlikely(tmp_called_value_30 == NULL)) {
                tmp_called_value_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[44]);
            }

            if (tmp_called_value_30 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 311;

                goto dict_build_exception_1;
            }
            tmp_expression_value_59 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_59 == NULL)) {
                tmp_expression_value_59 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_59 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 311;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_59 = mod_consts[114];
            tmp_args_element_value_30 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_59, tmp_subscript_value_59);
            if (tmp_args_element_value_30 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 311;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 311;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_30, tmp_args_element_value_30);
            Py_DECREF(tmp_args_element_value_30);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 311;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_31 = mod_consts[115];
            tmp_string_concat_values_31 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_31;
                PyObject *tmp_expression_value_60;
                PyObject *tmp_subscript_value_60;
                PyObject *tmp_format_spec_31;
                PyTuple_SET_ITEM0(tmp_string_concat_values_31, 0, tmp_tuple_element_31);
                tmp_expression_value_60 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_60 == NULL)) {
                    tmp_expression_value_60 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_60 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 313;

                    goto tuple_build_exception_31;
                }
                tmp_subscript_value_60 = mod_consts[116];
                tmp_format_value_31 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_60, tmp_subscript_value_60);
                if (tmp_format_value_31 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 313;

                    goto tuple_build_exception_31;
                }
                tmp_format_spec_31 = mod_consts[64];
                tmp_tuple_element_31 = BUILTIN_FORMAT(tstate, tmp_format_value_31, tmp_format_spec_31);
                Py_DECREF(tmp_format_value_31);
                if (tmp_tuple_element_31 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 313;

                    goto tuple_build_exception_31;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_31, 1, tmp_tuple_element_31);
                tmp_tuple_element_31 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_31, 2, tmp_tuple_element_31);
            }
            goto tuple_build_noexception_31;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_31:;
            Py_DECREF(tmp_string_concat_values_31);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_31:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_31);
            Py_DECREF(tmp_string_concat_values_31);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 313;

                goto dict_build_exception_1;
            }
            tmp_called_value_31 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[45]);

            if (unlikely(tmp_called_value_31 == NULL)) {
                tmp_called_value_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[45]);
            }

            if (tmp_called_value_31 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 314;

                goto dict_build_exception_1;
            }
            tmp_expression_value_61 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_61 == NULL)) {
                tmp_expression_value_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_61 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 314;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_61 = mod_consts[116];
            tmp_args_element_value_31 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_61, tmp_subscript_value_61);
            if (tmp_args_element_value_31 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 314;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 314;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_31, tmp_args_element_value_31);
            Py_DECREF(tmp_args_element_value_31);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 314;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_32 = mod_consts[117];
            tmp_string_concat_values_32 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_32;
                PyObject *tmp_expression_value_62;
                PyObject *tmp_subscript_value_62;
                PyObject *tmp_format_spec_32;
                PyTuple_SET_ITEM0(tmp_string_concat_values_32, 0, tmp_tuple_element_32);
                tmp_expression_value_62 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_62 == NULL)) {
                    tmp_expression_value_62 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_62 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 315;

                    goto tuple_build_exception_32;
                }
                tmp_subscript_value_62 = mod_consts[118];
                tmp_format_value_32 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_62, tmp_subscript_value_62);
                if (tmp_format_value_32 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 315;

                    goto tuple_build_exception_32;
                }
                tmp_format_spec_32 = mod_consts[64];
                tmp_tuple_element_32 = BUILTIN_FORMAT(tstate, tmp_format_value_32, tmp_format_spec_32);
                Py_DECREF(tmp_format_value_32);
                if (tmp_tuple_element_32 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 315;

                    goto tuple_build_exception_32;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_32, 1, tmp_tuple_element_32);
                tmp_tuple_element_32 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_32, 2, tmp_tuple_element_32);
            }
            goto tuple_build_noexception_32;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_32:;
            Py_DECREF(tmp_string_concat_values_32);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_32:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_32);
            Py_DECREF(tmp_string_concat_values_32);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 315;

                goto dict_build_exception_1;
            }
            tmp_called_value_32 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[45]);

            if (unlikely(tmp_called_value_32 == NULL)) {
                tmp_called_value_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[45]);
            }

            if (tmp_called_value_32 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 316;

                goto dict_build_exception_1;
            }
            tmp_expression_value_63 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_63 == NULL)) {
                tmp_expression_value_63 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_63 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 316;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_63 = mod_consts[118];
            tmp_args_element_value_32 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_63, tmp_subscript_value_63);
            if (tmp_args_element_value_32 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 316;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 316;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_32, tmp_args_element_value_32);
            Py_DECREF(tmp_args_element_value_32);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 316;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_33 = mod_consts[119];
            tmp_string_concat_values_33 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_33;
                PyObject *tmp_expression_value_64;
                PyObject *tmp_subscript_value_64;
                PyObject *tmp_format_spec_33;
                PyTuple_SET_ITEM0(tmp_string_concat_values_33, 0, tmp_tuple_element_33);
                tmp_expression_value_64 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_64 == NULL)) {
                    tmp_expression_value_64 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_64 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 318;

                    goto tuple_build_exception_33;
                }
                tmp_subscript_value_64 = mod_consts[120];
                tmp_format_value_33 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_64, tmp_subscript_value_64);
                if (tmp_format_value_33 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 318;

                    goto tuple_build_exception_33;
                }
                tmp_format_spec_33 = mod_consts[64];
                tmp_tuple_element_33 = BUILTIN_FORMAT(tstate, tmp_format_value_33, tmp_format_spec_33);
                Py_DECREF(tmp_format_value_33);
                if (tmp_tuple_element_33 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 318;

                    goto tuple_build_exception_33;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_33, 1, tmp_tuple_element_33);
                tmp_tuple_element_33 = mod_consts[89];
                PyTuple_SET_ITEM0(tmp_string_concat_values_33, 2, tmp_tuple_element_33);
            }
            goto tuple_build_noexception_33;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_33:;
            Py_DECREF(tmp_string_concat_values_33);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_33:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_33);
            Py_DECREF(tmp_string_concat_values_33);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 318;

                goto dict_build_exception_1;
            }
            tmp_called_value_33 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[46]);

            if (unlikely(tmp_called_value_33 == NULL)) {
                tmp_called_value_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[46]);
            }

            if (tmp_called_value_33 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 319;

                goto dict_build_exception_1;
            }
            tmp_expression_value_65 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_65 == NULL)) {
                tmp_expression_value_65 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_65 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 319;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_65 = mod_consts[120];
            tmp_args_element_value_33 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_65, tmp_subscript_value_65);
            if (tmp_args_element_value_33 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 319;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 319;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_33, tmp_args_element_value_33);
            Py_DECREF(tmp_args_element_value_33);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 319;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_34 = mod_consts[121];
            tmp_string_concat_values_34 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_34;
                PyObject *tmp_expression_value_66;
                PyObject *tmp_subscript_value_66;
                PyObject *tmp_format_spec_34;
                PyTuple_SET_ITEM0(tmp_string_concat_values_34, 0, tmp_tuple_element_34);
                tmp_expression_value_66 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_66 == NULL)) {
                    tmp_expression_value_66 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_66 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 320;

                    goto tuple_build_exception_34;
                }
                tmp_subscript_value_66 = mod_consts[120];
                tmp_format_value_34 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_66, tmp_subscript_value_66);
                if (tmp_format_value_34 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 320;

                    goto tuple_build_exception_34;
                }
                tmp_format_spec_34 = mod_consts[64];
                tmp_tuple_element_34 = BUILTIN_FORMAT(tstate, tmp_format_value_34, tmp_format_spec_34);
                Py_DECREF(tmp_format_value_34);
                if (tmp_tuple_element_34 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 320;

                    goto tuple_build_exception_34;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_34, 1, tmp_tuple_element_34);
                tmp_tuple_element_34 = mod_consts[91];
                PyTuple_SET_ITEM0(tmp_string_concat_values_34, 2, tmp_tuple_element_34);
            }
            goto tuple_build_noexception_34;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_34:;
            Py_DECREF(tmp_string_concat_values_34);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_34:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_34);
            Py_DECREF(tmp_string_concat_values_34);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 320;

                goto dict_build_exception_1;
            }
            tmp_called_value_34 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[47]);

            if (unlikely(tmp_called_value_34 == NULL)) {
                tmp_called_value_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[47]);
            }

            if (tmp_called_value_34 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 321;

                goto dict_build_exception_1;
            }
            tmp_expression_value_67 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_67 == NULL)) {
                tmp_expression_value_67 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_67 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 321;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_67 = mod_consts[120];
            tmp_args_element_value_34 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_67, tmp_subscript_value_67);
            if (tmp_args_element_value_34 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 321;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 321;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_34, tmp_args_element_value_34);
            Py_DECREF(tmp_args_element_value_34);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 321;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_35 = mod_consts[122];
            tmp_string_concat_values_35 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_35;
                PyObject *tmp_expression_value_68;
                PyObject *tmp_subscript_value_68;
                PyObject *tmp_format_spec_35;
                PyTuple_SET_ITEM0(tmp_string_concat_values_35, 0, tmp_tuple_element_35);
                tmp_expression_value_68 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_68 == NULL)) {
                    tmp_expression_value_68 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_68 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 322;

                    goto tuple_build_exception_35;
                }
                tmp_subscript_value_68 = mod_consts[120];
                tmp_format_value_35 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_68, tmp_subscript_value_68);
                if (tmp_format_value_35 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 322;

                    goto tuple_build_exception_35;
                }
                tmp_format_spec_35 = mod_consts[64];
                tmp_tuple_element_35 = BUILTIN_FORMAT(tstate, tmp_format_value_35, tmp_format_spec_35);
                Py_DECREF(tmp_format_value_35);
                if (tmp_tuple_element_35 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 322;

                    goto tuple_build_exception_35;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_35, 1, tmp_tuple_element_35);
                tmp_tuple_element_35 = mod_consts[93];
                PyTuple_SET_ITEM0(tmp_string_concat_values_35, 2, tmp_tuple_element_35);
            }
            goto tuple_build_noexception_35;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_35:;
            Py_DECREF(tmp_string_concat_values_35);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_35:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_35);
            Py_DECREF(tmp_string_concat_values_35);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 322;

                goto dict_build_exception_1;
            }
            tmp_called_value_35 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[48]);

            if (unlikely(tmp_called_value_35 == NULL)) {
                tmp_called_value_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[48]);
            }

            if (tmp_called_value_35 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 323;

                goto dict_build_exception_1;
            }
            tmp_expression_value_69 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_69 == NULL)) {
                tmp_expression_value_69 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_69 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 323;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_69 = mod_consts[120];
            tmp_args_element_value_35 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_69, tmp_subscript_value_69);
            if (tmp_args_element_value_35 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 323;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 323;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_35, tmp_args_element_value_35);
            Py_DECREF(tmp_args_element_value_35);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 323;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_36 = mod_consts[123];
            tmp_string_concat_values_36 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_36;
                PyObject *tmp_expression_value_70;
                PyObject *tmp_subscript_value_70;
                PyObject *tmp_format_spec_36;
                PyTuple_SET_ITEM0(tmp_string_concat_values_36, 0, tmp_tuple_element_36);
                tmp_expression_value_70 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_70 == NULL)) {
                    tmp_expression_value_70 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_70 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 324;

                    goto tuple_build_exception_36;
                }
                tmp_subscript_value_70 = mod_consts[120];
                tmp_format_value_36 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_70, tmp_subscript_value_70);
                if (tmp_format_value_36 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 324;

                    goto tuple_build_exception_36;
                }
                tmp_format_spec_36 = mod_consts[64];
                tmp_tuple_element_36 = BUILTIN_FORMAT(tstate, tmp_format_value_36, tmp_format_spec_36);
                Py_DECREF(tmp_format_value_36);
                if (tmp_tuple_element_36 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 324;

                    goto tuple_build_exception_36;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_36, 1, tmp_tuple_element_36);
                tmp_tuple_element_36 = mod_consts[95];
                PyTuple_SET_ITEM0(tmp_string_concat_values_36, 2, tmp_tuple_element_36);
            }
            goto tuple_build_noexception_36;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_36:;
            Py_DECREF(tmp_string_concat_values_36);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_36:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_36);
            Py_DECREF(tmp_string_concat_values_36);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 324;

                goto dict_build_exception_1;
            }
            tmp_called_value_36 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[49]);

            if (unlikely(tmp_called_value_36 == NULL)) {
                tmp_called_value_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[49]);
            }

            if (tmp_called_value_36 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 325;

                goto dict_build_exception_1;
            }
            tmp_expression_value_71 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_71 == NULL)) {
                tmp_expression_value_71 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_71 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 325;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_71 = mod_consts[120];
            tmp_args_element_value_36 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_71, tmp_subscript_value_71);
            if (tmp_args_element_value_36 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 325;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 325;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_36, tmp_args_element_value_36);
            Py_DECREF(tmp_args_element_value_36);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 325;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_37 = mod_consts[124];
            tmp_string_concat_values_37 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_37;
                PyObject *tmp_expression_value_72;
                PyObject *tmp_subscript_value_72;
                PyObject *tmp_format_spec_37;
                PyTuple_SET_ITEM0(tmp_string_concat_values_37, 0, tmp_tuple_element_37);
                tmp_expression_value_72 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_72 == NULL)) {
                    tmp_expression_value_72 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_72 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 326;

                    goto tuple_build_exception_37;
                }
                tmp_subscript_value_72 = mod_consts[125];
                tmp_format_value_37 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_72, tmp_subscript_value_72);
                if (tmp_format_value_37 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 326;

                    goto tuple_build_exception_37;
                }
                tmp_format_spec_37 = mod_consts[64];
                tmp_tuple_element_37 = BUILTIN_FORMAT(tstate, tmp_format_value_37, tmp_format_spec_37);
                Py_DECREF(tmp_format_value_37);
                if (tmp_tuple_element_37 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 326;

                    goto tuple_build_exception_37;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_37, 1, tmp_tuple_element_37);
                tmp_tuple_element_37 = mod_consts[89];
                PyTuple_SET_ITEM0(tmp_string_concat_values_37, 2, tmp_tuple_element_37);
            }
            goto tuple_build_noexception_37;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_37:;
            Py_DECREF(tmp_string_concat_values_37);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_37:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_37);
            Py_DECREF(tmp_string_concat_values_37);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 326;

                goto dict_build_exception_1;
            }
            tmp_called_value_37 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[46]);

            if (unlikely(tmp_called_value_37 == NULL)) {
                tmp_called_value_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[46]);
            }

            if (tmp_called_value_37 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 327;

                goto dict_build_exception_1;
            }
            tmp_expression_value_73 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_73 == NULL)) {
                tmp_expression_value_73 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_73 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 327;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_73 = mod_consts[125];
            tmp_args_element_value_37 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_73, tmp_subscript_value_73);
            if (tmp_args_element_value_37 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 327;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 327;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_37, tmp_args_element_value_37);
            Py_DECREF(tmp_args_element_value_37);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 327;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_38 = mod_consts[126];
            tmp_string_concat_values_38 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_38;
                PyObject *tmp_expression_value_74;
                PyObject *tmp_subscript_value_74;
                PyObject *tmp_format_spec_38;
                PyTuple_SET_ITEM0(tmp_string_concat_values_38, 0, tmp_tuple_element_38);
                tmp_expression_value_74 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_74 == NULL)) {
                    tmp_expression_value_74 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_74 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 328;

                    goto tuple_build_exception_38;
                }
                tmp_subscript_value_74 = mod_consts[125];
                tmp_format_value_38 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_74, tmp_subscript_value_74);
                if (tmp_format_value_38 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 328;

                    goto tuple_build_exception_38;
                }
                tmp_format_spec_38 = mod_consts[64];
                tmp_tuple_element_38 = BUILTIN_FORMAT(tstate, tmp_format_value_38, tmp_format_spec_38);
                Py_DECREF(tmp_format_value_38);
                if (tmp_tuple_element_38 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 328;

                    goto tuple_build_exception_38;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_38, 1, tmp_tuple_element_38);
                tmp_tuple_element_38 = mod_consts[91];
                PyTuple_SET_ITEM0(tmp_string_concat_values_38, 2, tmp_tuple_element_38);
            }
            goto tuple_build_noexception_38;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_38:;
            Py_DECREF(tmp_string_concat_values_38);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_38:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_38);
            Py_DECREF(tmp_string_concat_values_38);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 328;

                goto dict_build_exception_1;
            }
            tmp_called_value_38 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[47]);

            if (unlikely(tmp_called_value_38 == NULL)) {
                tmp_called_value_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[47]);
            }

            if (tmp_called_value_38 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 329;

                goto dict_build_exception_1;
            }
            tmp_expression_value_75 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_75 == NULL)) {
                tmp_expression_value_75 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_75 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 329;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_75 = mod_consts[125];
            tmp_args_element_value_38 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_75, tmp_subscript_value_75);
            if (tmp_args_element_value_38 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 329;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 329;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_38, tmp_args_element_value_38);
            Py_DECREF(tmp_args_element_value_38);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 329;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_39 = mod_consts[127];
            tmp_string_concat_values_39 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_39;
                PyObject *tmp_expression_value_76;
                PyObject *tmp_subscript_value_76;
                PyObject *tmp_format_spec_39;
                PyTuple_SET_ITEM0(tmp_string_concat_values_39, 0, tmp_tuple_element_39);
                tmp_expression_value_76 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_76 == NULL)) {
                    tmp_expression_value_76 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_76 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 330;

                    goto tuple_build_exception_39;
                }
                tmp_subscript_value_76 = mod_consts[125];
                tmp_format_value_39 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_76, tmp_subscript_value_76);
                if (tmp_format_value_39 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 330;

                    goto tuple_build_exception_39;
                }
                tmp_format_spec_39 = mod_consts[64];
                tmp_tuple_element_39 = BUILTIN_FORMAT(tstate, tmp_format_value_39, tmp_format_spec_39);
                Py_DECREF(tmp_format_value_39);
                if (tmp_tuple_element_39 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 330;

                    goto tuple_build_exception_39;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_39, 1, tmp_tuple_element_39);
                tmp_tuple_element_39 = mod_consts[93];
                PyTuple_SET_ITEM0(tmp_string_concat_values_39, 2, tmp_tuple_element_39);
            }
            goto tuple_build_noexception_39;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_39:;
            Py_DECREF(tmp_string_concat_values_39);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_39:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_39);
            Py_DECREF(tmp_string_concat_values_39);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 330;

                goto dict_build_exception_1;
            }
            tmp_called_value_39 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[48]);

            if (unlikely(tmp_called_value_39 == NULL)) {
                tmp_called_value_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[48]);
            }

            if (tmp_called_value_39 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 331;

                goto dict_build_exception_1;
            }
            tmp_expression_value_77 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_77 == NULL)) {
                tmp_expression_value_77 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_77 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 331;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_77 = mod_consts[125];
            tmp_args_element_value_39 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_77, tmp_subscript_value_77);
            if (tmp_args_element_value_39 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 331;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 331;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_39, tmp_args_element_value_39);
            Py_DECREF(tmp_args_element_value_39);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 331;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_40 = mod_consts[128];
            tmp_string_concat_values_40 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_40;
                PyObject *tmp_expression_value_78;
                PyObject *tmp_subscript_value_78;
                PyObject *tmp_format_spec_40;
                PyTuple_SET_ITEM0(tmp_string_concat_values_40, 0, tmp_tuple_element_40);
                tmp_expression_value_78 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_78 == NULL)) {
                    tmp_expression_value_78 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_78 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 332;

                    goto tuple_build_exception_40;
                }
                tmp_subscript_value_78 = mod_consts[125];
                tmp_format_value_40 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_78, tmp_subscript_value_78);
                if (tmp_format_value_40 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 332;

                    goto tuple_build_exception_40;
                }
                tmp_format_spec_40 = mod_consts[64];
                tmp_tuple_element_40 = BUILTIN_FORMAT(tstate, tmp_format_value_40, tmp_format_spec_40);
                Py_DECREF(tmp_format_value_40);
                if (tmp_tuple_element_40 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 332;

                    goto tuple_build_exception_40;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_40, 1, tmp_tuple_element_40);
                tmp_tuple_element_40 = mod_consts[95];
                PyTuple_SET_ITEM0(tmp_string_concat_values_40, 2, tmp_tuple_element_40);
            }
            goto tuple_build_noexception_40;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_40:;
            Py_DECREF(tmp_string_concat_values_40);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_40:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_40);
            Py_DECREF(tmp_string_concat_values_40);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 332;

                goto dict_build_exception_1;
            }
            tmp_called_value_40 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[49]);

            if (unlikely(tmp_called_value_40 == NULL)) {
                tmp_called_value_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[49]);
            }

            if (tmp_called_value_40 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 333;

                goto dict_build_exception_1;
            }
            tmp_expression_value_79 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_79 == NULL)) {
                tmp_expression_value_79 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_79 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 333;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_79 = mod_consts[125];
            tmp_args_element_value_40 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_79, tmp_subscript_value_79);
            if (tmp_args_element_value_40 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 333;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 333;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_40, tmp_args_element_value_40);
            Py_DECREF(tmp_args_element_value_40);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 333;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_41 = mod_consts[129];
            tmp_string_concat_values_41 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_41;
                PyObject *tmp_expression_value_80;
                PyObject *tmp_subscript_value_80;
                PyObject *tmp_format_spec_41;
                PyTuple_SET_ITEM0(tmp_string_concat_values_41, 0, tmp_tuple_element_41);
                tmp_expression_value_80 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_80 == NULL)) {
                    tmp_expression_value_80 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_80 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 335;

                    goto tuple_build_exception_41;
                }
                tmp_subscript_value_80 = mod_consts[130];
                tmp_format_value_41 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_80, tmp_subscript_value_80);
                if (tmp_format_value_41 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 335;

                    goto tuple_build_exception_41;
                }
                tmp_format_spec_41 = mod_consts[64];
                tmp_tuple_element_41 = BUILTIN_FORMAT(tstate, tmp_format_value_41, tmp_format_spec_41);
                Py_DECREF(tmp_format_value_41);
                if (tmp_tuple_element_41 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 335;

                    goto tuple_build_exception_41;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_41, 1, tmp_tuple_element_41);
                tmp_tuple_element_41 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_41, 2, tmp_tuple_element_41);
            }
            goto tuple_build_noexception_41;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_41:;
            Py_DECREF(tmp_string_concat_values_41);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_41:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_41);
            Py_DECREF(tmp_string_concat_values_41);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 335;

                goto dict_build_exception_1;
            }
            tmp_called_value_41 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[19]);

            if (unlikely(tmp_called_value_41 == NULL)) {
                tmp_called_value_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[19]);
            }

            if (tmp_called_value_41 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 336;

                goto dict_build_exception_1;
            }
            tmp_expression_value_81 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_81 == NULL)) {
                tmp_expression_value_81 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_81 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 336;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_81 = mod_consts[130];
            tmp_args_element_value_41 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_81, tmp_subscript_value_81);
            if (tmp_args_element_value_41 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 336;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 336;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_41, tmp_args_element_value_41);
            Py_DECREF(tmp_args_element_value_41);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 336;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_42 = mod_consts[131];
            tmp_string_concat_values_42 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_42;
                PyObject *tmp_expression_value_82;
                PyObject *tmp_subscript_value_82;
                PyObject *tmp_format_spec_42;
                PyTuple_SET_ITEM0(tmp_string_concat_values_42, 0, tmp_tuple_element_42);
                tmp_expression_value_82 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_82 == NULL)) {
                    tmp_expression_value_82 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_82 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 337;

                    goto tuple_build_exception_42;
                }
                tmp_subscript_value_82 = mod_consts[132];
                tmp_format_value_42 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_82, tmp_subscript_value_82);
                if (tmp_format_value_42 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 337;

                    goto tuple_build_exception_42;
                }
                tmp_format_spec_42 = mod_consts[64];
                tmp_tuple_element_42 = BUILTIN_FORMAT(tstate, tmp_format_value_42, tmp_format_spec_42);
                Py_DECREF(tmp_format_value_42);
                if (tmp_tuple_element_42 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 337;

                    goto tuple_build_exception_42;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_42, 1, tmp_tuple_element_42);
                tmp_tuple_element_42 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_42, 2, tmp_tuple_element_42);
            }
            goto tuple_build_noexception_42;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_42:;
            Py_DECREF(tmp_string_concat_values_42);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_42:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_42);
            Py_DECREF(tmp_string_concat_values_42);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 337;

                goto dict_build_exception_1;
            }
            tmp_called_value_42 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[19]);

            if (unlikely(tmp_called_value_42 == NULL)) {
                tmp_called_value_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[19]);
            }

            if (tmp_called_value_42 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 338;

                goto dict_build_exception_1;
            }
            tmp_expression_value_83 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_83 == NULL)) {
                tmp_expression_value_83 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_83 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 338;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_83 = mod_consts[132];
            tmp_args_element_value_42 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_83, tmp_subscript_value_83);
            if (tmp_args_element_value_42 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 338;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 338;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_42, tmp_args_element_value_42);
            Py_DECREF(tmp_args_element_value_42);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 338;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_43 = mod_consts[133];
            tmp_string_concat_values_43 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_43;
                PyObject *tmp_expression_value_84;
                PyObject *tmp_subscript_value_84;
                PyObject *tmp_format_spec_43;
                PyTuple_SET_ITEM0(tmp_string_concat_values_43, 0, tmp_tuple_element_43);
                tmp_expression_value_84 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_84 == NULL)) {
                    tmp_expression_value_84 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_84 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 339;

                    goto tuple_build_exception_43;
                }
                tmp_subscript_value_84 = mod_consts[134];
                tmp_format_value_43 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_84, tmp_subscript_value_84);
                if (tmp_format_value_43 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 339;

                    goto tuple_build_exception_43;
                }
                tmp_format_spec_43 = mod_consts[64];
                tmp_tuple_element_43 = BUILTIN_FORMAT(tstate, tmp_format_value_43, tmp_format_spec_43);
                Py_DECREF(tmp_format_value_43);
                if (tmp_tuple_element_43 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 339;

                    goto tuple_build_exception_43;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_43, 1, tmp_tuple_element_43);
                tmp_tuple_element_43 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_43, 2, tmp_tuple_element_43);
            }
            goto tuple_build_noexception_43;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_43:;
            Py_DECREF(tmp_string_concat_values_43);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_43:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_43);
            Py_DECREF(tmp_string_concat_values_43);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 339;

                goto dict_build_exception_1;
            }
            tmp_called_value_43 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[20]);

            if (unlikely(tmp_called_value_43 == NULL)) {
                tmp_called_value_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
            }

            if (tmp_called_value_43 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 340;

                goto dict_build_exception_1;
            }
            tmp_expression_value_85 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_85 == NULL)) {
                tmp_expression_value_85 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_85 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 340;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_85 = mod_consts[134];
            tmp_args_element_value_43 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_85, tmp_subscript_value_85);
            if (tmp_args_element_value_43 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 340;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 340;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_43, tmp_args_element_value_43);
            Py_DECREF(tmp_args_element_value_43);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 340;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_44 = mod_consts[135];
            tmp_string_concat_values_44 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_44;
                PyObject *tmp_expression_value_86;
                PyObject *tmp_subscript_value_86;
                PyObject *tmp_format_spec_44;
                PyTuple_SET_ITEM0(tmp_string_concat_values_44, 0, tmp_tuple_element_44);
                tmp_expression_value_86 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_86 == NULL)) {
                    tmp_expression_value_86 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_86 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 341;

                    goto tuple_build_exception_44;
                }
                tmp_subscript_value_86 = mod_consts[136];
                tmp_format_value_44 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_86, tmp_subscript_value_86);
                if (tmp_format_value_44 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 341;

                    goto tuple_build_exception_44;
                }
                tmp_format_spec_44 = mod_consts[64];
                tmp_tuple_element_44 = BUILTIN_FORMAT(tstate, tmp_format_value_44, tmp_format_spec_44);
                Py_DECREF(tmp_format_value_44);
                if (tmp_tuple_element_44 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 341;

                    goto tuple_build_exception_44;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_44, 1, tmp_tuple_element_44);
                tmp_tuple_element_44 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_44, 2, tmp_tuple_element_44);
            }
            goto tuple_build_noexception_44;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_44:;
            Py_DECREF(tmp_string_concat_values_44);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_44:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_44);
            Py_DECREF(tmp_string_concat_values_44);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 341;

                goto dict_build_exception_1;
            }
            tmp_called_value_44 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[20]);

            if (unlikely(tmp_called_value_44 == NULL)) {
                tmp_called_value_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[20]);
            }

            if (tmp_called_value_44 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 342;

                goto dict_build_exception_1;
            }
            tmp_expression_value_87 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_87 == NULL)) {
                tmp_expression_value_87 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_87 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 342;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_87 = mod_consts[136];
            tmp_args_element_value_44 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_87, tmp_subscript_value_87);
            if (tmp_args_element_value_44 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 342;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 342;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_44, tmp_args_element_value_44);
            Py_DECREF(tmp_args_element_value_44);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 342;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_45 = mod_consts[137];
            tmp_string_concat_values_45 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_45;
                PyObject *tmp_expression_value_88;
                PyObject *tmp_subscript_value_88;
                PyObject *tmp_format_spec_45;
                PyTuple_SET_ITEM0(tmp_string_concat_values_45, 0, tmp_tuple_element_45);
                tmp_expression_value_88 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_88 == NULL)) {
                    tmp_expression_value_88 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_88 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 344;

                    goto tuple_build_exception_45;
                }
                tmp_subscript_value_88 = mod_consts[138];
                tmp_format_value_45 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_88, tmp_subscript_value_88);
                if (tmp_format_value_45 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 344;

                    goto tuple_build_exception_45;
                }
                tmp_format_spec_45 = mod_consts[64];
                tmp_tuple_element_45 = BUILTIN_FORMAT(tstate, tmp_format_value_45, tmp_format_spec_45);
                Py_DECREF(tmp_format_value_45);
                if (tmp_tuple_element_45 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 344;

                    goto tuple_build_exception_45;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_45, 1, tmp_tuple_element_45);
                tmp_tuple_element_45 = mod_consts[139];
                PyTuple_SET_ITEM0(tmp_string_concat_values_45, 2, tmp_tuple_element_45);
            }
            goto tuple_build_noexception_45;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_45:;
            Py_DECREF(tmp_string_concat_values_45);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_45:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_45);
            Py_DECREF(tmp_string_concat_values_45);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 344;

                goto dict_build_exception_1;
            }
            tmp_called_value_45 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[55]);

            if (unlikely(tmp_called_value_45 == NULL)) {
                tmp_called_value_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[55]);
            }

            if (tmp_called_value_45 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 345;

                goto dict_build_exception_1;
            }
            tmp_expression_value_89 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_89 == NULL)) {
                tmp_expression_value_89 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_89 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 345;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_89 = mod_consts[138];
            tmp_args_element_value_45 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_89, tmp_subscript_value_89);
            if (tmp_args_element_value_45 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 345;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 345;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_45, tmp_args_element_value_45);
            Py_DECREF(tmp_args_element_value_45);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 345;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_46 = mod_consts[137];
            tmp_string_concat_values_46 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_46;
                PyObject *tmp_expression_value_90;
                PyObject *tmp_subscript_value_90;
                PyObject *tmp_format_spec_46;
                PyTuple_SET_ITEM0(tmp_string_concat_values_46, 0, tmp_tuple_element_46);
                tmp_expression_value_90 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_90 == NULL)) {
                    tmp_expression_value_90 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_90 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 346;

                    goto tuple_build_exception_46;
                }
                tmp_subscript_value_90 = mod_consts[140];
                tmp_format_value_46 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_90, tmp_subscript_value_90);
                if (tmp_format_value_46 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 346;

                    goto tuple_build_exception_46;
                }
                tmp_format_spec_46 = mod_consts[64];
                tmp_tuple_element_46 = BUILTIN_FORMAT(tstate, tmp_format_value_46, tmp_format_spec_46);
                Py_DECREF(tmp_format_value_46);
                if (tmp_tuple_element_46 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 346;

                    goto tuple_build_exception_46;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_46, 1, tmp_tuple_element_46);
                tmp_tuple_element_46 = mod_consts[141];
                PyTuple_SET_ITEM0(tmp_string_concat_values_46, 2, tmp_tuple_element_46);
            }
            goto tuple_build_noexception_46;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_46:;
            Py_DECREF(tmp_string_concat_values_46);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_46:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_46);
            Py_DECREF(tmp_string_concat_values_46);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 346;

                goto dict_build_exception_1;
            }
            tmp_called_value_46 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[56]);

            if (unlikely(tmp_called_value_46 == NULL)) {
                tmp_called_value_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[56]);
            }

            if (tmp_called_value_46 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 347;

                goto dict_build_exception_1;
            }
            tmp_expression_value_91 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_91 == NULL)) {
                tmp_expression_value_91 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_91 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 347;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_91 = mod_consts[140];
            tmp_args_element_value_46 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_91, tmp_subscript_value_91);
            if (tmp_args_element_value_46 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 347;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 347;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_46, tmp_args_element_value_46);
            Py_DECREF(tmp_args_element_value_46);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 347;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_47 = mod_consts[137];
            tmp_string_concat_values_47 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_47;
                PyObject *tmp_expression_value_92;
                PyObject *tmp_subscript_value_92;
                PyObject *tmp_format_spec_47;
                PyTuple_SET_ITEM0(tmp_string_concat_values_47, 0, tmp_tuple_element_47);
                tmp_expression_value_92 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_92 == NULL)) {
                    tmp_expression_value_92 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_92 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 348;

                    goto tuple_build_exception_47;
                }
                tmp_subscript_value_92 = mod_consts[142];
                tmp_format_value_47 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_92, tmp_subscript_value_92);
                if (tmp_format_value_47 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 348;

                    goto tuple_build_exception_47;
                }
                tmp_format_spec_47 = mod_consts[64];
                tmp_tuple_element_47 = BUILTIN_FORMAT(tstate, tmp_format_value_47, tmp_format_spec_47);
                Py_DECREF(tmp_format_value_47);
                if (tmp_tuple_element_47 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 348;

                    goto tuple_build_exception_47;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_47, 1, tmp_tuple_element_47);
                tmp_tuple_element_47 = mod_consts[143];
                PyTuple_SET_ITEM0(tmp_string_concat_values_47, 2, tmp_tuple_element_47);
            }
            goto tuple_build_noexception_47;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_47:;
            Py_DECREF(tmp_string_concat_values_47);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_47:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_47);
            Py_DECREF(tmp_string_concat_values_47);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 348;

                goto dict_build_exception_1;
            }
            tmp_called_value_47 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[57]);

            if (unlikely(tmp_called_value_47 == NULL)) {
                tmp_called_value_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[57]);
            }

            if (tmp_called_value_47 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 349;

                goto dict_build_exception_1;
            }
            tmp_expression_value_93 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_93 == NULL)) {
                tmp_expression_value_93 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_93 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 349;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_93 = mod_consts[142];
            tmp_args_element_value_47 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_93, tmp_subscript_value_93);
            if (tmp_args_element_value_47 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 349;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 349;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_47, tmp_args_element_value_47);
            Py_DECREF(tmp_args_element_value_47);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 349;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_48 = mod_consts[137];
            tmp_string_concat_values_48 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_48;
                PyObject *tmp_expression_value_94;
                PyObject *tmp_subscript_value_94;
                PyObject *tmp_format_spec_48;
                PyTuple_SET_ITEM0(tmp_string_concat_values_48, 0, tmp_tuple_element_48);
                tmp_expression_value_94 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_94 == NULL)) {
                    tmp_expression_value_94 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_94 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 350;

                    goto tuple_build_exception_48;
                }
                tmp_subscript_value_94 = mod_consts[142];
                tmp_format_value_48 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_94, tmp_subscript_value_94);
                if (tmp_format_value_48 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 350;

                    goto tuple_build_exception_48;
                }
                tmp_format_spec_48 = mod_consts[64];
                tmp_tuple_element_48 = BUILTIN_FORMAT(tstate, tmp_format_value_48, tmp_format_spec_48);
                Py_DECREF(tmp_format_value_48);
                if (tmp_tuple_element_48 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 350;

                    goto tuple_build_exception_48;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_48, 1, tmp_tuple_element_48);
                tmp_tuple_element_48 = mod_consts[144];
                PyTuple_SET_ITEM0(tmp_string_concat_values_48, 2, tmp_tuple_element_48);
            }
            goto tuple_build_noexception_48;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_48:;
            Py_DECREF(tmp_string_concat_values_48);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_48:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_48);
            Py_DECREF(tmp_string_concat_values_48);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 350;

                goto dict_build_exception_1;
            }
            tmp_called_value_48 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[58]);

            if (unlikely(tmp_called_value_48 == NULL)) {
                tmp_called_value_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[58]);
            }

            if (tmp_called_value_48 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 351;

                goto dict_build_exception_1;
            }
            tmp_expression_value_95 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_95 == NULL)) {
                tmp_expression_value_95 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_95 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 351;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_95 = mod_consts[142];
            tmp_args_element_value_48 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_95, tmp_subscript_value_95);
            if (tmp_args_element_value_48 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 351;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 351;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_48, tmp_args_element_value_48);
            Py_DECREF(tmp_args_element_value_48);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 351;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_49 = mod_consts[137];
            tmp_string_concat_values_49 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_49;
                PyObject *tmp_expression_value_96;
                PyObject *tmp_subscript_value_96;
                PyObject *tmp_format_spec_49;
                PyTuple_SET_ITEM0(tmp_string_concat_values_49, 0, tmp_tuple_element_49);
                tmp_expression_value_96 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_96 == NULL)) {
                    tmp_expression_value_96 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_96 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 352;

                    goto tuple_build_exception_49;
                }
                tmp_subscript_value_96 = mod_consts[142];
                tmp_format_value_49 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_96, tmp_subscript_value_96);
                if (tmp_format_value_49 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 352;

                    goto tuple_build_exception_49;
                }
                tmp_format_spec_49 = mod_consts[64];
                tmp_tuple_element_49 = BUILTIN_FORMAT(tstate, tmp_format_value_49, tmp_format_spec_49);
                Py_DECREF(tmp_format_value_49);
                if (tmp_tuple_element_49 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 352;

                    goto tuple_build_exception_49;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_49, 1, tmp_tuple_element_49);
                tmp_tuple_element_49 = mod_consts[145];
                PyTuple_SET_ITEM0(tmp_string_concat_values_49, 2, tmp_tuple_element_49);
            }
            goto tuple_build_noexception_49;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_49:;
            Py_DECREF(tmp_string_concat_values_49);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_49:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_49);
            Py_DECREF(tmp_string_concat_values_49);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 352;

                goto dict_build_exception_1;
            }
            tmp_called_value_49 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[59]);

            if (unlikely(tmp_called_value_49 == NULL)) {
                tmp_called_value_49 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[59]);
            }

            if (tmp_called_value_49 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 353;

                goto dict_build_exception_1;
            }
            tmp_expression_value_97 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_97 == NULL)) {
                tmp_expression_value_97 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_97 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 353;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_97 = mod_consts[142];
            tmp_args_element_value_49 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_97, tmp_subscript_value_97);
            if (tmp_args_element_value_49 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 353;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 353;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_49, tmp_args_element_value_49);
            Py_DECREF(tmp_args_element_value_49);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 353;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_50 = mod_consts[146];
            tmp_string_concat_values_50 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_50;
                PyObject *tmp_expression_value_98;
                PyObject *tmp_subscript_value_98;
                PyObject *tmp_format_spec_50;
                PyTuple_SET_ITEM0(tmp_string_concat_values_50, 0, tmp_tuple_element_50);
                tmp_expression_value_98 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_98 == NULL)) {
                    tmp_expression_value_98 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_98 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 355;

                    goto tuple_build_exception_50;
                }
                tmp_subscript_value_98 = mod_consts[147];
                tmp_format_value_50 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_98, tmp_subscript_value_98);
                if (tmp_format_value_50 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 355;

                    goto tuple_build_exception_50;
                }
                tmp_format_spec_50 = mod_consts[64];
                tmp_tuple_element_50 = BUILTIN_FORMAT(tstate, tmp_format_value_50, tmp_format_spec_50);
                Py_DECREF(tmp_format_value_50);
                if (tmp_tuple_element_50 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 355;

                    goto tuple_build_exception_50;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_50, 1, tmp_tuple_element_50);
                tmp_tuple_element_50 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_50, 2, tmp_tuple_element_50);
            }
            goto tuple_build_noexception_50;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_50:;
            Py_DECREF(tmp_string_concat_values_50);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_50:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_50);
            Py_DECREF(tmp_string_concat_values_50);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 355;

                goto dict_build_exception_1;
            }
            tmp_called_value_50 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[50]);

            if (unlikely(tmp_called_value_50 == NULL)) {
                tmp_called_value_50 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[50]);
            }

            if (tmp_called_value_50 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 356;

                goto dict_build_exception_1;
            }
            tmp_expression_value_99 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_99 == NULL)) {
                tmp_expression_value_99 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_99 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 356;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_99 = mod_consts[147];
            tmp_args_element_value_50 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_99, tmp_subscript_value_99);
            if (tmp_args_element_value_50 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 356;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 356;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_50, tmp_args_element_value_50);
            Py_DECREF(tmp_args_element_value_50);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 356;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_51 = mod_consts[148];
            tmp_string_concat_values_51 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_51;
                PyObject *tmp_expression_value_100;
                PyObject *tmp_subscript_value_100;
                PyObject *tmp_format_spec_51;
                PyTuple_SET_ITEM0(tmp_string_concat_values_51, 0, tmp_tuple_element_51);
                tmp_expression_value_100 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_100 == NULL)) {
                    tmp_expression_value_100 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_100 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 357;

                    goto tuple_build_exception_51;
                }
                tmp_subscript_value_100 = mod_consts[147];
                tmp_format_value_51 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_100, tmp_subscript_value_100);
                if (tmp_format_value_51 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 357;

                    goto tuple_build_exception_51;
                }
                tmp_format_spec_51 = mod_consts[64];
                tmp_tuple_element_51 = BUILTIN_FORMAT(tstate, tmp_format_value_51, tmp_format_spec_51);
                Py_DECREF(tmp_format_value_51);
                if (tmp_tuple_element_51 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 357;

                    goto tuple_build_exception_51;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_51, 1, tmp_tuple_element_51);
                tmp_tuple_element_51 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_51, 2, tmp_tuple_element_51);
            }
            goto tuple_build_noexception_51;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_51:;
            Py_DECREF(tmp_string_concat_values_51);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_51:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_51);
            Py_DECREF(tmp_string_concat_values_51);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 357;

                goto dict_build_exception_1;
            }
            tmp_called_value_51 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[51]);

            if (unlikely(tmp_called_value_51 == NULL)) {
                tmp_called_value_51 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[51]);
            }

            if (tmp_called_value_51 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 358;

                goto dict_build_exception_1;
            }
            tmp_expression_value_101 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_101 == NULL)) {
                tmp_expression_value_101 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_101 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 358;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_101 = mod_consts[147];
            tmp_args_element_value_51 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_101, tmp_subscript_value_101);
            if (tmp_args_element_value_51 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 358;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 358;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_51, tmp_args_element_value_51);
            Py_DECREF(tmp_args_element_value_51);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 358;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_52 = mod_consts[149];
            tmp_string_concat_values_52 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_52;
                PyObject *tmp_expression_value_102;
                PyObject *tmp_subscript_value_102;
                PyObject *tmp_format_spec_52;
                PyTuple_SET_ITEM0(tmp_string_concat_values_52, 0, tmp_tuple_element_52);
                tmp_expression_value_102 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_102 == NULL)) {
                    tmp_expression_value_102 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_102 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 359;

                    goto tuple_build_exception_52;
                }
                tmp_subscript_value_102 = mod_consts[147];
                tmp_format_value_52 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_102, tmp_subscript_value_102);
                if (tmp_format_value_52 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 359;

                    goto tuple_build_exception_52;
                }
                tmp_format_spec_52 = mod_consts[64];
                tmp_tuple_element_52 = BUILTIN_FORMAT(tstate, tmp_format_value_52, tmp_format_spec_52);
                Py_DECREF(tmp_format_value_52);
                if (tmp_tuple_element_52 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 359;

                    goto tuple_build_exception_52;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_52, 1, tmp_tuple_element_52);
                tmp_tuple_element_52 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_52, 2, tmp_tuple_element_52);
            }
            goto tuple_build_noexception_52;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_52:;
            Py_DECREF(tmp_string_concat_values_52);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_52:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_52);
            Py_DECREF(tmp_string_concat_values_52);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 359;

                goto dict_build_exception_1;
            }
            tmp_called_value_52 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[52]);

            if (unlikely(tmp_called_value_52 == NULL)) {
                tmp_called_value_52 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[52]);
            }

            if (tmp_called_value_52 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 360;

                goto dict_build_exception_1;
            }
            tmp_expression_value_103 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_103 == NULL)) {
                tmp_expression_value_103 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_103 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 360;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_103 = mod_consts[147];
            tmp_args_element_value_52 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_103, tmp_subscript_value_103);
            if (tmp_args_element_value_52 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 360;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 360;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_52, tmp_args_element_value_52);
            Py_DECREF(tmp_args_element_value_52);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 360;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_53 = mod_consts[150];
            tmp_string_concat_values_53 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_53;
                PyObject *tmp_expression_value_104;
                PyObject *tmp_subscript_value_104;
                PyObject *tmp_format_spec_53;
                PyTuple_SET_ITEM0(tmp_string_concat_values_53, 0, tmp_tuple_element_53);
                tmp_expression_value_104 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_104 == NULL)) {
                    tmp_expression_value_104 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_104 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 361;

                    goto tuple_build_exception_53;
                }
                tmp_subscript_value_104 = mod_consts[147];
                tmp_format_value_53 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_104, tmp_subscript_value_104);
                if (tmp_format_value_53 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 361;

                    goto tuple_build_exception_53;
                }
                tmp_format_spec_53 = mod_consts[64];
                tmp_tuple_element_53 = BUILTIN_FORMAT(tstate, tmp_format_value_53, tmp_format_spec_53);
                Py_DECREF(tmp_format_value_53);
                if (tmp_tuple_element_53 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 361;

                    goto tuple_build_exception_53;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_53, 1, tmp_tuple_element_53);
                tmp_tuple_element_53 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_53, 2, tmp_tuple_element_53);
            }
            goto tuple_build_noexception_53;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_53:;
            Py_DECREF(tmp_string_concat_values_53);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_53:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_53);
            Py_DECREF(tmp_string_concat_values_53);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 361;

                goto dict_build_exception_1;
            }
            tmp_called_value_53 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[53]);

            if (unlikely(tmp_called_value_53 == NULL)) {
                tmp_called_value_53 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[53]);
            }

            if (tmp_called_value_53 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 362;

                goto dict_build_exception_1;
            }
            tmp_expression_value_105 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_105 == NULL)) {
                tmp_expression_value_105 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_105 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 362;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_105 = mod_consts[147];
            tmp_args_element_value_53 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_105, tmp_subscript_value_105);
            if (tmp_args_element_value_53 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 362;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 362;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_53, tmp_args_element_value_53);
            Py_DECREF(tmp_args_element_value_53);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 362;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_54 = mod_consts[151];
            tmp_string_concat_values_54 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_54;
                PyObject *tmp_expression_value_106;
                PyObject *tmp_subscript_value_106;
                PyObject *tmp_format_spec_54;
                PyTuple_SET_ITEM0(tmp_string_concat_values_54, 0, tmp_tuple_element_54);
                tmp_expression_value_106 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_106 == NULL)) {
                    tmp_expression_value_106 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_106 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 364;

                    goto tuple_build_exception_54;
                }
                tmp_subscript_value_106 = mod_consts[54];
                tmp_format_value_54 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_106, tmp_subscript_value_106);
                if (tmp_format_value_54 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 364;

                    goto tuple_build_exception_54;
                }
                tmp_format_spec_54 = mod_consts[64];
                tmp_tuple_element_54 = BUILTIN_FORMAT(tstate, tmp_format_value_54, tmp_format_spec_54);
                Py_DECREF(tmp_format_value_54);
                if (tmp_tuple_element_54 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 364;

                    goto tuple_build_exception_54;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_54, 1, tmp_tuple_element_54);
                tmp_tuple_element_54 = mod_consts[91];
                PyTuple_SET_ITEM0(tmp_string_concat_values_54, 2, tmp_tuple_element_54);
            }
            goto tuple_build_noexception_54;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_54:;
            Py_DECREF(tmp_string_concat_values_54);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_54:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_54);
            Py_DECREF(tmp_string_concat_values_54);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 364;

                goto dict_build_exception_1;
            }
            tmp_called_value_54 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[54]);

            if (unlikely(tmp_called_value_54 == NULL)) {
                tmp_called_value_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[54]);
            }

            if (tmp_called_value_54 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 365;

                goto dict_build_exception_1;
            }
            tmp_expression_value_107 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_107 == NULL)) {
                tmp_expression_value_107 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_107 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 365;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_107 = mod_consts[54];
            tmp_args_element_value_54 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_107, tmp_subscript_value_107);
            if (tmp_args_element_value_54 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 365;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 365;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_54, tmp_args_element_value_54);
            Py_DECREF(tmp_args_element_value_54);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 365;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[27];
            tmp_called_value_55 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[27]);

            if (unlikely(tmp_called_value_55 == NULL)) {
                tmp_called_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[27]);
            }

            if (tmp_called_value_55 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 368;

                goto dict_build_exception_1;
            }
            tmp_expression_value_108 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_108 == NULL)) {
                tmp_expression_value_108 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_108 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 368;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_108 = mod_consts[27];
            tmp_args_element_value_55 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_108, tmp_subscript_value_108);
            if (tmp_args_element_value_55 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 368;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 368;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_55, tmp_args_element_value_55);
            Py_DECREF(tmp_args_element_value_55);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 368;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_dict_key_1 = mod_consts[29];
            tmp_called_value_56 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[29]);

            if (unlikely(tmp_called_value_56 == NULL)) {
                tmp_called_value_56 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[29]);
            }

            if (tmp_called_value_56 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 370;

                goto dict_build_exception_1;
            }
            tmp_expression_value_109 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_109 == NULL)) {
                tmp_expression_value_109 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_109 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 370;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_109 = mod_consts[29];
            tmp_args_element_value_56 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_109, tmp_subscript_value_109);
            if (tmp_args_element_value_56 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 370;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 370;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_56, tmp_args_element_value_56);
            Py_DECREF(tmp_args_element_value_56);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 370;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_55 = mod_consts[152];
            tmp_string_concat_values_55 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_55;
                PyObject *tmp_expression_value_110;
                PyObject *tmp_subscript_value_110;
                PyObject *tmp_format_spec_55;
                PyTuple_SET_ITEM0(tmp_string_concat_values_55, 0, tmp_tuple_element_55);
                tmp_expression_value_110 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_110 == NULL)) {
                    tmp_expression_value_110 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_110 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 372;

                    goto tuple_build_exception_55;
                }
                tmp_subscript_value_110 = mod_consts[153];
                tmp_format_value_55 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_110, tmp_subscript_value_110);
                if (tmp_format_value_55 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 372;

                    goto tuple_build_exception_55;
                }
                tmp_format_spec_55 = mod_consts[64];
                tmp_tuple_element_55 = BUILTIN_FORMAT(tstate, tmp_format_value_55, tmp_format_spec_55);
                Py_DECREF(tmp_format_value_55);
                if (tmp_tuple_element_55 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 372;

                    goto tuple_build_exception_55;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_55, 1, tmp_tuple_element_55);
                tmp_tuple_element_55 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_55, 2, tmp_tuple_element_55);
            }
            goto tuple_build_noexception_55;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_55:;
            Py_DECREF(tmp_string_concat_values_55);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_55:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_55);
            Py_DECREF(tmp_string_concat_values_55);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 372;

                goto dict_build_exception_1;
            }
            tmp_called_value_57 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[21]);

            if (unlikely(tmp_called_value_57 == NULL)) {
                tmp_called_value_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[21]);
            }

            if (tmp_called_value_57 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 373;

                goto dict_build_exception_1;
            }
            tmp_expression_value_111 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_111 == NULL)) {
                tmp_expression_value_111 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_111 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 373;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_111 = mod_consts[153];
            tmp_args_element_value_57 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_111, tmp_subscript_value_111);
            if (tmp_args_element_value_57 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 373;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 373;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_57, tmp_args_element_value_57);
            Py_DECREF(tmp_args_element_value_57);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 373;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_56 = mod_consts[152];
            tmp_string_concat_values_56 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_56;
                PyObject *tmp_expression_value_112;
                PyObject *tmp_subscript_value_112;
                PyObject *tmp_format_spec_56;
                PyTuple_SET_ITEM0(tmp_string_concat_values_56, 0, tmp_tuple_element_56);
                tmp_expression_value_112 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_112 == NULL)) {
                    tmp_expression_value_112 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_112 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 374;

                    goto tuple_build_exception_56;
                }
                tmp_subscript_value_112 = mod_consts[153];
                tmp_format_value_56 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_112, tmp_subscript_value_112);
                if (tmp_format_value_56 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 374;

                    goto tuple_build_exception_56;
                }
                tmp_format_spec_56 = mod_consts[64];
                tmp_tuple_element_56 = BUILTIN_FORMAT(tstate, tmp_format_value_56, tmp_format_spec_56);
                Py_DECREF(tmp_format_value_56);
                if (tmp_tuple_element_56 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 374;

                    goto tuple_build_exception_56;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_56, 1, tmp_tuple_element_56);
                tmp_tuple_element_56 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_56, 2, tmp_tuple_element_56);
            }
            goto tuple_build_noexception_56;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_56:;
            Py_DECREF(tmp_string_concat_values_56);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_56:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_56);
            Py_DECREF(tmp_string_concat_values_56);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 374;

                goto dict_build_exception_1;
            }
            tmp_called_value_58 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[22]);

            if (unlikely(tmp_called_value_58 == NULL)) {
                tmp_called_value_58 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[22]);
            }

            if (tmp_called_value_58 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 375;

                goto dict_build_exception_1;
            }
            tmp_expression_value_113 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_113 == NULL)) {
                tmp_expression_value_113 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_113 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 375;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_113 = mod_consts[153];
            tmp_args_element_value_58 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_113, tmp_subscript_value_113);
            if (tmp_args_element_value_58 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 375;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 375;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_58, tmp_args_element_value_58);
            Py_DECREF(tmp_args_element_value_58);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 375;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_57 = mod_consts[152];
            tmp_string_concat_values_57 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_57;
                PyObject *tmp_expression_value_114;
                PyObject *tmp_subscript_value_114;
                PyObject *tmp_format_spec_57;
                PyTuple_SET_ITEM0(tmp_string_concat_values_57, 0, tmp_tuple_element_57);
                tmp_expression_value_114 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_114 == NULL)) {
                    tmp_expression_value_114 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_114 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 376;

                    goto tuple_build_exception_57;
                }
                tmp_subscript_value_114 = mod_consts[153];
                tmp_format_value_57 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_114, tmp_subscript_value_114);
                if (tmp_format_value_57 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 376;

                    goto tuple_build_exception_57;
                }
                tmp_format_spec_57 = mod_consts[64];
                tmp_tuple_element_57 = BUILTIN_FORMAT(tstate, tmp_format_value_57, tmp_format_spec_57);
                Py_DECREF(tmp_format_value_57);
                if (tmp_tuple_element_57 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 376;

                    goto tuple_build_exception_57;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_57, 1, tmp_tuple_element_57);
                tmp_tuple_element_57 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_57, 2, tmp_tuple_element_57);
            }
            goto tuple_build_noexception_57;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_57:;
            Py_DECREF(tmp_string_concat_values_57);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_57:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_57);
            Py_DECREF(tmp_string_concat_values_57);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 376;

                goto dict_build_exception_1;
            }
            tmp_called_value_59 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[23]);

            if (unlikely(tmp_called_value_59 == NULL)) {
                tmp_called_value_59 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[23]);
            }

            if (tmp_called_value_59 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 377;

                goto dict_build_exception_1;
            }
            tmp_expression_value_115 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_115 == NULL)) {
                tmp_expression_value_115 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_115 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 377;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_115 = mod_consts[153];
            tmp_args_element_value_59 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_115, tmp_subscript_value_115);
            if (tmp_args_element_value_59 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 377;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 377;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_59, tmp_args_element_value_59);
            Py_DECREF(tmp_args_element_value_59);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 377;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_58 = mod_consts[152];
            tmp_string_concat_values_58 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_58;
                PyObject *tmp_expression_value_116;
                PyObject *tmp_subscript_value_116;
                PyObject *tmp_format_spec_58;
                PyTuple_SET_ITEM0(tmp_string_concat_values_58, 0, tmp_tuple_element_58);
                tmp_expression_value_116 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_116 == NULL)) {
                    tmp_expression_value_116 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_116 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 378;

                    goto tuple_build_exception_58;
                }
                tmp_subscript_value_116 = mod_consts[153];
                tmp_format_value_58 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_116, tmp_subscript_value_116);
                if (tmp_format_value_58 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 378;

                    goto tuple_build_exception_58;
                }
                tmp_format_spec_58 = mod_consts[64];
                tmp_tuple_element_58 = BUILTIN_FORMAT(tstate, tmp_format_value_58, tmp_format_spec_58);
                Py_DECREF(tmp_format_value_58);
                if (tmp_tuple_element_58 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 378;

                    goto tuple_build_exception_58;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_58, 1, tmp_tuple_element_58);
                tmp_tuple_element_58 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_58, 2, tmp_tuple_element_58);
            }
            goto tuple_build_noexception_58;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_58:;
            Py_DECREF(tmp_string_concat_values_58);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_58:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_58);
            Py_DECREF(tmp_string_concat_values_58);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 378;

                goto dict_build_exception_1;
            }
            tmp_called_value_60 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[24]);

            if (unlikely(tmp_called_value_60 == NULL)) {
                tmp_called_value_60 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[24]);
            }

            if (tmp_called_value_60 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 379;

                goto dict_build_exception_1;
            }
            tmp_expression_value_117 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_117 == NULL)) {
                tmp_expression_value_117 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_117 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 379;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_117 = mod_consts[153];
            tmp_args_element_value_60 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_117, tmp_subscript_value_117);
            if (tmp_args_element_value_60 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 379;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 379;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_60, tmp_args_element_value_60);
            Py_DECREF(tmp_args_element_value_60);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 379;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_59 = mod_consts[154];
            tmp_string_concat_values_59 = MAKE_TUPLE_EMPTY(5);
            {
                PyObject *tmp_format_value_59;
                PyObject *tmp_expression_value_118;
                PyObject *tmp_subscript_value_118;
                PyObject *tmp_format_spec_59;
                PyObject *tmp_format_value_60;
                PyObject *tmp_expression_value_119;
                PyObject *tmp_subscript_value_119;
                PyObject *tmp_format_spec_60;
                PyTuple_SET_ITEM0(tmp_string_concat_values_59, 0, tmp_tuple_element_59);
                tmp_expression_value_118 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_118 == NULL)) {
                    tmp_expression_value_118 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_118 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 381;

                    goto tuple_build_exception_59;
                }
                tmp_subscript_value_118 = mod_consts[25];
                tmp_format_value_59 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_118, tmp_subscript_value_118);
                if (tmp_format_value_59 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 381;

                    goto tuple_build_exception_59;
                }
                tmp_format_spec_59 = mod_consts[64];
                tmp_tuple_element_59 = BUILTIN_FORMAT(tstate, tmp_format_value_59, tmp_format_spec_59);
                Py_DECREF(tmp_format_value_59);
                if (tmp_tuple_element_59 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 381;

                    goto tuple_build_exception_59;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_59, 1, tmp_tuple_element_59);
                tmp_tuple_element_59 = mod_consts[155];
                PyTuple_SET_ITEM0(tmp_string_concat_values_59, 2, tmp_tuple_element_59);
                tmp_expression_value_119 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_119 == NULL)) {
                    tmp_expression_value_119 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_119 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 381;

                    goto tuple_build_exception_59;
                }
                tmp_subscript_value_119 = mod_consts[156];
                tmp_format_value_60 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_119, tmp_subscript_value_119);
                if (tmp_format_value_60 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 381;

                    goto tuple_build_exception_59;
                }
                tmp_format_spec_60 = mod_consts[64];
                tmp_tuple_element_59 = BUILTIN_FORMAT(tstate, tmp_format_value_60, tmp_format_spec_60);
                Py_DECREF(tmp_format_value_60);
                if (tmp_tuple_element_59 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 381;

                    goto tuple_build_exception_59;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_59, 3, tmp_tuple_element_59);
                tmp_tuple_element_59 = mod_consts[157];
                PyTuple_SET_ITEM0(tmp_string_concat_values_59, 4, tmp_tuple_element_59);
            }
            goto tuple_build_noexception_59;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_59:;
            Py_DECREF(tmp_string_concat_values_59);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_59:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_59);
            Py_DECREF(tmp_string_concat_values_59);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 381;

                goto dict_build_exception_1;
            }
            tmp_called_value_61 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[25]);

            if (unlikely(tmp_called_value_61 == NULL)) {
                tmp_called_value_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[25]);
            }

            if (tmp_called_value_61 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 382;

                goto dict_build_exception_1;
            }
            tmp_expression_value_120 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_120 == NULL)) {
                tmp_expression_value_120 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_120 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 382;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_120 = mod_consts[25];
            tmp_args_element_value_61 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_120, tmp_subscript_value_120);
            if (tmp_args_element_value_61 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 382;

                goto dict_build_exception_1;
            }
            tmp_expression_value_121 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_121 == NULL)) {
                tmp_expression_value_121 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_121 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);
                Py_DECREF(tmp_args_element_value_61);

                exception_lineno = 382;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_121 = mod_consts[156];
            tmp_args_element_value_62 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_121, tmp_subscript_value_121);
            if (tmp_args_element_value_62 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);
                Py_DECREF(tmp_args_element_value_61);

                exception_lineno = 382;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 382;
            {
                PyObject *call_args[] = {tmp_args_element_value_61, tmp_args_element_value_62};
                tmp_dict_value_1 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_61, call_args);
            }

            Py_DECREF(tmp_args_element_value_61);
            Py_DECREF(tmp_args_element_value_62);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 382;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_60 = mod_consts[158];
            tmp_string_concat_values_60 = MAKE_TUPLE_EMPTY(5);
            {
                PyObject *tmp_format_value_61;
                PyObject *tmp_expression_value_122;
                PyObject *tmp_subscript_value_122;
                PyObject *tmp_format_spec_61;
                PyObject *tmp_format_value_62;
                PyObject *tmp_expression_value_123;
                PyObject *tmp_subscript_value_123;
                PyObject *tmp_format_spec_62;
                PyTuple_SET_ITEM0(tmp_string_concat_values_60, 0, tmp_tuple_element_60);
                tmp_expression_value_122 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_122 == NULL)) {
                    tmp_expression_value_122 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_122 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 383;

                    goto tuple_build_exception_60;
                }
                tmp_subscript_value_122 = mod_consts[26];
                tmp_format_value_61 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_122, tmp_subscript_value_122);
                if (tmp_format_value_61 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 383;

                    goto tuple_build_exception_60;
                }
                tmp_format_spec_61 = mod_consts[64];
                tmp_tuple_element_60 = BUILTIN_FORMAT(tstate, tmp_format_value_61, tmp_format_spec_61);
                Py_DECREF(tmp_format_value_61);
                if (tmp_tuple_element_60 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 383;

                    goto tuple_build_exception_60;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_60, 1, tmp_tuple_element_60);
                tmp_tuple_element_60 = mod_consts[159];
                PyTuple_SET_ITEM0(tmp_string_concat_values_60, 2, tmp_tuple_element_60);
                tmp_expression_value_123 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_123 == NULL)) {
                    tmp_expression_value_123 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_123 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 383;

                    goto tuple_build_exception_60;
                }
                tmp_subscript_value_123 = mod_consts[156];
                tmp_format_value_62 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_123, tmp_subscript_value_123);
                if (tmp_format_value_62 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 383;

                    goto tuple_build_exception_60;
                }
                tmp_format_spec_62 = mod_consts[64];
                tmp_tuple_element_60 = BUILTIN_FORMAT(tstate, tmp_format_value_62, tmp_format_spec_62);
                Py_DECREF(tmp_format_value_62);
                if (tmp_tuple_element_60 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 383;

                    goto tuple_build_exception_60;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_60, 3, tmp_tuple_element_60);
                tmp_tuple_element_60 = mod_consts[157];
                PyTuple_SET_ITEM0(tmp_string_concat_values_60, 4, tmp_tuple_element_60);
            }
            goto tuple_build_noexception_60;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_60:;
            Py_DECREF(tmp_string_concat_values_60);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_60:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_60);
            Py_DECREF(tmp_string_concat_values_60);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 383;

                goto dict_build_exception_1;
            }
            tmp_called_value_62 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[26]);

            if (unlikely(tmp_called_value_62 == NULL)) {
                tmp_called_value_62 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[26]);
            }

            if (tmp_called_value_62 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 384;

                goto dict_build_exception_1;
            }
            tmp_expression_value_124 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_124 == NULL)) {
                tmp_expression_value_124 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_124 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 384;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_124 = mod_consts[26];
            tmp_args_element_value_63 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_124, tmp_subscript_value_124);
            if (tmp_args_element_value_63 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 384;

                goto dict_build_exception_1;
            }
            tmp_expression_value_125 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_125 == NULL)) {
                tmp_expression_value_125 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_125 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);
                Py_DECREF(tmp_args_element_value_63);

                exception_lineno = 384;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_125 = mod_consts[156];
            tmp_args_element_value_64 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_125, tmp_subscript_value_125);
            if (tmp_args_element_value_64 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);
                Py_DECREF(tmp_args_element_value_63);

                exception_lineno = 384;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 384;
            {
                PyObject *call_args[] = {tmp_args_element_value_63, tmp_args_element_value_64};
                tmp_dict_value_1 = CALL_FUNCTION_WITH_ARGS2(tstate, tmp_called_value_62, call_args);
            }

            Py_DECREF(tmp_args_element_value_63);
            Py_DECREF(tmp_args_element_value_64);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 384;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_61 = mod_consts[160];
            tmp_string_concat_values_61 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_63;
                PyObject *tmp_expression_value_126;
                PyObject *tmp_subscript_value_126;
                PyObject *tmp_format_spec_63;
                PyTuple_SET_ITEM0(tmp_string_concat_values_61, 0, tmp_tuple_element_61);
                tmp_expression_value_126 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_126 == NULL)) {
                    tmp_expression_value_126 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_126 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 386;

                    goto tuple_build_exception_61;
                }
                tmp_subscript_value_126 = mod_consts[161];
                tmp_format_value_63 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_126, tmp_subscript_value_126);
                if (tmp_format_value_63 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 386;

                    goto tuple_build_exception_61;
                }
                tmp_format_spec_63 = mod_consts[64];
                tmp_tuple_element_61 = BUILTIN_FORMAT(tstate, tmp_format_value_63, tmp_format_spec_63);
                Py_DECREF(tmp_format_value_63);
                if (tmp_tuple_element_61 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 386;

                    goto tuple_build_exception_61;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_61, 1, tmp_tuple_element_61);
                tmp_tuple_element_61 = mod_consts[162];
                PyTuple_SET_ITEM0(tmp_string_concat_values_61, 2, tmp_tuple_element_61);
            }
            goto tuple_build_noexception_61;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_61:;
            Py_DECREF(tmp_string_concat_values_61);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_61:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_61);
            Py_DECREF(tmp_string_concat_values_61);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 386;

                goto dict_build_exception_1;
            }
            tmp_called_value_63 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[28]);

            if (unlikely(tmp_called_value_63 == NULL)) {
                tmp_called_value_63 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[28]);
            }

            if (tmp_called_value_63 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 387;

                goto dict_build_exception_1;
            }
            tmp_expression_value_127 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_127 == NULL)) {
                tmp_expression_value_127 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_127 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 387;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_127 = mod_consts[161];
            tmp_args_element_value_65 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_127, tmp_subscript_value_127);
            if (tmp_args_element_value_65 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 387;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 387;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_63, tmp_args_element_value_65);
            Py_DECREF(tmp_args_element_value_65);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 387;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
            tmp_tuple_element_62 = mod_consts[163];
            tmp_string_concat_values_62 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_64;
                PyObject *tmp_expression_value_128;
                PyObject *tmp_subscript_value_128;
                PyObject *tmp_format_spec_64;
                PyTuple_SET_ITEM0(tmp_string_concat_values_62, 0, tmp_tuple_element_62);
                tmp_expression_value_128 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_128 == NULL)) {
                    tmp_expression_value_128 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_128 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 388;

                    goto tuple_build_exception_62;
                }
                tmp_subscript_value_128 = mod_consts[164];
                tmp_format_value_64 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_128, tmp_subscript_value_128);
                if (tmp_format_value_64 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 388;

                    goto tuple_build_exception_62;
                }
                tmp_format_spec_64 = mod_consts[64];
                tmp_tuple_element_62 = BUILTIN_FORMAT(tstate, tmp_format_value_64, tmp_format_spec_64);
                Py_DECREF(tmp_format_value_64);
                if (tmp_tuple_element_62 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 388;

                    goto tuple_build_exception_62;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_62, 1, tmp_tuple_element_62);
                tmp_tuple_element_62 = mod_consts[162];
                PyTuple_SET_ITEM0(tmp_string_concat_values_62, 2, tmp_tuple_element_62);
            }
            goto tuple_build_noexception_62;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_62:;
            Py_DECREF(tmp_string_concat_values_62);
            goto dict_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_62:;
            tmp_dict_key_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_62);
            Py_DECREF(tmp_string_concat_values_62);
            if (tmp_dict_key_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 388;

                goto dict_build_exception_1;
            }
            tmp_called_value_64 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[28]);

            if (unlikely(tmp_called_value_64 == NULL)) {
                tmp_called_value_64 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[28]);
            }

            if (tmp_called_value_64 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 389;

                goto dict_build_exception_1;
            }
            tmp_expression_value_129 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_129 == NULL)) {
                tmp_expression_value_129 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_129 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 389;

                goto dict_build_exception_1;
            }
            tmp_subscript_value_129 = mod_consts[164];
            tmp_args_element_value_66 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_129, tmp_subscript_value_129);
            if (tmp_args_element_value_66 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 389;

                goto dict_build_exception_1;
            }
            frame_c882f4f0f7cca0ca41864096797f6688->m_frame.f_lineno = 389;
            tmp_dict_value_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tstate, tmp_called_value_64, tmp_args_element_value_66);
            Py_DECREF(tmp_args_element_value_66);
            if (tmp_dict_value_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_dict_key_1);

                exception_lineno = 389;

                goto dict_build_exception_1;
            }
            tmp_res = PyDict_SetItem(tmp_assign_source_46, tmp_dict_key_1, tmp_dict_value_1);
            Py_DECREF(tmp_dict_value_1);
            Py_DECREF(tmp_dict_key_1);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_1;
        // Exception handling pass through code for dict_build:
        dict_build_exception_1:;
        Py_DECREF(tmp_assign_source_46);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_1:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[165], tmp_assign_source_46);
    }
    {
        PyObject *tmp_assign_source_47;
        PyObject *tmp_list_element_1;
        PyObject *tmp_string_concat_values_63;
        PyObject *tmp_tuple_element_63;
        tmp_tuple_element_63 = mod_consts[160];
        tmp_string_concat_values_63 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_65;
            PyObject *tmp_expression_value_130;
            PyObject *tmp_subscript_value_130;
            PyObject *tmp_format_spec_65;
            PyTuple_SET_ITEM0(tmp_string_concat_values_63, 0, tmp_tuple_element_63);
            tmp_expression_value_130 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_130 == NULL)) {
                tmp_expression_value_130 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_130 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 393;

                goto tuple_build_exception_63;
            }
            tmp_subscript_value_130 = mod_consts[161];
            tmp_format_value_65 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_130, tmp_subscript_value_130);
            if (tmp_format_value_65 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 393;

                goto tuple_build_exception_63;
            }
            tmp_format_spec_65 = mod_consts[64];
            tmp_tuple_element_63 = BUILTIN_FORMAT(tstate, tmp_format_value_65, tmp_format_spec_65);
            Py_DECREF(tmp_format_value_65);
            if (tmp_tuple_element_63 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 393;

                goto tuple_build_exception_63;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_63, 1, tmp_tuple_element_63);
            tmp_tuple_element_63 = mod_consts[162];
            PyTuple_SET_ITEM0(tmp_string_concat_values_63, 2, tmp_tuple_element_63);
        }
        goto tuple_build_noexception_63;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_63:;
        Py_DECREF(tmp_string_concat_values_63);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_63:;
        tmp_list_element_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_63);
        Py_DECREF(tmp_string_concat_values_63);
        if (tmp_list_element_1 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 393;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_47 = MAKE_LIST_EMPTY(2);
        {
            PyObject *tmp_string_concat_values_64;
            PyObject *tmp_tuple_element_64;
            PyList_SET_ITEM(tmp_assign_source_47, 0, tmp_list_element_1);
            tmp_tuple_element_64 = mod_consts[163];
            tmp_string_concat_values_64 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_66;
                PyObject *tmp_expression_value_131;
                PyObject *tmp_subscript_value_131;
                PyObject *tmp_format_spec_66;
                PyTuple_SET_ITEM0(tmp_string_concat_values_64, 0, tmp_tuple_element_64);
                tmp_expression_value_131 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_131 == NULL)) {
                    tmp_expression_value_131 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_131 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 394;

                    goto tuple_build_exception_64;
                }
                tmp_subscript_value_131 = mod_consts[164];
                tmp_format_value_66 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_131, tmp_subscript_value_131);
                if (tmp_format_value_66 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 394;

                    goto tuple_build_exception_64;
                }
                tmp_format_spec_66 = mod_consts[64];
                tmp_tuple_element_64 = BUILTIN_FORMAT(tstate, tmp_format_value_66, tmp_format_spec_66);
                Py_DECREF(tmp_format_value_66);
                if (tmp_tuple_element_64 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 394;

                    goto tuple_build_exception_64;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_64, 1, tmp_tuple_element_64);
                tmp_tuple_element_64 = mod_consts[162];
                PyTuple_SET_ITEM0(tmp_string_concat_values_64, 2, tmp_tuple_element_64);
            }
            goto tuple_build_noexception_64;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_64:;
            Py_DECREF(tmp_string_concat_values_64);
            goto list_build_exception_1;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_64:;
            tmp_list_element_1 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_64);
            Py_DECREF(tmp_string_concat_values_64);
            if (tmp_list_element_1 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 394;

                goto list_build_exception_1;
            }
            PyList_SET_ITEM(tmp_assign_source_47, 1, tmp_list_element_1);
        }
        goto list_build_noexception_1;
        // Exception handling pass through code for list_build:
        list_build_exception_1:;
        Py_DECREF(tmp_assign_source_47);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_1:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[166], tmp_assign_source_47);
    }
    {
        PyObject *tmp_assign_source_48;
        PyObject *tmp_dict_key_2;
        PyObject *tmp_dict_value_2;
        PyObject *tmp_list_element_2;
        PyObject *tmp_string_concat_values_65;
        PyObject *tmp_tuple_element_65;
        tmp_dict_key_2 = mod_consts[167];
        tmp_tuple_element_65 = mod_consts[62];
        tmp_string_concat_values_65 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_67;
            PyObject *tmp_expression_value_132;
            PyObject *tmp_subscript_value_132;
            PyObject *tmp_format_spec_67;
            PyTuple_SET_ITEM0(tmp_string_concat_values_65, 0, tmp_tuple_element_65);
            tmp_expression_value_132 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_132 == NULL)) {
                tmp_expression_value_132 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_132 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 398;

                goto tuple_build_exception_65;
            }
            tmp_subscript_value_132 = mod_consts[63];
            tmp_format_value_67 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_132, tmp_subscript_value_132);
            if (tmp_format_value_67 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 398;

                goto tuple_build_exception_65;
            }
            tmp_format_spec_67 = mod_consts[64];
            tmp_tuple_element_65 = BUILTIN_FORMAT(tstate, tmp_format_value_67, tmp_format_spec_67);
            Py_DECREF(tmp_format_value_67);
            if (tmp_tuple_element_65 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 398;

                goto tuple_build_exception_65;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_65, 1, tmp_tuple_element_65);
            tmp_tuple_element_65 = mod_consts[65];
            PyTuple_SET_ITEM0(tmp_string_concat_values_65, 2, tmp_tuple_element_65);
        }
        goto tuple_build_noexception_65;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_65:;
        Py_DECREF(tmp_string_concat_values_65);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_65:;
        tmp_list_element_2 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_65);
        Py_DECREF(tmp_string_concat_values_65);
        if (tmp_list_element_2 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 398;

            goto frame_exception_exit_1;
        }
        tmp_dict_value_2 = MAKE_LIST_EMPTY(2);
        {
            PyObject *tmp_string_concat_values_66;
            PyObject *tmp_tuple_element_66;
            PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_2);
            tmp_tuple_element_66 = mod_consts[66];
            tmp_string_concat_values_66 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_68;
                PyObject *tmp_expression_value_133;
                PyObject *tmp_subscript_value_133;
                PyObject *tmp_format_spec_68;
                PyTuple_SET_ITEM0(tmp_string_concat_values_66, 0, tmp_tuple_element_66);
                tmp_expression_value_133 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_133 == NULL)) {
                    tmp_expression_value_133 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_133 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 399;

                    goto tuple_build_exception_66;
                }
                tmp_subscript_value_133 = mod_consts[67];
                tmp_format_value_68 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_133, tmp_subscript_value_133);
                if (tmp_format_value_68 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 399;

                    goto tuple_build_exception_66;
                }
                tmp_format_spec_68 = mod_consts[64];
                tmp_tuple_element_66 = BUILTIN_FORMAT(tstate, tmp_format_value_68, tmp_format_spec_68);
                Py_DECREF(tmp_format_value_68);
                if (tmp_tuple_element_66 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 399;

                    goto tuple_build_exception_66;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_66, 1, tmp_tuple_element_66);
                tmp_tuple_element_66 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_66, 2, tmp_tuple_element_66);
            }
            goto tuple_build_noexception_66;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_66:;
            Py_DECREF(tmp_string_concat_values_66);
            goto list_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_66:;
            tmp_list_element_2 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_66);
            Py_DECREF(tmp_string_concat_values_66);
            if (tmp_list_element_2 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 399;

                goto list_build_exception_2;
            }
            PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_2);
        }
        goto list_build_noexception_2;
        // Exception handling pass through code for list_build:
        list_build_exception_2:;
        Py_DECREF(tmp_dict_value_2);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_2:;
        tmp_assign_source_48 = _PyDict_NewPresized( 7 );
        {
            PyObject *tmp_list_element_3;
            PyObject *tmp_string_concat_values_67;
            PyObject *tmp_tuple_element_67;
            PyObject *tmp_list_element_4;
            PyObject *tmp_string_concat_values_69;
            PyObject *tmp_tuple_element_69;
            PyObject *tmp_list_element_5;
            PyObject *tmp_string_concat_values_71;
            PyObject *tmp_tuple_element_71;
            PyObject *tmp_list_element_6;
            PyObject *tmp_string_concat_values_73;
            PyObject *tmp_tuple_element_73;
            PyObject *tmp_list_element_7;
            PyObject *tmp_string_concat_values_81;
            PyObject *tmp_tuple_element_81;
            PyObject *tmp_list_element_8;
            PyObject *tmp_string_concat_values_83;
            PyObject *tmp_tuple_element_83;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
            tmp_dict_key_2 = mod_consts[168];
            tmp_tuple_element_67 = mod_consts[68];
            tmp_string_concat_values_67 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_69;
                PyObject *tmp_expression_value_134;
                PyObject *tmp_subscript_value_134;
                PyObject *tmp_format_spec_69;
                PyTuple_SET_ITEM0(tmp_string_concat_values_67, 0, tmp_tuple_element_67);
                tmp_expression_value_134 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_134 == NULL)) {
                    tmp_expression_value_134 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_134 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 402;

                    goto tuple_build_exception_67;
                }
                tmp_subscript_value_134 = mod_consts[63];
                tmp_format_value_69 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_134, tmp_subscript_value_134);
                if (tmp_format_value_69 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 402;

                    goto tuple_build_exception_67;
                }
                tmp_format_spec_69 = mod_consts[64];
                tmp_tuple_element_67 = BUILTIN_FORMAT(tstate, tmp_format_value_69, tmp_format_spec_69);
                Py_DECREF(tmp_format_value_69);
                if (tmp_tuple_element_67 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 402;

                    goto tuple_build_exception_67;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_67, 1, tmp_tuple_element_67);
                tmp_tuple_element_67 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_67, 2, tmp_tuple_element_67);
            }
            goto tuple_build_noexception_67;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_67:;
            Py_DECREF(tmp_string_concat_values_67);
            goto dict_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_67:;
            tmp_list_element_3 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_67);
            Py_DECREF(tmp_string_concat_values_67);
            if (tmp_list_element_3 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 402;

                goto dict_build_exception_2;
            }
            tmp_dict_value_2 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_68;
                PyObject *tmp_tuple_element_68;
                PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_3);
                tmp_tuple_element_68 = mod_consts[70];
                tmp_string_concat_values_68 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_70;
                    PyObject *tmp_expression_value_135;
                    PyObject *tmp_subscript_value_135;
                    PyObject *tmp_format_spec_70;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_68, 0, tmp_tuple_element_68);
                    tmp_expression_value_135 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_135 == NULL)) {
                        tmp_expression_value_135 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_135 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 403;

                        goto tuple_build_exception_68;
                    }
                    tmp_subscript_value_135 = mod_consts[67];
                    tmp_format_value_70 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_135, tmp_subscript_value_135);
                    if (tmp_format_value_70 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 403;

                        goto tuple_build_exception_68;
                    }
                    tmp_format_spec_70 = mod_consts[64];
                    tmp_tuple_element_68 = BUILTIN_FORMAT(tstate, tmp_format_value_70, tmp_format_spec_70);
                    Py_DECREF(tmp_format_value_70);
                    if (tmp_tuple_element_68 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 403;

                        goto tuple_build_exception_68;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_68, 1, tmp_tuple_element_68);
                    tmp_tuple_element_68 = mod_consts[69];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_68, 2, tmp_tuple_element_68);
                }
                goto tuple_build_noexception_68;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_68:;
                Py_DECREF(tmp_string_concat_values_68);
                goto list_build_exception_3;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_68:;
                tmp_list_element_3 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_68);
                Py_DECREF(tmp_string_concat_values_68);
                if (tmp_list_element_3 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 403;

                    goto list_build_exception_3;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_3);
            }
            goto list_build_noexception_3;
            // Exception handling pass through code for list_build:
            list_build_exception_3:;
            Py_DECREF(tmp_dict_value_2);
            goto dict_build_exception_2;
            // Finished with no exception for list_build:
            list_build_noexception_3:;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
            tmp_dict_key_2 = mod_consts[169];
            tmp_tuple_element_69 = mod_consts[71];
            tmp_string_concat_values_69 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_71;
                PyObject *tmp_expression_value_136;
                PyObject *tmp_subscript_value_136;
                PyObject *tmp_format_spec_71;
                PyTuple_SET_ITEM0(tmp_string_concat_values_69, 0, tmp_tuple_element_69);
                tmp_expression_value_136 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_136 == NULL)) {
                    tmp_expression_value_136 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_136 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 406;

                    goto tuple_build_exception_69;
                }
                tmp_subscript_value_136 = mod_consts[63];
                tmp_format_value_71 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_136, tmp_subscript_value_136);
                if (tmp_format_value_71 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 406;

                    goto tuple_build_exception_69;
                }
                tmp_format_spec_71 = mod_consts[64];
                tmp_tuple_element_69 = BUILTIN_FORMAT(tstate, tmp_format_value_71, tmp_format_spec_71);
                Py_DECREF(tmp_format_value_71);
                if (tmp_tuple_element_69 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 406;

                    goto tuple_build_exception_69;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_69, 1, tmp_tuple_element_69);
                tmp_tuple_element_69 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_69, 2, tmp_tuple_element_69);
            }
            goto tuple_build_noexception_69;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_69:;
            Py_DECREF(tmp_string_concat_values_69);
            goto dict_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_69:;
            tmp_list_element_4 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_69);
            Py_DECREF(tmp_string_concat_values_69);
            if (tmp_list_element_4 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 406;

                goto dict_build_exception_2;
            }
            tmp_dict_value_2 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_70;
                PyObject *tmp_tuple_element_70;
                PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_4);
                tmp_tuple_element_70 = mod_consts[73];
                tmp_string_concat_values_70 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_72;
                    PyObject *tmp_expression_value_137;
                    PyObject *tmp_subscript_value_137;
                    PyObject *tmp_format_spec_72;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_70, 0, tmp_tuple_element_70);
                    tmp_expression_value_137 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_137 == NULL)) {
                        tmp_expression_value_137 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_137 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 407;

                        goto tuple_build_exception_70;
                    }
                    tmp_subscript_value_137 = mod_consts[67];
                    tmp_format_value_72 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_137, tmp_subscript_value_137);
                    if (tmp_format_value_72 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 407;

                        goto tuple_build_exception_70;
                    }
                    tmp_format_spec_72 = mod_consts[64];
                    tmp_tuple_element_70 = BUILTIN_FORMAT(tstate, tmp_format_value_72, tmp_format_spec_72);
                    Py_DECREF(tmp_format_value_72);
                    if (tmp_tuple_element_70 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 407;

                        goto tuple_build_exception_70;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_70, 1, tmp_tuple_element_70);
                    tmp_tuple_element_70 = mod_consts[72];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_70, 2, tmp_tuple_element_70);
                }
                goto tuple_build_noexception_70;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_70:;
                Py_DECREF(tmp_string_concat_values_70);
                goto list_build_exception_4;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_70:;
                tmp_list_element_4 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_70);
                Py_DECREF(tmp_string_concat_values_70);
                if (tmp_list_element_4 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 407;

                    goto list_build_exception_4;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_4);
            }
            goto list_build_noexception_4;
            // Exception handling pass through code for list_build:
            list_build_exception_4:;
            Py_DECREF(tmp_dict_value_2);
            goto dict_build_exception_2;
            // Finished with no exception for list_build:
            list_build_noexception_4:;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
            tmp_dict_key_2 = mod_consts[170];
            tmp_tuple_element_71 = mod_consts[74];
            tmp_string_concat_values_71 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_73;
                PyObject *tmp_expression_value_138;
                PyObject *tmp_subscript_value_138;
                PyObject *tmp_format_spec_73;
                PyTuple_SET_ITEM0(tmp_string_concat_values_71, 0, tmp_tuple_element_71);
                tmp_expression_value_138 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_138 == NULL)) {
                    tmp_expression_value_138 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_138 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 410;

                    goto tuple_build_exception_71;
                }
                tmp_subscript_value_138 = mod_consts[63];
                tmp_format_value_73 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_138, tmp_subscript_value_138);
                if (tmp_format_value_73 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 410;

                    goto tuple_build_exception_71;
                }
                tmp_format_spec_73 = mod_consts[64];
                tmp_tuple_element_71 = BUILTIN_FORMAT(tstate, tmp_format_value_73, tmp_format_spec_73);
                Py_DECREF(tmp_format_value_73);
                if (tmp_tuple_element_71 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 410;

                    goto tuple_build_exception_71;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_71, 1, tmp_tuple_element_71);
                tmp_tuple_element_71 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_71, 2, tmp_tuple_element_71);
            }
            goto tuple_build_noexception_71;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_71:;
            Py_DECREF(tmp_string_concat_values_71);
            goto dict_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_71:;
            tmp_list_element_5 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_71);
            Py_DECREF(tmp_string_concat_values_71);
            if (tmp_list_element_5 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 410;

                goto dict_build_exception_2;
            }
            tmp_dict_value_2 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_72;
                PyObject *tmp_tuple_element_72;
                PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_5);
                tmp_tuple_element_72 = mod_consts[76];
                tmp_string_concat_values_72 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_74;
                    PyObject *tmp_expression_value_139;
                    PyObject *tmp_subscript_value_139;
                    PyObject *tmp_format_spec_74;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_72, 0, tmp_tuple_element_72);
                    tmp_expression_value_139 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_139 == NULL)) {
                        tmp_expression_value_139 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_139 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 411;

                        goto tuple_build_exception_72;
                    }
                    tmp_subscript_value_139 = mod_consts[67];
                    tmp_format_value_74 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_139, tmp_subscript_value_139);
                    if (tmp_format_value_74 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 411;

                        goto tuple_build_exception_72;
                    }
                    tmp_format_spec_74 = mod_consts[64];
                    tmp_tuple_element_72 = BUILTIN_FORMAT(tstate, tmp_format_value_74, tmp_format_spec_74);
                    Py_DECREF(tmp_format_value_74);
                    if (tmp_tuple_element_72 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 411;

                        goto tuple_build_exception_72;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_72, 1, tmp_tuple_element_72);
                    tmp_tuple_element_72 = mod_consts[75];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_72, 2, tmp_tuple_element_72);
                }
                goto tuple_build_noexception_72;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_72:;
                Py_DECREF(tmp_string_concat_values_72);
                goto list_build_exception_5;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_72:;
                tmp_list_element_5 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_72);
                Py_DECREF(tmp_string_concat_values_72);
                if (tmp_list_element_5 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 411;

                    goto list_build_exception_5;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_5);
            }
            goto list_build_noexception_5;
            // Exception handling pass through code for list_build:
            list_build_exception_5:;
            Py_DECREF(tmp_dict_value_2);
            goto dict_build_exception_2;
            // Finished with no exception for list_build:
            list_build_noexception_5:;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
            tmp_dict_key_2 = mod_consts[64];
            tmp_tuple_element_73 = mod_consts[87];
            tmp_string_concat_values_73 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_75;
                PyObject *tmp_expression_value_140;
                PyObject *tmp_subscript_value_140;
                PyObject *tmp_format_spec_75;
                PyTuple_SET_ITEM0(tmp_string_concat_values_73, 0, tmp_tuple_element_73);
                tmp_expression_value_140 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_140 == NULL)) {
                    tmp_expression_value_140 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_140 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 414;

                    goto tuple_build_exception_73;
                }
                tmp_subscript_value_140 = mod_consts[88];
                tmp_format_value_75 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_140, tmp_subscript_value_140);
                if (tmp_format_value_75 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 414;

                    goto tuple_build_exception_73;
                }
                tmp_format_spec_75 = mod_consts[64];
                tmp_tuple_element_73 = BUILTIN_FORMAT(tstate, tmp_format_value_75, tmp_format_spec_75);
                Py_DECREF(tmp_format_value_75);
                if (tmp_tuple_element_73 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 414;

                    goto tuple_build_exception_73;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_73, 1, tmp_tuple_element_73);
                tmp_tuple_element_73 = mod_consts[89];
                PyTuple_SET_ITEM0(tmp_string_concat_values_73, 2, tmp_tuple_element_73);
            }
            goto tuple_build_noexception_73;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_73:;
            Py_DECREF(tmp_string_concat_values_73);
            goto dict_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_73:;
            tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_73);
            Py_DECREF(tmp_string_concat_values_73);
            if (tmp_list_element_6 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 414;

                goto dict_build_exception_2;
            }
            tmp_dict_value_2 = MAKE_LIST_EMPTY(8);
            {
                PyObject *tmp_string_concat_values_74;
                PyObject *tmp_tuple_element_74;
                PyObject *tmp_string_concat_values_75;
                PyObject *tmp_tuple_element_75;
                PyObject *tmp_string_concat_values_76;
                PyObject *tmp_tuple_element_76;
                PyObject *tmp_string_concat_values_77;
                PyObject *tmp_tuple_element_77;
                PyObject *tmp_string_concat_values_78;
                PyObject *tmp_tuple_element_78;
                PyObject *tmp_string_concat_values_79;
                PyObject *tmp_tuple_element_79;
                PyObject *tmp_string_concat_values_80;
                PyObject *tmp_tuple_element_80;
                PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_6);
                tmp_tuple_element_74 = mod_consts[90];
                tmp_string_concat_values_74 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_76;
                    PyObject *tmp_expression_value_141;
                    PyObject *tmp_subscript_value_141;
                    PyObject *tmp_format_spec_76;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_74, 0, tmp_tuple_element_74);
                    tmp_expression_value_141 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_141 == NULL)) {
                        tmp_expression_value_141 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_141 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 415;

                        goto tuple_build_exception_74;
                    }
                    tmp_subscript_value_141 = mod_consts[88];
                    tmp_format_value_76 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_141, tmp_subscript_value_141);
                    if (tmp_format_value_76 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 415;

                        goto tuple_build_exception_74;
                    }
                    tmp_format_spec_76 = mod_consts[64];
                    tmp_tuple_element_74 = BUILTIN_FORMAT(tstate, tmp_format_value_76, tmp_format_spec_76);
                    Py_DECREF(tmp_format_value_76);
                    if (tmp_tuple_element_74 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 415;

                        goto tuple_build_exception_74;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_74, 1, tmp_tuple_element_74);
                    tmp_tuple_element_74 = mod_consts[91];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_74, 2, tmp_tuple_element_74);
                }
                goto tuple_build_noexception_74;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_74:;
                Py_DECREF(tmp_string_concat_values_74);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_74:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_74);
                Py_DECREF(tmp_string_concat_values_74);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 415;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_6);
                tmp_tuple_element_75 = mod_consts[92];
                tmp_string_concat_values_75 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_77;
                    PyObject *tmp_expression_value_142;
                    PyObject *tmp_subscript_value_142;
                    PyObject *tmp_format_spec_77;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_75, 0, tmp_tuple_element_75);
                    tmp_expression_value_142 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_142 == NULL)) {
                        tmp_expression_value_142 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_142 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 416;

                        goto tuple_build_exception_75;
                    }
                    tmp_subscript_value_142 = mod_consts[88];
                    tmp_format_value_77 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_142, tmp_subscript_value_142);
                    if (tmp_format_value_77 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 416;

                        goto tuple_build_exception_75;
                    }
                    tmp_format_spec_77 = mod_consts[64];
                    tmp_tuple_element_75 = BUILTIN_FORMAT(tstate, tmp_format_value_77, tmp_format_spec_77);
                    Py_DECREF(tmp_format_value_77);
                    if (tmp_tuple_element_75 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 416;

                        goto tuple_build_exception_75;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_75, 1, tmp_tuple_element_75);
                    tmp_tuple_element_75 = mod_consts[93];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_75, 2, tmp_tuple_element_75);
                }
                goto tuple_build_noexception_75;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_75:;
                Py_DECREF(tmp_string_concat_values_75);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_75:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_75);
                Py_DECREF(tmp_string_concat_values_75);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 416;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 2, tmp_list_element_6);
                tmp_tuple_element_76 = mod_consts[94];
                tmp_string_concat_values_76 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_78;
                    PyObject *tmp_expression_value_143;
                    PyObject *tmp_subscript_value_143;
                    PyObject *tmp_format_spec_78;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_76, 0, tmp_tuple_element_76);
                    tmp_expression_value_143 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_143 == NULL)) {
                        tmp_expression_value_143 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_143 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 417;

                        goto tuple_build_exception_76;
                    }
                    tmp_subscript_value_143 = mod_consts[88];
                    tmp_format_value_78 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_143, tmp_subscript_value_143);
                    if (tmp_format_value_78 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 417;

                        goto tuple_build_exception_76;
                    }
                    tmp_format_spec_78 = mod_consts[64];
                    tmp_tuple_element_76 = BUILTIN_FORMAT(tstate, tmp_format_value_78, tmp_format_spec_78);
                    Py_DECREF(tmp_format_value_78);
                    if (tmp_tuple_element_76 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 417;

                        goto tuple_build_exception_76;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_76, 1, tmp_tuple_element_76);
                    tmp_tuple_element_76 = mod_consts[95];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_76, 2, tmp_tuple_element_76);
                }
                goto tuple_build_noexception_76;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_76:;
                Py_DECREF(tmp_string_concat_values_76);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_76:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_76);
                Py_DECREF(tmp_string_concat_values_76);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 417;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 3, tmp_list_element_6);
                tmp_tuple_element_77 = mod_consts[96];
                tmp_string_concat_values_77 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_79;
                    PyObject *tmp_expression_value_144;
                    PyObject *tmp_subscript_value_144;
                    PyObject *tmp_format_spec_79;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_77, 0, tmp_tuple_element_77);
                    tmp_expression_value_144 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_144 == NULL)) {
                        tmp_expression_value_144 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_144 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 418;

                        goto tuple_build_exception_77;
                    }
                    tmp_subscript_value_144 = mod_consts[97];
                    tmp_format_value_79 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_144, tmp_subscript_value_144);
                    if (tmp_format_value_79 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 418;

                        goto tuple_build_exception_77;
                    }
                    tmp_format_spec_79 = mod_consts[64];
                    tmp_tuple_element_77 = BUILTIN_FORMAT(tstate, tmp_format_value_79, tmp_format_spec_79);
                    Py_DECREF(tmp_format_value_79);
                    if (tmp_tuple_element_77 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 418;

                        goto tuple_build_exception_77;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_77, 1, tmp_tuple_element_77);
                    tmp_tuple_element_77 = mod_consts[89];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_77, 2, tmp_tuple_element_77);
                }
                goto tuple_build_noexception_77;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_77:;
                Py_DECREF(tmp_string_concat_values_77);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_77:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_77);
                Py_DECREF(tmp_string_concat_values_77);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 418;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 4, tmp_list_element_6);
                tmp_tuple_element_78 = mod_consts[98];
                tmp_string_concat_values_78 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_80;
                    PyObject *tmp_expression_value_145;
                    PyObject *tmp_subscript_value_145;
                    PyObject *tmp_format_spec_80;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_78, 0, tmp_tuple_element_78);
                    tmp_expression_value_145 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_145 == NULL)) {
                        tmp_expression_value_145 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_145 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 419;

                        goto tuple_build_exception_78;
                    }
                    tmp_subscript_value_145 = mod_consts[97];
                    tmp_format_value_80 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_145, tmp_subscript_value_145);
                    if (tmp_format_value_80 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 419;

                        goto tuple_build_exception_78;
                    }
                    tmp_format_spec_80 = mod_consts[64];
                    tmp_tuple_element_78 = BUILTIN_FORMAT(tstate, tmp_format_value_80, tmp_format_spec_80);
                    Py_DECREF(tmp_format_value_80);
                    if (tmp_tuple_element_78 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 419;

                        goto tuple_build_exception_78;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_78, 1, tmp_tuple_element_78);
                    tmp_tuple_element_78 = mod_consts[91];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_78, 2, tmp_tuple_element_78);
                }
                goto tuple_build_noexception_78;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_78:;
                Py_DECREF(tmp_string_concat_values_78);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_78:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_78);
                Py_DECREF(tmp_string_concat_values_78);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 419;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 5, tmp_list_element_6);
                tmp_tuple_element_79 = mod_consts[99];
                tmp_string_concat_values_79 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_81;
                    PyObject *tmp_expression_value_146;
                    PyObject *tmp_subscript_value_146;
                    PyObject *tmp_format_spec_81;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_79, 0, tmp_tuple_element_79);
                    tmp_expression_value_146 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_146 == NULL)) {
                        tmp_expression_value_146 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_146 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 420;

                        goto tuple_build_exception_79;
                    }
                    tmp_subscript_value_146 = mod_consts[97];
                    tmp_format_value_81 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_146, tmp_subscript_value_146);
                    if (tmp_format_value_81 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 420;

                        goto tuple_build_exception_79;
                    }
                    tmp_format_spec_81 = mod_consts[64];
                    tmp_tuple_element_79 = BUILTIN_FORMAT(tstate, tmp_format_value_81, tmp_format_spec_81);
                    Py_DECREF(tmp_format_value_81);
                    if (tmp_tuple_element_79 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 420;

                        goto tuple_build_exception_79;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_79, 1, tmp_tuple_element_79);
                    tmp_tuple_element_79 = mod_consts[93];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_79, 2, tmp_tuple_element_79);
                }
                goto tuple_build_noexception_79;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_79:;
                Py_DECREF(tmp_string_concat_values_79);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_79:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_79);
                Py_DECREF(tmp_string_concat_values_79);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 420;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 6, tmp_list_element_6);
                tmp_tuple_element_80 = mod_consts[100];
                tmp_string_concat_values_80 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_82;
                    PyObject *tmp_expression_value_147;
                    PyObject *tmp_subscript_value_147;
                    PyObject *tmp_format_spec_82;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_80, 0, tmp_tuple_element_80);
                    tmp_expression_value_147 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_147 == NULL)) {
                        tmp_expression_value_147 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_147 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 421;

                        goto tuple_build_exception_80;
                    }
                    tmp_subscript_value_147 = mod_consts[97];
                    tmp_format_value_82 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_147, tmp_subscript_value_147);
                    if (tmp_format_value_82 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 421;

                        goto tuple_build_exception_80;
                    }
                    tmp_format_spec_82 = mod_consts[64];
                    tmp_tuple_element_80 = BUILTIN_FORMAT(tstate, tmp_format_value_82, tmp_format_spec_82);
                    Py_DECREF(tmp_format_value_82);
                    if (tmp_tuple_element_80 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 421;

                        goto tuple_build_exception_80;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_80, 1, tmp_tuple_element_80);
                    tmp_tuple_element_80 = mod_consts[95];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_80, 2, tmp_tuple_element_80);
                }
                goto tuple_build_noexception_80;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_80:;
                Py_DECREF(tmp_string_concat_values_80);
                goto list_build_exception_6;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_80:;
                tmp_list_element_6 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_80);
                Py_DECREF(tmp_string_concat_values_80);
                if (tmp_list_element_6 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 421;

                    goto list_build_exception_6;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 7, tmp_list_element_6);
            }
            goto list_build_noexception_6;
            // Exception handling pass through code for list_build:
            list_build_exception_6:;
            Py_DECREF(tmp_dict_value_2);
            goto dict_build_exception_2;
            // Finished with no exception for list_build:
            list_build_noexception_6:;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
            tmp_dict_key_2 = mod_consts[171];
            tmp_tuple_element_81 = mod_consts[77];
            tmp_string_concat_values_81 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_83;
                PyObject *tmp_expression_value_148;
                PyObject *tmp_subscript_value_148;
                PyObject *tmp_format_spec_83;
                PyTuple_SET_ITEM0(tmp_string_concat_values_81, 0, tmp_tuple_element_81);
                tmp_expression_value_148 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_148 == NULL)) {
                    tmp_expression_value_148 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_148 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 424;

                    goto tuple_build_exception_81;
                }
                tmp_subscript_value_148 = mod_consts[78];
                tmp_format_value_83 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_148, tmp_subscript_value_148);
                if (tmp_format_value_83 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 424;

                    goto tuple_build_exception_81;
                }
                tmp_format_spec_83 = mod_consts[64];
                tmp_tuple_element_81 = BUILTIN_FORMAT(tstate, tmp_format_value_83, tmp_format_spec_83);
                Py_DECREF(tmp_format_value_83);
                if (tmp_tuple_element_81 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 424;

                    goto tuple_build_exception_81;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_81, 1, tmp_tuple_element_81);
                tmp_tuple_element_81 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_81, 2, tmp_tuple_element_81);
            }
            goto tuple_build_noexception_81;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_81:;
            Py_DECREF(tmp_string_concat_values_81);
            goto dict_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_81:;
            tmp_list_element_7 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_81);
            Py_DECREF(tmp_string_concat_values_81);
            if (tmp_list_element_7 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 424;

                goto dict_build_exception_2;
            }
            tmp_dict_value_2 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_82;
                PyObject *tmp_tuple_element_82;
                PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_7);
                tmp_tuple_element_82 = mod_consts[80];
                tmp_string_concat_values_82 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_84;
                    PyObject *tmp_expression_value_149;
                    PyObject *tmp_subscript_value_149;
                    PyObject *tmp_format_spec_84;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_82, 0, tmp_tuple_element_82);
                    tmp_expression_value_149 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_149 == NULL)) {
                        tmp_expression_value_149 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_149 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 425;

                        goto tuple_build_exception_82;
                    }
                    tmp_subscript_value_149 = mod_consts[81];
                    tmp_format_value_84 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_149, tmp_subscript_value_149);
                    if (tmp_format_value_84 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 425;

                        goto tuple_build_exception_82;
                    }
                    tmp_format_spec_84 = mod_consts[64];
                    tmp_tuple_element_82 = BUILTIN_FORMAT(tstate, tmp_format_value_84, tmp_format_spec_84);
                    Py_DECREF(tmp_format_value_84);
                    if (tmp_tuple_element_82 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 425;

                        goto tuple_build_exception_82;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_82, 1, tmp_tuple_element_82);
                    tmp_tuple_element_82 = mod_consts[79];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_82, 2, tmp_tuple_element_82);
                }
                goto tuple_build_noexception_82;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_82:;
                Py_DECREF(tmp_string_concat_values_82);
                goto list_build_exception_7;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_82:;
                tmp_list_element_7 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_82);
                Py_DECREF(tmp_string_concat_values_82);
                if (tmp_list_element_7 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 425;

                    goto list_build_exception_7;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_7);
            }
            goto list_build_noexception_7;
            // Exception handling pass through code for list_build:
            list_build_exception_7:;
            Py_DECREF(tmp_dict_value_2);
            goto dict_build_exception_2;
            // Finished with no exception for list_build:
            list_build_noexception_7:;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
            tmp_dict_key_2 = mod_consts[172];
            tmp_tuple_element_83 = mod_consts[82];
            tmp_string_concat_values_83 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_85;
                PyObject *tmp_expression_value_150;
                PyObject *tmp_subscript_value_150;
                PyObject *tmp_format_spec_85;
                PyTuple_SET_ITEM0(tmp_string_concat_values_83, 0, tmp_tuple_element_83);
                tmp_expression_value_150 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_150 == NULL)) {
                    tmp_expression_value_150 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_150 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 428;

                    goto tuple_build_exception_83;
                }
                tmp_subscript_value_150 = mod_consts[83];
                tmp_format_value_85 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_150, tmp_subscript_value_150);
                if (tmp_format_value_85 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 428;

                    goto tuple_build_exception_83;
                }
                tmp_format_spec_85 = mod_consts[64];
                tmp_tuple_element_83 = BUILTIN_FORMAT(tstate, tmp_format_value_85, tmp_format_spec_85);
                Py_DECREF(tmp_format_value_85);
                if (tmp_tuple_element_83 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 428;

                    goto tuple_build_exception_83;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_83, 1, tmp_tuple_element_83);
                tmp_tuple_element_83 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_83, 2, tmp_tuple_element_83);
            }
            goto tuple_build_noexception_83;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_83:;
            Py_DECREF(tmp_string_concat_values_83);
            goto dict_build_exception_2;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_83:;
            tmp_list_element_8 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_83);
            Py_DECREF(tmp_string_concat_values_83);
            if (tmp_list_element_8 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 428;

                goto dict_build_exception_2;
            }
            tmp_dict_value_2 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_84;
                PyObject *tmp_tuple_element_84;
                PyList_SET_ITEM(tmp_dict_value_2, 0, tmp_list_element_8);
                tmp_tuple_element_84 = mod_consts[85];
                tmp_string_concat_values_84 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_86;
                    PyObject *tmp_expression_value_151;
                    PyObject *tmp_subscript_value_151;
                    PyObject *tmp_format_spec_86;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_84, 0, tmp_tuple_element_84);
                    tmp_expression_value_151 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_151 == NULL)) {
                        tmp_expression_value_151 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_151 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 429;

                        goto tuple_build_exception_84;
                    }
                    tmp_subscript_value_151 = mod_consts[86];
                    tmp_format_value_86 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_151, tmp_subscript_value_151);
                    if (tmp_format_value_86 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 429;

                        goto tuple_build_exception_84;
                    }
                    tmp_format_spec_86 = mod_consts[64];
                    tmp_tuple_element_84 = BUILTIN_FORMAT(tstate, tmp_format_value_86, tmp_format_spec_86);
                    Py_DECREF(tmp_format_value_86);
                    if (tmp_tuple_element_84 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 429;

                        goto tuple_build_exception_84;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_84, 1, tmp_tuple_element_84);
                    tmp_tuple_element_84 = mod_consts[84];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_84, 2, tmp_tuple_element_84);
                }
                goto tuple_build_noexception_84;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_84:;
                Py_DECREF(tmp_string_concat_values_84);
                goto list_build_exception_8;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_84:;
                tmp_list_element_8 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_84);
                Py_DECREF(tmp_string_concat_values_84);
                if (tmp_list_element_8 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 429;

                    goto list_build_exception_8;
                }
                PyList_SET_ITEM(tmp_dict_value_2, 1, tmp_list_element_8);
            }
            goto list_build_noexception_8;
            // Exception handling pass through code for list_build:
            list_build_exception_8:;
            Py_DECREF(tmp_dict_value_2);
            goto dict_build_exception_2;
            // Finished with no exception for list_build:
            list_build_noexception_8:;
            tmp_res = PyDict_SetItem(tmp_assign_source_48, tmp_dict_key_2, tmp_dict_value_2);
            Py_DECREF(tmp_dict_value_2);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_2;
        // Exception handling pass through code for dict_build:
        dict_build_exception_2:;
        Py_DECREF(tmp_assign_source_48);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_2:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[173], tmp_assign_source_48);
    }
    {
        PyObject *tmp_assign_source_49;
        PyObject *tmp_dict_key_3;
        PyObject *tmp_dict_value_3;
        PyObject *tmp_list_element_9;
        PyObject *tmp_string_concat_values_85;
        PyObject *tmp_tuple_element_85;
        tmp_dict_key_3 = mod_consts[167];
        tmp_tuple_element_85 = mod_consts[101];
        tmp_string_concat_values_85 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_87;
            PyObject *tmp_expression_value_152;
            PyObject *tmp_subscript_value_152;
            PyObject *tmp_format_spec_87;
            PyTuple_SET_ITEM0(tmp_string_concat_values_85, 0, tmp_tuple_element_85);
            tmp_expression_value_152 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_152 == NULL)) {
                tmp_expression_value_152 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_152 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 434;

                goto tuple_build_exception_85;
            }
            tmp_subscript_value_152 = mod_consts[102];
            tmp_format_value_87 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_152, tmp_subscript_value_152);
            if (tmp_format_value_87 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 434;

                goto tuple_build_exception_85;
            }
            tmp_format_spec_87 = mod_consts[64];
            tmp_tuple_element_85 = BUILTIN_FORMAT(tstate, tmp_format_value_87, tmp_format_spec_87);
            Py_DECREF(tmp_format_value_87);
            if (tmp_tuple_element_85 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 434;

                goto tuple_build_exception_85;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_85, 1, tmp_tuple_element_85);
            tmp_tuple_element_85 = mod_consts[65];
            PyTuple_SET_ITEM0(tmp_string_concat_values_85, 2, tmp_tuple_element_85);
        }
        goto tuple_build_noexception_85;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_85:;
        Py_DECREF(tmp_string_concat_values_85);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_85:;
        tmp_list_element_9 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_85);
        Py_DECREF(tmp_string_concat_values_85);
        if (tmp_list_element_9 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 434;

            goto frame_exception_exit_1;
        }
        tmp_dict_value_3 = MAKE_LIST_EMPTY(2);
        {
            PyObject *tmp_string_concat_values_86;
            PyObject *tmp_tuple_element_86;
            PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_9);
            tmp_tuple_element_86 = mod_consts[103];
            tmp_string_concat_values_86 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_88;
                PyObject *tmp_expression_value_153;
                PyObject *tmp_subscript_value_153;
                PyObject *tmp_format_spec_88;
                PyTuple_SET_ITEM0(tmp_string_concat_values_86, 0, tmp_tuple_element_86);
                tmp_expression_value_153 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_153 == NULL)) {
                    tmp_expression_value_153 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_153 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 435;

                    goto tuple_build_exception_86;
                }
                tmp_subscript_value_153 = mod_consts[104];
                tmp_format_value_88 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_153, tmp_subscript_value_153);
                if (tmp_format_value_88 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 435;

                    goto tuple_build_exception_86;
                }
                tmp_format_spec_88 = mod_consts[64];
                tmp_tuple_element_86 = BUILTIN_FORMAT(tstate, tmp_format_value_88, tmp_format_spec_88);
                Py_DECREF(tmp_format_value_88);
                if (tmp_tuple_element_86 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 435;

                    goto tuple_build_exception_86;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_86, 1, tmp_tuple_element_86);
                tmp_tuple_element_86 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_86, 2, tmp_tuple_element_86);
            }
            goto tuple_build_noexception_86;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_86:;
            Py_DECREF(tmp_string_concat_values_86);
            goto list_build_exception_9;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_86:;
            tmp_list_element_9 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_86);
            Py_DECREF(tmp_string_concat_values_86);
            if (tmp_list_element_9 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 435;

                goto list_build_exception_9;
            }
            PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_9);
        }
        goto list_build_noexception_9;
        // Exception handling pass through code for list_build:
        list_build_exception_9:;
        Py_DECREF(tmp_dict_value_3);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_9:;
        tmp_assign_source_49 = _PyDict_NewPresized( 7 );
        {
            PyObject *tmp_list_element_10;
            PyObject *tmp_string_concat_values_87;
            PyObject *tmp_tuple_element_87;
            PyObject *tmp_list_element_11;
            PyObject *tmp_string_concat_values_89;
            PyObject *tmp_tuple_element_89;
            PyObject *tmp_list_element_12;
            PyObject *tmp_string_concat_values_91;
            PyObject *tmp_tuple_element_91;
            PyObject *tmp_list_element_13;
            PyObject *tmp_string_concat_values_93;
            PyObject *tmp_tuple_element_93;
            PyObject *tmp_list_element_14;
            PyObject *tmp_string_concat_values_101;
            PyObject *tmp_tuple_element_101;
            PyObject *tmp_list_element_15;
            PyObject *tmp_string_concat_values_103;
            PyObject *tmp_tuple_element_103;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
            tmp_dict_key_3 = mod_consts[168];
            tmp_tuple_element_87 = mod_consts[105];
            tmp_string_concat_values_87 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_89;
                PyObject *tmp_expression_value_154;
                PyObject *tmp_subscript_value_154;
                PyObject *tmp_format_spec_89;
                PyTuple_SET_ITEM0(tmp_string_concat_values_87, 0, tmp_tuple_element_87);
                tmp_expression_value_154 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_154 == NULL)) {
                    tmp_expression_value_154 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_154 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 438;

                    goto tuple_build_exception_87;
                }
                tmp_subscript_value_154 = mod_consts[102];
                tmp_format_value_89 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_154, tmp_subscript_value_154);
                if (tmp_format_value_89 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 438;

                    goto tuple_build_exception_87;
                }
                tmp_format_spec_89 = mod_consts[64];
                tmp_tuple_element_87 = BUILTIN_FORMAT(tstate, tmp_format_value_89, tmp_format_spec_89);
                Py_DECREF(tmp_format_value_89);
                if (tmp_tuple_element_87 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 438;

                    goto tuple_build_exception_87;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_87, 1, tmp_tuple_element_87);
                tmp_tuple_element_87 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_87, 2, tmp_tuple_element_87);
            }
            goto tuple_build_noexception_87;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_87:;
            Py_DECREF(tmp_string_concat_values_87);
            goto dict_build_exception_3;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_87:;
            tmp_list_element_10 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_87);
            Py_DECREF(tmp_string_concat_values_87);
            if (tmp_list_element_10 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 438;

                goto dict_build_exception_3;
            }
            tmp_dict_value_3 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_88;
                PyObject *tmp_tuple_element_88;
                PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_10);
                tmp_tuple_element_88 = mod_consts[106];
                tmp_string_concat_values_88 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_90;
                    PyObject *tmp_expression_value_155;
                    PyObject *tmp_subscript_value_155;
                    PyObject *tmp_format_spec_90;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_88, 0, tmp_tuple_element_88);
                    tmp_expression_value_155 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_155 == NULL)) {
                        tmp_expression_value_155 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_155 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 439;

                        goto tuple_build_exception_88;
                    }
                    tmp_subscript_value_155 = mod_consts[104];
                    tmp_format_value_90 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_155, tmp_subscript_value_155);
                    if (tmp_format_value_90 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 439;

                        goto tuple_build_exception_88;
                    }
                    tmp_format_spec_90 = mod_consts[64];
                    tmp_tuple_element_88 = BUILTIN_FORMAT(tstate, tmp_format_value_90, tmp_format_spec_90);
                    Py_DECREF(tmp_format_value_90);
                    if (tmp_tuple_element_88 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 439;

                        goto tuple_build_exception_88;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_88, 1, tmp_tuple_element_88);
                    tmp_tuple_element_88 = mod_consts[69];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_88, 2, tmp_tuple_element_88);
                }
                goto tuple_build_noexception_88;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_88:;
                Py_DECREF(tmp_string_concat_values_88);
                goto list_build_exception_10;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_88:;
                tmp_list_element_10 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_88);
                Py_DECREF(tmp_string_concat_values_88);
                if (tmp_list_element_10 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 439;

                    goto list_build_exception_10;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_10);
            }
            goto list_build_noexception_10;
            // Exception handling pass through code for list_build:
            list_build_exception_10:;
            Py_DECREF(tmp_dict_value_3);
            goto dict_build_exception_3;
            // Finished with no exception for list_build:
            list_build_noexception_10:;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
            tmp_dict_key_3 = mod_consts[169];
            tmp_tuple_element_89 = mod_consts[107];
            tmp_string_concat_values_89 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_91;
                PyObject *tmp_expression_value_156;
                PyObject *tmp_subscript_value_156;
                PyObject *tmp_format_spec_91;
                PyTuple_SET_ITEM0(tmp_string_concat_values_89, 0, tmp_tuple_element_89);
                tmp_expression_value_156 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_156 == NULL)) {
                    tmp_expression_value_156 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_156 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 442;

                    goto tuple_build_exception_89;
                }
                tmp_subscript_value_156 = mod_consts[102];
                tmp_format_value_91 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_156, tmp_subscript_value_156);
                if (tmp_format_value_91 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 442;

                    goto tuple_build_exception_89;
                }
                tmp_format_spec_91 = mod_consts[64];
                tmp_tuple_element_89 = BUILTIN_FORMAT(tstate, tmp_format_value_91, tmp_format_spec_91);
                Py_DECREF(tmp_format_value_91);
                if (tmp_tuple_element_89 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 442;

                    goto tuple_build_exception_89;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_89, 1, tmp_tuple_element_89);
                tmp_tuple_element_89 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_89, 2, tmp_tuple_element_89);
            }
            goto tuple_build_noexception_89;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_89:;
            Py_DECREF(tmp_string_concat_values_89);
            goto dict_build_exception_3;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_89:;
            tmp_list_element_11 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_89);
            Py_DECREF(tmp_string_concat_values_89);
            if (tmp_list_element_11 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 442;

                goto dict_build_exception_3;
            }
            tmp_dict_value_3 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_90;
                PyObject *tmp_tuple_element_90;
                PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_11);
                tmp_tuple_element_90 = mod_consts[108];
                tmp_string_concat_values_90 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_92;
                    PyObject *tmp_expression_value_157;
                    PyObject *tmp_subscript_value_157;
                    PyObject *tmp_format_spec_92;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_90, 0, tmp_tuple_element_90);
                    tmp_expression_value_157 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_157 == NULL)) {
                        tmp_expression_value_157 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_157 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 443;

                        goto tuple_build_exception_90;
                    }
                    tmp_subscript_value_157 = mod_consts[104];
                    tmp_format_value_92 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_157, tmp_subscript_value_157);
                    if (tmp_format_value_92 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 443;

                        goto tuple_build_exception_90;
                    }
                    tmp_format_spec_92 = mod_consts[64];
                    tmp_tuple_element_90 = BUILTIN_FORMAT(tstate, tmp_format_value_92, tmp_format_spec_92);
                    Py_DECREF(tmp_format_value_92);
                    if (tmp_tuple_element_90 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 443;

                        goto tuple_build_exception_90;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_90, 1, tmp_tuple_element_90);
                    tmp_tuple_element_90 = mod_consts[72];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_90, 2, tmp_tuple_element_90);
                }
                goto tuple_build_noexception_90;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_90:;
                Py_DECREF(tmp_string_concat_values_90);
                goto list_build_exception_11;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_90:;
                tmp_list_element_11 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_90);
                Py_DECREF(tmp_string_concat_values_90);
                if (tmp_list_element_11 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 443;

                    goto list_build_exception_11;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_11);
            }
            goto list_build_noexception_11;
            // Exception handling pass through code for list_build:
            list_build_exception_11:;
            Py_DECREF(tmp_dict_value_3);
            goto dict_build_exception_3;
            // Finished with no exception for list_build:
            list_build_noexception_11:;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
            tmp_dict_key_3 = mod_consts[170];
            tmp_tuple_element_91 = mod_consts[109];
            tmp_string_concat_values_91 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_93;
                PyObject *tmp_expression_value_158;
                PyObject *tmp_subscript_value_158;
                PyObject *tmp_format_spec_93;
                PyTuple_SET_ITEM0(tmp_string_concat_values_91, 0, tmp_tuple_element_91);
                tmp_expression_value_158 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_158 == NULL)) {
                    tmp_expression_value_158 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_158 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 446;

                    goto tuple_build_exception_91;
                }
                tmp_subscript_value_158 = mod_consts[102];
                tmp_format_value_93 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_158, tmp_subscript_value_158);
                if (tmp_format_value_93 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 446;

                    goto tuple_build_exception_91;
                }
                tmp_format_spec_93 = mod_consts[64];
                tmp_tuple_element_91 = BUILTIN_FORMAT(tstate, tmp_format_value_93, tmp_format_spec_93);
                Py_DECREF(tmp_format_value_93);
                if (tmp_tuple_element_91 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 446;

                    goto tuple_build_exception_91;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_91, 1, tmp_tuple_element_91);
                tmp_tuple_element_91 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_91, 2, tmp_tuple_element_91);
            }
            goto tuple_build_noexception_91;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_91:;
            Py_DECREF(tmp_string_concat_values_91);
            goto dict_build_exception_3;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_91:;
            tmp_list_element_12 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_91);
            Py_DECREF(tmp_string_concat_values_91);
            if (tmp_list_element_12 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 446;

                goto dict_build_exception_3;
            }
            tmp_dict_value_3 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_92;
                PyObject *tmp_tuple_element_92;
                PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_12);
                tmp_tuple_element_92 = mod_consts[110];
                tmp_string_concat_values_92 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_94;
                    PyObject *tmp_expression_value_159;
                    PyObject *tmp_subscript_value_159;
                    PyObject *tmp_format_spec_94;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_92, 0, tmp_tuple_element_92);
                    tmp_expression_value_159 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_159 == NULL)) {
                        tmp_expression_value_159 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_159 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 447;

                        goto tuple_build_exception_92;
                    }
                    tmp_subscript_value_159 = mod_consts[104];
                    tmp_format_value_94 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_159, tmp_subscript_value_159);
                    if (tmp_format_value_94 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 447;

                        goto tuple_build_exception_92;
                    }
                    tmp_format_spec_94 = mod_consts[64];
                    tmp_tuple_element_92 = BUILTIN_FORMAT(tstate, tmp_format_value_94, tmp_format_spec_94);
                    Py_DECREF(tmp_format_value_94);
                    if (tmp_tuple_element_92 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 447;

                        goto tuple_build_exception_92;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_92, 1, tmp_tuple_element_92);
                    tmp_tuple_element_92 = mod_consts[75];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_92, 2, tmp_tuple_element_92);
                }
                goto tuple_build_noexception_92;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_92:;
                Py_DECREF(tmp_string_concat_values_92);
                goto list_build_exception_12;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_92:;
                tmp_list_element_12 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_92);
                Py_DECREF(tmp_string_concat_values_92);
                if (tmp_list_element_12 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 447;

                    goto list_build_exception_12;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_12);
            }
            goto list_build_noexception_12;
            // Exception handling pass through code for list_build:
            list_build_exception_12:;
            Py_DECREF(tmp_dict_value_3);
            goto dict_build_exception_3;
            // Finished with no exception for list_build:
            list_build_noexception_12:;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
            tmp_dict_key_3 = mod_consts[64];
            tmp_tuple_element_93 = mod_consts[119];
            tmp_string_concat_values_93 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_95;
                PyObject *tmp_expression_value_160;
                PyObject *tmp_subscript_value_160;
                PyObject *tmp_format_spec_95;
                PyTuple_SET_ITEM0(tmp_string_concat_values_93, 0, tmp_tuple_element_93);
                tmp_expression_value_160 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_160 == NULL)) {
                    tmp_expression_value_160 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_160 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 450;

                    goto tuple_build_exception_93;
                }
                tmp_subscript_value_160 = mod_consts[120];
                tmp_format_value_95 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_160, tmp_subscript_value_160);
                if (tmp_format_value_95 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 450;

                    goto tuple_build_exception_93;
                }
                tmp_format_spec_95 = mod_consts[64];
                tmp_tuple_element_93 = BUILTIN_FORMAT(tstate, tmp_format_value_95, tmp_format_spec_95);
                Py_DECREF(tmp_format_value_95);
                if (tmp_tuple_element_93 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 450;

                    goto tuple_build_exception_93;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_93, 1, tmp_tuple_element_93);
                tmp_tuple_element_93 = mod_consts[89];
                PyTuple_SET_ITEM0(tmp_string_concat_values_93, 2, tmp_tuple_element_93);
            }
            goto tuple_build_noexception_93;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_93:;
            Py_DECREF(tmp_string_concat_values_93);
            goto dict_build_exception_3;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_93:;
            tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_93);
            Py_DECREF(tmp_string_concat_values_93);
            if (tmp_list_element_13 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 450;

                goto dict_build_exception_3;
            }
            tmp_dict_value_3 = MAKE_LIST_EMPTY(8);
            {
                PyObject *tmp_string_concat_values_94;
                PyObject *tmp_tuple_element_94;
                PyObject *tmp_string_concat_values_95;
                PyObject *tmp_tuple_element_95;
                PyObject *tmp_string_concat_values_96;
                PyObject *tmp_tuple_element_96;
                PyObject *tmp_string_concat_values_97;
                PyObject *tmp_tuple_element_97;
                PyObject *tmp_string_concat_values_98;
                PyObject *tmp_tuple_element_98;
                PyObject *tmp_string_concat_values_99;
                PyObject *tmp_tuple_element_99;
                PyObject *tmp_string_concat_values_100;
                PyObject *tmp_tuple_element_100;
                PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_13);
                tmp_tuple_element_94 = mod_consts[121];
                tmp_string_concat_values_94 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_96;
                    PyObject *tmp_expression_value_161;
                    PyObject *tmp_subscript_value_161;
                    PyObject *tmp_format_spec_96;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_94, 0, tmp_tuple_element_94);
                    tmp_expression_value_161 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_161 == NULL)) {
                        tmp_expression_value_161 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_161 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 451;

                        goto tuple_build_exception_94;
                    }
                    tmp_subscript_value_161 = mod_consts[120];
                    tmp_format_value_96 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_161, tmp_subscript_value_161);
                    if (tmp_format_value_96 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 451;

                        goto tuple_build_exception_94;
                    }
                    tmp_format_spec_96 = mod_consts[64];
                    tmp_tuple_element_94 = BUILTIN_FORMAT(tstate, tmp_format_value_96, tmp_format_spec_96);
                    Py_DECREF(tmp_format_value_96);
                    if (tmp_tuple_element_94 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 451;

                        goto tuple_build_exception_94;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_94, 1, tmp_tuple_element_94);
                    tmp_tuple_element_94 = mod_consts[91];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_94, 2, tmp_tuple_element_94);
                }
                goto tuple_build_noexception_94;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_94:;
                Py_DECREF(tmp_string_concat_values_94);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_94:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_94);
                Py_DECREF(tmp_string_concat_values_94);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 451;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_13);
                tmp_tuple_element_95 = mod_consts[122];
                tmp_string_concat_values_95 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_97;
                    PyObject *tmp_expression_value_162;
                    PyObject *tmp_subscript_value_162;
                    PyObject *tmp_format_spec_97;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_95, 0, tmp_tuple_element_95);
                    tmp_expression_value_162 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_162 == NULL)) {
                        tmp_expression_value_162 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_162 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 452;

                        goto tuple_build_exception_95;
                    }
                    tmp_subscript_value_162 = mod_consts[120];
                    tmp_format_value_97 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_162, tmp_subscript_value_162);
                    if (tmp_format_value_97 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 452;

                        goto tuple_build_exception_95;
                    }
                    tmp_format_spec_97 = mod_consts[64];
                    tmp_tuple_element_95 = BUILTIN_FORMAT(tstate, tmp_format_value_97, tmp_format_spec_97);
                    Py_DECREF(tmp_format_value_97);
                    if (tmp_tuple_element_95 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 452;

                        goto tuple_build_exception_95;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_95, 1, tmp_tuple_element_95);
                    tmp_tuple_element_95 = mod_consts[93];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_95, 2, tmp_tuple_element_95);
                }
                goto tuple_build_noexception_95;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_95:;
                Py_DECREF(tmp_string_concat_values_95);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_95:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_95);
                Py_DECREF(tmp_string_concat_values_95);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 452;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 2, tmp_list_element_13);
                tmp_tuple_element_96 = mod_consts[123];
                tmp_string_concat_values_96 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_98;
                    PyObject *tmp_expression_value_163;
                    PyObject *tmp_subscript_value_163;
                    PyObject *tmp_format_spec_98;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_96, 0, tmp_tuple_element_96);
                    tmp_expression_value_163 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_163 == NULL)) {
                        tmp_expression_value_163 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_163 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 453;

                        goto tuple_build_exception_96;
                    }
                    tmp_subscript_value_163 = mod_consts[120];
                    tmp_format_value_98 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_163, tmp_subscript_value_163);
                    if (tmp_format_value_98 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 453;

                        goto tuple_build_exception_96;
                    }
                    tmp_format_spec_98 = mod_consts[64];
                    tmp_tuple_element_96 = BUILTIN_FORMAT(tstate, tmp_format_value_98, tmp_format_spec_98);
                    Py_DECREF(tmp_format_value_98);
                    if (tmp_tuple_element_96 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 453;

                        goto tuple_build_exception_96;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_96, 1, tmp_tuple_element_96);
                    tmp_tuple_element_96 = mod_consts[95];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_96, 2, tmp_tuple_element_96);
                }
                goto tuple_build_noexception_96;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_96:;
                Py_DECREF(tmp_string_concat_values_96);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_96:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_96);
                Py_DECREF(tmp_string_concat_values_96);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 453;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 3, tmp_list_element_13);
                tmp_tuple_element_97 = mod_consts[124];
                tmp_string_concat_values_97 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_99;
                    PyObject *tmp_expression_value_164;
                    PyObject *tmp_subscript_value_164;
                    PyObject *tmp_format_spec_99;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_97, 0, tmp_tuple_element_97);
                    tmp_expression_value_164 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_164 == NULL)) {
                        tmp_expression_value_164 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_164 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 454;

                        goto tuple_build_exception_97;
                    }
                    tmp_subscript_value_164 = mod_consts[125];
                    tmp_format_value_99 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_164, tmp_subscript_value_164);
                    if (tmp_format_value_99 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 454;

                        goto tuple_build_exception_97;
                    }
                    tmp_format_spec_99 = mod_consts[64];
                    tmp_tuple_element_97 = BUILTIN_FORMAT(tstate, tmp_format_value_99, tmp_format_spec_99);
                    Py_DECREF(tmp_format_value_99);
                    if (tmp_tuple_element_97 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 454;

                        goto tuple_build_exception_97;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_97, 1, tmp_tuple_element_97);
                    tmp_tuple_element_97 = mod_consts[89];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_97, 2, tmp_tuple_element_97);
                }
                goto tuple_build_noexception_97;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_97:;
                Py_DECREF(tmp_string_concat_values_97);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_97:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_97);
                Py_DECREF(tmp_string_concat_values_97);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 454;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 4, tmp_list_element_13);
                tmp_tuple_element_98 = mod_consts[126];
                tmp_string_concat_values_98 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_100;
                    PyObject *tmp_expression_value_165;
                    PyObject *tmp_subscript_value_165;
                    PyObject *tmp_format_spec_100;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_98, 0, tmp_tuple_element_98);
                    tmp_expression_value_165 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_165 == NULL)) {
                        tmp_expression_value_165 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_165 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 455;

                        goto tuple_build_exception_98;
                    }
                    tmp_subscript_value_165 = mod_consts[125];
                    tmp_format_value_100 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_165, tmp_subscript_value_165);
                    if (tmp_format_value_100 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 455;

                        goto tuple_build_exception_98;
                    }
                    tmp_format_spec_100 = mod_consts[64];
                    tmp_tuple_element_98 = BUILTIN_FORMAT(tstate, tmp_format_value_100, tmp_format_spec_100);
                    Py_DECREF(tmp_format_value_100);
                    if (tmp_tuple_element_98 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 455;

                        goto tuple_build_exception_98;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_98, 1, tmp_tuple_element_98);
                    tmp_tuple_element_98 = mod_consts[91];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_98, 2, tmp_tuple_element_98);
                }
                goto tuple_build_noexception_98;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_98:;
                Py_DECREF(tmp_string_concat_values_98);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_98:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_98);
                Py_DECREF(tmp_string_concat_values_98);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 455;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 5, tmp_list_element_13);
                tmp_tuple_element_99 = mod_consts[127];
                tmp_string_concat_values_99 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_101;
                    PyObject *tmp_expression_value_166;
                    PyObject *tmp_subscript_value_166;
                    PyObject *tmp_format_spec_101;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_99, 0, tmp_tuple_element_99);
                    tmp_expression_value_166 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_166 == NULL)) {
                        tmp_expression_value_166 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_166 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 456;

                        goto tuple_build_exception_99;
                    }
                    tmp_subscript_value_166 = mod_consts[125];
                    tmp_format_value_101 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_166, tmp_subscript_value_166);
                    if (tmp_format_value_101 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 456;

                        goto tuple_build_exception_99;
                    }
                    tmp_format_spec_101 = mod_consts[64];
                    tmp_tuple_element_99 = BUILTIN_FORMAT(tstate, tmp_format_value_101, tmp_format_spec_101);
                    Py_DECREF(tmp_format_value_101);
                    if (tmp_tuple_element_99 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 456;

                        goto tuple_build_exception_99;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_99, 1, tmp_tuple_element_99);
                    tmp_tuple_element_99 = mod_consts[93];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_99, 2, tmp_tuple_element_99);
                }
                goto tuple_build_noexception_99;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_99:;
                Py_DECREF(tmp_string_concat_values_99);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_99:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_99);
                Py_DECREF(tmp_string_concat_values_99);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 456;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 6, tmp_list_element_13);
                tmp_tuple_element_100 = mod_consts[128];
                tmp_string_concat_values_100 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_102;
                    PyObject *tmp_expression_value_167;
                    PyObject *tmp_subscript_value_167;
                    PyObject *tmp_format_spec_102;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_100, 0, tmp_tuple_element_100);
                    tmp_expression_value_167 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_167 == NULL)) {
                        tmp_expression_value_167 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_167 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 457;

                        goto tuple_build_exception_100;
                    }
                    tmp_subscript_value_167 = mod_consts[125];
                    tmp_format_value_102 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_167, tmp_subscript_value_167);
                    if (tmp_format_value_102 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 457;

                        goto tuple_build_exception_100;
                    }
                    tmp_format_spec_102 = mod_consts[64];
                    tmp_tuple_element_100 = BUILTIN_FORMAT(tstate, tmp_format_value_102, tmp_format_spec_102);
                    Py_DECREF(tmp_format_value_102);
                    if (tmp_tuple_element_100 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 457;

                        goto tuple_build_exception_100;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_100, 1, tmp_tuple_element_100);
                    tmp_tuple_element_100 = mod_consts[95];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_100, 2, tmp_tuple_element_100);
                }
                goto tuple_build_noexception_100;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_100:;
                Py_DECREF(tmp_string_concat_values_100);
                goto list_build_exception_13;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_100:;
                tmp_list_element_13 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_100);
                Py_DECREF(tmp_string_concat_values_100);
                if (tmp_list_element_13 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 457;

                    goto list_build_exception_13;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 7, tmp_list_element_13);
            }
            goto list_build_noexception_13;
            // Exception handling pass through code for list_build:
            list_build_exception_13:;
            Py_DECREF(tmp_dict_value_3);
            goto dict_build_exception_3;
            // Finished with no exception for list_build:
            list_build_noexception_13:;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
            tmp_dict_key_3 = mod_consts[171];
            tmp_tuple_element_101 = mod_consts[111];
            tmp_string_concat_values_101 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_103;
                PyObject *tmp_expression_value_168;
                PyObject *tmp_subscript_value_168;
                PyObject *tmp_format_spec_103;
                PyTuple_SET_ITEM0(tmp_string_concat_values_101, 0, tmp_tuple_element_101);
                tmp_expression_value_168 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_168 == NULL)) {
                    tmp_expression_value_168 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_168 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 460;

                    goto tuple_build_exception_101;
                }
                tmp_subscript_value_168 = mod_consts[112];
                tmp_format_value_103 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_168, tmp_subscript_value_168);
                if (tmp_format_value_103 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 460;

                    goto tuple_build_exception_101;
                }
                tmp_format_spec_103 = mod_consts[64];
                tmp_tuple_element_101 = BUILTIN_FORMAT(tstate, tmp_format_value_103, tmp_format_spec_103);
                Py_DECREF(tmp_format_value_103);
                if (tmp_tuple_element_101 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 460;

                    goto tuple_build_exception_101;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_101, 1, tmp_tuple_element_101);
                tmp_tuple_element_101 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_101, 2, tmp_tuple_element_101);
            }
            goto tuple_build_noexception_101;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_101:;
            Py_DECREF(tmp_string_concat_values_101);
            goto dict_build_exception_3;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_101:;
            tmp_list_element_14 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_101);
            Py_DECREF(tmp_string_concat_values_101);
            if (tmp_list_element_14 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 460;

                goto dict_build_exception_3;
            }
            tmp_dict_value_3 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_102;
                PyObject *tmp_tuple_element_102;
                PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_14);
                tmp_tuple_element_102 = mod_consts[113];
                tmp_string_concat_values_102 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_104;
                    PyObject *tmp_expression_value_169;
                    PyObject *tmp_subscript_value_169;
                    PyObject *tmp_format_spec_104;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_102, 0, tmp_tuple_element_102);
                    tmp_expression_value_169 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_169 == NULL)) {
                        tmp_expression_value_169 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_169 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 461;

                        goto tuple_build_exception_102;
                    }
                    tmp_subscript_value_169 = mod_consts[114];
                    tmp_format_value_104 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_169, tmp_subscript_value_169);
                    if (tmp_format_value_104 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 461;

                        goto tuple_build_exception_102;
                    }
                    tmp_format_spec_104 = mod_consts[64];
                    tmp_tuple_element_102 = BUILTIN_FORMAT(tstate, tmp_format_value_104, tmp_format_spec_104);
                    Py_DECREF(tmp_format_value_104);
                    if (tmp_tuple_element_102 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 461;

                        goto tuple_build_exception_102;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_102, 1, tmp_tuple_element_102);
                    tmp_tuple_element_102 = mod_consts[79];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_102, 2, tmp_tuple_element_102);
                }
                goto tuple_build_noexception_102;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_102:;
                Py_DECREF(tmp_string_concat_values_102);
                goto list_build_exception_14;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_102:;
                tmp_list_element_14 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_102);
                Py_DECREF(tmp_string_concat_values_102);
                if (tmp_list_element_14 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 461;

                    goto list_build_exception_14;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_14);
            }
            goto list_build_noexception_14;
            // Exception handling pass through code for list_build:
            list_build_exception_14:;
            Py_DECREF(tmp_dict_value_3);
            goto dict_build_exception_3;
            // Finished with no exception for list_build:
            list_build_noexception_14:;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
            tmp_dict_key_3 = mod_consts[172];
            tmp_tuple_element_103 = mod_consts[115];
            tmp_string_concat_values_103 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_105;
                PyObject *tmp_expression_value_170;
                PyObject *tmp_subscript_value_170;
                PyObject *tmp_format_spec_105;
                PyTuple_SET_ITEM0(tmp_string_concat_values_103, 0, tmp_tuple_element_103);
                tmp_expression_value_170 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_170 == NULL)) {
                    tmp_expression_value_170 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_170 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 464;

                    goto tuple_build_exception_103;
                }
                tmp_subscript_value_170 = mod_consts[116];
                tmp_format_value_105 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_170, tmp_subscript_value_170);
                if (tmp_format_value_105 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 464;

                    goto tuple_build_exception_103;
                }
                tmp_format_spec_105 = mod_consts[64];
                tmp_tuple_element_103 = BUILTIN_FORMAT(tstate, tmp_format_value_105, tmp_format_spec_105);
                Py_DECREF(tmp_format_value_105);
                if (tmp_tuple_element_103 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 464;

                    goto tuple_build_exception_103;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_103, 1, tmp_tuple_element_103);
                tmp_tuple_element_103 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_103, 2, tmp_tuple_element_103);
            }
            goto tuple_build_noexception_103;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_103:;
            Py_DECREF(tmp_string_concat_values_103);
            goto dict_build_exception_3;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_103:;
            tmp_list_element_15 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_103);
            Py_DECREF(tmp_string_concat_values_103);
            if (tmp_list_element_15 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 464;

                goto dict_build_exception_3;
            }
            tmp_dict_value_3 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_104;
                PyObject *tmp_tuple_element_104;
                PyList_SET_ITEM(tmp_dict_value_3, 0, tmp_list_element_15);
                tmp_tuple_element_104 = mod_consts[117];
                tmp_string_concat_values_104 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_106;
                    PyObject *tmp_expression_value_171;
                    PyObject *tmp_subscript_value_171;
                    PyObject *tmp_format_spec_106;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_104, 0, tmp_tuple_element_104);
                    tmp_expression_value_171 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_171 == NULL)) {
                        tmp_expression_value_171 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_171 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 465;

                        goto tuple_build_exception_104;
                    }
                    tmp_subscript_value_171 = mod_consts[118];
                    tmp_format_value_106 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_171, tmp_subscript_value_171);
                    if (tmp_format_value_106 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 465;

                        goto tuple_build_exception_104;
                    }
                    tmp_format_spec_106 = mod_consts[64];
                    tmp_tuple_element_104 = BUILTIN_FORMAT(tstate, tmp_format_value_106, tmp_format_spec_106);
                    Py_DECREF(tmp_format_value_106);
                    if (tmp_tuple_element_104 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 465;

                        goto tuple_build_exception_104;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_104, 1, tmp_tuple_element_104);
                    tmp_tuple_element_104 = mod_consts[84];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_104, 2, tmp_tuple_element_104);
                }
                goto tuple_build_noexception_104;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_104:;
                Py_DECREF(tmp_string_concat_values_104);
                goto list_build_exception_15;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_104:;
                tmp_list_element_15 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_104);
                Py_DECREF(tmp_string_concat_values_104);
                if (tmp_list_element_15 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 465;

                    goto list_build_exception_15;
                }
                PyList_SET_ITEM(tmp_dict_value_3, 1, tmp_list_element_15);
            }
            goto list_build_noexception_15;
            // Exception handling pass through code for list_build:
            list_build_exception_15:;
            Py_DECREF(tmp_dict_value_3);
            goto dict_build_exception_3;
            // Finished with no exception for list_build:
            list_build_noexception_15:;
            tmp_res = PyDict_SetItem(tmp_assign_source_49, tmp_dict_key_3, tmp_dict_value_3);
            Py_DECREF(tmp_dict_value_3);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_3;
        // Exception handling pass through code for dict_build:
        dict_build_exception_3:;
        Py_DECREF(tmp_assign_source_49);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_3:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[174], tmp_assign_source_49);
    }
    {
        PyObject *tmp_assign_source_50;
        PyObject *tmp_dict_key_4;
        PyObject *tmp_dict_value_4;
        PyObject *tmp_list_element_16;
        PyObject *tmp_string_concat_values_105;
        PyObject *tmp_tuple_element_105;
        tmp_dict_key_4 = mod_consts[171];
        tmp_tuple_element_105 = mod_consts[129];
        tmp_string_concat_values_105 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_107;
            PyObject *tmp_expression_value_172;
            PyObject *tmp_subscript_value_172;
            PyObject *tmp_format_spec_107;
            PyTuple_SET_ITEM0(tmp_string_concat_values_105, 0, tmp_tuple_element_105);
            tmp_expression_value_172 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_172 == NULL)) {
                tmp_expression_value_172 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_172 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 470;

                goto tuple_build_exception_105;
            }
            tmp_subscript_value_172 = mod_consts[130];
            tmp_format_value_107 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_172, tmp_subscript_value_172);
            if (tmp_format_value_107 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 470;

                goto tuple_build_exception_105;
            }
            tmp_format_spec_107 = mod_consts[64];
            tmp_tuple_element_105 = BUILTIN_FORMAT(tstate, tmp_format_value_107, tmp_format_spec_107);
            Py_DECREF(tmp_format_value_107);
            if (tmp_tuple_element_105 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 470;

                goto tuple_build_exception_105;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_105, 1, tmp_tuple_element_105);
            tmp_tuple_element_105 = mod_consts[79];
            PyTuple_SET_ITEM0(tmp_string_concat_values_105, 2, tmp_tuple_element_105);
        }
        goto tuple_build_noexception_105;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_105:;
        Py_DECREF(tmp_string_concat_values_105);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_105:;
        tmp_list_element_16 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_105);
        Py_DECREF(tmp_string_concat_values_105);
        if (tmp_list_element_16 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 470;

            goto frame_exception_exit_1;
        }
        tmp_dict_value_4 = MAKE_LIST_EMPTY(2);
        {
            PyObject *tmp_string_concat_values_106;
            PyObject *tmp_tuple_element_106;
            PyList_SET_ITEM(tmp_dict_value_4, 0, tmp_list_element_16);
            tmp_tuple_element_106 = mod_consts[131];
            tmp_string_concat_values_106 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_108;
                PyObject *tmp_expression_value_173;
                PyObject *tmp_subscript_value_173;
                PyObject *tmp_format_spec_108;
                PyTuple_SET_ITEM0(tmp_string_concat_values_106, 0, tmp_tuple_element_106);
                tmp_expression_value_173 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_173 == NULL)) {
                    tmp_expression_value_173 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_173 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 471;

                    goto tuple_build_exception_106;
                }
                tmp_subscript_value_173 = mod_consts[132];
                tmp_format_value_108 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_173, tmp_subscript_value_173);
                if (tmp_format_value_108 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 471;

                    goto tuple_build_exception_106;
                }
                tmp_format_spec_108 = mod_consts[64];
                tmp_tuple_element_106 = BUILTIN_FORMAT(tstate, tmp_format_value_108, tmp_format_spec_108);
                Py_DECREF(tmp_format_value_108);
                if (tmp_tuple_element_106 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 471;

                    goto tuple_build_exception_106;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_106, 1, tmp_tuple_element_106);
                tmp_tuple_element_106 = mod_consts[79];
                PyTuple_SET_ITEM0(tmp_string_concat_values_106, 2, tmp_tuple_element_106);
            }
            goto tuple_build_noexception_106;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_106:;
            Py_DECREF(tmp_string_concat_values_106);
            goto list_build_exception_16;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_106:;
            tmp_list_element_16 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_106);
            Py_DECREF(tmp_string_concat_values_106);
            if (tmp_list_element_16 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 471;

                goto list_build_exception_16;
            }
            PyList_SET_ITEM(tmp_dict_value_4, 1, tmp_list_element_16);
        }
        goto list_build_noexception_16;
        // Exception handling pass through code for list_build:
        list_build_exception_16:;
        Py_DECREF(tmp_dict_value_4);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_16:;
        tmp_assign_source_50 = _PyDict_NewPresized( 2 );
        {
            PyObject *tmp_list_element_17;
            PyObject *tmp_string_concat_values_107;
            PyObject *tmp_tuple_element_107;
            tmp_res = PyDict_SetItem(tmp_assign_source_50, tmp_dict_key_4, tmp_dict_value_4);
            Py_DECREF(tmp_dict_value_4);
            assert(!(tmp_res != 0));
            tmp_dict_key_4 = mod_consts[172];
            tmp_tuple_element_107 = mod_consts[133];
            tmp_string_concat_values_107 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_109;
                PyObject *tmp_expression_value_174;
                PyObject *tmp_subscript_value_174;
                PyObject *tmp_format_spec_109;
                PyTuple_SET_ITEM0(tmp_string_concat_values_107, 0, tmp_tuple_element_107);
                tmp_expression_value_174 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_174 == NULL)) {
                    tmp_expression_value_174 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_174 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 474;

                    goto tuple_build_exception_107;
                }
                tmp_subscript_value_174 = mod_consts[134];
                tmp_format_value_109 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_174, tmp_subscript_value_174);
                if (tmp_format_value_109 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 474;

                    goto tuple_build_exception_107;
                }
                tmp_format_spec_109 = mod_consts[64];
                tmp_tuple_element_107 = BUILTIN_FORMAT(tstate, tmp_format_value_109, tmp_format_spec_109);
                Py_DECREF(tmp_format_value_109);
                if (tmp_tuple_element_107 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 474;

                    goto tuple_build_exception_107;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_107, 1, tmp_tuple_element_107);
                tmp_tuple_element_107 = mod_consts[84];
                PyTuple_SET_ITEM0(tmp_string_concat_values_107, 2, tmp_tuple_element_107);
            }
            goto tuple_build_noexception_107;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_107:;
            Py_DECREF(tmp_string_concat_values_107);
            goto dict_build_exception_4;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_107:;
            tmp_list_element_17 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_107);
            Py_DECREF(tmp_string_concat_values_107);
            if (tmp_list_element_17 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 474;

                goto dict_build_exception_4;
            }
            tmp_dict_value_4 = MAKE_LIST_EMPTY(2);
            {
                PyObject *tmp_string_concat_values_108;
                PyObject *tmp_tuple_element_108;
                PyList_SET_ITEM(tmp_dict_value_4, 0, tmp_list_element_17);
                tmp_tuple_element_108 = mod_consts[135];
                tmp_string_concat_values_108 = MAKE_TUPLE_EMPTY(3);
                {
                    PyObject *tmp_format_value_110;
                    PyObject *tmp_expression_value_175;
                    PyObject *tmp_subscript_value_175;
                    PyObject *tmp_format_spec_110;
                    PyTuple_SET_ITEM0(tmp_string_concat_values_108, 0, tmp_tuple_element_108);
                    tmp_expression_value_175 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                    if (unlikely(tmp_expression_value_175 == NULL)) {
                        tmp_expression_value_175 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                    }

                    if (tmp_expression_value_175 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 475;

                        goto tuple_build_exception_108;
                    }
                    tmp_subscript_value_175 = mod_consts[136];
                    tmp_format_value_110 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_175, tmp_subscript_value_175);
                    if (tmp_format_value_110 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 475;

                        goto tuple_build_exception_108;
                    }
                    tmp_format_spec_110 = mod_consts[64];
                    tmp_tuple_element_108 = BUILTIN_FORMAT(tstate, tmp_format_value_110, tmp_format_spec_110);
                    Py_DECREF(tmp_format_value_110);
                    if (tmp_tuple_element_108 == NULL) {
                        assert(HAS_ERROR_OCCURRED(tstate));

                        FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                        exception_lineno = 475;

                        goto tuple_build_exception_108;
                    }
                    PyTuple_SET_ITEM(tmp_string_concat_values_108, 1, tmp_tuple_element_108);
                    tmp_tuple_element_108 = mod_consts[84];
                    PyTuple_SET_ITEM0(tmp_string_concat_values_108, 2, tmp_tuple_element_108);
                }
                goto tuple_build_noexception_108;
                // Exception handling pass through code for tuple_build:
                tuple_build_exception_108:;
                Py_DECREF(tmp_string_concat_values_108);
                goto list_build_exception_17;
                // Finished with no exception for tuple_build:
                tuple_build_noexception_108:;
                tmp_list_element_17 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_108);
                Py_DECREF(tmp_string_concat_values_108);
                if (tmp_list_element_17 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 475;

                    goto list_build_exception_17;
                }
                PyList_SET_ITEM(tmp_dict_value_4, 1, tmp_list_element_17);
            }
            goto list_build_noexception_17;
            // Exception handling pass through code for list_build:
            list_build_exception_17:;
            Py_DECREF(tmp_dict_value_4);
            goto dict_build_exception_4;
            // Finished with no exception for list_build:
            list_build_noexception_17:;
            tmp_res = PyDict_SetItem(tmp_assign_source_50, tmp_dict_key_4, tmp_dict_value_4);
            Py_DECREF(tmp_dict_value_4);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_4;
        // Exception handling pass through code for dict_build:
        dict_build_exception_4:;
        Py_DECREF(tmp_assign_source_50);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_4:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[175], tmp_assign_source_50);
    }
    {
        PyObject *tmp_assign_source_51;
        PyObject *tmp_dict_key_5;
        PyObject *tmp_dict_value_5;
        PyObject *tmp_list_element_18;
        PyObject *tmp_string_concat_values_109;
        PyObject *tmp_tuple_element_109;
        tmp_dict_key_5 = mod_consts[64];
        tmp_tuple_element_109 = mod_consts[137];
        tmp_string_concat_values_109 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_111;
            PyObject *tmp_expression_value_176;
            PyObject *tmp_subscript_value_176;
            PyObject *tmp_format_spec_111;
            PyTuple_SET_ITEM0(tmp_string_concat_values_109, 0, tmp_tuple_element_109);
            tmp_expression_value_176 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_176 == NULL)) {
                tmp_expression_value_176 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_176 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 480;

                goto tuple_build_exception_109;
            }
            tmp_subscript_value_176 = mod_consts[142];
            tmp_format_value_111 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_176, tmp_subscript_value_176);
            if (tmp_format_value_111 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 480;

                goto tuple_build_exception_109;
            }
            tmp_format_spec_111 = mod_consts[64];
            tmp_tuple_element_109 = BUILTIN_FORMAT(tstate, tmp_format_value_111, tmp_format_spec_111);
            Py_DECREF(tmp_format_value_111);
            if (tmp_tuple_element_109 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 480;

                goto tuple_build_exception_109;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_109, 1, tmp_tuple_element_109);
            tmp_tuple_element_109 = mod_consts[143];
            PyTuple_SET_ITEM0(tmp_string_concat_values_109, 2, tmp_tuple_element_109);
        }
        goto tuple_build_noexception_109;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_109:;
        Py_DECREF(tmp_string_concat_values_109);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_109:;
        tmp_list_element_18 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_109);
        Py_DECREF(tmp_string_concat_values_109);
        if (tmp_list_element_18 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 480;

            goto frame_exception_exit_1;
        }
        tmp_dict_value_5 = MAKE_LIST_EMPTY(3);
        {
            PyObject *tmp_string_concat_values_110;
            PyObject *tmp_tuple_element_110;
            PyObject *tmp_string_concat_values_111;
            PyObject *tmp_tuple_element_111;
            PyList_SET_ITEM(tmp_dict_value_5, 0, tmp_list_element_18);
            tmp_tuple_element_110 = mod_consts[137];
            tmp_string_concat_values_110 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_112;
                PyObject *tmp_expression_value_177;
                PyObject *tmp_subscript_value_177;
                PyObject *tmp_format_spec_112;
                PyTuple_SET_ITEM0(tmp_string_concat_values_110, 0, tmp_tuple_element_110);
                tmp_expression_value_177 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_177 == NULL)) {
                    tmp_expression_value_177 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_177 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 481;

                    goto tuple_build_exception_110;
                }
                tmp_subscript_value_177 = mod_consts[142];
                tmp_format_value_112 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_177, tmp_subscript_value_177);
                if (tmp_format_value_112 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 481;

                    goto tuple_build_exception_110;
                }
                tmp_format_spec_112 = mod_consts[64];
                tmp_tuple_element_110 = BUILTIN_FORMAT(tstate, tmp_format_value_112, tmp_format_spec_112);
                Py_DECREF(tmp_format_value_112);
                if (tmp_tuple_element_110 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 481;

                    goto tuple_build_exception_110;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_110, 1, tmp_tuple_element_110);
                tmp_tuple_element_110 = mod_consts[144];
                PyTuple_SET_ITEM0(tmp_string_concat_values_110, 2, tmp_tuple_element_110);
            }
            goto tuple_build_noexception_110;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_110:;
            Py_DECREF(tmp_string_concat_values_110);
            goto list_build_exception_18;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_110:;
            tmp_list_element_18 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_110);
            Py_DECREF(tmp_string_concat_values_110);
            if (tmp_list_element_18 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 481;

                goto list_build_exception_18;
            }
            PyList_SET_ITEM(tmp_dict_value_5, 1, tmp_list_element_18);
            tmp_tuple_element_111 = mod_consts[137];
            tmp_string_concat_values_111 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_113;
                PyObject *tmp_expression_value_178;
                PyObject *tmp_subscript_value_178;
                PyObject *tmp_format_spec_113;
                PyTuple_SET_ITEM0(tmp_string_concat_values_111, 0, tmp_tuple_element_111);
                tmp_expression_value_178 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_178 == NULL)) {
                    tmp_expression_value_178 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_178 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 482;

                    goto tuple_build_exception_111;
                }
                tmp_subscript_value_178 = mod_consts[142];
                tmp_format_value_113 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_178, tmp_subscript_value_178);
                if (tmp_format_value_113 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 482;

                    goto tuple_build_exception_111;
                }
                tmp_format_spec_113 = mod_consts[64];
                tmp_tuple_element_111 = BUILTIN_FORMAT(tstate, tmp_format_value_113, tmp_format_spec_113);
                Py_DECREF(tmp_format_value_113);
                if (tmp_tuple_element_111 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 482;

                    goto tuple_build_exception_111;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_111, 1, tmp_tuple_element_111);
                tmp_tuple_element_111 = mod_consts[145];
                PyTuple_SET_ITEM0(tmp_string_concat_values_111, 2, tmp_tuple_element_111);
            }
            goto tuple_build_noexception_111;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_111:;
            Py_DECREF(tmp_string_concat_values_111);
            goto list_build_exception_18;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_111:;
            tmp_list_element_18 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_111);
            Py_DECREF(tmp_string_concat_values_111);
            if (tmp_list_element_18 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 482;

                goto list_build_exception_18;
            }
            PyList_SET_ITEM(tmp_dict_value_5, 2, tmp_list_element_18);
        }
        goto list_build_noexception_18;
        // Exception handling pass through code for list_build:
        list_build_exception_18:;
        Py_DECREF(tmp_dict_value_5);
        goto frame_exception_exit_1;
        // Finished with no exception for list_build:
        list_build_noexception_18:;
        tmp_assign_source_51 = _PyDict_NewPresized( 3 );
        {
            PyObject *tmp_list_element_19;
            PyObject *tmp_string_concat_values_112;
            PyObject *tmp_tuple_element_112;
            PyObject *tmp_list_element_20;
            PyObject *tmp_string_concat_values_113;
            PyObject *tmp_tuple_element_113;
            tmp_res = PyDict_SetItem(tmp_assign_source_51, tmp_dict_key_5, tmp_dict_value_5);
            Py_DECREF(tmp_dict_value_5);
            assert(!(tmp_res != 0));
            tmp_dict_key_5 = mod_consts[171];
            tmp_tuple_element_112 = mod_consts[137];
            tmp_string_concat_values_112 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_114;
                PyObject *tmp_expression_value_179;
                PyObject *tmp_subscript_value_179;
                PyObject *tmp_format_spec_114;
                PyTuple_SET_ITEM0(tmp_string_concat_values_112, 0, tmp_tuple_element_112);
                tmp_expression_value_179 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_179 == NULL)) {
                    tmp_expression_value_179 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_179 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 485;

                    goto tuple_build_exception_112;
                }
                tmp_subscript_value_179 = mod_consts[138];
                tmp_format_value_114 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_179, tmp_subscript_value_179);
                if (tmp_format_value_114 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 485;

                    goto tuple_build_exception_112;
                }
                tmp_format_spec_114 = mod_consts[64];
                tmp_tuple_element_112 = BUILTIN_FORMAT(tstate, tmp_format_value_114, tmp_format_spec_114);
                Py_DECREF(tmp_format_value_114);
                if (tmp_tuple_element_112 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 485;

                    goto tuple_build_exception_112;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_112, 1, tmp_tuple_element_112);
                tmp_tuple_element_112 = mod_consts[139];
                PyTuple_SET_ITEM0(tmp_string_concat_values_112, 2, tmp_tuple_element_112);
            }
            goto tuple_build_noexception_112;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_112:;
            Py_DECREF(tmp_string_concat_values_112);
            goto dict_build_exception_5;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_112:;
            tmp_list_element_19 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_112);
            Py_DECREF(tmp_string_concat_values_112);
            if (tmp_list_element_19 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 485;

                goto dict_build_exception_5;
            }
            tmp_dict_value_5 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_5, 0, tmp_list_element_19);
            tmp_res = PyDict_SetItem(tmp_assign_source_51, tmp_dict_key_5, tmp_dict_value_5);
            Py_DECREF(tmp_dict_value_5);
            assert(!(tmp_res != 0));
            tmp_dict_key_5 = mod_consts[172];
            tmp_tuple_element_113 = mod_consts[137];
            tmp_string_concat_values_113 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_115;
                PyObject *tmp_expression_value_180;
                PyObject *tmp_subscript_value_180;
                PyObject *tmp_format_spec_115;
                PyTuple_SET_ITEM0(tmp_string_concat_values_113, 0, tmp_tuple_element_113);
                tmp_expression_value_180 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_180 == NULL)) {
                    tmp_expression_value_180 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_180 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 488;

                    goto tuple_build_exception_113;
                }
                tmp_subscript_value_180 = mod_consts[140];
                tmp_format_value_115 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_180, tmp_subscript_value_180);
                if (tmp_format_value_115 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 488;

                    goto tuple_build_exception_113;
                }
                tmp_format_spec_115 = mod_consts[64];
                tmp_tuple_element_113 = BUILTIN_FORMAT(tstate, tmp_format_value_115, tmp_format_spec_115);
                Py_DECREF(tmp_format_value_115);
                if (tmp_tuple_element_113 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 488;

                    goto tuple_build_exception_113;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_113, 1, tmp_tuple_element_113);
                tmp_tuple_element_113 = mod_consts[141];
                PyTuple_SET_ITEM0(tmp_string_concat_values_113, 2, tmp_tuple_element_113);
            }
            goto tuple_build_noexception_113;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_113:;
            Py_DECREF(tmp_string_concat_values_113);
            goto dict_build_exception_5;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_113:;
            tmp_list_element_20 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_113);
            Py_DECREF(tmp_string_concat_values_113);
            if (tmp_list_element_20 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 488;

                goto dict_build_exception_5;
            }
            tmp_dict_value_5 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_5, 0, tmp_list_element_20);
            tmp_res = PyDict_SetItem(tmp_assign_source_51, tmp_dict_key_5, tmp_dict_value_5);
            Py_DECREF(tmp_dict_value_5);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_5;
        // Exception handling pass through code for dict_build:
        dict_build_exception_5:;
        Py_DECREF(tmp_assign_source_51);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_5:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[176], tmp_assign_source_51);
    }
    {
        PyObject *tmp_assign_source_52;
        PyObject *tmp_dict_key_6;
        PyObject *tmp_dict_value_6;
        PyObject *tmp_list_element_21;
        PyObject *tmp_string_concat_values_114;
        PyObject *tmp_tuple_element_114;
        tmp_dict_key_6 = mod_consts[64];
        tmp_tuple_element_114 = mod_consts[151];
        tmp_string_concat_values_114 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_116;
            PyObject *tmp_expression_value_181;
            PyObject *tmp_subscript_value_181;
            PyObject *tmp_format_spec_116;
            PyTuple_SET_ITEM0(tmp_string_concat_values_114, 0, tmp_tuple_element_114);
            tmp_expression_value_181 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_181 == NULL)) {
                tmp_expression_value_181 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_181 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 492;

                goto tuple_build_exception_114;
            }
            tmp_subscript_value_181 = mod_consts[54];
            tmp_format_value_116 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_181, tmp_subscript_value_181);
            if (tmp_format_value_116 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 492;

                goto tuple_build_exception_114;
            }
            tmp_format_spec_116 = mod_consts[64];
            tmp_tuple_element_114 = BUILTIN_FORMAT(tstate, tmp_format_value_116, tmp_format_spec_116);
            Py_DECREF(tmp_format_value_116);
            if (tmp_tuple_element_114 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 492;

                goto tuple_build_exception_114;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_114, 1, tmp_tuple_element_114);
            tmp_tuple_element_114 = mod_consts[91];
            PyTuple_SET_ITEM0(tmp_string_concat_values_114, 2, tmp_tuple_element_114);
        }
        goto tuple_build_noexception_114;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_114:;
        Py_DECREF(tmp_string_concat_values_114);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_114:;
        tmp_list_element_21 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_114);
        Py_DECREF(tmp_string_concat_values_114);
        if (tmp_list_element_21 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 492;

            goto frame_exception_exit_1;
        }
        tmp_dict_value_6 = MAKE_LIST_EMPTY(1);
        PyList_SET_ITEM(tmp_dict_value_6, 0, tmp_list_element_21);
        tmp_assign_source_52 = _PyDict_NewPresized( 5 );
        {
            PyObject *tmp_list_element_22;
            PyObject *tmp_string_concat_values_115;
            PyObject *tmp_tuple_element_115;
            PyObject *tmp_list_element_23;
            PyObject *tmp_string_concat_values_116;
            PyObject *tmp_tuple_element_116;
            PyObject *tmp_list_element_24;
            PyObject *tmp_string_concat_values_117;
            PyObject *tmp_tuple_element_117;
            PyObject *tmp_list_element_25;
            PyObject *tmp_string_concat_values_118;
            PyObject *tmp_tuple_element_118;
            tmp_res = PyDict_SetItem(tmp_assign_source_52, tmp_dict_key_6, tmp_dict_value_6);
            Py_DECREF(tmp_dict_value_6);
            assert(!(tmp_res != 0));
            tmp_dict_key_6 = mod_consts[167];
            tmp_tuple_element_115 = mod_consts[146];
            tmp_string_concat_values_115 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_117;
                PyObject *tmp_expression_value_182;
                PyObject *tmp_subscript_value_182;
                PyObject *tmp_format_spec_117;
                PyTuple_SET_ITEM0(tmp_string_concat_values_115, 0, tmp_tuple_element_115);
                tmp_expression_value_182 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_182 == NULL)) {
                    tmp_expression_value_182 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_182 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 493;

                    goto tuple_build_exception_115;
                }
                tmp_subscript_value_182 = mod_consts[147];
                tmp_format_value_117 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_182, tmp_subscript_value_182);
                if (tmp_format_value_117 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 493;

                    goto tuple_build_exception_115;
                }
                tmp_format_spec_117 = mod_consts[64];
                tmp_tuple_element_115 = BUILTIN_FORMAT(tstate, tmp_format_value_117, tmp_format_spec_117);
                Py_DECREF(tmp_format_value_117);
                if (tmp_tuple_element_115 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 493;

                    goto tuple_build_exception_115;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_115, 1, tmp_tuple_element_115);
                tmp_tuple_element_115 = mod_consts[65];
                PyTuple_SET_ITEM0(tmp_string_concat_values_115, 2, tmp_tuple_element_115);
            }
            goto tuple_build_noexception_115;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_115:;
            Py_DECREF(tmp_string_concat_values_115);
            goto dict_build_exception_6;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_115:;
            tmp_list_element_22 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_115);
            Py_DECREF(tmp_string_concat_values_115);
            if (tmp_list_element_22 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 493;

                goto dict_build_exception_6;
            }
            tmp_dict_value_6 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_6, 0, tmp_list_element_22);
            tmp_res = PyDict_SetItem(tmp_assign_source_52, tmp_dict_key_6, tmp_dict_value_6);
            Py_DECREF(tmp_dict_value_6);
            assert(!(tmp_res != 0));
            tmp_dict_key_6 = mod_consts[168];
            tmp_tuple_element_116 = mod_consts[148];
            tmp_string_concat_values_116 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_118;
                PyObject *tmp_expression_value_183;
                PyObject *tmp_subscript_value_183;
                PyObject *tmp_format_spec_118;
                PyTuple_SET_ITEM0(tmp_string_concat_values_116, 0, tmp_tuple_element_116);
                tmp_expression_value_183 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_183 == NULL)) {
                    tmp_expression_value_183 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_183 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 494;

                    goto tuple_build_exception_116;
                }
                tmp_subscript_value_183 = mod_consts[147];
                tmp_format_value_118 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_183, tmp_subscript_value_183);
                if (tmp_format_value_118 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 494;

                    goto tuple_build_exception_116;
                }
                tmp_format_spec_118 = mod_consts[64];
                tmp_tuple_element_116 = BUILTIN_FORMAT(tstate, tmp_format_value_118, tmp_format_spec_118);
                Py_DECREF(tmp_format_value_118);
                if (tmp_tuple_element_116 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 494;

                    goto tuple_build_exception_116;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_116, 1, tmp_tuple_element_116);
                tmp_tuple_element_116 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_116, 2, tmp_tuple_element_116);
            }
            goto tuple_build_noexception_116;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_116:;
            Py_DECREF(tmp_string_concat_values_116);
            goto dict_build_exception_6;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_116:;
            tmp_list_element_23 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_116);
            Py_DECREF(tmp_string_concat_values_116);
            if (tmp_list_element_23 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 494;

                goto dict_build_exception_6;
            }
            tmp_dict_value_6 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_6, 0, tmp_list_element_23);
            tmp_res = PyDict_SetItem(tmp_assign_source_52, tmp_dict_key_6, tmp_dict_value_6);
            Py_DECREF(tmp_dict_value_6);
            assert(!(tmp_res != 0));
            tmp_dict_key_6 = mod_consts[169];
            tmp_tuple_element_117 = mod_consts[149];
            tmp_string_concat_values_117 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_119;
                PyObject *tmp_expression_value_184;
                PyObject *tmp_subscript_value_184;
                PyObject *tmp_format_spec_119;
                PyTuple_SET_ITEM0(tmp_string_concat_values_117, 0, tmp_tuple_element_117);
                tmp_expression_value_184 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_184 == NULL)) {
                    tmp_expression_value_184 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_184 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 495;

                    goto tuple_build_exception_117;
                }
                tmp_subscript_value_184 = mod_consts[147];
                tmp_format_value_119 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_184, tmp_subscript_value_184);
                if (tmp_format_value_119 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 495;

                    goto tuple_build_exception_117;
                }
                tmp_format_spec_119 = mod_consts[64];
                tmp_tuple_element_117 = BUILTIN_FORMAT(tstate, tmp_format_value_119, tmp_format_spec_119);
                Py_DECREF(tmp_format_value_119);
                if (tmp_tuple_element_117 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 495;

                    goto tuple_build_exception_117;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_117, 1, tmp_tuple_element_117);
                tmp_tuple_element_117 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_117, 2, tmp_tuple_element_117);
            }
            goto tuple_build_noexception_117;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_117:;
            Py_DECREF(tmp_string_concat_values_117);
            goto dict_build_exception_6;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_117:;
            tmp_list_element_24 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_117);
            Py_DECREF(tmp_string_concat_values_117);
            if (tmp_list_element_24 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 495;

                goto dict_build_exception_6;
            }
            tmp_dict_value_6 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_6, 0, tmp_list_element_24);
            tmp_res = PyDict_SetItem(tmp_assign_source_52, tmp_dict_key_6, tmp_dict_value_6);
            Py_DECREF(tmp_dict_value_6);
            assert(!(tmp_res != 0));
            tmp_dict_key_6 = mod_consts[170];
            tmp_tuple_element_118 = mod_consts[150];
            tmp_string_concat_values_118 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_120;
                PyObject *tmp_expression_value_185;
                PyObject *tmp_subscript_value_185;
                PyObject *tmp_format_spec_120;
                PyTuple_SET_ITEM0(tmp_string_concat_values_118, 0, tmp_tuple_element_118);
                tmp_expression_value_185 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_185 == NULL)) {
                    tmp_expression_value_185 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_185 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 496;

                    goto tuple_build_exception_118;
                }
                tmp_subscript_value_185 = mod_consts[147];
                tmp_format_value_120 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_185, tmp_subscript_value_185);
                if (tmp_format_value_120 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 496;

                    goto tuple_build_exception_118;
                }
                tmp_format_spec_120 = mod_consts[64];
                tmp_tuple_element_118 = BUILTIN_FORMAT(tstate, tmp_format_value_120, tmp_format_spec_120);
                Py_DECREF(tmp_format_value_120);
                if (tmp_tuple_element_118 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 496;

                    goto tuple_build_exception_118;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_118, 1, tmp_tuple_element_118);
                tmp_tuple_element_118 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_118, 2, tmp_tuple_element_118);
            }
            goto tuple_build_noexception_118;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_118:;
            Py_DECREF(tmp_string_concat_values_118);
            goto dict_build_exception_6;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_118:;
            tmp_list_element_25 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_118);
            Py_DECREF(tmp_string_concat_values_118);
            if (tmp_list_element_25 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 496;

                goto dict_build_exception_6;
            }
            tmp_dict_value_6 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_6, 0, tmp_list_element_25);
            tmp_res = PyDict_SetItem(tmp_assign_source_52, tmp_dict_key_6, tmp_dict_value_6);
            Py_DECREF(tmp_dict_value_6);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_6;
        // Exception handling pass through code for dict_build:
        dict_build_exception_6:;
        Py_DECREF(tmp_assign_source_52);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_6:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[177], tmp_assign_source_52);
    }
    {
        PyObject *tmp_assign_source_53;
        PyObject *tmp_dict_key_7;
        PyObject *tmp_dict_value_7;
        PyObject *tmp_list_element_26;
        PyObject *tmp_string_concat_values_119;
        PyObject *tmp_tuple_element_119;
        tmp_dict_key_7 = mod_consts[167];
        tmp_tuple_element_119 = mod_consts[152];
        tmp_string_concat_values_119 = MAKE_TUPLE_EMPTY(3);
        {
            PyObject *tmp_format_value_121;
            PyObject *tmp_expression_value_186;
            PyObject *tmp_subscript_value_186;
            PyObject *tmp_format_spec_121;
            PyTuple_SET_ITEM0(tmp_string_concat_values_119, 0, tmp_tuple_element_119);
            tmp_expression_value_186 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

            if (unlikely(tmp_expression_value_186 == NULL)) {
                tmp_expression_value_186 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
            }

            if (tmp_expression_value_186 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 501;

                goto tuple_build_exception_119;
            }
            tmp_subscript_value_186 = mod_consts[153];
            tmp_format_value_121 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_186, tmp_subscript_value_186);
            if (tmp_format_value_121 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 501;

                goto tuple_build_exception_119;
            }
            tmp_format_spec_121 = mod_consts[64];
            tmp_tuple_element_119 = BUILTIN_FORMAT(tstate, tmp_format_value_121, tmp_format_spec_121);
            Py_DECREF(tmp_format_value_121);
            if (tmp_tuple_element_119 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 501;

                goto tuple_build_exception_119;
            }
            PyTuple_SET_ITEM(tmp_string_concat_values_119, 1, tmp_tuple_element_119);
            tmp_tuple_element_119 = mod_consts[65];
            PyTuple_SET_ITEM0(tmp_string_concat_values_119, 2, tmp_tuple_element_119);
        }
        goto tuple_build_noexception_119;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_119:;
        Py_DECREF(tmp_string_concat_values_119);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_119:;
        tmp_list_element_26 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_119);
        Py_DECREF(tmp_string_concat_values_119);
        if (tmp_list_element_26 == NULL) {
            assert(HAS_ERROR_OCCURRED(tstate));

            FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


            exception_lineno = 501;

            goto frame_exception_exit_1;
        }
        tmp_dict_value_7 = MAKE_LIST_EMPTY(1);
        PyList_SET_ITEM(tmp_dict_value_7, 0, tmp_list_element_26);
        tmp_assign_source_53 = _PyDict_NewPresized( 6 );
        {
            PyObject *tmp_list_element_27;
            PyObject *tmp_string_concat_values_120;
            PyObject *tmp_tuple_element_120;
            PyObject *tmp_list_element_28;
            PyObject *tmp_string_concat_values_121;
            PyObject *tmp_tuple_element_121;
            PyObject *tmp_list_element_29;
            PyObject *tmp_string_concat_values_122;
            PyObject *tmp_tuple_element_122;
            PyObject *tmp_list_element_30;
            PyObject *tmp_string_concat_values_123;
            PyObject *tmp_tuple_element_123;
            PyObject *tmp_list_element_31;
            PyObject *tmp_string_concat_values_124;
            PyObject *tmp_tuple_element_124;
            tmp_res = PyDict_SetItem(tmp_assign_source_53, tmp_dict_key_7, tmp_dict_value_7);
            Py_DECREF(tmp_dict_value_7);
            assert(!(tmp_res != 0));
            tmp_dict_key_7 = mod_consts[168];
            tmp_tuple_element_120 = mod_consts[152];
            tmp_string_concat_values_120 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_122;
                PyObject *tmp_expression_value_187;
                PyObject *tmp_subscript_value_187;
                PyObject *tmp_format_spec_122;
                PyTuple_SET_ITEM0(tmp_string_concat_values_120, 0, tmp_tuple_element_120);
                tmp_expression_value_187 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_187 == NULL)) {
                    tmp_expression_value_187 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_187 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 504;

                    goto tuple_build_exception_120;
                }
                tmp_subscript_value_187 = mod_consts[153];
                tmp_format_value_122 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_187, tmp_subscript_value_187);
                if (tmp_format_value_122 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 504;

                    goto tuple_build_exception_120;
                }
                tmp_format_spec_122 = mod_consts[64];
                tmp_tuple_element_120 = BUILTIN_FORMAT(tstate, tmp_format_value_122, tmp_format_spec_122);
                Py_DECREF(tmp_format_value_122);
                if (tmp_tuple_element_120 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 504;

                    goto tuple_build_exception_120;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_120, 1, tmp_tuple_element_120);
                tmp_tuple_element_120 = mod_consts[69];
                PyTuple_SET_ITEM0(tmp_string_concat_values_120, 2, tmp_tuple_element_120);
            }
            goto tuple_build_noexception_120;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_120:;
            Py_DECREF(tmp_string_concat_values_120);
            goto dict_build_exception_7;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_120:;
            tmp_list_element_27 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_120);
            Py_DECREF(tmp_string_concat_values_120);
            if (tmp_list_element_27 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 504;

                goto dict_build_exception_7;
            }
            tmp_dict_value_7 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_7, 0, tmp_list_element_27);
            tmp_res = PyDict_SetItem(tmp_assign_source_53, tmp_dict_key_7, tmp_dict_value_7);
            Py_DECREF(tmp_dict_value_7);
            assert(!(tmp_res != 0));
            tmp_dict_key_7 = mod_consts[169];
            tmp_tuple_element_121 = mod_consts[152];
            tmp_string_concat_values_121 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_123;
                PyObject *tmp_expression_value_188;
                PyObject *tmp_subscript_value_188;
                PyObject *tmp_format_spec_123;
                PyTuple_SET_ITEM0(tmp_string_concat_values_121, 0, tmp_tuple_element_121);
                tmp_expression_value_188 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_188 == NULL)) {
                    tmp_expression_value_188 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_188 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 507;

                    goto tuple_build_exception_121;
                }
                tmp_subscript_value_188 = mod_consts[153];
                tmp_format_value_123 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_188, tmp_subscript_value_188);
                if (tmp_format_value_123 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 507;

                    goto tuple_build_exception_121;
                }
                tmp_format_spec_123 = mod_consts[64];
                tmp_tuple_element_121 = BUILTIN_FORMAT(tstate, tmp_format_value_123, tmp_format_spec_123);
                Py_DECREF(tmp_format_value_123);
                if (tmp_tuple_element_121 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 507;

                    goto tuple_build_exception_121;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_121, 1, tmp_tuple_element_121);
                tmp_tuple_element_121 = mod_consts[72];
                PyTuple_SET_ITEM0(tmp_string_concat_values_121, 2, tmp_tuple_element_121);
            }
            goto tuple_build_noexception_121;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_121:;
            Py_DECREF(tmp_string_concat_values_121);
            goto dict_build_exception_7;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_121:;
            tmp_list_element_28 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_121);
            Py_DECREF(tmp_string_concat_values_121);
            if (tmp_list_element_28 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 507;

                goto dict_build_exception_7;
            }
            tmp_dict_value_7 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_7, 0, tmp_list_element_28);
            tmp_res = PyDict_SetItem(tmp_assign_source_53, tmp_dict_key_7, tmp_dict_value_7);
            Py_DECREF(tmp_dict_value_7);
            assert(!(tmp_res != 0));
            tmp_dict_key_7 = mod_consts[170];
            tmp_tuple_element_122 = mod_consts[152];
            tmp_string_concat_values_122 = MAKE_TUPLE_EMPTY(3);
            {
                PyObject *tmp_format_value_124;
                PyObject *tmp_expression_value_189;
                PyObject *tmp_subscript_value_189;
                PyObject *tmp_format_spec_124;
                PyTuple_SET_ITEM0(tmp_string_concat_values_122, 0, tmp_tuple_element_122);
                tmp_expression_value_189 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_189 == NULL)) {
                    tmp_expression_value_189 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_189 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 510;

                    goto tuple_build_exception_122;
                }
                tmp_subscript_value_189 = mod_consts[153];
                tmp_format_value_124 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_189, tmp_subscript_value_189);
                if (tmp_format_value_124 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 510;

                    goto tuple_build_exception_122;
                }
                tmp_format_spec_124 = mod_consts[64];
                tmp_tuple_element_122 = BUILTIN_FORMAT(tstate, tmp_format_value_124, tmp_format_spec_124);
                Py_DECREF(tmp_format_value_124);
                if (tmp_tuple_element_122 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 510;

                    goto tuple_build_exception_122;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_122, 1, tmp_tuple_element_122);
                tmp_tuple_element_122 = mod_consts[75];
                PyTuple_SET_ITEM0(tmp_string_concat_values_122, 2, tmp_tuple_element_122);
            }
            goto tuple_build_noexception_122;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_122:;
            Py_DECREF(tmp_string_concat_values_122);
            goto dict_build_exception_7;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_122:;
            tmp_list_element_29 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_122);
            Py_DECREF(tmp_string_concat_values_122);
            if (tmp_list_element_29 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 510;

                goto dict_build_exception_7;
            }
            tmp_dict_value_7 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_7, 0, tmp_list_element_29);
            tmp_res = PyDict_SetItem(tmp_assign_source_53, tmp_dict_key_7, tmp_dict_value_7);
            Py_DECREF(tmp_dict_value_7);
            assert(!(tmp_res != 0));
            tmp_dict_key_7 = mod_consts[171];
            tmp_tuple_element_123 = mod_consts[154];
            tmp_string_concat_values_123 = MAKE_TUPLE_EMPTY(5);
            {
                PyObject *tmp_format_value_125;
                PyObject *tmp_expression_value_190;
                PyObject *tmp_subscript_value_190;
                PyObject *tmp_format_spec_125;
                PyObject *tmp_format_value_126;
                PyObject *tmp_expression_value_191;
                PyObject *tmp_subscript_value_191;
                PyObject *tmp_format_spec_126;
                PyTuple_SET_ITEM0(tmp_string_concat_values_123, 0, tmp_tuple_element_123);
                tmp_expression_value_190 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_190 == NULL)) {
                    tmp_expression_value_190 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_190 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 513;

                    goto tuple_build_exception_123;
                }
                tmp_subscript_value_190 = mod_consts[25];
                tmp_format_value_125 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_190, tmp_subscript_value_190);
                if (tmp_format_value_125 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 513;

                    goto tuple_build_exception_123;
                }
                tmp_format_spec_125 = mod_consts[64];
                tmp_tuple_element_123 = BUILTIN_FORMAT(tstate, tmp_format_value_125, tmp_format_spec_125);
                Py_DECREF(tmp_format_value_125);
                if (tmp_tuple_element_123 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 513;

                    goto tuple_build_exception_123;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_123, 1, tmp_tuple_element_123);
                tmp_tuple_element_123 = mod_consts[155];
                PyTuple_SET_ITEM0(tmp_string_concat_values_123, 2, tmp_tuple_element_123);
                tmp_expression_value_191 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_191 == NULL)) {
                    tmp_expression_value_191 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_191 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 513;

                    goto tuple_build_exception_123;
                }
                tmp_subscript_value_191 = mod_consts[156];
                tmp_format_value_126 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_191, tmp_subscript_value_191);
                if (tmp_format_value_126 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 513;

                    goto tuple_build_exception_123;
                }
                tmp_format_spec_126 = mod_consts[64];
                tmp_tuple_element_123 = BUILTIN_FORMAT(tstate, tmp_format_value_126, tmp_format_spec_126);
                Py_DECREF(tmp_format_value_126);
                if (tmp_tuple_element_123 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 513;

                    goto tuple_build_exception_123;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_123, 3, tmp_tuple_element_123);
                tmp_tuple_element_123 = mod_consts[157];
                PyTuple_SET_ITEM0(tmp_string_concat_values_123, 4, tmp_tuple_element_123);
            }
            goto tuple_build_noexception_123;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_123:;
            Py_DECREF(tmp_string_concat_values_123);
            goto dict_build_exception_7;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_123:;
            tmp_list_element_30 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_123);
            Py_DECREF(tmp_string_concat_values_123);
            if (tmp_list_element_30 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 513;

                goto dict_build_exception_7;
            }
            tmp_dict_value_7 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_7, 0, tmp_list_element_30);
            tmp_res = PyDict_SetItem(tmp_assign_source_53, tmp_dict_key_7, tmp_dict_value_7);
            Py_DECREF(tmp_dict_value_7);
            assert(!(tmp_res != 0));
            tmp_dict_key_7 = mod_consts[172];
            tmp_tuple_element_124 = mod_consts[158];
            tmp_string_concat_values_124 = MAKE_TUPLE_EMPTY(5);
            {
                PyObject *tmp_format_value_127;
                PyObject *tmp_expression_value_192;
                PyObject *tmp_subscript_value_192;
                PyObject *tmp_format_spec_127;
                PyObject *tmp_format_value_128;
                PyObject *tmp_expression_value_193;
                PyObject *tmp_subscript_value_193;
                PyObject *tmp_format_spec_128;
                PyTuple_SET_ITEM0(tmp_string_concat_values_124, 0, tmp_tuple_element_124);
                tmp_expression_value_192 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_192 == NULL)) {
                    tmp_expression_value_192 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_192 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 516;

                    goto tuple_build_exception_124;
                }
                tmp_subscript_value_192 = mod_consts[26];
                tmp_format_value_127 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_192, tmp_subscript_value_192);
                if (tmp_format_value_127 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 516;

                    goto tuple_build_exception_124;
                }
                tmp_format_spec_127 = mod_consts[64];
                tmp_tuple_element_124 = BUILTIN_FORMAT(tstate, tmp_format_value_127, tmp_format_spec_127);
                Py_DECREF(tmp_format_value_127);
                if (tmp_tuple_element_124 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 516;

                    goto tuple_build_exception_124;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_124, 1, tmp_tuple_element_124);
                tmp_tuple_element_124 = mod_consts[159];
                PyTuple_SET_ITEM0(tmp_string_concat_values_124, 2, tmp_tuple_element_124);
                tmp_expression_value_193 = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[61]);

                if (unlikely(tmp_expression_value_193 == NULL)) {
                    tmp_expression_value_193 = GET_MODULE_VARIABLE_VALUE_FALLBACK(tstate, mod_consts[61]);
                }

                if (tmp_expression_value_193 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 516;

                    goto tuple_build_exception_124;
                }
                tmp_subscript_value_193 = mod_consts[156];
                tmp_format_value_128 = LOOKUP_SUBSCRIPT(tstate, tmp_expression_value_193, tmp_subscript_value_193);
                if (tmp_format_value_128 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 516;

                    goto tuple_build_exception_124;
                }
                tmp_format_spec_128 = mod_consts[64];
                tmp_tuple_element_124 = BUILTIN_FORMAT(tstate, tmp_format_value_128, tmp_format_spec_128);
                Py_DECREF(tmp_format_value_128);
                if (tmp_tuple_element_124 == NULL) {
                    assert(HAS_ERROR_OCCURRED(tstate));

                    FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                    exception_lineno = 516;

                    goto tuple_build_exception_124;
                }
                PyTuple_SET_ITEM(tmp_string_concat_values_124, 3, tmp_tuple_element_124);
                tmp_tuple_element_124 = mod_consts[157];
                PyTuple_SET_ITEM0(tmp_string_concat_values_124, 4, tmp_tuple_element_124);
            }
            goto tuple_build_noexception_124;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_124:;
            Py_DECREF(tmp_string_concat_values_124);
            goto dict_build_exception_7;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_124:;
            tmp_list_element_31 = PyUnicode_Join(mod_consts[64], tmp_string_concat_values_124);
            Py_DECREF(tmp_string_concat_values_124);
            if (tmp_list_element_31 == NULL) {
                assert(HAS_ERROR_OCCURRED(tstate));

                FETCH_ERROR_OCCURRED(tstate, &exception_type, &exception_value, &exception_tb);


                exception_lineno = 516;

                goto dict_build_exception_7;
            }
            tmp_dict_value_7 = MAKE_LIST_EMPTY(1);
            PyList_SET_ITEM(tmp_dict_value_7, 0, tmp_list_element_31);
            tmp_res = PyDict_SetItem(tmp_assign_source_53, tmp_dict_key_7, tmp_dict_value_7);
            Py_DECREF(tmp_dict_value_7);
            assert(!(tmp_res != 0));
        }
        goto dict_build_noexception_7;
        // Exception handling pass through code for dict_build:
        dict_build_exception_7:;
        Py_DECREF(tmp_assign_source_53);
        goto frame_exception_exit_1;
        // Finished with no exception for dict_build:
        dict_build_noexception_7:;
        UPDATE_STRING_DICT1(moduledict_general$consumables, (Nuitka_StringObject *)mod_consts[178], tmp_assign_source_53);
    }


    // Put the previous frame back on top.
    popFrameStack(tstate);

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_c882f4f0f7cca0ca41864096797f6688, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_c882f4f0f7cca0ca41864096797f6688->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_c882f4f0f7cca0ca41864096797f6688, exception_lineno);
    }



    assertFrameObject(frame_c882f4f0f7cca0ca41864096797f6688);

    // Put the previous frame back on top.
    popFrameStack(tstate);

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("general$consumables", false);

    Py_INCREF(module_general$consumables);
    return module_general$consumables;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_general$consumables, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(tstate, module_name);
        }
    }
#endif
    PGO_onModuleExit("general$consumables", false);

    RESTORE_ERROR_OCCURRED(tstate, exception_type, exception_value, exception_tb);
    return NULL;
}
