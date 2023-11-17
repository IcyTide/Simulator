import gradio as gr
from ui.constant import WEAPON_ENCHANTS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WINES, SNACKS
from ui.constant import TEAM_GAINS_NAME


def build_gain():
    attr_state = gr.State()
    gain_state = gr.State()
    consumable_attrs = gr.State({})
    team_gains = gr.State({})
    gain_components = {"attr_state": attr_state, "gain_state": gain_state,
                       "consumable_attrs": consumable_attrs, "team_gains": team_gains,
                       "consumables": {}, "teams": {}}
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("消耗品"):
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
                        weapon_enchant = gr.Dropdown(choices=[""] + list(WEAPON_ENCHANTS), label="武器磨石", scale=1)
                        gain_components['consumables']['武器磨石'] = weapon_enchant
                    with gr.Group():
                        wine = gr.Dropdown(choices=[""] + list(WINES), label="家园酒", scale=2)
                        gain_components['consumables']['家园酒'] = wine
                    with gr.Group():
                        snack = gr.Dropdown(choices=[""] + list(SNACKS), label="家园食物", scale=2)
                        gain_components['consumables']['家园食物'] = snack
                with gr.Row(equal_height=False):
                    with gr.Group():
                        tong_ze = gr.CheckboxGroup(choices=["234破招/无双"], label="同泽宴", scale=1)
                        gain_components['consumables']['同泽宴'] = tong_ze
                    with gr.Group():
                        streamed_fish = gr.CheckboxGroup(choices=["517无双"], label="蒸鱼菜盘", scale=1)
                        gain_components['consumables']['蒸鱼菜盘'] = streamed_fish
                    with gr.Group():
                        spread = gr.Dropdown(choices=["", "水晶芙蓉宴", "玉笛谁家听落梅", "二十四桥明月夜"],
                                             label="宴席", scale=2)
                        gain_components['consumables']['宴席'] = spread
                    with gr.Group():
                        boiled_fish = gr.Dropdown(choices=["", "炼狱水煮鱼(100破招/无双)", "百炼水煮鱼(400破招/无双)"],
                                                  label="水煮鱼", scale=2)
                        gain_components['consumables']['水煮鱼'] = boiled_fish

            with gr.Tab("团队增益"):
                with gr.Tab("七秀"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            xiu_qi = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["袖气"]], label="袖气")
                            gain_components['teams']['袖气'] = xiu_qi
                        with gr.Group():
                            gain_components['teams']['左旋右转'] = {}
                            zuo_xuan_you_zhuan_stack = gr.Slider(minimum=0, maximum=100, step=1,
                                                                 label=TEAM_GAINS_NAME["左旋右转"], info="层数")
                            gain_components['teams']['左旋右转']['层数'] = zuo_xuan_you_zhuan_stack
                with gr.Tab("天策"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            han_ru_lei = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["撼如雷"]], label="撼如雷")
                            gain_components['teams']['撼如雷'] = han_ru_lei
                        with gr.Group():
                            gain_components['teams']['破风'] = {}
                            po_feng = gr.Dropdown(["", TEAM_GAINS_NAME["破风"], TEAM_GAINS_NAME["劲风"]],
                                                  label="破风", info="")
                            gain_components['teams']['破风'][''] = po_feng
                        with gr.Group():
                            cheng_long_jian = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["乘龙箭"]], label="乘龙箭")
                            gain_components['teams']['乘龙箭'] = cheng_long_jian
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            gain_components['teams']['号令三军'] = {}
                            hao_ling_san_jun_stack = gr.Slider(minimum=0, maximum=48, step=1,
                                                               label=TEAM_GAINS_NAME["号令三军"], info="层数")
                            gain_components['teams']['号令三军']['层数'] = hao_ling_san_jun_stack
                        with gr.Group():
                            gain_components['teams']['激雷'] = {}
                            ji_lei_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                    label=TEAM_GAINS_NAME["激雷"], info="覆盖")
                            gain_components['teams']['激雷']['覆盖'] = ji_lei_rate
                with gr.Tab("少林"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            gain_components['teams']['立地成佛'] = {}
                            li_di_cheng_fo_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                            label=TEAM_GAINS_NAME["立地成佛"], info="覆盖")
                            gain_components['teams']['立地成佛']['覆盖'] = li_di_cheng_fo_rate
                    with gr.Row(equal_height=False):
                        gain_components['teams']['舍身弘法'] = {}
                        with gr.Group():
                            she_shen_hong_fa_stack = gr.Slider(minimum=0, maximum=36, step=1,
                                                               label=TEAM_GAINS_NAME["舍身弘法"], info="层数")
                            gain_components['teams']['舍身弘法']['层数'] = she_shen_hong_fa_stack
                        with gr.Group():
                            she_shen_hong_fa_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                              label=TEAM_GAINS_NAME["舍身弘法"], info="覆盖")
                            gain_components['teams']['舍身弘法']['覆盖'] = she_shen_hong_fa_rate
                with gr.Tab("万花"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            qiu_su = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["秋肃"]], label="秋肃")
                            gain_components['teams']['秋肃'] = qiu_su
                        with gr.Group():
                            gain_components['teams']['皎素'] = {}
                            luo_zi_wu_hui_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                           label=TEAM_GAINS_NAME["皎素"], info="覆盖")
                            gain_components['teams']['皎素']['覆盖'] = luo_zi_wu_hui_rate
                with gr.Tab("纯阳"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            sui_xing_chen = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["碎星辰"]], label="碎星辰")
                            gain_components['teams']['碎星辰'] = sui_xing_chen
                        with gr.Group():
                            po_cang_qiong = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["破苍穹"]], label="破苍穹")
                            gain_components['teams']['破苍穹'] = po_cang_qiong
                with gr.Tab("藏剑"):
                    gain_components['teams']['剑锋百锻'] = {}
                    jian_feng_bai_duan_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                        label=TEAM_GAINS_NAME["剑锋百锻"], info="覆盖")
                    gain_components['teams']['剑锋百锻']['覆盖'] = jian_feng_bai_duan_rate
                with gr.Tab("五毒"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            shan_you = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["善友"]], label="善友")
                            gain_components['teams']['善友'] = shan_you
                        with gr.Group():
                            gain_components['teams']['仙王蛊鼎'] = {}
                            xian_wang_gu_ding_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                               label=TEAM_GAINS_NAME["仙王蛊鼎"], info="覆盖")
                            gain_components['teams']['仙王蛊鼎']['覆盖'] = xian_wang_gu_ding_rate
                with gr.Tab("明教"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            jie_huo = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["戒火"]], label="戒火")
                            gain_components['teams']['戒火'] = jie_huo
                        with gr.Group():
                            lie_ri = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["烈日"]], label="烈日")
                            gain_components['teams']['烈日'] = lie_ri
                        with gr.Group():
                            gain_components['teams']['朝圣言'] = {}
                            chao_sheng_yan = gr.Dropdown(["", TEAM_GAINS_NAME["朝圣言"], TEAM_GAINS_NAME["圣浴明心"]],
                                                         label="朝圣言", info="")
                            gain_components['teams']['朝圣言'][''] = chao_sheng_yan
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            chao_sheng_yan_stack = gr.Slider(minimum=0, maximum=24, step=1,
                                                             label="朝圣言", info="层数")
                            gain_components['teams']['朝圣言']['层数'] = chao_sheng_yan_stack
                        with gr.Group():
                            chao_sheng_yan_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                            label="朝圣言", info="覆盖")
                            gain_components['teams']['朝圣言']['覆盖'] = chao_sheng_yan_rate
                with gr.Tab("丐帮"):
                    jiu_zhong_xian = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["酒中仙"]], label="酒中仙")
                    gain_components['teams']['酒中仙'] = jiu_zhong_xian
                with gr.Tab("苍云"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            xu_ruo = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["虚弱"]], label="虚弱")
                            gain_components['teams']['虚弱'] = xu_ruo
                        with gr.Group():
                            gain_components['teams']['寒啸千军'] = {}
                            han_xiao_qian_jun_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                               label=TEAM_GAINS_NAME["寒啸千军"], info="覆盖")
                            gain_components['teams']['寒啸千军']['覆盖'] = han_xiao_qian_jun_rate
                    with gr.Row(equal_height=False):
                        gain_components['teams']['振奋'] = {}
                        with gr.Group():
                            zhen_fen_stack = gr.Slider(minimum=0, maximum=100, step=1,
                                                       label=TEAM_GAINS_NAME["振奋"], info="层数")
                            gain_components['teams']['振奋']['层数'] = zhen_fen_stack
                        with gr.Group():
                            zhen_fen_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                      label=TEAM_GAINS_NAME["振奋"], info="覆盖")
                            gain_components['teams']['振奋']['覆盖'] = zhen_fen_rate
                with gr.Tab("长歌"):
                    with gr.Row(equal_height=False):
                        gain_components['teams']['庄周梦'] = {}
                        with gr.Group():
                            zhuang_zhou_meng_stack = gr.Slider(minimum=0, maximum=150, step=1,
                                                               label=TEAM_GAINS_NAME["庄周梦"], info="层数")
                            gain_components['teams']['庄周梦']['层数'] = zhuang_zhou_meng_stack
                        with gr.Group():
                            zhuang_zhou_meng_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                              label=TEAM_GAINS_NAME["庄周梦"], info="覆盖")
                            gain_components['teams']['庄周梦']['覆盖'] = zhuang_zhou_meng_rate
                with gr.Tab("霸刀"):
                    gain_components['teams']['疏狂'] = {}
                    shu_kuang_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                               label=TEAM_GAINS_NAME["疏狂"], info="覆盖")
                    gain_components['teams']['疏狂']['覆盖'] = shu_kuang_rate
                with gr.Tab("药宗"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            gain_components['teams']['飘黄'] = {}
                            piao_huang_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                        label=TEAM_GAINS_NAME["飘黄"], info="覆盖")
                            gain_components['teams']['飘黄']['覆盖'] = piao_huang_rate
                        with gr.Group():
                            gain_components['teams']['配伍'] = {}
                            pei_wu_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                    label=TEAM_GAINS_NAME["配伍"], info="覆盖")
                            gain_components['teams']['配伍']['覆盖'] = pei_wu_rate

        with gr.Column(scale=3):
            with gr.Row():
                attrs = gr.Textbox(label="消耗品属性")
                gain_components['attrs'] = attrs
                # gains = gr.Textbox(label="团队效果")
                # gain_components['gains'] = gains
    with gr.Row(equal_height=False):
        consumable_names = gr.Textbox(label="当前消耗品")
        gain_components['consumable_names'] = consumable_names
        team_names = gr.Textbox(label="当前增益")
        gain_components['team_gain_names'] = team_names
    return gain_components
