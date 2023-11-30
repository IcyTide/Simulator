from base.buff import Buff
from base.skill import Skill
from base.status import Status


class ShangChun:
    def __call__(self, status: Status):
        status.skills["剑破虚空"].skill_damage_addition += 102 / 1024


class QingMeiXiu:
    def __call__(self, status: Status):
        status.skills["玳弦急曲"].skill_critical_strike += 0.1
        status.skills["玳弦急曲"].skill_critical_power += 102 / 1024


class QianLiBingFen:
    def __call__(self, status: Status):
        status.skills["剑破虚空"].skill_critical_strike += 0.1
        status.skills["剑破虚空"].skill_critical_power += 102 / 1024


class JingHan:
    def __call__(self, status: Status):
        status.skills["剑气长江"].skill_damage_addition += 154 / 1024
        status.skills["江海凝光"].skill_damage_addition += 154 / 1024


class XinZhuang:
    @staticmethod
    def xin_zhuang_post_hit(self: Skill):
        self.status.skills["玳弦急曲·新妆"].cast()

    def __call__(self, status: Status):
        status.skills["玳弦急曲"].ji_qu = False
        status.skills["玳弦急曲"].interval_base = 13
        status.skills["玳弦急曲"].post_hit_effect.append(self.xin_zhuang_post_hit)


class QingMei:
    def __call__(self, status: Status):
        status.skills["急曲·持续"].attack_power_cof_gain += 0.15


class ZhenShang:
    @staticmethod
    def zhen_shang_critical_hit(self: Skill):
        self.status.buffs["枕上"].trigger()

    def __call__(self, status: Status):
        related_skills = ["剑破虚空", "剑气长江", "玳弦急曲", "剑影留痕"]
        for skill in related_skills:
            status.skills[skill].critical_hit_effect.append(self.zhen_shang_critical_hit)


class ShengLian:
    def __call__(self, status: Status):
        status.skills["剑破虚空"].skill_damage_addition += 358 / 1024


class GuangLingYue:
    @staticmethod
    def guang_ling_yue_post_hit(self: Skill):
        if self.status.stacks["广陵月"]:
            self.status.skills["广陵月·伤害"].cast()

    def __call__(self, status: Status):
        status.skills["广陵月"].activate = True
        for skill in status.skills.values():
            if skill.is_hit and skill.name != "广陵月·伤害":
                skill.post_hit_effect.append(self.guang_ling_yue_post_hit)


class LiuYu:
    @staticmethod
    def jian_ying_liu_hen_post_cast(self: Skill):
        self.status.buffs["流玉"].trigger()

    @staticmethod
    def dai_xian_ji_qu_post_cast(self: Skill):
        if self.status.stacks["流玉"]:
            self.status.buffs["流玉"].clear()
            self.status.skills["流玉·持续"].cast()

    def __call__(self, status: Status):
        status.skills["剑影留痕"].cd_base = 15 * 16
        status.skills["剑影留痕"].post_cast_effect.append(self.jian_ying_liu_hen_post_cast)
        status.skills["玳弦急曲"].post_cast_effect.append(self.dai_xian_ji_qu_post_cast)


class ChaiYan:
    @staticmethod
    def chai_yan_post_cast(self: Skill):
        if self.status.stacks[f"{self.name}·钗燕"]:
            self.status.buffs["钗燕·计数"].clear()
        self.status.buffs[f"{self.name}·钗燕"].trigger()

    def __call__(self, status: Status):
        status.skills["剑影留痕"].cd_base = 15 * 16
        related_skills = ["江海凝光", "玳弦急曲", "剑破虚空", "剑气长江", "剑影留痕"]
        for skill in related_skills:
            status.skills[skill].post_cast_effect.append(self.chai_yan_post_cast)


class YuanJun:
    def __call__(self, status: Status):
        status.attribute.magical_critical_strike_gain += 0.1 * 0.5
        status.attribute.magical_critical_power_gain += 102 / 1024 * 0.5


class ShuangFeng:
    def __call__(self, status: Status):
        status.attribute.spirit_gain += 102 / 1024


