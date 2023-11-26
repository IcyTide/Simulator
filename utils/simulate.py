import random
import time
from multiprocessing import Pool, cpu_count

from base.constant import MINOR_DELTA
from base.simulator import Simulator
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


def simulate_delta(damage_func, attribute_class, iteration, simulator, delta=True):
    attribute = simulator.status.attribute
    start = time.time()
    origin_result = simulate_concurrent(iteration, simulator)
    print(time.time() - start)
    attribute.all_critical_strike_base += MINOR_DELTA
    start = time.time()
    delta_result = simulate_concurrent(iteration, simulator)
    print(time.time() - start)
    start = time.time()
    origin_dps, origin_details, fix_gradients = analyze_details(
        iteration, simulator.duration, damage_func, attribute_class, attribute.fix_grad_attrs, origin_result)
    delta_dps, delta_details, float_gradients = analyze_details(
        iteration, simulator.duration, damage_func, attribute_class, attribute.float_grad_attrs, delta_result)
    print(time.time() - start)
    gradients = {}
    for attr, residual in fix_gradients.items():
        gradients[attr] = (residual, residual / attribute.fix_grad_attrs[attr])
    for attr, residual in float_gradients.items():
        residual = residual + delta_dps - origin_dps
        gradients[attr] = (residual, residual / attribute.float_grad_attrs[attr])

    return origin_dps, origin_details, gradients


def simulate_verbose(damage_func, attribute, skills, buffs, gains, target, duration, prepare, priority, loop):
    simulator = Simulator(attribute, skills, buffs, gains,
                          target, duration, prepare, priority, loop, verbose=True)

    dps, details, _ = analyze_details(1, duration, attribute, damage_func, {}, simulator())

    return dps, details, simulator.actions, simulator.events
