import gradio as gr

from ui.constant import MAX_TALENTS


def build_talent():
    gain_state = gr.State()
    talent_gains = {}
    talent_components = {"gain_state": gain_state, "talents": {}}
    with gr.Row():
        for i in range(MAX_TALENTS // 2):
            with gr.Group():
                talent_components["talents"][i] = gr.Dropdown(choices=[""], value="", label=f"第{i + 1}层")
                talent_gains[i] = {}
    with gr.Row():
        for i in range(MAX_TALENTS // 2, MAX_TALENTS):
            with gr.Group():
                talent_components["talents"][i] = gr.Dropdown(choices=[""], value="", label=f"第{i + 1}层")
                talent_gains[i] = {}
    talent_components['talent_gains'] = gr.State(talent_gains)
    return talent_components
