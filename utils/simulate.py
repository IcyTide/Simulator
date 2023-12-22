import copy
import random
import time
from collections import Counter
from multiprocessing import Pool, cpu_count

from utils.analyze import analyze_details

processes = cpu_count()
min_iteration = processes * 4


def simulate_single(simulator, i):
    random.seed(i)
    return simulator()


def simulate_concurrent(iteration, simulator):
    pool = Pool(processes)
    results = pool.starmap(simulate_single, [(simulator, i) for i in range(iteration)])
    pool.close()
    pool.join()

    total_result = sum(results, Counter())

    return total_result


def simulate_serial(iteration, simulator):
    total_result = Counter()
    for i in range(iteration):
        total_result += simulate_single(copy.deepcopy(simulator), i)
    return total_result


def simulate_delta(iteration, simulator, delta):
    attribute = simulator.status.attribute
    simulate_func = simulate_serial if iteration < min_iteration else simulate_concurrent
    start = time.time()
    origin_result = simulate_func(iteration, simulator)
    cost = time.time() - start

    origin_dps, origin_details, origin_gradients = analyze_details(
        iteration, simulator, origin_result)

    for attr, residual in origin_gradients.items():
        origin_gradients[attr] = (residual, residual / attribute.grad_attrs[attr])

    if delta:
        setattr(attribute, attribute.delta_attr, getattr(attribute, attribute.delta_attr) + delta)
        delta_result = simulate_func(iteration, simulator)
        delta_dps, delta_details, delta_gradients = analyze_details(
            iteration, simulator, delta_result, delta)
        residual_dps = delta_dps - origin_dps
        for attr, residual in delta_gradients.items():
            residual = (residual + residual_dps) / delta * attribute.delta_grad_attrs[attr]
            delta_gradients[attr] = (residual * attribute.grad_attrs[attr], residual)

        return cost, origin_dps, origin_details, origin_gradients, delta_dps, delta_details, delta_gradients
    return cost, origin_dps, origin_details, origin_gradients, 0, {}, {}
