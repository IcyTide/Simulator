import json

import gradio as gr
import pandas as pd

from base.attribute import Attribute
from ui.constant import SUPPORT_CLASS


def build_top():
    top_components = {}
    class_name = gr.Dropdown(choices=SUPPORT_CLASS, label="心法")
    top_components["class_name"] = class_name
    class_attr = gr.State({})
    top_components["class_attr"] = class_attr
    return top_components
