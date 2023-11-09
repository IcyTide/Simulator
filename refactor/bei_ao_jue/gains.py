from base.skill import Skill
from base.status import Status


def dao_xiao_set_gain(status: Status):
    status.skills["刀啸风吟"].skill_damage_addition += 0.1


def shang_jiang_set_gain(status: Status):
    status.skills["上将军印"].skill_damage_addition += 0.1
    status.skills["见尘"].skill_damage_addition += 0.1


def attribute_set_gain(status: Status):
    def attribute_set_post_cast(self: Skill):
        self.status.buffs["朔气"].trigger()

    for skill in status.skills.values():
        if skill.is_hit:
            skill.post_hit_effect.append(attribute_set_post_cast)


def dao_xiao_divine_gain(status: Status):
    status.skills["刀啸风吟"].skill_damage_addition += 0.05


def xiang_wang_divine_gain(status: Status):
    pass


def divine_effect(status: Status):
    pass


def shang_jiang_divine_gain(status: Status):
    pass


gains = [dao_xiao_set_gain, shang_jiang_set_gain, attribute_set_gain]
