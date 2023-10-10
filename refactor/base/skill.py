from dataclasses import dataclass


class Skill:
    def __init__(self):
        name: str

        prepare: int
        channel: int

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