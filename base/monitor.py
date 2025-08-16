from base.character import Character
from base.scene import Scene
from base.script import GlobalScript


class Monitor:
    def __init__(self):
        self.players: list[Character] = []
        self.employees: list[Character] = []
        self.enemies: list[Character] = []
        self.id2character: dict[int, Character] = {}

    def add_character(self, is_player, *args):
        character_id = len(self.id2character) + 1
        character = self.id2character[character_id] = Character(character_id, 1)
        character.is_player = is_player
        return character
    def remove_character(self, character: Character):
        self.id2character.pop(character.id)
        self.employees.remove(character)

    def get_character(self, character_id):
        return self.id2character.get(character_id)

    def is_player(self, character_id: int):
        if character := self.get_character(character_id):
            return character.is_player
        return False

    def add_player(self, *args):
        self.players.append(self.add_character(True, *args))
        return self.players[-1]

    def add_employee(self, template_id: int, employer_id: int, left_interval: int, *args):
        self.employees.append(self.add_character(False, *args))
        npc = self.employees[-1]
        npc.employer_id = employer_id
        npc.left_interval = left_interval
        npc.target = self.get_character(employer_id).target
        return npc

    def add_enemy(self, *args):
        self.enemies.append(self.add_character(False, *args))
        for player in self.players:
            player.target = self.enemies[-1]
        return self.enemies[-1]

    def is_enemy(self, player_id: int, enemy_id: int):
        for enemy in self.enemies:
            if enemy.id == enemy_id:
                return True
        return False

    def create_npc_with_employer_id(
            self, template_id: int, x: int, y: int, z: int, face_direction: int, interval: int, employer_id: int, *args
    ):
        return self.add_employee(template_id, employer_id, interval)

    def process(self):
        for character in self.id2character.values():
            character.process(1)
        remove_npc = []
        for npc in self.employees:
            npc.left_interval -= 1
            if npc.left_interval <= 0:
                remove_npc.append(npc)
        for npc in remove_npc:
            self.remove_character(npc)


monitor = Monitor()

GlobalScript.is_player = monitor.is_player
GlobalScript.is_enemy = monitor.is_enemy
GlobalScript.get_player = monitor.get_character
GlobalScript.get_npc = monitor.get_character
Scene.create_npc_with_employer_id = monitor.create_npc_with_employer_id
