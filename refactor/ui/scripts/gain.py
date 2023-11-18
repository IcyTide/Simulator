import gradio as gr

from ui.constant import TEAM_GAINS, TEAM_GAINS_NAME


def gain_script(gain_components):
    def team_gain_params_update(team_gain_type, *team_gain_keys):
        def inner(team_gains, *team_gain_values):
            if all(team_gain_values):
                team_gains[team_gain_type] = {
                    "param": "\t".join([f"{k}{v}" for k, v in zip(team_gain_keys, team_gain_values)]),
                    "gain": TEAM_GAINS[team_gain_type](*team_gain_values)}
            else:
                team_gains[team_gain_type] = {}
            return team_gains

        return inner

    def team_gain_checkbox_update(team_gain_type):
        def inner(team_gains, team_gain):
            if team_gain:
                team_gains[team_gain_type] = {"gain": TEAM_GAINS[team_gain_type]}
            else:
                team_gains[team_gain_type] = {}

            return team_gains

        return inner

    def update_gain(team_gains):
        gains = []
        name_texts = []
        for team_gain_type, team_gain in team_gains.items():
            if not team_gain:
                continue
            gains.append(team_gain['gain'])
            if param := team_gain.get('param'):
                name_texts.append(f"{TEAM_GAINS_NAME[team_gain_type]}: {param}")
            else:
                name_texts.append(f"{team_gain_type}: {TEAM_GAINS_NAME[team_gain_type]}")

        return "\n".join(name_texts), gains

    for team, component in gain_components['teams'].items():
        if isinstance(component, dict):
            for sub_component in component.values():
                sub_component.input(
                    team_gain_params_update(team, *component.keys()),
                    [gain_components['team_gains'], *component.values()],
                    gain_components['team_gains'],
                    trigger_mode="always_last"
                ).then(
                    update_gain,
                    gain_components['team_gains'],
                    [gain_components['team_gain_names'], gain_components['gain_state']],
                    trigger_mode="always_last"
                )
        elif isinstance(component, gr.CheckboxGroup):
            component.input(
                team_gain_checkbox_update(team),
                [gain_components['team_gains'], component],
                gain_components['team_gains']
            ).then(
                update_gain,
                gain_components['team_gains'],
                [gain_components['team_gain_names'], gain_components['gain_state']]
            )
