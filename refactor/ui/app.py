import gradio as gr
from ui.components.equipment import build_equipment


if __name__ == '__main__':
    with gr.Blocks() as app:
        with gr.Tab("配装"):
            build_equipment()
    app.queue()
    app.launch()
