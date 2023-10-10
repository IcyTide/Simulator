from abstract import Simulator, divine, melee
from constants import FLOAT_POINT
from shaolin.skills import weituo_skill, nayun_skill, channa_gain_list, channa_lost_list, erye_skill, fumo_effect, \
    jiasha_effect, pudu_skill, pudu_effect, hengsao_skill, hengsao_dot, bufeng_skill, bufeng_effect, counter, \
    shouque_skill, luohan_skill, luohan_effect, qianjin_skill, zhuoying_skill, qinlong_skill, qinlong_effect, \
    tanpo_effect, tanpo_break_list, tanpo_list
from shaolin.talents import xiangmo_weituo_skill, xiangmo_nayun_skill, sansheng_talent, zhongchen_talent, \
    zhongchen_effect, longzhao_list, longzhao_skill, rilun_effect, zhongchen_list, shenyi_talent, shenyi_effect, \
    rilun_talent, fenyun_talent, fenyun_wuqu_effect, fenyun_wushe_effect, rilun_list, rilun_skill, sansheng_effect, \
    bingxin_list, bingxin_talent, suodi_effect, suodi_talent, suodi_list, suodi_skill, xiangmo_talent, jingguo_talent, \
    jingguo_list, nayun_effect, yeyin_talent, yeyin_pre_effect, yeyin_map, yeyin_effect, guobao_effect, zhuyin_map, \
    guobao_list, guobao_map, yeyin_shouque_effect, yeyin_hengsao_effect, zhuyin_shouque_effect, zhuyin_hengsao_effect, \
    guobao_shouque_skill, guobao_hengsao_skill, foguo_talent, foguo_list, foguo_skill


def attribute_set(attribute):
    attribute.magical_critical_strike_gain += 0.032
    attribute.magical_critical_effect_gain += 0.032


def skill_set():
    weituo_skill.k_b += 0.1
    xiangmo_weituo_skill.k_b += 0.1
    nayun_skill.k_b += 0.1
    xiangmo_nayun_skill.k_b += 0.1


