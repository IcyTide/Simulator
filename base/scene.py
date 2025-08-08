from base.character import Character


class Scene:
    def __init__(self):
        self.players: list[Character] = []
        self.enemies: list[Character] = []
        self.id2character: dict[int, Character] = {}

    def add_character(self, *args):
        character_id = len(self.id2character) + 1
        character = self.id2character[character_id] = Character(character_id, 1)
        return character

    def add_player(self, *args):
        self.players.append(self.add_character(*args))
        return self.players[-1]

    def add_enemy(self, *args):
        self.enemies.append(self.add_character(*args))
        for player in self.players:
            player.target = self.enemies[-1]
        return self.enemies[-1]

    def process(self):
        for character in self.id2character.values():
            character.process(1)

    def get_character_by_id(self, character_id):
        return self.id2character.get(character_id)


scene = Scene()
