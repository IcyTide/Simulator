import torch

spirit = 8000


# 1
def suixingchen(attribute):
    attribute.physical_critical_effect_gain += 0.1


def jiuzhongxian(attribute):
    attribute.physical_critical_strike_gain += 0.1


# 2
def hanrulei(attribute):
    attribute.physical_attack_power_gain += 0.05


def xiuqi(attribute):
    with torch.no_grad():
        attribute.strength += 111


# 3
def zuoxuanyouzhuan(attribute):
    with torch.no_grad():
        attribute.counter += spirit / 100 * 54


def zhuangzhoumeng(attribute):
    with torch.no_grad():
        attribute.strain += spirit / 100 * 60


def xianwangguding(attribute):
    attribute.k_d += 0.12


# 4
def haolingsanjun(attribute, vitality):
    with torch.no_grad():
        attribute.strain += max(48, vitality / 1230) * 440


def sheshenhongfa(attribute, vitality):
    with torch.no_grad():
        attribute.strain += max(36, vitality / 1500) * 400


def zhenfen(attribute, parry):
    with torch.no_grad():
        attribute.base_physical_overcome += parry / 1500 * 60
        attribute.base_magical_overcome += parry / 1500 * 60


def hanxiaoqianjun(attribute):
    attribute.physical_overcome_gain += 0.2
    attribute.magical_overcome_gain += 0.2


# 奶歌楯100点根骨加60无双
# 奶秀左旋右转100根骨54破招
# 奶毒鼎 直接提高12%伤害，持续25s，两分钟cd
# 奶花秋肃6%易伤顶戒火