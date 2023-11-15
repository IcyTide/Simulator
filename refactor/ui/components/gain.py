import gradio as gr
from general import gains
from ui.constant import WEAPON_ENCHANTS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WINES, SNACKS


def build_gain():
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
                with gr.Tab("七秀"):
                    with gr.Row():
                        xiu_qi = gr.CheckboxGroup(choices=["秀气"], label="秀气")
                        zuo_xuan_you_zhuan_stack = gr.Number(label="左旋右转层数")
                with gr.Tab("天策"):
                    with gr.Row():
                        han_ru_lei = gr.CheckboxGroup(choices=["撼如雷"], label="撼如雷")
                        po_feng = gr.Dropdown(["", "破风", "劲风"], label="破风")
                        cheng_long_jian = gr.CheckboxGroup(choices=["乘龙箭"], label="乘龙箭")
                        hao_ling_san_jun_stack = gr.Number(maximum=48, label="号令三军层数")
                        ji_lei_rate = gr.Number(maximum=100, label="激雷覆盖")
                with gr.Tab("少林"):
                    with gr.Row():
                        li_di_cheng_fo_rate = gr.Number(maximum=100, label="立地成佛覆盖")
                        she_shen_hong_fa_stack = gr.Number(maximum=36, label="舍身弘法层数")
                        she_shen_hong_fa_rate = gr.Number(maximum=100, label="舍身弘法覆盖")
                with gr.Tab("万花"):
                    with gr.Row():
                        qiu_su = gr.CheckboxGroup(choices=["秋肃"], label="秋肃")
                        luo_zi_wu_hui_rate = gr.Number(maximum=100, label="落子无悔覆盖")
                with gr.Tab("纯阳"):
                    with gr.Row():
                        sui_xing_chen = gr.CheckboxGroup(choices=["碎星辰"], label="碎星辰")
                        po_cang_qiong = gr.CheckboxGroup(choices=["破苍穹"], label="破苍穹")
                with gr.Tab("藏剑"):
                    with gr.Row():
                        jian_feng_bai_duan_rate = gr.CheckboxGroup(choices=["剑锋百锻"], label="剑锋百锻")
                with gr.Tab("五毒"):
                    with gr.Row():
                        shan_you = gr.CheckboxGroup(choices=["善友"], label="善友")
                        xian_wang_gu_ding_rate = gr.Number(maximum=100, label="仙王蛊鼎覆盖")
                with gr.Tab("明教"):
                    with gr.Row():
                        jie_huo = gr.CheckboxGroup(choices=["戒火"], label="戒火")
                        lie_ri = gr.CheckboxGroup(choices=["烈日"], label="烈日")
                        chao_sheng_yan = gr.Dropdown(["", "朝圣言", "圣浴明心"], label="朝圣言")
                        chao_sheng_yan_stack = gr.Number(maximum=24, label="朝圣言层数")
                        chao_sheng_yan_rate = gr.Number(maximum=100, label="朝圣言覆盖")
                with gr.Tab("丐帮"):
                    with gr.Row():
                        jiu_zhong_xian = gr.CheckboxGroup(choices=["酒中仙"], label="酒中仙")
                with gr.Tab("苍云"):
                    with gr.Row():
                        xu_ruo = gr.CheckboxGroup(choices=["虚弱"], label="虚弱")
                        zhen_fen_stack = gr.Number(label="振奋层数")
                        zhen_fen_rate = gr.Number(maximum=100, label="振奋覆盖")
                        han_xiao_qian_jun_rate = gr.Number(maximum=100, label="寒啸千军覆盖")
                with gr.Tab("长歌"):
                    with gr.Row():
                        zhuang_zhou_meng_stack = gr.Number(label="庄周梦层数")
                        zhuang_zhou_meng_rate = gr.Number(maximum=100, label="庄周梦覆盖")
                with gr.Tab("霸刀"):
                    with gr.Row():
                        shu_kuang_rate = gr.Number(maximum=100, label="疏狂覆盖")
                with gr.Tab("药宗"):
                    with gr.Row():
                        piao_huang_rate = gr.Number(maximum=100, label="飘黄覆盖")
                        pei_wu_rate = gr.Number(maximum=100, label="配伍覆盖")

        with gr.Column(scale=3):
            gain_box = gr.Textbox(label="当前增益")
