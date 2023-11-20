from ui.constant import RECIPE_GAINS


def recipe_script(recipe_components):
    def update_recipe(n):
        def inner(recipes, recipe_gains):
            if recipes:
                recipe_gains[n] = [{"gain": RECIPE_GAINS[recipe]} for recipe in recipes]
            else:
                recipe_gains[n] = {}
            return recipe_gains

        return inner

    def update_gain(recipe_gains):
        gains = []
        for recipe_gain in recipe_gains:
            if not recipe_gain:
                continue
            gains.extend([gain['gain'] for gain in recipe_gain])

        return gains

    for i, recipe_component in enumerate(recipe_components['recipes']):
        recipe_component.input(
            update_recipe(i), [recipe_component, recipe_components['recipe_gains']], recipe_components['recipe_gains']
        ).then(
            update_gain, recipe_components['recipe_gains'], recipe_components['gain_state']
        )
