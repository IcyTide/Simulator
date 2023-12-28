import gradio as gr

from gradio.constant import MAX_RECIPE_SKILLS, MAX_RECIPES


def build_recipe():
    gain_state = gr.State([])
    recipe_gains = []
    recipe_components = {"gain_state": gain_state, "recipes": []}
    for i in range(MAX_RECIPE_SKILLS):
        recipe_components["recipes"].append(gr.Dropdown(choices=[""], visible=False, multiselect=True,
                                                        max_choices=MAX_RECIPES, label=f"技能{i + 1}"))
        recipe_gains.append([])
    recipe_components["recipe_gains"] = gr.State(recipe_gains)
    return recipe_components
