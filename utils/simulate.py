import random
from multiprocessing import Pool, cpu_count

from utils.analyze import analyze_details

processes = cpu_count()


def simulate_single(simulator, i):
    random.seed(i)
    return simulator()


def simulate_concurrent(iteration, simulator):
    pool = Pool(processes)
    results = pool.starmap(simulate_single, [(simulator, i) for i in range(iteration)])
    pool.close()
    pool.join()

    total_result = {}
    for result in results:
        for k, v in result.items():
            if k not in total_result:
                total_result[k] = 0
            total_result[k] += v

    return total_result


def simulate_delta(damage_func, attribute_class, iteration, simulator, delta_value):
    attribute = simulator.status.attribute
    origin_result = simulate_concurrent(iteration, simulator)
    origin_dps, origin_details, origin_gradients = analyze_details(
        iteration, simulator.duration, damage_func, attribute_class, attribute.grad_attrs, origin_result)

    for attr, residual in origin_gradients.items():
        origin_gradients[attr] = (residual, residual / attribute.grad_attrs[attr])

    if delta_value:
        setattr(attribute, attribute.delta_attr, getattr(attribute, attribute.delta_attr) + delta_value)
        delta_result = simulate_concurrent(iteration, simulator)
        delta_dps, delta_details, delta_gradients = analyze_details(
            iteration, simulator.duration, damage_func, attribute_class, attribute.delta_grad_attrs, delta_result,
            delta_value)
        residual_dps = delta_dps - origin_dps
        for attr, residual in delta_gradients.items():
            residual = (residual + residual_dps) / delta_value * attribute.delta_grad_attrs[attr]
            delta_gradients[attr] = (residual * attribute.grad_attrs[attr], residual)

        return origin_dps, origin_details, origin_gradients, delta_dps, delta_details, delta_gradients
    return origin_dps, origin_details, origin_gradients, 0, {}, {}
