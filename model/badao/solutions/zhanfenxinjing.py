from badao.attributes import *
from abstract import wait, divine
from badao.simulator import BadaoSimulator, attribute_set, skill_set, skills, effects
from badao.talents import *
from badao.recipes import shangjiang_recipe, pofu_recipe, daoxiao_recipe, qinlong_recipe, zuizhan_recipe
from zhenfa import *


def priority_func(self):
    return [
            (pofu_skill, lambda: not self.cd_list[divine]),
            (jianbi_skill, lambda: self.cd_list[zuizhan_skill] <= GCD),
            (pofu_skill, lambda: self.overdraw[pofu_skill] > pofu_skill.overdraw - 1),
            (zuizhan_skill, lambda: True),
            (wait, lambda: self.cd_list[zuizhan_skill] < 0.5 or self.cd_list[jianbi_skill] < 0.5),
            (daoxiao_skill, lambda: self.duration_list[hanfeng_effect] <= 2.5 or self.effect_list[
                hanfeng_effect] < hanfeng_effect.max_layers),
            (pofu_skill, lambda: self.cd_list[jianbi_skill] > GCD),
            (wait, lambda: self.cd_list[pofu_skill] < 0.5),
            (shangjiang_skill, lambda: self.cd_list[pofu_skill] >= shangjiang_skill.cast_time),
            (daoxiao_skill, lambda: True)
        ]


if __name__ == '__main__':
    qixue_list = [guihan_talent, minggu_talent, huajiao_talent, jianchen_talent, hanfeng_talent, zhanfen_talent,
                  xinghuo_talent, jueqi_talent, jinghong_talent, lifeng_talent, xinjing_talent]
    recipe_list = [(shangjiang_recipe, (0.09, 0.04)),
                   (pofu_recipe, (0.12, 0.04)),
                   (qinlong_recipe, (0.05, 0.04)),
                   (daoxiao_recipe, (0.09, 0.04)),
                   (zuizhan_recipe, (0.09, 0.07))]
    prepare_skill_list = [daoxiao_skill, naoxumi_skill, jianbi_skill]

    epochs, duration = 1, 300
    buffs = []
    zhenfa = lingxue
    simulator = BadaoSimulator(skills, effects, prepare_skill_list, True, divine_counter, duration,
                               priority_func=priority_func, talent_list=qixue_list, recipe_list=recipe_list,
                               skill_set=skill_set, attribute_set=attribute_set, zhenyan=zhenfa, buffs=buffs)
    simulator.simulate(epochs)
    print(simulator.dps)
    for skill, detail in simulator.summary.items():
        print(f"{skill}: {detail}")


    def print_attribute(attribute):
        details = {
            "基础力道": str(attribute.base_strength),
            "最终力道": str(attribute.strength),
            "基础攻击": str(attribute.base_physical_attack_power),
            "最终攻击": str(attribute.attack_power),
            "武伤": str(attribute.weapon_damage),
            "基础会心": str(attribute.base_physical_critical_strike),
            "最终会心": str(attribute.critical_strike),
            "基础会效": str(attribute.base_physical_critical_effect),
            "最终会效": str(attribute.critical_effect),
            "基础破防": str(attribute.base_physical_overcome),
            "最终破防": str(attribute.overcome),
            "破招": str(attribute.counter),
            "基础无双": str(attribute.base_strain),
            "最终无双": str(attribute.strain)
        }
        print(details)


    def print_gradient(attribute):
        gradients = {
            "力道": str(attribute.base_strength.grad),
            "基础": str(attribute.base_physical_attack_power.grad),
            "武伤": str(attribute.weapon_damage.grad),
            "会心": str(attribute.base_physical_critical_strike.grad),
            "会效": str(attribute.base_physical_critical_effect.grad),
            "破防": str(attribute.base_physical_overcome.grad),
            "破招": str(attribute.counter.grad),
            "无双": str(attribute.base_strain.grad)
        }
        print(gradients)


    print_attribute(simulator.attribute)
    print_gradient(simulator.attribute)
