import copy
from multiprocessing import Pool, cpu_count

from base.simulator import Simulator


def simulate(attribute, skills, buffs, gains, target, duration, prepare, priority, loop):
    simulator = Simulator(attribute, skills, buffs, gains,
                          target, duration, prepare, priority, loop)
    return simulator()


def simulate_concurrent(iteration, attribute, skills, buffs, gains, target, duration, prepare, priority, loop):
    pool = Pool(cpu_count())
    results = []
    for _ in range(iteration):
        results.append(pool.apply_async(simulate, args=(
            copy.deepcopy(attribute), skills, buffs, gains, copy.deepcopy(target), duration, prepare, priority, loop
        )))

    result = {}
    for r in results:
        for k, v in r.get().items():
            if k not in result:
                result[k] = 0
            result[k] += v
    return result
