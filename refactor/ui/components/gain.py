import gradio as gr
from ui.constant import WEAPON_ENCHANTS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WINES, SNACKS


def build_gain():
    attr_state = gr.State()
    gain_state = gr.State()
    consumable_attrs = gr.State({})
    team_gains = gr.JSON({}, visible=False)
    gain_components = {"attr_state": attr_state, "gain_state": gain_state,
                       "consumable_attrs": consumable_attrs, "team_gains": team_gains,
                       "consumables": {}, "teams": {}}
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("Consumable"):
                with gr.Row():
                    with gr.Group():
                        major_food = gr.Dropdown(choices=[""] + list(MAJOR_FOODS), label="辅助类食品")
                        gain_components['consumables']['辅助类食品'] = major_food
                    with gr.Group():
                        minor_food = gr.Dropdown(choices=[""] + list(MINOR_FOODS), label="增强类食品")
                        gain_components['consumables']['增强类食品'] = minor_food
                    with gr.Group():
                        major_potion = gr.Dropdown(choices=[""] + list(MAJOR_POTIONS), label="辅助类药品")
                        gain_components['consumables']['辅助类药品'] = major_potion
                    with gr.Group():
                        minor_potion = gr.Dropdown(choices=[""] + list(MINOR_POTIONS), label="增强类药品")
                        gain_components['consumables']['增强类药品'] = minor_potion
                with gr.Row():
                    with gr.Group():
                        weapon_enchant = gr.Dropdown(choices=[""] + list(WEAPON_ENCHANTS), label="武器磨石")
                        gain_components['consumables']['武器磨石'] = weapon_enchant
                    with gr.Group():
                        wine = gr.Dropdown(choices=[""] + list(WINES), label="家园酒")
                        gain_components['consumables']['家园酒'] = wine
                    with gr.Group():
                        snack = gr.Dropdown(choices=[""] + list(SNACKS), label="家园食物")
                        gain_components['consumables']['家园食物'] = snack
                with gr.Row(equal_height=False):
                    with gr.Group():
                        tong_ze = gr.CheckboxGroup(choices=["同泽宴"], label="同泽宴")
                        gain_components['consumables']['同泽宴'] = tong_ze
                    with gr.Group():
                        streamed_fish = gr.CheckboxGroup(choices=["蒸鱼菜盘"], label="蒸鱼菜盘")
                        gain_components['consumables']['蒸鱼菜盘'] = streamed_fish
                    with gr.Group():
                        spread = gr.Dropdown(choices=["", "水晶芙蓉宴", "玉笛谁家听落梅"], label="宴席")
                        gain_components['consumables']['宴席'] = spread
                    with gr.Group():
                        boiled_fish = gr.Dropdown(choices=["", "炼狱水煮鱼", "百炼水煮鱼"], label="水煮鱼")
                        gain_components['consumables']['水煮鱼'] = boiled_fish

            with gr.Tab("Team Gain"):
                with gr.Tab("七秀"):
                    with gr.Row():
                        xiu_qi = gr.CheckboxGroup(choices=["袖气"], label="袖气")
                        gain_components['teams']['袖气'] = xiu_qi
                        zuo_xuan_you_zhuan_stack = gr.Number(label="左旋右转层数")
                        gain_components['teams']['左旋右转层数'] = zuo_xuan_you_zhuan_stack
                with gr.Tab("天策"):
                    with gr.Row():
                        han_ru_lei = gr.CheckboxGroup(choices=["撼如雷"], label="撼如雷")
                        gain_components['teams']['撼如雷'] = han_ru_lei
                        po_feng = gr.Dropdown(["", "破风", "劲风"], label="破风")
                        gain_components['teams']['破风'] = po_feng
                        cheng_long_jian = gr.CheckboxGroup(choices=["乘龙箭"], label="乘龙箭")
                        gain_components['teams']['乘龙箭'] = cheng_long_jian
                        hao_ling_san_jun_stack = gr.Number(maximum=48, label="号令三军层数")
                        gain_components['teams']['号令三军层数'] = hao_ling_san_jun_stack
                        ji_lei_rate = gr.Number(maximum=100, label="激雷覆盖")
                        gain_components['teams']['激雷覆盖'] = ji_lei_rate
                with gr.Tab("少林"):
                    with gr.Row():
                        li_di_cheng_fo_rate = gr.Number(maximum=100, label="立地成佛覆盖")
                        gain_components['teams']['立地成佛覆盖'] = li_di_cheng_fo_rate
                        she_shen_hong_fa_stack = gr.Number(maximum=36, label="舍身弘法层数")
                        gain_components['teams']['舍身弘法层数'] = she_shen_hong_fa_stack
                        she_shen_hong_fa_rate = gr.Number(maximum=100, label="舍身弘法覆盖")
                        gain_components['teams']['舍身弘法覆盖'] = she_shen_hong_fa_rate
                with gr.Tab("万花"):
                    with gr.Row():
                        qiu_su = gr.CheckboxGroup(choices=["秋肃"], label="秋肃")
                        gain_components['teams']['秋肃'] = qiu_su
                        luo_zi_wu_hui_rate = gr.Number(maximum=100, label="落子无悔覆盖")
                        gain_components['teams']['落子无悔覆盖'] = luo_zi_wu_hui_rate
                with gr.Tab("纯阳"):
                    with gr.Row():
                        sui_xing_chen = gr.CheckboxGroup(choices=["碎星辰"], label="碎星辰")
                        gain_components['teams']['碎星辰'] = sui_xing_chen
                        po_cang_qiong = gr.CheckboxGroup(choices=["破苍穹"], label="破苍穹")
                        gain_components['teams']['破苍穹'] = po_cang_qiong
                with gr.Tab("藏剑"):
                    with gr.Row():
                        jian_feng_bai_duan_rate = gr.CheckboxGroup(choices=["剑锋百锻覆盖"], label="剑锋百锻覆盖")
                        gain_components['teams']['剑锋百锻覆盖'] = jian_feng_bai_duan_rate
                with gr.Tab("五毒"):
                    with gr.Row():
                        shan_you = gr.CheckboxGroup(choices=["善友"], label="善友")
                        gain_components['teams']['善友'] = shan_you
                        xian_wang_gu_ding_rate = gr.Number(maximum=100, label="仙王蛊鼎覆盖")
                        gain_components['teams']['仙王蛊鼎覆盖'] = xian_wang_gu_ding_rate
                with gr.Tab("明教"):
                    with gr.Row():
                        jie_huo = gr.CheckboxGroup(choices=["戒火"], label="戒火")
                        gain_components['teams']['戒火'] = jie_huo
                        lie_ri = gr.CheckboxGroup(choices=["烈日"], label="烈日")
                        gain_components['teams']['烈日'] = lie_ri
                        chao_sheng_yan = gr.Dropdown(["朝圣言", "圣浴明心"], value="朝圣言", label="朝圣言")
                        gain_components['teams']['朝圣言'] = chao_sheng_yan
                        chao_sheng_yan_stack = gr.Number(maximum=24, label="朝圣言层数")
                        gain_components['teams']['朝圣言层数'] = chao_sheng_yan_stack
                        chao_sheng_yan_rate = gr.Number(maximum=100, label="朝圣言覆盖")
                        gain_components['teams']['朝圣言覆盖'] = chao_sheng_yan_rate
                with gr.Tab("丐帮"):
                    with gr.Row():
                        jiu_zhong_xian = gr.CheckboxGroup(choices=["酒中仙"], label="酒中仙")
                        gain_components['teams']['酒中仙'] = jiu_zhong_xian
                with gr.Tab("苍云"):
                    with gr.Row():
                        xu_ruo = gr.CheckboxGroup(choices=["虚弱"], label="虚弱")
                        gain_components['teams']['虚弱'] = xu_ruo
                        zhen_fen_stack = gr.Number(label="振奋层数")
                        gain_components['teams']['振奋层数'] = zhen_fen_stack
                        zhen_fen_rate = gr.Number(maximum=100, label="振奋覆盖")
                        gain_components['teams']['振奋覆盖'] = zhen_fen_rate
                        han_xiao_qian_jun_rate = gr.Number(maximum=100, label="寒啸千军覆盖")
                        gain_components['teams']['寒啸千军覆盖'] = han_xiao_qian_jun_rate
                with gr.Tab("长歌"):
                    with gr.Row():
                        zhuang_zhou_meng_stack = gr.Number(label="庄周梦层数")
                        gain_components['teams']['庄周梦层数'] = zhuang_zhou_meng_stack
                        zhuang_zhou_meng_rate = gr.Number(maximum=100, label="庄周梦覆盖")
                        gain_components['teams']['庄周梦覆盖'] = zhuang_zhou_meng_rate
                with gr.Tab("霸刀"):
                    with gr.Row():
                        shu_kuang_rate = gr.Number(maximum=100, label="疏狂覆盖")
                        gain_components['teams']['疏狂覆盖'] = shu_kuang_rate
                with gr.Tab("药宗"):
                    with gr.Row():
                        piao_huang_rate = gr.Number(maximum=100, label="飘黄覆盖")
                        gain_components['teams']['飘黄覆盖'] = piao_huang_rate
                        pei_wu_rate = gr.Number(maximum=100, label="配伍覆盖")
                        gain_components['teams']['配伍覆盖'] = pei_wu_rate

        with gr.Column(scale=3):
            with gr.Row():
                attrs = gr.Textbox(label="消耗品属性")
                gain_components['attrs'] = attrs
                gains = gr.Textbox(label="团队效果")
                gain_components['gains'] = gains
    with gr.Row():
        consumable_names = gr.Textbox(label="当前消耗品")
        gain_components['consumable_names'] = consumable_names
        team_names = gr.Textbox(label="当前增益")
        gain_components['team_names'] = team_names
    return gain_components
