from enum import IntEnum, StrEnum, auto


class GLOBAL(IntEnum):
    GAME_FPS = 16


class ABSORB_ATTRIBUTE_SHIELD_TYPE(IntEnum):
    GLOBAL = auto()
    PHYSICS = auto()
    SOLAR = auto()
    LUNAR = auto()
    NEUTRAL = auto()
    POISON = auto()


class EXECUTE_TYPE(StrEnum):
    APPLY = "Apply"
    APPLY_SETUP = "ApplySetup"
    APPLY_BULLET_TO_DEST = "ApplyBulletToDest"
    APPLY_BULLET_TO_DEST_AND_ROLLBACK = "ApplyBulletToDestAndRollback"
    UNAPPLY = "UnApply"
    UNAPPLY_SETUP = "UnApplySetup"
    UNAPPLY_BULLET_TO_DEST = "UnApplyBulletToDest"
    UNAPPLY_BULLET_TO_DEST_AND_ROLLBACK = "UnApplyBulletToDestAndRollback"
    GET_SKILL_LEVEL_DATA = "GetSkillLevelData"
    GET_SKILL_RECIPE_DATA = "GetSkillRecipeData"

    ON_CHANNEL_BEGIN = "OnChannelBegin"
    ON_CHANNEL_END = "OnChannelEnd"
    ON_SKILL_LEVEL_UP = "OnSkillLevelUp"
    ON_SKILL_FORGOTTEN = "OnSkillForgotten"
    ON_BULLET_DESTROY = "OnBulletDestroy"
    ON_REMOVE = "OnRemove"


class ATTRIBUTE_EFFECT_MODE(IntEnum):
    EFFECT_TO_SELF_AND_ROLLBACK = auto()
    EFFECT_TO_DEST_AND_ROLLBACK = auto()
    EFFECT_TO_SELF_NOT_ROLLBACK = auto()
    EFFECT_TO_DEST_NOT_ROLLBACK = auto()


class ATTRIBUTE_TYPE(IntEnum):
    USELESS = 0

    # Useless Attribute
    CHANGE_POSE_STATE = 0

    # Behavior
    EXECUTE_SCRIPT = auto()
    EXECUTE_SCRIPT_SETUP = auto()
    EXECUTE_SCRIPT_BULLET_TO_DEST = auto()
    EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK = auto()
    CAST_SKILL = auto()
    CALL_BUFF = auto()
    SET_TALENT_RECIPE = auto()

    # Damage Attribute
    SKILL_PHYSICS_DAMAGE = auto()
    SKILL_SOLAR_DAMAGE = auto()
    SKILL_LUNAR_DAMAGE = auto()
    SKILL_NEUTRAL_DAMAGE = auto()
    SKILL_POISON_DAMAGE = auto()

    SKILL_PHYSICS_DAMAGE_RAND = auto()
    SKILL_SOLAR_DAMAGE_RAND = auto()
    SKILL_LUNAR_DAMAGE_RAND = auto()
    SKILL_NEUTRAL_DAMAGE_RAND = auto()
    SKILL_POISON_DAMAGE_RAND = auto()

    CALL_PHYSICS_DAMAGE = auto()
    CALL_SOLAR_DAMAGE = auto()
    CALL_LUNAR_DAMAGE = auto()
    CALL_NEUTRAL_DAMAGE = auto()
    CALL_POISON_DAMAGE = auto()

    CALL_SURPLUS_PHYSICS_DAMAGE = auto()
    CALL_SURPLUS_SOLAR_DAMAGE = auto()
    CALL_SURPLUS_LUNAR_DAMAGE = auto()
    CALL_SURPLUS_NEUTRAL_DAMAGE = auto()
    CALL_SURPLUS_POISON_DAMAGE = auto()

    # Attack Attribute
    PHYSICS_ATTACK_POWER_BASE = auto()
    SOLAR_ATTACK_POWER_BASE = auto()
    LUNAR_ATTACK_POWER_BASE = auto()

    PHYSICS_ATTACK_POWER_PERCENT = auto()
    SOLAR_ATTACK_POWER_PERCENT = auto()
    LUNAR_ATTACK_POWER_PERCENT = auto()

    # Major Attribute

    # Critical Attribute
    PHYSICS_CRITICAL_STRIKE_BASE_RATE = auto()
    SOLAR_CRITICAL_STRIKE_BASE_RATE = auto()
    LUNAR_CRITICAL_STRIKE_BASE_RATE = auto()

    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = auto()

    # Minor Attribute
    STRAIN_PERCENT = auto()

    # Defense Attribute
    PHYSICS_SHIELD_BASE = auto()
    MAGIC_SHIELD = auto()

    # Cof Attribute
    STRENGTH_TO_PHYSICS_ATTACK_POWER_COF = auto()
    STRENGTH_TO_PHYSICS_OVERCOME_COF = auto()
    SPUNK_TO_SOLAR_AND_LUNAR_ATTACK_POWER_COF = auto()
    SPUNK_TO_SOLAR_AND_LUNAR_CRITICAL_STRIKE_COF = auto()

    # Other Attribute
    ALL_SHIELD_IGNORE_PERCENT = auto()
    DST_NPC_DAMAGE_COEFFICIENT = auto()
    GLOBAL_DAMGAGE_FACTOR = auto()


class BUFF_COMPARE_FLAG(IntEnum):
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    LESS = auto()


class SKILL_COMPARE_FLAG(IntEnum):
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    LESS = auto()


ENV_VARIABLES = [
    GLOBAL, ABSORB_ATTRIBUTE_SHIELD_TYPE,
    EXECUTE_TYPE, ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE, BUFF_COMPARE_FLAG, SKILL_COMPARE_FLAG
]
