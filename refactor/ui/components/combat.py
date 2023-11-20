import gradio as gr

from base.constant import SHIELD_BASE_MAP


def build_combat():
    combat_components = {"class_attr": gr.State(), "simulator": gr.State()}
    with gr.Row():
        with gr.Group():
            target_level = gr.Dropdown(choices=list(SHIELD_BASE_MAP), value=list(SHIELD_BASE_MAP)[0], label="目标等级")
            combat_components['target_level'] = target_level
        with gr.Group():
            duration = gr.Number(minimum=1, value=180, label="时长")
            combat_components['duration'] = duration
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("属性"):
                attribute_button = gr.Button("构造属性")
                combat_components['attribute_button'] = attribute_button
                with gr.Row():
                    init_attribute = gr.Textbox(label="增益前属性")
                    combat_components['init_attribute'] = init_attribute
                    gain_attribute = gr.Textbox(label="增益后属性")
                    combat_components['gain_attribute'] = gain_attribute
            with gr.Tab("模拟"):
                simulate_button = gr.Button("请构造属性", interactive=False)
                combat_components['simulate_button'] = simulate_button
                with gr.Column(scale=3):
                    actions = gr.Textbox(label="动作日志")
                    combat_components['actions'] = actions
                with gr.Column(scale=7):
                    events = gr.Textbox(label="事件日志")
                    combat_components['events'] = events
        with gr.Column(scale=3):
            damage = gr.Textbox()

    return combat_components
