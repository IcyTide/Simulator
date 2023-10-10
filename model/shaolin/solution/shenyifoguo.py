from constants import GCD
from shaolin.attributes import *
from shaolin.recipes import *
from shaolin.simulator import ShaolinSimulator, attribute_set, skill_set, skills, effects
from shaolin.skills import *
from shaolin.talents import *


def priority_func(self: ShaolinSimulator):
    return [
        (qinlong_skill, lambda: self.channa < 2 and self.effect_list[fumo_effect]),
        (luohan_skill, lambda: self.channa == 3),
        (erye_skill, lambda: (self.effect_list[fumo_effect] and not self.effect_list[qinlong_effect]) or self.effect_list[yeyin_effect] == yeyin_effect.max_layers),

        (hengsao_skill, lambda: self.duration_list[hengsao_dot] < 2 * GCD),

        (nayun_skill, lambda: self.channa > 2 and self.effect_list[nayun_effect] > 1),
        (weituo_skill, lambda: self.channa > 2),

        (zhuoying_skill, lambda: self.tanpo_count == 3 or (
                    self.tanpo_count == 2 and self.channa == 2 and self.effect_list[nayun_effect])),

        (shouque_skill, lambda: self.effect_list[yeyin_shouque_effect] < 2 and self.effect_list[jiasha_effect]),
        (hengsao_skill, lambda: self.effect_list[yeyin_hengsao_effect] < 2 and self.effect_list[jiasha_effect]),

        (pudu_skill,
         lambda: self.effect_list[pudu_effect] < pudu_effect.max_layers or self.duration_list[pudu_effect] < 3 * GCD),
        (shouque_skill, lambda: self.channa == 2 and self.charge[shouque_skill] > 1 and self.duration_list[luohan_effect] > GCD),
        (hengsao_skill, lambda: True),
        (pudu_skill, lambda: True)
    ]


if __name__ == '__main__':
    qixue_list = [mingfa_talent, huanshen_talent, shenyi_talent, suodi_talent, xiangmo_talent, jingang_talent,
                  jingguo_talent, sansheng_talent, zhongchen_talent, huaxiang_talent, foguo_talent, yeyin_talent]
    recipe_list = [(nayun_recipe, (0.12,)),
                   (weituo_recipe, (0.12,)),
                   (shouque_recipe, (0.09, 0.07)),
                   (pudu_recipe, (0.09, 1)),
                   (hengsao_recipe, (0.5, 6)),
                   (bufeng_recipe, (0.25, 1))]

    prepare_skill_list = [luohan_skill, erye_skill, hengsao_skill, hengsao_skill, shouque_skill, weituo_skill,
                          shouque_skill, erye_skill]

    epochs, duration = 1, 306
    buffs = []
    zhenfa = None
    simulator = ShaolinSimulator(skills, effects, prepare_skill_list, False, test, duration,
                                 priority_func=priority_func, talent_list=qixue_list, recipe_list=recipe_list,
                                 skill_set=skill_set, attribute_set=attribute_set, zhenyan=zhenfa, buffs=buffs)
    simulator.simulate(epochs)
    print(simulator.dps)
    for skill, detail in simulator.summary.items():
        print(f"{skill}: {detail}")


    def print_attribute(attribute):
        details = {
            "基础元气": str(attribute.base_spunk),
            "最终元气": str(attribute.spunk),
            "基础攻击": str(attribute.base_magical_attack_power),
            "最终攻击": str(attribute.attack_power),
            "武伤": str(attribute.weapon_damage),
            "基础会心": str(attribute.base_magical_critical_strike),
            "最终会心": str(attribute.critical_strike),
            "基础会效": str(attribute.base_magical_critical_effect),
            "最终会效": str(attribute.critical_effect),
            "基础破防": str(attribute.base_magical_overcome),
            "最终破防": str(attribute.overcome),
            "破招": str(attribute.counter),
            "基础无双": str(attribute.base_strain),
            "最终无双": str(attribute.strain)
        }
        print(details)


    def print_gradient(attribute):
        gradients = {
            "元气": str(attribute.base_spunk.grad),
            "基础": str(attribute.base_magical_attack_power.grad),
            "武伤": str(attribute.weapon_damage.grad),
            "会心": str(attribute.base_magical_critical_strike.grad),
            "会效": str(attribute.base_magical_critical_effect.grad),
            "破防": str(attribute.base_magical_overcome.grad),
            "破招": str(attribute.counter.grad),
            "无双": str(attribute.base_strain.grad)
        }
        print(gradients)


    print_attribute(simulator.attribute)
    print_gradient(simulator.attribute)
