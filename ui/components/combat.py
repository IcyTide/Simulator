import gradio as gr

from base.constant import SHIELD_BASE_MAP


def build_combat():
    combat_components = {"class_attr": gr.State(), "attribute": gr.State(), "simulator": gr.State()}
    with gr.Row():
        with gr.Group():
            target_level = gr.Dropdown(choices=list(SHIELD_BASE_MAP), value=list(SHIELD_BASE_MAP)[0], label="目标等级")
            combat_components['target_level'] = target_level
        with gr.Group():
            duration = gr.Number(minimum=1, value=180, precision=0, label="战斗时长")
            combat_components['duration'] = duration
        with gr.Group():
            iteration = gr.Number(minimum=1, value=1000, precision=0, label="模拟次数")
            combat_components['iteration'] = iteration
    simulate = gr.Button("开始模拟!")
    combat_components['simulate'] = simulate
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("属性"):
                with gr.Row():
                    init_attribute = gr.Textbox(label="增益前属性", lines=20)
                    combat_components['init_attribute'] = init_attribute
                    gain_attribute = gr.Textbox(label="增益后属性", lines=20)
                    combat_components['gain_attribute'] = gain_attribute
            with gr.Tab("统计"):
                summary = gr.Textbox(label="总结", lines=20)
                combat_components['summary'] = summary
        with gr.Column(scale=3):
            dps = gr.Number(label="DPS")
            combat_components['dps'] = dps
            gradient = gr.Textbox(label="属性收益", lines=20)
            combat_components['gradient'] = gradient

    return combat_components
