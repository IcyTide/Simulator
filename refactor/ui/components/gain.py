import gradio as gr
from general.gains.team import TEAM_GAINS_NAME


def build_gain():
    gain_state = gr.State()
    team_gains = {}
    gain_components = {"gain_state": gain_state, "formations": {"core_formation": gr.State()}, "teams": {}}
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("阵法增益"):
                with gr.Row(equal_height=False):
                    team_gains['阵法'] = {}
                    with gr.Group():
                        formation = gr.Dropdown(choices=[""], label="阵法")
                        gain_components['formations']['formation'] = formation
                    with gr.Group():
                        formation_rate = gr.Slider(minimum=0, maximum=1, step=0.01, value=1, label="五重覆盖率")
                        gain_components['formations']['formation_rate'] = formation_rate
                    core_rate = gr.Slider(minimum=0, maximum=1, step=0.01, visible=False, label="阵眼覆盖率")
                    gain_components['formations']['core_rate'] = core_rate
            with gr.Tab("团队增益"):
                with gr.Tab("七秀"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["袖气"] = {}
                            xiu_qi = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["袖气"]], label="袖气")
                            gain_components['teams']['袖气'] = xiu_qi
                        with gr.Group():
                            team_gains["左旋右转"] = {}
                            gain_components['teams']['左旋右转'] = {}
                            zuo_xuan_you_zhuan_stack = gr.Slider(minimum=0, maximum=100, step=1,
                                                                 label=TEAM_GAINS_NAME["左旋右转"], info="层数")
                            gain_components['teams']['左旋右转']['层数'] = zuo_xuan_you_zhuan_stack
                with gr.Tab("天策"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["撼如雷"] = {}
                            han_ru_lei = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["撼如雷"]], label="撼如雷")
                            gain_components['teams']['撼如雷'] = han_ru_lei
                        with gr.Group():
                            team_gains["破风"] = {}
                            gain_components['teams']['破风'] = {}
                            po_feng = gr.Dropdown(
                                ["", TEAM_GAINS_NAME["破风(基础)"], TEAM_GAINS_NAME["破风(劲风)"]],
                                label="破风", info="")
                            gain_components['teams']['破风'][''] = po_feng
                        with gr.Group():
                            team_gains["乘龙箭"] = {}
                            cheng_long_jian = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["乘龙箭"]], label="乘龙箭")
                            gain_components['teams']['乘龙箭'] = cheng_long_jian
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["号令三军"] = {}
                            gain_components['teams']['号令三军'] = {}
                            hao_ling_san_jun_stack = gr.Slider(minimum=0, maximum=48, step=1,
                                                               label=TEAM_GAINS_NAME["号令三军"], info="层数")
                            gain_components['teams']['号令三军']['层数'] = hao_ling_san_jun_stack
                        with gr.Group():
                            team_gains["激雷"] = {}
                            gain_components['teams']['激雷'] = {}
                            ji_lei_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                    label=TEAM_GAINS_NAME["激雷"], info="覆盖")
                            gain_components['teams']['激雷']['覆盖'] = ji_lei_rate
                with gr.Tab("少林"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["立地成佛"] = {}
                            gain_components['teams']['立地成佛'] = {}
                            li_di_cheng_fo_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                            label=TEAM_GAINS_NAME["立地成佛"], info="覆盖")
                            gain_components['teams']['立地成佛']['覆盖'] = li_di_cheng_fo_rate
                    with gr.Row(equal_height=False):
                        team_gains["舍身弘法"] = {}
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
                            team_gains["秋肃"] = {}
                            qiu_su = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["秋肃"]], label="秋肃")
                            gain_components['teams']['秋肃'] = qiu_su
                        with gr.Group():
                            team_gains["皎素"] = {}
                            gain_components['teams']['皎素'] = {}
                            luo_zi_wu_hui_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                           label=TEAM_GAINS_NAME["皎素"], info="覆盖")
                            gain_components['teams']['皎素']['覆盖'] = luo_zi_wu_hui_rate
                with gr.Tab("纯阳"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["碎星辰"] = {}
                            sui_xing_chen = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["碎星辰"]], label="碎星辰")
                            gain_components['teams']['碎星辰'] = sui_xing_chen
                        with gr.Group():
                            team_gains["破苍穹"] = {}
                            po_cang_qiong = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["破苍穹"]], label="破苍穹")
                            gain_components['teams']['破苍穹'] = po_cang_qiong
                with gr.Tab("藏剑"):
                    team_gains["剑锋百锻"] = {}
                    gain_components['teams']['剑锋百锻'] = {}
                    jian_feng_bai_duan_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                        label=TEAM_GAINS_NAME["剑锋百锻"], info="覆盖")
                    gain_components['teams']['剑锋百锻']['覆盖'] = jian_feng_bai_duan_rate
                with gr.Tab("五毒"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["善友"] = {}
                            shan_you = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["善友"]], label="善友")
                            gain_components['teams']['善友'] = shan_you
                        with gr.Group():
                            team_gains["仙王蛊鼎"] = {}
                            gain_components['teams']['仙王蛊鼎'] = {}
                            xian_wang_gu_ding_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                               label=TEAM_GAINS_NAME["仙王蛊鼎"], info="覆盖")
                            gain_components['teams']['仙王蛊鼎']['覆盖'] = xian_wang_gu_ding_rate
                with gr.Tab("明教"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["戒火"] = {}
                            jie_huo = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["戒火"]], label="戒火")
                            gain_components['teams']['戒火'] = jie_huo
                        with gr.Group():
                            team_gains["烈日"] = {}
                            lie_ri = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["烈日"]], label="烈日")
                            gain_components['teams']['烈日'] = lie_ri
                        with gr.Group():
                            team_gains["朝圣言"] = {}
                            gain_components['teams']['朝圣言'] = {}
                            chao_sheng_yan = gr.Dropdown(
                                ["", TEAM_GAINS_NAME["朝圣言(基础)"], TEAM_GAINS_NAME["朝圣言(圣浴明心)"]],
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
                    team_gains["酒中仙"] = {}
                    jiu_zhong_xian = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["酒中仙"]], label="酒中仙")
                    gain_components['teams']['酒中仙'] = jiu_zhong_xian
                with gr.Tab("苍云"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["虚弱"] = {}
                            xu_ruo = gr.CheckboxGroup(choices=[TEAM_GAINS_NAME["虚弱"]], label="虚弱")
                            gain_components['teams']['虚弱'] = xu_ruo
                        with gr.Group():
                            team_gains["寒啸千军"] = {}
                            gain_components['teams']['寒啸千军'] = {}
                            han_xiao_qian_jun_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                               label=TEAM_GAINS_NAME["寒啸千军"], info="覆盖")
                            gain_components['teams']['寒啸千军']['覆盖'] = han_xiao_qian_jun_rate
                    with gr.Row(equal_height=False):
                        team_gains["振奋"] = {}
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
                        team_gains["庄周梦"] = {}
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
                    team_gains["疏狂"] = {}
                    gain_components['teams']['疏狂'] = {}
                    shu_kuang_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                               label=TEAM_GAINS_NAME["疏狂"], info="覆盖")
                    gain_components['teams']['疏狂']['覆盖'] = shu_kuang_rate
                with gr.Tab("药宗"):
                    with gr.Row(equal_height=False):
                        with gr.Group():
                            team_gains["飘黄"] = {}
                            gain_components['teams']['飘黄'] = {}
                            piao_huang_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                        label=TEAM_GAINS_NAME["飘黄"], info="覆盖")
                            gain_components['teams']['飘黄']['覆盖'] = piao_huang_rate
                        with gr.Group():
                            team_gains["配伍"] = {}
                            gain_components['teams']['配伍'] = {}
                            pei_wu_rate = gr.Slider(minimum=0, maximum=1, step=0.01,
                                                    label=TEAM_GAINS_NAME["配伍"], info="覆盖")
                            gain_components['teams']['配伍']['覆盖'] = pei_wu_rate

        gain_components["team_gains"] = gr.State(team_gains)
    with gr.Row(equal_height=False):
        team_names = gr.Textbox(label="当前增益")
        gain_components['team_gain_names'] = team_names
    return gain_components
