import copy
import json
import random
from functools import lru_cache

from tqdm import tqdm

import torch
from constants import *

random.seed(2023)


class Attribute:
    def __init__(self, base_agility=0, agility_gain=1, base_spunk=0, spunk_gain=1, base_strength=0, strength_gain=1,
                 base_spirit=0, spirit_gain=1,
                 base_physical_attack_power=0, physical_attack_power_gain=1, base_magical_attack_power=0,
                 magical_attack_power_gain=1,
                 base_physical_critical_strike=0, physical_critical_strike_gain=0, base_magical_critical_strike=0,
                 magical_critical_strike_gain=0,
                 base_physical_critical_effect=0, physical_critical_effect_gain=0, base_magical_critical_effect=0,
                 magical_critical_effect_gain=0,
                 base_physical_overcome=0, physical_overcome_gain=1, base_magical_overcome=0, magical_overcome_gain=1,
                 base_strain=0, strain_gain=0, haste=0, weapon_damage=0, counter=0, ignore_defense=0, target_level=121,
                 k_b=0, k_c=0, k_d=0):
        self.base_agility = torch.tensor(base_agility, dtype=torch.float32, requires_grad=True)
        self.agility_gain = agility_gain
        self.base_spunk = torch.tensor(base_spunk, dtype=torch.float32, requires_grad=True)
        self.spunk_gain = spunk_gain
        self.base_strength = torch.tensor(base_strength, dtype=torch.float32, requires_grad=True)
        self.strength_gain = strength_gain
        self.base_spirit = torch.tensor(base_spirit, dtype=torch.float32, requires_grad=True)
        self.spirit_gain = spirit_gain

        self.base_physical_attack_power = torch.tensor(base_physical_attack_power, dtype=torch.float32,
                                                       requires_grad=True)
        self.physical_attack_power_gain = physical_attack_power_gain
        self.base_magical_attack_power = torch.tensor(base_magical_attack_power, dtype=torch.float32,
                                                      requires_grad=True)
        self.magical_attack_power_gain = magical_attack_power_gain

        self.base_physical_critical_strike = torch.tensor(base_physical_critical_strike, dtype=torch.float32,
                                                          requires_grad=True)
        self.physical_critical_strike_gain = physical_critical_strike_gain
        self.base_magical_critical_strike = torch.tensor(base_magical_critical_strike, dtype=torch.float32,
                                                         requires_grad=True)
        self.magical_critical_strike_gain = magical_critical_strike_gain

        self.base_physical_critical_effect = torch.tensor(base_physical_critical_effect, dtype=torch.float32,
                                                          requires_grad=True)
        self.physical_critical_effect_gain = physical_critical_effect_gain
        self.base_magical_critical_effect = torch.tensor(base_magical_critical_effect, dtype=torch.float32,
                                                         requires_grad=True)
        self.magical_critical_effect_gain = magical_critical_effect_gain

        self.base_physical_overcome = torch.tensor(base_physical_overcome, dtype=torch.float32, requires_grad=True)
        self.physical_overcome_gain = physical_overcome_gain
        self.base_magical_overcome = torch.tensor(base_magical_overcome, dtype=torch.float32, requires_grad=True)
        self.magical_overcome_gain = magical_overcome_gain

        self.base_strain = torch.tensor(base_strain, dtype=torch.float32, requires_grad=True)
        self.strain_gain = strain_gain

        self.haste = haste
        self.weapon_damage = torch.tensor(weapon_damage, dtype=torch.float32, requires_grad=True)
        self.counter = torch.tensor(counter, dtype=torch.float32, requires_grad=True)

        self.target_defense = DEFENSE_COF[target_level][1]
        self.defense_scale = DEFENSE_COF[target_level][0]
        self.suppress = DEFENSE_COF[target_level][2]
        self.ignore_defense = ignore_defense

        self.k_b = k_b
        self.k_c = k_c
        self.k_d = k_d

        self.k_npc = 0
        self.k_counter = 0

    @property
    def gcd(self):
        # self.haste
        return 1.44

    @property
    def agility(self):
        return self.base_agility * self.agility_gain

    @property
    def spunk(self):
        return self.base_spunk * self.spunk_gain

    @property
    def strength(self):
        return self.base_strength * self.strength_gain

    @property
    def spirit(self):
        return self.base_spirit * self.spirit_gain

    @property
    def physical_attack_power(self):
        return (self.base_physical_attack_power + self.strength * 0.15) * self.physical_attack_power_gain

    @property
    def magical_attack_power(self):
        return (self.base_magical_attack_power + self.spunk * 0.18) * self.magical_attack_power_gain

    @property
    def attack_power(self):
        raise NotImplementedError

    @property
    def physical_critical_strike(self):
        return (
                self.base_physical_critical_strike + self.agility * 0.64) / CRITICAL_STRIKE_SCALE + self.physical_critical_strike_gain

    @property
    def magical_critical_strike(self):
        return (
                self.base_magical_critical_strike + + self.spirit * 0.64) / CRITICAL_STRIKE_SCALE + self.magical_critical_strike_gain

    @property
    def critical_strike(self):
        raise NotImplementedError

    @property
    def physical_critical_effect(self):
        return 1.75 + self.base_physical_critical_effect / CRITICAL_EFFECT_SCALE + self.physical_critical_effect_gain

    @property
    def magical_critical_effect(self):
        return 1.75 + self.base_magical_critical_effect / CRITICAL_EFFECT_SCALE + self.magical_critical_effect_gain

    @property
    def critical_effect(self):
        raise NotImplementedError

    @property
    def physical_overcome(self):
        return (self.base_physical_overcome + self.strength * 0.3) / OVERCOME_SCALE * self.physical_overcome_gain

    @property
    def magical_overcome(self):
        return (self.base_magical_overcome + self.spunk * 0.3) / OVERCOME_SCALE * self.magical_overcome_gain

    @property
    def overcome(self):
        raise NotImplementedError

    @property
    def strain(self):
        return self.base_strain / STRAIN_SCALE + self.strain_gain

    def scale_gradient(self):
        if self.base_agility.grad:
            self.base_agility.grad *= 1
        if self.base_spunk.grad:
            self.base_spunk.grad *= 1
        if self.base_strength.grad:
            self.base_strength.grad *= 1
        if self.base_spirit.grad:
            self.base_spirit.grad *= 1

        if self.base_physical_attack_power.grad:
            self.base_physical_attack_power.grad *= 2
        if self.base_magical_attack_power.grad:
            self.base_magical_attack_power.grad *= 2

        if self.base_physical_critical_strike.grad:
            self.base_physical_critical_strike.grad *= 4.45
        if self.base_magical_critical_strike.grad:
            self.base_magical_critical_strike.grad *= 4.45

        if self.base_physical_critical_effect.grad:
            self.base_physical_critical_effect.grad *= 4.45
        if self.base_magical_critical_effect.grad:
            self.base_magical_critical_effect.grad *= 4.45

        if self.base_physical_overcome.grad:
            self.base_physical_overcome.grad *= 4.45
        if self.base_magical_overcome.grad:
            self.base_magical_overcome.grad *= 4.45

        if self.base_strain.grad:
            self.base_strain.grad *= 4.45
        if self.counter.grad:
            self.counter.grad *= 4.45
        if self.weapon_damage.grad:
            self.weapon_damage.grad *= 220 / 73


