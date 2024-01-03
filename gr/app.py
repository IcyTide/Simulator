import gradio as gr

from gr.components.equipment import build_equipment
from gr.components.consumable import build_consumable
from gr.components.gain import build_gain
from gr.components.talent import build_talent
from gr.components.recipe import build_recipe
from gr.components.combat import build_combat
from gr.components.top import build_top

from gr.scripts.equipment import equipment_script
from gr.scripts.consumable import consumable_script
from gr.scripts.gain import gain_script
from gr.scripts.talent import talent_script
from gr.scripts.recipe import recipe_script
from gr.scripts.combat import combat_script
from gr.scripts.top import top_script

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
