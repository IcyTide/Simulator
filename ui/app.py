import gradio as gr


def equipment_component():
    hat_equip = gr.Dropdown()
    jacket_equip = gr.Dropdown()
    belt_equip = gr.Dropdown()
    wrist_equip = gr.Dropdown()
    bottoms_equip = gr.Dropdown()
    shoes_equip = gr.Dropdown()
    necklace_equip = gr.Dropdown()
    pendant_equip = gr.Dropdown()
    ring_1_equip = gr.Dropdown()
    ring_2_equip = gr.Dropdown()
    primary_weapon_equip = gr.Dropdown()
    secondary_weapon_equip = gr.Dropdown()
    tertiary_weapon_equip = gr.Dropdown()

    equipment_dropdowns = [hat_equip, jacket_equip, belt_equip, wrist_equip, bottoms_equip, shoes_equip,
                           necklace_equip, pendant_equip, ring_1_equip, ring_2_equip,
                           primary_weapon_equip, secondary_weapon_equip, tertiary_weapon_equip]


def consumable_component():
    pass


def gains_component():
    pass