class Skill:
    def __init__(self, name, cast_time=0, period=0, duration=0, max_duration=0, direct=False,
                 periods=None, cd=0, gcd=False, cast=False, snapshot=False, charge=1, overdraw=1,
                 base_damage=0, weapon_damage_cof=0, attack_power_cof=0, critical_strike=0, critical_effect=0,
                 k_b=0, k_c=0, k_d=0, k_npc=0, increasing_k_b=0, increasing_k_c=0, increasing_k_d=0,
                 ignore_defense=0):
        self.name = name
        self.cast_time = cast_time
        self.period = period
        self.duration = duration
        self.max_duration = max_duration if max_duration else duration
        self.periods = periods
        self.direct = direct
        self.cd = cd
        self.gcd = gcd
        self.cast = cast
        self.snapshot = snapshot
        self.charge = charge
        self.overdraw = overdraw

        self.base_damage = base_damage
        self.weapon_damage_cof = weapon_damage_cof
        self.attack_power_cof = attack_power_cof
        self.critical_strike = critical_strike
        self.critical_effect = critical_effect

        self.k_b = k_b
        self.k_c = k_c
        self.k_d = k_d
        self.k_npc = k_npc
        self.increasing_k_b = increasing_k_b
        self.increasing_k_c = increasing_k_c
        self.increasing_k_d = increasing_k_d

        self.ignore_defense = ignore_defense

    @property
    def times(self):
        return len(self.clips)

    @property
    def clips(self):
        if self.periods:
            return self.periods
        clips = []
        if self.duration:
            duration = self.duration + MINIMUM_TIME
            if self.direct:
                clips.append(self.duration)
            while duration > self.period:
                duration = round(duration - self.period, FLOAT_POINT)
                clips.append(duration)
        elif not self.period:
            clips.append(self.cast_time)
        else:
            cast_time = self.cast_time
            if self.direct:
                clips.append(0)
            while cast_time >= self.period:
                clips.append(self.period)
                cast_time = round(cast_time - self.period, FLOAT_POINT)
        return clips

    def critical(self, attribute):
        dice = random.random()
        critical_strike = attribute.critical_strike + self.critical_strike
        if dice < critical_strike:
            return True
        return False

    def hit_damage(self, attribute, increasing_k_b, increasing_k_c, increasing_k_d):
        target_defence = attribute.target_defense * (1 - self.ignore_defense - attribute.ignore_defense)

        defense_rate = target_defence / (attribute.defense_scale + target_defence)

        k_b = attribute.k_b + self.k_b + increasing_k_b
        k_c = attribute.k_c + self.k_c + increasing_k_c
        k_d = attribute.k_d + self.k_d + increasing_k_d
        k_npc = attribute.k_npc + self.k_npc
        base_damage = self.base_damage
        base_damage += attribute.attack_power * self.attack_power_cof
        base_damage += attribute.weapon_damage * self.weapon_damage_cof
        base_damage *= (1 + attribute.overcome) * (1 + attribute.strain) * (1 - defense_rate)

        base_damage *= (1 + k_b) * (1 + k_c) * (1 + k_d) * (1 + k_npc)
        hit_damage = base_damage * attribute.suppress
        return hit_damage

    def critical_damage(self, attribute, increasing_k_b, increasing_k_c, increasing_k_d):
        critical_effect = attribute.critical_effect + self.critical_effect
        return self.hit_damage(attribute, increasing_k_b, increasing_k_c, increasing_k_d) * critical_effect

    def expect_damage(self, attribute: Attribute, increasing_k_b, increasing_k_c, increasing_k_d):
        critical_strike = attribute.critical_strike + self.critical_strike

        expect_damage = self.critical_damage(attribute, increasing_k_b, increasing_k_c,
                                             increasing_k_d) * critical_strike
        expect_damage += self.hit_damage(attribute, increasing_k_b, increasing_k_c, increasing_k_d) * (
                1 - critical_strike)
        return expect_damage

    def __repr__(self):
        return self.name

    def __call__(self, attribute: Attribute, expect=True):
        damages = []
        for i in range(self.times):
            if expect:
                damage = self.expect_damage(attribute, self.increasing_k_b * i, self.increasing_k_c * i,
                                            self.increasing_k_d * i)
            else:
                critical = self.critical(attribute)
                if self.critical(attribute):
                    damage = self.critical_damage(attribute, self.increasing_k_b * i, self.increasing_k_c * i,
                                                  self.increasing_k_d * i)
                else:
                    damage = self.hit_damage(attribute, self.increasing_k_b * i, self.increasing_k_c * i,
                                             self.increasing_k_d * i)
                damage = (critical, damage)
            damages.append(damage)
        return damages


