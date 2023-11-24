

def analyze_details(iteration, duration, attribute, damage_func, grad_attrs, counts):
    scale = iteration * duration
    result = {}
    total_damage = 0
    grad_results = {attr: 0 for attr in grad_attrs}
    for (attribute_params, damage_params), count in counts.items():
        for attr, value in attribute_params:
            setattr(attribute, attr, value)

        attribute_params = dict(attribute_params)
        damage_params = dict(damage_params)
        for attr, value in grad_attrs.items():
            setattr(attribute, attr, value + attribute_params[attr])
            grad_results[attr] += damage_func(attribute, damage_params)[-1] * count
            setattr(attribute, attr, attribute_params[attr])

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
        details[skill] = {k: round(v / iteration) for k, v in result[skill].items()}

    gradients = {attr: grad_results[attr] / scale - dps for attr, grad_result in grad_results.items()}
    return dps, details, gradients
