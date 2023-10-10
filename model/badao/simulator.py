from abstract import Simulator, wait, divine_effect, divine
from badao.talents import *


def attribute_set(attribute):
    attribute.physical_critical_strike_gain += 0.032
    attribute.physical_critical_effect_gain += 0.032


def skill_set():
    shangjiang_skill.k_b += 0.1
    jianchen_dot.k_b += 0.1
    daoxiao_skill.k_b += 0.1


class BadaoSimulator(Simulator):
    def _init(self):
        self.divine_list = divine_list
        if xinghuo_talent in self.talent_list:
            self.attribute.strength_gain += 0.1

    def _cd_timer(self, gap):
        gap = gap * ZHONGYAN_RATE
        if zhongyan_talent in self.talent_list and self.effect_list[chenshen_effect]:
            self.cd_timer(gap)
            self.cd_list[melee] += gap
            self.cd_list[divine] += gap

    def _pre_cast(self, skill):
        if skill in chenshen_list:
            self.add_effect(chenshen_effect)
            self.remove_effect(zhuwu_effect)
            self.remove_effect(jinping_effect)
        elif skill in zhuwu_list:
            self.remove_effect(chenshen_effect)
            self.add_effect(zhuwu_effect)
            self.remove_effect(jinping_effect)
        elif skill in jinping_list:
            self.remove_effect(chenshen_effect)
            self.remove_effect(zhuwu_effect)
            self.add_effect(jinping_effect)

        if skill is qinlongliuzhan_skill:
            self.cast(qinlong_list[self.effect_list[qinlong_effect]])
            self.add_effect(qinlong_effect)

        if skill is shangjiang_skill and jianchen_talent in self.talent_list:
            self.cast(jianchen_dot)
        elif skill is jueqi_skill:
            self.cast(naoxumi_dot)
        elif skill is zuizhan_skill:
            if zhanfen_talent in self.talent_list:
                self.add_effect(zhanfen_effect)

    def _post_cast(self, skill):
        if self.effect_list[divine_effect]:
            self.cd_list[pofu_skill] = 0

        if skill is pofu_skill:
            if self.effect_list[pofu_counter_effect]:
                self.cast(pofu_counter)
                # self.remove_effect(pofu_counter_effect)
            if jinghong_talent in self.talent_list:
                self.cast(jinghong_skill)
            if self.effect_list[divine_effect]:
                self.cast(divine_dot)
                self.add_effect(divine_dot_effect)
        if skill is yangdao_skill:
            self.cast(yangdao_dot)
            if xinjing_talent in self.talent_list:
                self.add_effect(xinjing_effect)

        if skill is qinlongliuzhan_skill and self.effect_list[qinlong_effect] == qinlong_effect.max_layers:
            self.remove_effects(qinlong_effect)

        elif skill is naoxumi_skill:
            self.cast(naoxumi_dot)
        elif skill is xiangqi_skill:
            self.cast(xiangqi_dot)
            self.add_effect(xiangqi_effect)
            self.remove_effects(xiangqi_ready_effect)
        elif skill in qinlong_list:
            self.cast(qinlong_counter)
            self.add_effect(xiangqi_pre_effect)
            if self.effect_list[xiangqi_pre_effect] == xiangqi_pre_effect.max_layers:
                self.remove_effects(xiangqi_pre_effect)
                self.add_effect(xiangqi_ready_effect)

        elif skill is jianbi_skill:
            self.cast(jianbi_dot)
            if xinjing_talent in self.talent_list:
                self.add_effect(xinjing_effect)
        elif skill is daoxiao_skill:
            self.cast(daoxiao_counter)
            self.add_effect(pofu_counter_effect)
            if hanfeng_talent in self.talent_list:
                self.add_effect(hanfeng_effect)

    def _post_damage(self, skill):
        if jueqi_talent in self.talent_list and skill in jueqi_list and self.duration_list[naoxumi_dot] and self.roll(
                JUEQI_RATE):
            self.cast(jueqi_skill)
        if linjiang_talent in self.talent_list and skill in linjiang_list:
            self.cast(linjiang_skill)


skills = [xiangwang_skill, xiangwang_whirl_skill, pofu_skill, shangjiang_skill, pofu_counter,
          naoxumi_skill, naoxumi_dot, jingyan_skill, zhuying_skill, konghe_skill, qifeng_skill, tengjiao_skill,
          qinlong_skill, qinlong_counter, qinlongliuzhan_skill,
          zuizhan_skill, daoxiao_skill, jianbi_skill, jianbi_dot, daoxiao_counter,
          jinghong_skill, linjiang_skill, jueqi_skill, yangdao_skill, yangdao_dot,
          jianchen_dot, xiangqi_skill, xiangqi_dot, divine_dot]
effects = [chenshen_effect, zhuwu_effect, jinping_effect, pofu_counter_effect, hanfeng_effect, zhanfen_effect,
           xiangqi_pre_effect, xiangqi_ready_effect, xiangqi_effect, divine_dot_effect, xinjing_effect, qinlong_effect]