class Counter(Skill):
    def __init__(self, name, counter_cof, **args):
        self.counter_cof = counter_cof
        super().__init__(name, **args)

    def hit_damage(self, attribute: Attribute, increasing_k_b, increasing_k_c, increasing_k_d):
        target_defence = attribute.target_defense * (1 - self.ignore_defense - attribute.ignore_defense)

        defense_rate = target_defence / (attribute.defense_scale + target_defence)

        k_b = attribute.k_b + self.k_b + increasing_k_b
        k_c = attribute.k_c + self.k_c + increasing_k_c
        k_d = attribute.k_d + self.k_d + increasing_k_d
        k_npc = attribute.k_npc + self.k_npc
        k_counter = attribute.k_counter

        base_damage = self.counter_cof * attribute.counter
        base_damage *= (1 + k_b) * (1 + k_c) * (1 + k_d) * (1 + k_npc) * (1 + k_counter)

        base_damage *= (1 + attribute.overcome) * (1 + attribute.strain)

        hit_damage = base_damage * (1 - defense_rate) * attribute.suppress
        return hit_damage


class Effect:
    def __init__(self, name, period=0, periods=None, duration=0, max_duration=0, layer=1, max_layers=0,
                 apply=None, revoke=None):
        self.name = name
        self.period = period
        self.periods = periods
        self.duration = duration
        self.max_duration = max_duration if max_duration else duration
        self.layer = layer
        self.max_layers = max_layers if max_layers else layer
        self.apply = apply
        self.revoke = revoke

    def __repr__(self):
        return self.name


