from dataclasses import dataclass
from broadcast_service import broadcast_service


@dataclass
class Skill:
    name: str

    casting: bool = True
    channeling: bool = False

    interval: int = 0
    count: int = 1

    gcd_group: int = 0

    gcd_base: int = 24
    cd_base: int = 0
    charge_base: int = 1
    overdraw_base: int = 1

    base_damage: int = 0
    attack_power: int = 0
    weapon_damage: int = 0

    damage_gain: int = 0
    critical_strike_gain: int = 0
    critical_damage_gain: int = 0
    shield_ignore_gain: int = 0

    def __post_init__(self):
        self.cd = 0
        self.overdraw = self.overdraw_base
        broadcast_service.subscribe("haste", self.update_gcd)

    @property
    def charge(self):
        if not self.cd_base:
            return self.charge_base
        return (self.cd_base * self.charge_base - self.cd) // self.cd_base

    @property
    def condition(self):
        return True

    def _pre_cast(self):
        pass

    def _post_cast(self):
        pass

    @broadcast_service.listen("haste")
    def update_gcd(self, haste):
        self.gcd_base = self.gcd_base // haste

    def set_gcd(self):
        broadcast_service.broadcast(f"gcd_group{self.gcd_group}", self.gcd_base)

    def set_cd(self):
        self.cd += self.cd_base
        self.overdraw -= 1

    def pre_cast(self):
        self.set_cd()
        self._pre_cast()

    def post_cast(self):
        self._post_cast()

    def damage(self):
        self.pre_damage()
        self.post_damage()

    def pre_damage(self):
        pass

    def post_damage(self):
        pass

