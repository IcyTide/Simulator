from ui.constant import TALENT_GAINS


def talent_script(talent_components):
    def update_talent(n):
        def inner(talent, talent_gains):
            if talent:
                talent_gains[n] = {"gain": TALENT_GAINS[talent]}
            else:
                talent_gains[n] = {}
            return talent_gains

        return inner

    def update_gain(talent_gains):
        gains = []
        for talent_gain in talent_gains:
            if not talent_gain:
                continue
            gains.append(talent_gain['gain'])

        return gains

    for i, talent_component in enumerate(talent_components['talents']):
        talent_component.input(
            update_talent(i), [talent_component, talent_components['talent_gains']], talent_components['talent_gains']
        ).then(
            update_gain, talent_components['talent_gains'], talent_components['gain_state']
        )
