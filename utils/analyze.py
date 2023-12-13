import math


def analyze_details(
        iteration, duration, damage_func, attribute_class, grad_attrs, counts, delta_value=None):
    scale = iteration * duration
    attribute = attribute_class()
    result = {}
    total_damage = 0
    grad_results = {attr: 0 for attr in grad_attrs}
    for (attribute_params, damage_params), count in counts.items():
        for attr, value in attribute_params:
            setattr(attribute, attr, value)

        attribute_params = dict(attribute_params)
        damage_params = dict(damage_params)

        for attr, value in grad_attrs.items():
            origin_value = attribute_params.get(attr, 0)
            if delta_value:
                setattr(attribute, attr, origin_value + delta_value / value)
                setattr(attribute, attribute.delta_attr, getattr(attribute, attribute.delta_attr) - delta_value)
                grad_results[attr] += damage_func(attribute, damage_params)[-1] * count
                setattr(attribute, attr, origin_value)
                setattr(attribute, attribute.delta_attr, attribute_params.get(attribute.delta_attr, 0))
            else:
                setattr(attribute, attr, origin_value + value)
                grad_results[attr] += damage_func(attribute, damage_params)[-1] * count
                setattr(attribute, attr, origin_value)

        skill, critical, damage = damage_func(attribute, damage_params)

        if skill not in result:
            result[skill] = {"hit": 0, "critical": 0, "damage": 0}

        if critical:
            result[skill]["critical"] += count
        else:
            result[skill]["hit"] += count

        result[skill]["damage"] += damage * count
        total_damage += damage * count

    dps = total_damage / scale

    details = {}
    for skill in sorted(result, key=lambda x: result[x]['damage'], reverse=True):
        details[skill] = {k: round(v / iteration, 2) for k, v in result[skill].items()}

    gradients = {attr: grad_results[attr] / scale - dps for attr, grad_result in grad_results.items()}
    return dps, details, gradients