wait = Skill("wait")
divine = Skill("divine", cd=30)
divine_effect = Effect("divine_effect", duration=8)
melee = Skill("melee", weapon_damage_cof=1, attack_power_cof=0.1, cd=GCD)
base_skills = [wait, divine, melee]
base_effects = [divine_effect]


class Simulator:
    def __init__(self, skills, effects, prepare_skill_list, divine_tag, attribute, duration, frame=0.06,
                 priority_func=None, loop_func=None, talent_list=[], recipe_list=[], attribute_set=None, skill_set=None, zhenyan=None,
                 buffs=[]):
        self.skills = base_skills + skills
        self.effects = base_effects + effects

        self.prepare_skill_list = prepare_skill_list
        self.divine_tag = divine_tag
        self.attribute = attribute
        self.duration = duration
        self.frame = frame

        self.priority_func = priority_func
        self.priority = self.priority_func(self) if self.priority_func else None
        self.loop_func = loop_func
        self.loop = self.loop_func() if self.loop_func else None
        self.divine_list = None
        self.talent_list = talent_list
        self.recipe_list = recipe_list

        self.gcd = None
        self.frame_duration = None

        self.current_time = None
        self.current_skill = None
        self.last_skill = None

        self._init()

        if skill_set:
            skill_set()
        if attribute_set:
            attribute_set(self.attribute)
        if zhenyan:
            zhenyan(self.attribute)

        for buff in buffs:
            buff(self.attribute)

        for func in self.talent_list:
            func()
        for func, args in self.recipe_list:
            func(*args)

        self.cd_list = {}
        self.duration_list = {}
        self.effect_list = {}
        self.snapshots = {}

        self._overdraw = {}

        self.skill_count = {}
        self.cast_seq = []
        self.cast_seqs = []
        self.action_seq = []
        self.action_seqs = []

    def _init(self):
        pass

    @property
    def available(self):
        available = {}
        for skill, cd in self.cd_list.items():
            available[skill] = (skill in [divine, melee] or self.frame_duration == self.frame) and (
                    not skill.gcd or not self.gcd) and (self.overdraw[skill] or self.charge[skill])
        return available

    @property
    def overdraw(self):
        for skill, cd in self.cd_list.items():
            if not cd:
                self._overdraw[skill] = skill.overdraw
        return self._overdraw

    @property
    def charge(self):
        charge = {}
        for skill, cd in self.cd_list.items():
            if not cd or not skill.cd:
                charge[skill] = skill.charge
            else:
                charge[skill] = max(0, skill.charge - cd // skill.cd - 1)
        return charge

    @property
    def total_damage(self) -> torch.Tensor:
        total_damage = 0
        for e in self.action_seq:
            total_damage += e[-1]
        return total_damage

    @property
    def dps(self) -> torch.Tensor:
        return self.total_damage / self.duration

    @property
    def summary(self):
        details = {}
        for _, skill_name, damage in self.action_seq:
            if skill_name not in details:
                details[skill_name] = {"damage": 0, "times": 0}
            details[skill_name]["times"] += 1
            details[skill_name]["damage"] += damage.item()
        for skill_name, detail in details.items():
            detail["rate"] = round(detail["damage"] / self.total_damage.item() * 100, FLOAT_POINT)
            detail["damage"] = round(detail["damage"], FLOAT_POINT)

        return details

    @staticmethod
    def roll(rate):
        dice = random.random()
        if dice < rate:
            return True
        return False

    def divine(self):
        if self.available[divine] and self.roll(self.attribute.divine_rate):
            self.cast(divine)
            self.add_effect(divine_effect)

    def melee(self):
        if self.available[melee] and not self.duration_list[melee]:
            self.cast(melee)

    def _cd_timer(self, gap):
        pass

    def _duration_timer(self, gap):
        pass

    def cd_timer(self, gap):
        for skill, cd in self.cd_list.items():
            if cd:
                self.cd_list[skill] = max(0, round(self.cd_list[skill] - gap, FLOAT_POINT))

    def duration_timer(self, gap):
        for entity, duration in self.duration_list.items():
            if duration:
                self.duration_list[entity] = max(0, round(duration - gap, FLOAT_POINT))
                if isinstance(entity, Skill) and entity.base_damage and duration in entity.clips:
                    self.damage(entity, entity.clips.index(duration))
            else:
                if isinstance(entity, Effect):
                    self.remove_effects(entity)

    def frame_timer(self, gap):
        if self.frame_duration:
            self.frame_duration = max(0, round(self.frame_duration - gap, FLOAT_POINT))

    def gcd_timer(self, gap):
        if self.gcd:
            self.gcd = max(0, round(self.gcd - gap, FLOAT_POINT))

    def _timer(self, gap):
        self._cd_timer(gap)
        self._duration_timer(gap)

    def timer(self, gap):
        while gap > 0:
            self.current_time = round(self.current_time + MINIMUM_TIME, FLOAT_POINT)
            self.gcd_timer(MINIMUM_TIME)
            self.frame_timer(MINIMUM_TIME)
            self.cd_timer(MINIMUM_TIME)
            self.duration_timer(MINIMUM_TIME)
            self._timer(MINIMUM_TIME)
            self.melee()
            gap = round(gap - MINIMUM_TIME, FLOAT_POINT)

    def pre_cast(self, skill):
        self.cd_list[skill] += skill.cd
        self.overdraw[skill] -= 1

        if skill.gcd:
            self.gcd = GCD
        if skill.snapshot:
            self.snapshots[skill] = skill(self.attribute)
        if skill.cast_time:
            self.duration_list[melee] = skill.cast_time

        self._pre_cast(skill)

    def add_effects(self, effect, num):
        for _ in range(num):
            self.add_effect(effect)

    def add_effect(self, effect):
        if self.effect_list[effect] < effect.max_layers:
            count = min(effect.max_layers - self.effect_list[effect], effect.layer)
            self.effect_list[effect] += count
            if effect.apply:
                for _ in range(count):
                    effect.apply(self.skills, self.attribute)
        if effect.duration:
            self.refresh_duration(effect)

    def remove_effects(self, effect):
        for _ in range(self.effect_list[effect]):
            self.remove_effect(effect)

    def remove_effect(self, effect):
        if self.effect_list[effect]:
            self.effect_list[effect] -= 1
            if effect.revoke:
                effect.revoke(self.skills, self.attribute)
        if effect in self.duration_list and not self.effect_list[effect]:
            self.duration_list[effect] = 0

    def refresh_duration(self, entity):
        if entity.period:
            if self.duration_list[entity] > entity.period:
                next_period = self.duration_list[entity] % entity.period - entity.period
            else:
                next_period = self.duration_list[entity]
        else:
            next_period = 0
        self.duration_list[entity] += entity.duration
        self.duration_list[entity] = min(entity.max_duration, self.duration_list[entity])
        self.duration_list[entity] += next_period

    def _pre_cast(self, skill):
        pass

    def post_cast(self, skill):
        if not self.frame_duration:
            self.frame_duration = self.frame
        self._post_cast(skill)

    def _post_cast(self, skill):
        pass

    def cast(self, skill):
        self.pre_cast(skill)

        if skill is wait:
            self.timer(self.frame_duration)
        elif skill.duration:
            self.refresh_duration(skill)
        else:
            for i, clip in enumerate(skill.clips):
                self.timer(clip)
                self.damage(skill, i)

        self.post_cast(skill)

    def _pre_damage(self, skill):
        pass

    def _post_damage(self, skill):
        pass

    def record(self, skill_name, damage):
        if isinstance(damage, tuple):
            self.action_seq.append((self.current_time, skill_name, *damage))
        else:
            # self.action_seq.append((self.current_time, ";".join([f"{e}:{l}" for e, l in self.effect_list.items() if l]), skill_name, damage))
            self.action_seq.append((self.current_time, skill_name, damage))

    def count(self, skill_name):
        skill_name_effect = skill_name + "".join([f"({e}:{l})" for e, l in self.effect_list.items() if l and e.apply])
        if skill_name_effect not in self.skill_count:
            self.skill_count[skill_name_effect] = 0
        self.skill_count[skill_name_effect] += 1

    def damage(self, skill, i=0):
        self._pre_damage(skill)

        if skill.snapshot:
            damage = self.snapshots[skill]
        else:
            damage = skill(self.attribute)

        self.record(skill.name, damage[i])
        # self.count(skill.name)

        if self.divine_tag and skill in self.divine_list:
            self.divine()
        self._post_damage(skill)

    def _epoch_init(self):
        pass

    def epoch_init(self):
        self.gcd = 0
        self.frame_duration = 0

        self.current_skill = wait
        self.last_skill = wait

        self.current_time = 0
        self.cd_list = {skill: 0 for skill in self.skills}
        self._overdraw = {}
        self.duration_list = {entity: 0 for entity in self.skills + self.effects if
                              entity.duration or entity is melee}
        self.effect_list = {effect: 0 for effect in self.effects}

        self.snapshots = {}

        self.cast_seq = []
        self.action_seq = []
        self._epoch_init()

    def wait(self):
        self.cast(wait)

    def epoch_prepare(self):
        for skill in self.prepare_skill_list:
            while not self.available[skill]:
                self.wait()
            self.cast_seq.append((self.current_time, skill.name))
            self.cast(skill)

    def init_attribute(self):
        for effect in self.effect_list:
            if self.effect_list[effect]:
                self.remove_effects(effect)

    def priority_simulate(self):
        while self.current_time < self.duration:
            for skill, condition in self.priority:
                if self.available[skill] and condition():
                    if skill is not wait:
                        self.current_skill = skill
                        self.cast_seq.append((self.current_time, skill.name))
                        self.cast(self.current_skill)
                        self.last_skill = skill
                    else:
                        self.wait()
                    break
            else:
                self.wait()

    def loop_simulate(self):
        loop_list = copy.copy(self.loop)
        while self.current_time < self.duration:
            skill = loop_list.pop(0)
            while not self.available[skill]:
                self.wait()
            self.current_skill = skill
            self.cast_seq.append((self.current_time, skill.name))
            self.cast(self.current_skill)
            self.last_skill = skill

            if not loop_list:
                loop_list = copy.copy(self.loop)

    def simulate(self, epochs):
        for _ in tqdm(range(epochs)):
            self.epoch_init()
            self.epoch_prepare()
            if self.priority:
                self.priority_simulate()
            elif self.loop:
                self.loop_simulate()
            self.init_attribute()
            self.action_seqs.append(self.action_seq)
            self.cast_seqs.append(self.cast_seq)
        self.dps.backward()
        self.attribute.scale_gradient()
