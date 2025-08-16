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

class PLAYER_ARENA_TYPE(IntEnum):
    DPS = auto()


class SKILL_KIND_TYPE(IntEnum):
    PHYSICS = auto()
    LEAP = auto()


class TARGET(IntEnum):
    PLAYER = auto()
    NPC = auto()


class MOVE_STATE(IntEnum):
    ON_STAND = auto()
    ON_HALT = auto()
    ON_FREEZE = auto()
    ON_KNOCKED_DOWN = auto()


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
    KUNGFU_TYPE = 0
    SET_ADAPTIVE_SKILL_TYPE = 0
    IGNORE_OTHER_ALARM_RANGE = 0
    NEGATIVE_SHIELD = 0

    DECRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = 0
    DROP_DEFENCE = 0
    ACTIVE_THREAT_COEFFICIENT = 0
    BEAT_BACK_RATE = 0
    MANA_REPLENISH_EXT = 0
    MOVE_SPEED_PERCENT = 0
    GLOBAL_RESIST_PERCENT = 0

    MOUNTING_RATE = 0
    KNOCKED_DOWN_RATE = 0
    KNOCKED_BACK_RATE = 0
    REPULSED_RATE = 0
    PULL_RATE = 0
    IMMUNE_SKILL_MOVE = 0
    IMMUNITY_BEAT_BREAK = 0

    CHANGE_POSE_STATE = 0
    DASH_TO_POINT = 0

    # Behavior
    IMMUNITY = auto()
    SILENCE = auto()
    DIRECT_CAST_MASK = auto()
    SET_NEXT_BUFF_COUNT = auto()
    CALL_SUB_BUFF = auto()

    EXECUTE_SCRIPT = auto()
    EXECUTE_SCRIPT_SETUP = auto()
    EXECUTE_SCRIPT_BULLET_TO_DEST = auto()
    EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK = auto()
    CAST_SKILL = auto()
    CALL_BUFF = auto()
    SET_TALENT_RECIPE = auto()
    SKILL_EVENT_HANDLER = auto()

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

    ALL_DAMAGE_ADD_PERCENT = auto()
    ALL_PHYSICS_DAMAGE_ADD_PERCENT = auto()
    ALL_MAGIC_DAMAGE_ADD_PERCENT = auto()

    # Resource Attribute
    MAX_LIFE_PERCENT_ADD = auto()

    # Attack Attribute
    PHYSICS_ATTACK_POWER_BASE = auto()

    PHYSICS_ATTACK_POWER_PERCENT = auto()

    # Major Attribute

    # Critical Attribute
    PHYSICS_CRITICAL_STRIKE_BASE_RATE = auto()
    PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = auto()

    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = auto()

    # Minor Attribute
    STRAIN_PERCENT = auto()

    # Defense Attribute
    PHYSICS_SHIELD_BASE = auto()
    MAGIC_SHIELD = auto()

    RESIST_CRITICAL_STRIKE_RATE = auto()

    # Cof Attribute
    STRENGTH_TO_PHYSICS_ATTACK_POWER_COF = auto()
    STRENGTH_TO_PHYSICS_OVERCOME_COF = auto()

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
    GLOBAL, ABSORB_ATTRIBUTE_SHIELD_TYPE, PLAYER_ARENA_TYPE, SKILL_KIND_TYPE,
    TARGET, MOVE_STATE, EXECUTE_TYPE, ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE, BUFF_COMPARE_FLAG, SKILL_COMPARE_FLAG
]
