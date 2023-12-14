import gradio as gr
from ui.constant import SUPPORT_SCHOOL


def build_top():
    top_components = {}
    class_name = gr.Dropdown(choices=SUPPORT_SCHOOL, label="心法")
    top_components["class_name"] = class_name
    return top_components
