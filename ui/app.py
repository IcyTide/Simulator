import gradio as gr

from ui.components.equipment import build_equipment
from ui.components.consumable import build_consumable
from ui.components.gain import build_gain
from ui.components.talent import build_talent
from ui.components.recipe import build_recipe
from ui.components.combat import build_combat
from ui.components.top import build_top

from ui.scripts.equipment import equipment_script
from ui.scripts.consumable import consumable_script
from ui.scripts.gain import gain_script
from ui.scripts.talent import talent_script
from ui.scripts.recipe import recipe_script
from ui.scripts.combat import combat_script
from ui.scripts.top import top_script

if __name__ == '__main__':
    with gr.Blocks(title="Ango Simulator") as app:
        top_components = build_top()
        with gr.Row(visible=False) as detail:
            with gr.Tab("配装"):
                equipments, enchants, stones, equip_components = build_equipment()
            with gr.Tab("消耗品"):
                consumable_components = build_consumable()
            with gr.Tab("增益"):
                gain_components = build_gain()
            with gr.Tab("奇穴"):
                talent_components = build_talent()
            with gr.Tab("秘籍"):
                recipe_components = build_recipe()
            with gr.Tab("战斗"):
                combat_components = build_combat()

        top_script(equipments, detail, top_components, combat_components,
                   equip_components, consumable_components, gain_components, talent_components, recipe_components)
        equipment_script(equipments, enchants, stones, equip_components)
        consumable_script(consumable_components)
        gain_script(gain_components)
        talent_script(talent_components)
        recipe_script(recipe_components)
        combat_script(combat_components,
                      equip_components, consumable_components, gain_components, talent_components, recipe_components)
    app.queue()
    app.launch(server_name="0.0.0.0", inbrowser=True)
