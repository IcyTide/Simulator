import gradio as gr

from general.gains.formation import FORMATION_GAINS, FORMATION_GAIN_NAMES
from general.gains.team import TEAM_GAINS, TEAM_GAINS_NAME


def gain_script(gain_components):
    def update_team_gain_params(team_gain_type, *team_gain_keys):

        def inner(team_gains, *team_gain_values):
            if all(team_gain_values):
                team_gains[team_gain_type] = {
                    "params": "\t".join([f"{k}{v}" for k, v in zip(team_gain_keys, team_gain_values)]),
                    "gain": TEAM_GAINS[team_gain_type](*team_gain_values)}
            else:
                team_gains[team_gain_type] = {}
            return team_gains

        return inner

    def update_team_gain(team_gain_type):
        def inner(team_gains, team_gain):
            if team_gain:
                team_gains[team_gain_type] = {"gain": TEAM_GAINS[team_gain_type]}
            else:
                team_gains[team_gain_type] = {}

            return team_gains

        return inner

    def update_formation(team_gains, core_formation, formation, formation_rate, core_rate):
        if formation:
            params = f"五重覆盖{formation_rate}\t阵眼覆盖{core_rate}" if core_rate else f"五重覆盖{formation_rate}"
            team_gains["阵法"] = {
                "name": f"{FORMATION_GAIN_NAMES[formation]}: {params}",
                "gain": FORMATION_GAINS[formation](formation_rate)
            }
        else:
            team_gains["阵法"] = {}

        return team_gains, gr.update(visible=core_formation == formation)

    def update_formation_rate(team_gains, core_formation, formation, formation_rate, core_rate):
        if formation:
            params = f"五重覆盖{formation_rate}\t阵眼覆盖{core_rate}" if core_rate else f"五重覆盖{formation_rate}"
            team_gains["阵法"] = {
                "name": f"{FORMATION_GAIN_NAMES[formation]}: {params}",
                "gain": FORMATION_GAINS[formation](formation_rate)
            }
        else:
            team_gains["阵法"] = {}

        return team_gains

    def update_gain(team_gains):
        gains = []
        name_texts = []
        for team_gain_type, team_gain in team_gains.items():
            if not team_gain:
                continue
            gains.append(team_gain['gain'])
            if name := team_gain.get('name'):
                name_texts.append(name)
            elif params := team_gain.get('params'):
                name_texts.append(f"{TEAM_GAINS_NAME[team_gain_type]}: {params}")
            else:
                name_texts.append(f"{team_gain_type}: {TEAM_GAINS_NAME[team_gain_type]}")

        return "\n".join(name_texts), gains

    gain_components['formations']['formation'].input(
        update_formation,
        [gain_components['team_gains'], *gain_components['formations'].values()],
        [gain_components['team_gains'], gain_components['formations']['core_rate']],
        trigger_mode="always_last"
    ).then(
        update_gain,
        gain_components['team_gains'],
        [gain_components['team_gain_names'], gain_components['gain_state']],
        trigger_mode="always_last"
    )

    gain_components['formations']['formation_rate'].input(
        update_formation_rate,
        [gain_components['team_gains'], *gain_components['formations'].values()],
        gain_components['team_gains'],
        trigger_mode="always_last"
    ).then(
        update_gain,
        gain_components['team_gains'],
        [gain_components['team_gain_names'], gain_components['gain_state']],
        trigger_mode="always_last"
    )
    gain_components['formations']['core_rate'].input(
        update_formation_rate,
        [gain_components['team_gains'], *gain_components['formations'].values()],
        gain_components['team_gains'],
        trigger_mode="always_last"
    ).then(
        update_gain,
        gain_components['team_gains'],
        [gain_components['team_gain_names'], gain_components['gain_state']],
        trigger_mode="always_last"
    )

    for gain_type, component in gain_components['teams'].items():
        if isinstance(component, dict):
            for sub_component in component.values():
                sub_component.input(
                    update_team_gain_params(gain_type, *component.keys()),
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
                update_team_gain(gain_type),
                [gain_components['team_gains'], component],
                gain_components['team_gains']
            ).then(
                update_gain,
                gain_components['team_gains'],
                [gain_components['team_gain_names'], gain_components['gain_state']]
            )
