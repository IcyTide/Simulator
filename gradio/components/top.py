import gradio as gr
from gradio.constant import SUPPORT_SCHOOL


def build_top():
    top_components = {}
    school_name = gr.Dropdown(choices=SUPPORT_SCHOOL, label="心法")
    top_components["school_name"] = school_name
    return top_components
