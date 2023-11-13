import gradio as gr
from general import gains
from ui.constant import WEAPON_ENCHANTS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WINES, SNACKS


def build_gain():
    gains_json = gr.JSON({})

    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("消耗品"):
                with gr.Row():
                    with gr.Group():
                        major_food = gr.Dropdown(choices=[""] + list(MAJOR_FOODS), label="辅助类食品")
                    with gr.Group():
                        minor_food = gr.Dropdown(choices=[""] + list(MINOR_FOODS), label="增强类食品")
                    with gr.Group():
                        major_potion = gr.Dropdown(choices=[""] + list(MAJOR_POTIONS), label="辅助类药品")
                    with gr.Group():
                        minor_potion = gr.Dropdown(choices=[""] + list(MINOR_POTIONS), label="增强类药品")
                with gr.Row(equal_height=False):
                    with gr.Group():
                        weapon_enchant = gr.Dropdown(choices=[""] + list(WEAPON_ENCHANTS), label="武器磨石")
                    with gr.Group():
                        wine = gr.Dropdown(choices=[""] + list(WINES), label="家园酒")
                    with gr.Group():
                        snack = gr.Dropdown(choices=[""] + list(SNACKS), label="家园食物")
                    with gr.Column(min_width=100):
                        tong_ze = gr.Checkbox(label="同泽宴")
                        streamed_fish = gr.Checkbox(label="蒸鱼餐盘")
                    with gr.Column(min_width=100):
                        spread = gr.Dropdown(choices=["", "水晶芙蓉宴", "玉笛谁家听落梅"], label="宴席")
                        boiled_fish = gr.Dropdown(choices=["", "炼狱水煮鱼", "百炼水煮鱼"], label="水煮鱼")

            with gr.Tab("T/奶增益"):
                with gr.Row(equal_height=False):
                    with gr.Group():
                        han_ru_lei = gr.Checkbox(label="撼如雷")
                        xiu_qi = gr.Checkbox(label="秀气")
                    po_feng = gr.Dropdown(["", "破风", "劲风"], label="破风")
                    xu_ruo = gr.Dropdown(["", "盾飞"], label="虚弱")
                    vulnerable = gr.Dropdown(["", "戒火", "秋肃"], label="易伤")
                with gr.Row(equal_height=False):
                    with gr.Group():
                        hao_ling_san_jun = gr.Number(maximum=48, label="号令三军层数")
                    with gr.Group():
                        she_shen_hong_fa = gr.Number(maximum=36, label="舍身弘法层数")
                        she_shen_hong_fa_num = gr.Number(maximum=2, label="舍身弘法数量")
                    with gr.Group():
                        chao_sheng_yan = gr.Dropdown(["", "朝圣言", "圣浴明心"], label="朝圣言")
                        chao_sheng_yan_cd = gr.Number(minimum=120, maximum=300, value=180, label="朝圣言冷却")
                    with gr.Group():
                        chao_sheng_yan_stacks = gr.Number(maximum=24, label="朝圣言层数")
                        chao_sheng_yan_num = gr.Number(maximum=15, label="朝圣言数量")
                    with gr.Group():
                        zhen_fen = gr.Number(label="振奋层数")
                        han_xiao_qian_jun = gr.Number(maximum=2, label="寒啸千军数量")
                with gr.Row(equal_height=False):
                    with gr.Group():
                        zuo_xuan_you_zhuan = gr.Number(label="左旋右转层数")
                    with gr.Group():
                        xian_wang_gu_ding = gr.Number(maximum=5, label="仙王蛊鼎数量")
                    with gr.Group():
                        zhuang_zhou_meng = gr.Number(label="庄周梦层数")
                        zhuang_zhou_meng_rate = gr.Number(maximum=100, step=1, label="庄周梦覆盖")
                    with gr.Group():
                        piao_huang = gr.Number(maximum=2, label="飘黄数量")
                        pei_wu = gr.Number(maximum=100, step=1, label="配伍覆盖")

            with gr.Tab("DPS增益"):
                with gr.Row():
                    with gr.Group():
                        sui_xing_chen = gr.Checkbox(label="碎星辰")
                        jiu_zhong_xian = gr.Checkbox(label="酒中仙")
                        jian_feng_bai_duan = gr.Checkbox(label="剑锋百锻")
                        shan_you = gr.Checkbox(label="善友")
                    with gr.Group():
                        ji_lei = gr.Number(maximum=5, label="激雷数量")
                    with gr.Row():
                        shu_kuang = gr.Number(maximum=4, label="疏狂数量")
                        shu_kuang_cd = gr.Number(minimum=40, maximum=50, value=48, label="疏狂冷却")

        with gr.Column(scale=3):
            gain_box = gr.Textbox(label="当前增益")

        def consumable_func(name, mapping):
            def inner(x, gains_dict):
                if x:
                    gains_dict[name] = mapping[x]
                return gains_dict
            return inner
        major_food.input(consumable_func("辅助类食品", MAJOR_FOODS), [major_food, gains_json], gains_json)
        minor_food.input(consumable_func("增强类食品", MAJOR_FOODS), [minor_food, gains_json], gains_json)
        major_potion.input(consumable_func("辅助类药品", MAJOR_FOODS), [major_potion, gains_json], gains_json)
        minor_potion.input(consumable_func("增强类药品", MAJOR_FOODS), [minor_potion, gains_json], gains_json)
        weapon_enchant.input(consumable_func("武器磨石", MAJOR_FOODS), [weapon_enchant, gains_json], gains_json)
        wine.input(consumable_func("家园酒", WINES), [wine, gains_json], gains_json)
        snack.input(consumable_func("家园食物", SNACKS), [snack, gains_json], gains_json)
        wine.input(consumable_func("家园酒", WINES), [wine, gains_json], gains_json)
