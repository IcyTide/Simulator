import gradio as gr
from components.equipment import build_equipment


if __name__ == '__main__':
    with gr.Blocks() as app:
        build_equipment()
    app.queue()
    app.launch()
