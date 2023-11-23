from base.constant import GRADIENT_DELTA


def analyze(iteration, attribute_class, damage_func, grad_attrs, counts):
    attribute = attribute_class()

    result = {}
    grad_results = {attr: 0 for attr in grad_attrs}
    for (attribute_params, damage_params), count in counts.items():
        for attr, value in attribute_params:
            if attr in grad_attrs:
                setattr(attribute, attr, value + GRADIENT_DELTA)
                grad_results[attr] += damage_func(attribute, damage_params)[-1] * count

            setattr(attribute, attr, value)
            skill, critical, damage = damage_func(attribute, damage_params)

            if skill not in result:
                result[skill] = {"hit": 0, "critical": 0, "damage": 0}
            result[skill]["hit"] += count
            if critical:
                result[skill]["critical"] += count
            result[skill]["damage"] += damage * count

    total_damage = sum(result.values())
    dps = total_damage / iteration

    sorted_result = {}
    for skill in sorted(result, key=lambda x: x['damage'], reverse=True):
        sorted_result[skill] = {k: v / iteration for k, v in result[skill].items()}

    gradients = {attr: sum(grad_result.values()) / iteration - dps for attr, grad_result in grad_results.items()}
    return total_damage, dps, sorted_result, gradients
