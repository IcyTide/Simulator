import gradio as gr

from base.constant import SHIELD_BASE_MAP


def build_combat():
    combat_components = {"class_attr": gr.State(), "simulator": gr.State()}
    with gr.Row():
        with gr.Group():
            target_level = gr.Dropdown(choices=list(SHIELD_BASE_MAP), value=list(SHIELD_BASE_MAP)[0], label="目标等级")
            combat_components['target_level'] = target_level
        with gr.Group():
            duration = gr.Number(minimum=1, value=300, precision=0, label="时长")
            combat_components['duration'] = duration
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
            with gr.Tab("日志"):
                with gr.Row():
                    with gr.Column(scale=4):
                        actions = gr.Textbox(label="动作日志", autoscroll=False, lines=20)
                        combat_components['actions'] = actions
                    with gr.Column(scale=6):
                        events = gr.Textbox(label="事件日志", autoscroll=False, lines=20)
                        combat_components['events'] = events
        with gr.Column(scale=3):
            dps = gr.Number(label="DPS")
            combat_components['dps'] = dps
            summary = gr.Textbox(label="战斗总结", lines=20)
            combat_components['summary'] = summary

    return combat_components
