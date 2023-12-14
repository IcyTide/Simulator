import gradio as gr

from base.constant import SHIELD_BASE_MAP


def build_combat():
    combat_components = {"school_attr": gr.State(), "attribute": gr.State(), "simulator": gr.State()}
    with gr.Row():
        with gr.Group():
            target_level = gr.Dropdown(choices=list(SHIELD_BASE_MAP), value=list(SHIELD_BASE_MAP)[0], label="目标等级")
            combat_components['target_level'] = target_level
        with gr.Group():
            duration = gr.Number(minimum=1, value=180, precision=0, label="战斗时长")
            combat_components['duration'] = duration
        with gr.Group():
            iteration = gr.Number(minimum=1, value=1000, precision=0, label="模拟次数")
            combat_components['iteration'] = iteration
        with gr.Group():
            delta_value = gr.Number(value=0, precision=0, label="残差会心(如果会心影响技能数)")
            combat_components['delta_value'] = delta_value
    simulate = gr.Button("开始模拟!")
    combat_components['simulate'] = simulate
    with gr.Row():
        with gr.Column(scale=7):
            with gr.Tab("属性"):
                with gr.Row():
                    init_attribute = gr.Textbox(label="增益前属性", lines=20)
                    combat_components['init_attribute'] = init_attribute
                    gain_attribute = gr.Textbox(label="增益后属性", lines=20)
                    combat_components['gain_attribute'] = gain_attribute
            with gr.Tab("统计"):
                summary = gr.Textbox(label="总结", lines=20)
                combat_components['summary'] = summary
                delta_summary = gr.Textbox(label="残差总结", lines=20, visible=False)
                combat_components['delta_summary'] = delta_summary
            with gr.Tab("序列"):
                combat_components['sequences'] = {}
                prepare = gr.Textbox(label="预备序列")
                combat_components['sequences']['prepare'] = prepare
                priority = gr.Textbox(label="优先级序列")
                combat_components['sequences']['priority'] = priority
                loop = gr.Textbox(label="循环序列", lines=20)
                combat_components['sequences']['loop'] = loop
        with gr.Column(scale=3):
            with gr.Row():
                dps = gr.Number(label="DPS")
                combat_components['dps'] = dps
                delta_dps = gr.Number(label="残差DPS", visible=False)
                combat_components['delta_dps'] = delta_dps
            gradient = gr.Textbox(label="属性收益", lines=10)
            combat_components['gradient'] = gradient
            delta_gradient = gr.Textbox(label="残差收益", lines=10, visible=False)
            combat_components['delta_gradient'] = delta_gradient

    return combat_components
