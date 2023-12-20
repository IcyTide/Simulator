from collections import defaultdict


def analyze_origin(skill, skill_level, times, count, status, grad_results):
    attribute = status.attribute
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        grad_results[attr] += status.skills[skill].calculate(skill_level, times) * count
        setattr(attribute, attr, origin_value)


def analyze_delta(skill, skill_level, times, count, status, grad_results, delta):
    attribute = status.attribute
    for attr, value in attribute.delta_grad_attrs.items():
        origin_value = getattr(attribute, attr)
        origin_delta = getattr(attribute, attribute.delta_attr)
        setattr(attribute, attr, origin_value + delta / value)
        setattr(attribute, attribute.delta_attr, getattr(attribute, attribute.delta_attr) - delta)
        grad_results[attr] += status.skills[skill].calculate(skill_level, times) * count
        setattr(attribute, attr, origin_value)
        setattr(attribute, attribute.delta_attr, origin_delta)


def refresh_status(gains, existed_gains, status):
    for gain in [gain for gain in existed_gains if gain not in gains]:
        existed_gains.remove(gain)
        status.buffs[gain[0]].remove(gain[1], gain[2])

    for gain in [gain for gain in gains if gain not in existed_gains]:
        existed_gains.append(gain)
        status.buffs[gain[0]].add(gain[1], gain[2])


def analyze_details(iteration, simulator, counts, delta=None):
    scale = iteration * simulator.duration
    status = simulator.status

    result = defaultdict(lambda: {"hit": 0, "critical": 0, "damage": 0})
    total_damage = 0
    grad_results = defaultdict(int)

    existed_gains = []
    for (skill, critical, skill_level, times, gains), count in counts.items():
        refresh_status(gains, existed_gains, status)

        if delta:
            analyze_delta(skill, skill_level, times, count, status, grad_results, delta)
        else:
            analyze_origin(skill, skill_level, times, count, status, grad_results)

        damage = status.skills[skill].calculate(skill_level, times)

        if critical:
            result[skill]["critical"] += count
        else:
            result[skill]["hit"] += count

        result[skill]["damage"] += damage * count
        total_damage += damage * count

    refresh_status([], existed_gains, status)

    dps = total_damage / scale

    details = {}
    for skill in sorted(result, key=lambda x: result[x]['damage'], reverse=True):
        details[skill] = {k: round(v / iteration, 2) for k, v in result[skill].items()}

    gradients = {attr: grad_results[attr] / scale - dps for attr, grad_result in grad_results.items()}
    return dps, details, gradients
