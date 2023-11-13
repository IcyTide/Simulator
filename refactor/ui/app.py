import gradio as gr
from ui.components.equipment import build_equipment
from ui.components.gain import build_gain

if __name__ == '__main__':
    with gr.Blocks() as app:
        with gr.Tab("配装"):
            attribute, gains = build_equipment()
        with gr.Tab("增益"):
            build_gain(attribute, gains)
    app.queue()
    app.launch()
