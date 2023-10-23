from base.buff import Buff


class XiuMingChenShen(Buff):
    name = "秀明尘身"

    duration = 60


class SongYanZhuWu(Buff):
    name = "松烟竹雾"

    duration = 60

    related_skills = []

    def remove(self):
        super(SongYanZhuWu, self).remove()
        for skill in self.related_skills:
            skill.activate = False


class XueXuJinPing(Buff):
    name = "雪絮金屏"

    duration = 60


class JianChen(Buff):
    pass


class HanFeng(Buff):
    related_skills = ["刀啸风吟", "醉斩白蛇", "坚壁清野"]

    def add_effect(self):
        self.status.attribute.physical_critical_strike_gain += 0.05
        self.status.attribute.physical_critical_damage_gain += 0.05
        for skill in self.related_skills:
            self.status.skills[skill].damage_addition_gain += 0.05

    def remove_effect(self):
        self.status.attribute.physical_critical_strike_gain += 0.05
        self.status.attribute.physical_critical_damage_gain += 0.05
        for skill in self.related_skills:
            self.status.skills[skill].damage_addition_gain += 0.05


class XiangQiPrefix(Buff):
    def add_effect(self):
        if self.status.stacks["降麒式-前置"] == 6:
            self.expire()
        self.status.buffs["降麒式-就绪"].refresh()


class XiangQiReady(Buff):
    pass


class XiangQiShi(Buff):
    def add_effect(self):
        self.status.buffs["降麒式-前置"].expire()
        self.status.buffs["降麒式-就绪"].expire()
        self.status.attribute.damage_addition += 0.1