class ShaolinSimulator(Simulator):
    def _init(self):
        self.priority = self.priority_func(self)
        self.max_channa = 3
        self.channa = self.max_channa
        self.rilun_list = set()
        self.rilun_list_size = 2
        self.bingxin_list = set()
        self.bing_list_size = 3
        self.tanpo_count = 0

    @property
    def available(self):
        available = {}
        for skill, cd in self.cd_list.items():
            available[skill] = (skill is qianjin_skill and (
                    self.effect_list[fenyun_wuqu_effect] or self.effect_list[fenyun_wushe_effect])) or (
                                           skill in [divine, melee] or self.frame_duration == self.frame) and (
                                       not skill.gcd or not self.gcd) and (
                                       self.overdraw[skill] > 0 or self.charge[skill] > 0)
        return available

    def _duration_timer(self, gap):
        if self.duration_list[qinlong_effect] and not self.duration_list[qinlong_effect] % 1.5:
            self.add_channa()

    def _pre_cast(self, skill):
        if xiangmo_talent in self.talent_list:
            if skill is weituo_skill:
                self.cast(xiangmo_weituo_skill)
            if skill is nayun_skill:
                self.cast(xiangmo_nayun_skill)

    def add_channa(self, num=1):
        self.channa = min(self.channa + num, self.max_channa)
        if sansheng_talent in self.talent_list:
            self.add_effects(sansheng_effect, num)

    def remove_channa(self):
        self.channa = 0
        if sansheng_talent in self.talent_list:
            self.remove_effects(sansheng_effect)

    def _pre_damage(self, skill):
        pass

    def _post_cast(self, skill):
        if skill in tanpo_break_list:
            self.tanpo_count = 0
        if skill in tanpo_list:
            self.tanpo_count += 1
        if self.tanpo_count == 4:
            self.remove_effects(tanpo_effect)
            self.tanpo_count = 0

        if suodi_talent in self.talent_list and self.effect_list[suodi_effect] and skill in suodi_list:
            self.cast(suodi_skill)
            self.remove_effects(suodi_effect)
        if foguo_talent in self.talent_list and self.effect_list[luohan_effect]:
            if skill in foguo_list and self.roll(0.7):
                self.cast(foguo_skill)
        if skill in channa_lost_list:
            self.remove_channa()
            if suodi_talent in self.talent_list and self.roll(0.5):
                self.add_effect(suodi_effect)
        if skill in channa_gain_list:
            self.add_channa()

        if jingguo_talent in self.talent_list and skill in jingguo_list and self.roll(0.3):
            self.add_effect(nayun_effect)

        if self.effect_list[rilun_effect]:
            if skill in longzhao_list:
                self.cast(longzhao_skill)
            if skill in rilun_list:
                self.rilun_list.add(skill)
                if len(self.rilun_list) == self.rilun_list_size:
                    self.cast(rilun_skill)
                    self.remove_effects(rilun_effect)
                    self.rilun_list = set()
        if bingxin_talent in self.talent_list and skill in bingxin_list:
            self.bingxin_list.add(skill)
            if len(self.bingxin_list) == self.bing_list_size:
                self.bingxin_list = set()
                self.add_effect(nayun_effect)

        if yeyin_talent in self.talent_list:
            if self.effect_list[yeyin_pre_effect]:
                if self.effect_list[yeyin_effect] <= 4 and skill in yeyin_map:
                    self.add_effect(yeyin_map[skill])
                    self.add_effect(yeyin_effect)
                    self.remove_effect(yeyin_pre_effect)
                    self.cd_list[erye_skill] = round(self.cd_list[erye_skill] - 10, FLOAT_POINT)
                    self.cd_list[skill] = 0
            if self.effect_list[guobao_effect] and skill in guobao_list:
                for zhuyin in guobao_map:
                    if self.effect_list[zhuyin]:
                        self.cast(guobao_map[zhuyin])
                self.add_channa()
                self.remove_effect(guobao_effect)
                if not self.effect_list[guobao_effect]:
                    for yeyin, zhuyin in zhuyin_map.items():
                        self.remove_effects(yeyin)
                        self.remove_effects(zhuyin)

        if skill is erye_skill:
            if self.effect_list[jiasha_effect]:
                self.remove_effects(jiasha_effect)
                self.add_effect(fumo_effect)
                self.add_channa(self.max_channa)
                if yeyin_talent in self.talent_list:
                    self.add_effects(guobao_effect, self.effect_list[yeyin_effect])
                    self.remove_effects(yeyin_effect)
                    for yeyin in zhuyin_map:
                        if self.effect_list[yeyin] >= 2:
                            self.add_effect(zhuyin_map[yeyin])
            else:
                self.remove_effects(fumo_effect)
                self.add_effect(jiasha_effect)
                if yeyin_talent in self.talent_list:
                    self.add_effect(yeyin_pre_effect)
                    self.cd_list[hengsao_skill] = 0
                    self.cd_list[shouque_skill] = 0

        elif skill is pudu_skill:
            self.add_effect(pudu_effect)
        elif skill is weituo_skill:
            self.cast(counter)
            self.add_effect(tanpo_effect)
        elif skill is hengsao_skill:
            self.cast(hengsao_dot)
            if zhongchen_talent in self.talent_list:
                self.add_effect(zhongchen_effect)
        elif skill is bufeng_skill:
            self.add_effect(bufeng_effect)
        elif skill is zhuoying_skill:
            self.remove_effects(bufeng_effect)
        elif skill is nayun_skill:
            self.cast(counter)
            self.add_effect(tanpo_effect)
            self.remove_effect(nayun_effect)
        elif skill is shouque_skill and shenyi_talent in self.talent_list:
            self.add_effect(shenyi_effect)

        elif skill is luohan_skill:
            self.add_effect(luohan_effect)
        elif skill is qianjin_skill:
            if rilun_talent in self.talent_list:
                self.add_effect(rilun_effect)
                self.rilun_list = set()
            if fenyun_talent in self.talent_list:
                if self.effect_list[fenyun_wushe_effect]:
                    self.remove_effects(fenyun_wushe_effect)
                    self.cd_list[qianjin_skill] = round(self.cd_list[qianjin_skill] - qianjin_skill.cd, FLOAT_POINT)
                    self.add_channa()
                elif self.effect_list[fenyun_wuqu_effect]:
                    self.remove_effects(fenyun_wuqu_effect)
                    self.cd_list[qianjin_skill] = round(self.cd_list[qianjin_skill] - qianjin_skill.cd, FLOAT_POINT)
                    self.add_effect(fenyun_wushe_effect)
                    self.add_channa()
                else:
                    self.add_effect(fenyun_wuqu_effect)

        elif skill is qinlong_skill:
            self.add_channa(self.max_channa)
            self.add_effect(qinlong_effect)

    def _epoch_init(self):
        pass


skills = [counter, pudu_skill, weituo_skill, hengsao_skill, hengsao_dot, bufeng_skill, zhuoying_skill, nayun_skill,
          shouque_skill, luohan_skill, erye_skill, qianjin_skill, qinlong_skill, suodi_skill, xiangmo_weituo_skill,
          xiangmo_nayun_skill, longzhao_skill, rilun_skill, guobao_shouque_skill, guobao_hengsao_skill, foguo_skill]
effects = [pudu_effect, bufeng_effect, luohan_effect, fumo_effect, jiasha_effect, qinlong_effect, nayun_effect,
           fenyun_wuqu_effect, fenyun_wushe_effect, suodi_effect, sansheng_effect, zhongchen_effect, rilun_effect,
           yeyin_pre_effect, yeyin_effect, yeyin_shouque_effect, yeyin_hengsao_effect, zhuyin_shouque_effect,
           zhuyin_hengsao_effect, guobao_effect, tanpo_effect, shenyi_effect]