class YingXiu:
    @staticmethod
    def ying_xiu_post_cast(self: Skill):
        self.status.buffs["盈袖"].trigger()

    @staticmethod
    def ying_xiu_post_hit(self: Skill):
        if self.status.stacks["盈袖"]:
            self.status.skills["盈袖"].cast()

    def __call__(self, status: Status):
        status.skills["繁音急节"].post_cast_effect.append(self.ying_xiu_post_cast)
        status.skills["玳弦急曲"].post_hit_effect.append(self.ying_xiu_post_hit)


class HuaBing:
    @staticmethod
    def hua_bing_post_cast(self: Skill):
        self.status.buffs["化冰"].trigger()

    @staticmethod
    def hua_bing_post_hit(self: Skill):
        if self.status.stacks["化冰"]:
            self.status.buffs["化冰·计数"].trigger()

    def __call__(self, status: Status):
        status.skills["心鼓弦"].cd_base = 120 * 16
        status.skills["心鼓弦"].post_cast_effect.append(self.hua_bing_post_cast)
        status.skills["玳弦急曲"].post_hit_effect.append(self.hua_bing_post_hit)


class YeTian:
    @staticmethod
    def ye_tian_critical_hit(self: Skill):
        self.status.buffs["夜天"].trigger()

    def __call__(self, status: Status):
        status.skills["剑气长江"].critical_hit_effect.append(self.ye_tian_critical_hit)


class QiongXiao:
    @staticmethod
    def qiong_xiao_post_cast(self: Skill):
        self.status.buffs["剑神无我"].trigger()

    def __call__(self, status: Status):
        status.skills["婆罗门"].post_cast_effect.append(self.qiong_xiao_post_cast)


class NingHua:
    @staticmethod
    def jiang_hai_ning_guang_post_cast(self: Skill):
        self.status.buffs["凝华"].trigger()

    @staticmethod
    def jian_qi_chang_jiang_post_cast(self: Skill):
        for _ in range(self.status.stacks["凝华"]):
            self.status.skills["凝华"].cast()
        self.status.buffs["凝华"].clear()

    def __call__(self, status: Status):
        status.skills["江海凝光"].cd_base += 4 * 16
        status.skills["江海凝光"].post_cast_effect.append(self.jiang_hai_ning_guang_post_cast)
        status.skills["剑气长江"].post_cast_effect.append(self.jian_qi_chang_jiang_post_cast)


class ShuangJiang:
    @staticmethod
    def shuang_jiang_add(self: Buff):
        for i, buff in enumerate(["霜降·15%", "霜降·30%", "霜降·45%"]):
            if i + 1 == self.status.stacks[self.name]:
                self.status.buffs[buff].trigger()
            else:
                self.status.buffs[buff].clear()

    @staticmethod
    def shuang_jiang_remove(self: Buff):
        self.status.buffs["霜降·15%"].clear()
        self.status.buffs["霜降·30%"].clear()
        self.status.buffs["霜降·45%"].clear()

    def __call__(self, status: Status):
        status.buffs["急曲·持续"].add_effect.append(self.shuang_jiang_add)
        status.buffs["急曲·持续"].remove_effect.append(self.shuang_jiang_remove)


TALENTS = [
    ["伤春", "青梅嗅"],
    ["千里冰封", "惊寒"],
    ["新妆"],
    ["青梅"],
    ["枕上"],
    ["广陵月", "生莲"],
    ["流玉"],
    ["钗燕", "元君"],
    ["盈袖", "霜风"],
    ["化冰"],
    ["夜天", "琼霄"],
    ["凝华", "霜降"]
]
TALENT_GAINS = {
    "伤春": ShangChun(),
    "青梅嗅": QingMeiXiu(),
    "千里冰封": QianLiBingFen(),
    "惊寒": JingHan(),
    "新妆": XinZhuang(),
    "青梅": QingMei(),
    "枕上": ZhenShang(),
    "生莲": ShengLian(),
    "广陵月": GuangLingYue(),
    "流玉": LiuYu(),
    "钗燕": ChaiYan(),
    "元君": YuanJun(),
    "霜风": ShuangFeng(),
    "盈袖": YingXiu(),
    "化冰": HuaBing(),
    "夜天": YeTian(),
    "琼霄": QiongXiao(),
    "凝华": NingHua(),
    "霜降": ShuangJiang(),
}
