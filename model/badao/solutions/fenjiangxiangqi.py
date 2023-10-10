from badao.attributes import *
from abstract import wait, divine_effect, divine
from badao.simulator import BadaoSimulator, skill_set, attribute_set, skills, effects
from badao.talents import *
from badao.recipes import shangjiang_recipe, pofu_recipe, daoxiao_recipe, qinlong_recipe
from buff import zuoxuanyouzhuan
from zhenfa import *


# def priority_func(self: BadaoSimulator):
#     return [
#         (xiangqi_skill, lambda: self.effect_list[xiangqi_ready_effect]),
#         (pofu_skill, lambda: self.cd_list[divine] > 8 or not self.cd_list[divine]),
#         (qinlongliuzhan_skill, lambda: self.cd_list[divine] < 8 and self.effect_list[xiangqi_pre_effect] < 6),
#         (daoxiao_skill, lambda: self.duration_list[hanfeng_effect] < 3),
#         (qinlongliuzhan_skill, lambda: True),
#         (shangjiang_skill, lambda: True),
#         (jianbi_skill, lambda: True),
#         (daoxiao_skill, lambda: True)
#     ]
def priority_func(self: BadaoSimulator):
    return [
        (xiangqi_skill, lambda: self.effect_list[xiangqi_ready_effect]),
        (qinlongliuzhan_skill, lambda: not self.cd_list[qinlongliuzhan_skill]),
        (shangjiang_skill, lambda: not self.last_skill == qinlongliuzhan_skill),
        (wait, lambda: self.cd_list[shangjiang_skill] < 1 or self.cd_list[qinlongliuzhan_skill] < 1),
        (daoxiao_skill, lambda: self.duration_list[hanfeng_effect] < 4),
        (jianbi_skill, lambda: True),
        (pofu_skill, lambda: True),
        (wait, lambda: self.cd_list[pofu_skill] < 1),
        (daoxiao_skill, lambda: True)
    ]


def loop_func():
    shang, po, tan, qin, dao = shangjiang_skill, pofu_skill, jianbi_skill, jingyan_skill, daoxiao_skill
    return [shang, po, tan, po, shang, dao, qin, po, shang, po, qin, qin,
            shang, po, dao, po, shang, qin, tan, po, shang, po, dao, qin,
            shang, po, qin, po, shang, dao, qin, po, shang, po, tan, qin,
            shang, po, dao, po, shang, qin, qin, po, shang, po, dao, qin]


if __name__ == '__main__':
    qixue_list = [longxi_talent, guihan_talent, yangguan_talent, shuangtian_talent, jianchen_talent, hanfeng_talent,
                  fenjiang_talent,
                  xinghuo_talent, jueqi_talent, jinghong_talent, zhongyan_talent, xiangqi_talent]
    recipe_list = [(shangjiang_recipe, (0.09, 0.04)),
                   (pofu_recipe, (0.12, 0.04)),
                   (qinlong_recipe, (0.09, 0.04)),
                   (daoxiao_recipe, (0.09, 0.07))]
    buffs = []
    zhenfa = None

    # prepare_skill_list = [daoxiao_skill, naoxumi_skill, jingyan_skill]
    prepare_skill_list = [daoxiao_skill, naoxumi_skill, qinlongliuzhan_skill, jianbi_skill]

    epochs, duration = 1, 186

    simulator = BadaoSimulator(skills, effects, prepare_skill_list, False, my_strain, duration,
                               priority_func=priority_func,
                               # loop_func=loop_func,
                               talent_list=qixue_list, recipe_list=recipe_list,
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
