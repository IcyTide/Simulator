import gradio as gr
from general import gains
from ui.constant import WEAPON_ENCHANTS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WINES, SNACKS


def build_gain():
    gains_json = gr.JSON({}, visible=False)

    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("Consumable"):
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
                        tong_ze = gr.CheckboxGroup(choices=["同泽宴"], label="同泽宴")
                        streamed_fish = gr.CheckboxGroup(choices=["蒸鱼餐盘"], label="蒸鱼餐盘")
                    with gr.Column(min_width=100):
                        spread = gr.Dropdown(choices=["", "水晶芙蓉宴", "玉笛谁家听落梅"], label="宴席")
                        boiled_fish = gr.Dropdown(choices=["", "炼狱水煮鱼", "百炼水煮鱼"], label="水煮鱼")

            with gr.Tab("Team Gain"):
                with gr.Accordion("七秀"):
                    with gr.Row():
                        xiu_qi = gr.CheckboxGroup(choices=["秀气"], label="秀气")
                        zuo_xuan_you_zhuan = gr.Number(label="左旋右转层数")
                with gr.Accordion("天策"):
                    with gr.Row():
                        hao_ling_san_jun = gr.Number(maximum=48, label="号令三军层数")
                        han_ru_lei = gr.CheckboxGroup(choices=["撼如雷"], label="撼如雷")
                        ji_lei = gr.Number(maximum=100, label="激雷覆盖", visible=False)
                        po_feng = gr.Dropdown(["", "破风", "劲风"], label="破风", visible=False)
                with gr.Accordion("少林"):
                    with gr.Row():
                        she_shen_hong_fa = gr.Number(maximum=36, label="舍身弘法层数")
                        she_shen_hong_fa_num = gr.Number(maximum=100, label="舍身弘法覆盖")
                with gr.Accordion("万花"):
                    with gr.Row():
                        qiu_su = gr.CheckboxGroup(choices=["秋肃"], label="秋肃")
                with gr.Accordion("纯阳"):
                    with gr.Row():
                        sui_xing_chen = gr.CheckboxGroup(choices=["碎星辰"], label="碎星辰")
                with gr.Accordion("藏剑"):
                    with gr.Row():
                        jian_feng_bai_duan = gr.CheckboxGroup(choices=["剑锋百锻"], label="剑锋百锻")
                with gr.Accordion("五毒"):
                    with gr.Row():
                        shan_you = gr.CheckboxGroup(choices=["善友"], label="善友")
                        xian_wang_gu_ding = gr.Number(maximum=100, label="仙王蛊鼎覆盖")
                with gr.Accordion("明教"):
                    with gr.Row():
                        jie_huo = gr.CheckboxGroup(choices=["戒火"], label="戒火")
                        chao_sheng_yan = gr.Dropdown(["", "朝圣言", "圣浴明心"], label="朝圣言")
                        chao_sheng_yan_stacks = gr.Number(maximum=24, label="朝圣言层数")
                        chao_sheng_yan_rate = gr.Number(maximum=100, label="朝圣言覆盖")
                with gr.Accordion("丐帮"):
                    with gr.Row():
                        jiu_zhong_xian = gr.CheckboxGroup(choices=["酒中仙"], label="酒中仙")
                with gr.Accordion("苍云"):
                    with gr.Row():
                        zhen_fen = gr.Number(label="振奋层数")
                        han_xiao_qian_jun = gr.Number(maximum=100, label="寒啸千军覆盖")
                        xu_ruo = gr.CheckboxGroup(choices=["虚弱"], label="虚弱")
                with gr.Accordion("长歌"):
                    with gr.Row():
                        zhuang_zhou_meng = gr.Number(label="庄周梦层数")
                        zhuang_zhou_meng_rate = gr.Number(maximum=100, step=1, label="庄周梦覆盖")
                with gr.Accordion("霸刀"):
                    with gr.Row():
                        shu_kuang = gr.Number(maximum=100, label="疏狂覆盖")
                with gr.Accordion("药宗"):
                    with gr.Row():
                        piao_huang = gr.Number(maximum=100, label="飘黄覆盖")
                        pei_wu = gr.Number(maximum=100, label="配伍覆盖")

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
