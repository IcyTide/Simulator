import gradio as gr
from ui.constant import WEAPON_ENCHANTS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WINES, SNACKS


def build_consumable():
    attr_state = gr.State()
    consumable_attrs = {}
    consumable_components = {"attr_state": attr_state, "consumables": {}}
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Row():
                with gr.Group():
                    major_food = gr.Dropdown(choices=[""] + list(MAJOR_FOODS), label="辅助类食品")
                    consumable_components['consumables']['辅助类食品'] = major_food
                    consumable_attrs["辅助类食品"] = {}
                with gr.Group():
                    minor_food = gr.Dropdown(choices=[""] + list(MINOR_FOODS), label="增强类食品")
                    consumable_components['consumables']['增强类食品'] = minor_food
                    consumable_attrs["增强类食品"] = {}
                with gr.Group():
                    major_potion = gr.Dropdown(choices=[""] + list(MAJOR_POTIONS), label="辅助类药品")
                    consumable_components['consumables']['辅助类药品'] = major_potion
                    consumable_attrs["辅助类药品"] = {}
                with gr.Group():
                    minor_potion = gr.Dropdown(choices=[""] + list(MINOR_POTIONS), label="增强类药品")
                    consumable_components['consumables']['增强类药品'] = minor_potion
                    consumable_attrs["增强类药品"] = {}
            with gr.Row():
                with gr.Group():
                    weapon_enchant = gr.Dropdown(choices=[""] + list(WEAPON_ENCHANTS), label="武器磨石", scale=1)
                    consumable_components['consumables']['武器磨石'] = weapon_enchant
                    consumable_attrs["武器磨石"] = {}
                with gr.Group():
                    snack = gr.Dropdown(choices=[""] + list(SNACKS), label="家园食物", scale=2)
                    consumable_components['consumables']['家园食物'] = snack
                    consumable_attrs["家园食物"] = {}
                with gr.Group():
                    wine = gr.Dropdown(choices=[""] + list(WINES), label="家园酒", scale=2)
                    consumable_components['consumables']['家园酒'] = wine
                    consumable_attrs["家园酒"] = {}
            with gr.Row(equal_height=False):
                with gr.Group():
                    tong_ze = gr.CheckboxGroup(choices=["234破招/无双"], label="同泽宴", scale=1)
                    consumable_components['consumables']['同泽宴'] = tong_ze
                    consumable_attrs["同泽宴"] = {}
                with gr.Group():
                    streamed_fish = gr.CheckboxGroup(choices=["517无双"], label="蒸鱼菜盘", scale=1)
                    consumable_components['consumables']['蒸鱼菜盘'] = streamed_fish
                    consumable_attrs["蒸鱼菜盘"] = {}
                with gr.Group():
                    spread = gr.Dropdown(choices=["", "水晶芙蓉宴", "玉笛谁家听落梅", "二十四桥明月夜"],
                                         label="宴席", scale=2)
                    consumable_components['consumables']['宴席'] = spread
                    consumable_attrs["宴席"] = {}
                with gr.Group():
                    boiled_fish = gr.Dropdown(choices=["", "炼狱水煮鱼(100破招/无双)", "百炼水煮鱼(400破招/无双)"],
                                              label="水煮鱼", scale=2)
                    consumable_components['consumables']['水煮鱼'] = boiled_fish
                    consumable_attrs["水煮鱼"] = {}

        consumable_components["consumable_attrs"] = gr.State(consumable_attrs)
        
        with gr.Column(scale=3):
            with gr.Row():
                attrs = gr.Textbox(label="消耗品属性")
                consumable_components['attrs'] = attrs
                # gains = gr.Textbox(label="团队效果")
                # consumable_components['gains'] = gains
    with gr.Row(equal_height=False):
        consumable_names = gr.Textbox(label="当前消耗品")
        consumable_components['consumable_names'] = consumable_names
    return consumable_components
