import gradio as gr

from ui.components.equipment import build_equipment
from ui.components.gain import build_gain
from ui.components.top import build_top
from ui.scripts.equipment import equipment_script
from ui.scripts.gain import gain_script
from ui.scripts.top import top_script

if __name__ == '__main__':
    with gr.Blocks() as app:
        top_components = build_top()
        with gr.Row(visible=False) as detail:
            with gr.Tab("配装"):
                equipments, enchants, stones, equip_components = build_equipment()
            with gr.Tab("增益"):
                gain_components = build_gain()
        top_script(equipments, detail, top_components, equip_components, gain_components)
        equipment_script(equipments, enchants, stones, equip_components)
        gain_script(gain_components)
    app.queue()
    app.launch()
