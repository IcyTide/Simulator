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


def wu_xiang_zhan(status: Status):
    pass


EQUIP_GAINS_NAME = {
    '22035-1': "五相斩",
    "1925": "朔气4%套装",
    "4290": "刀啸风吟10%套装",
    "4291": "上将军印10%套装",
    "4294": "刀啸风吟5%橙武",
    "4295": "项王击鼎5%橙武",
    "2430": "橙武特效",
    "1942": "上将军印-神兵"
}
EQUIP_GAINS = {
    '22035-1': wu_xiang_zhan,
    "1925": attribute_set_gain,
    "4290": dao_xiao_set_gain,
    "4291": shang_jiang_set_gain,
    "4294": dao_xiao_divine_gain,
    "4295": xiang_wang_divine_gain,
    "2430": divine_effect,
    "1942": shang_jiang_divine_gain
}
