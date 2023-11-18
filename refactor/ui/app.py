import gradio as gr

from ui.components.equipment import build_equipment
from ui.components.consumable import build_consumable
from ui.components.gain import build_gain
from ui.components.talents import build_talent
from ui.components.top import build_top
from ui.scripts.equipment import equipment_script
from ui.scripts.consumable import consumable_script
from ui.scripts.gain import gain_script
from ui.scripts.top import top_script


if __name__ == '__main__':
    with gr.Blocks() as app:
        top_components = build_top()
        with gr.Row(visible=False) as detail:
            # with gr.Tab("配装"):
            #     equipments, enchants, stones, equip_components = build_equipment()
            # with gr.Tab("消耗品"):
            #     consumable_components = build_consumable()
            # with gr.Tab("增益"):
            #     gain_components = build_gain()
            with gr.Tab("奇穴"):
                talent_components = build_talent()
        # top_script(equipments, detail, top_components, equip_components, consumable_components)
        # equipment_script(equipments, enchants, stones, equip_components)
        # consumable_script(consumable_components)
        # gain_script(gain_components)
    app.queue()
    app.launch()
