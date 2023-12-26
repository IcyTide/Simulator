from base.status import Status
from schools.wen_shui_jue.attribute import WenShuiJue
from schools.wen_shui_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.wen_shui_jue.skills import SKILLS
from schools.wen_shui_jue.buffs import BUFFS
from schools.wen_shui_jue.talents import TALENTS, TALENT_GAINS
from schools.wen_shui_jue.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.buffs["剑气"].increase(30)
    status.skills["剑气衰减"].cast()
    status.buffs["山居剑意"].trigger()


prepare = """
飞来闻踪,夕照雷峰,云飞玉皇,啸日,九溪弥烟,玉虹贯日,黄龙吐翠,啸日,
夕照雷峰,听雷,风来吴山,莺鸣柳,云飞玉皇,夕照雷峰,夕照雷峰,夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇
"""
priority = """
三柴剑法,四季剑法
"""
loop = """
啸日,九溪弥烟,玉虹贯日,黄龙吐翠,啸日,
听雷,夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,莺鸣柳,云飞玉皇,夕照雷峰,夕照雷峰,夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇,夕照雷峰,听雷,
啸日,九溪弥烟,玉虹贯日,黄龙吐翠,啸日,
夕照雷峰,云飞玉皇,听雷,夕照雷峰,飞来闻踪,云飞玉皇,夕照雷峰,夕照雷峰,夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇,夕照雷峰,听雷,
啸日,九溪弥烟,玉虹贯日,黄龙吐翠,啸日,
夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇,云栖松,夕照雷峰,听雷,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇,夕照雷峰,听雷,
啸日,九溪弥烟,玉虹贯日,黄龙吐翠,啸日,
夕照雷峰,云飞玉皇,飞来闻踪,夕照雷峰,听雷,风来吴山,莺鸣柳,云飞玉皇,夕照雷峰,夕照雷峰,夕照雷峰,云飞玉皇,夕照雷峰,听雷,夕照雷峰,云飞玉皇,夕照雷峰,听雷,

云栖松(九溪弥烟:cd>90&山居剑意:stack>0&云飞玉皇:cd>1.4&剑气:stack<60),
飞来闻踪(九溪弥烟:cd>90&山居剑意:stack>0&云飞玉皇:cd<1.4&剑气:stack<60)
"""
