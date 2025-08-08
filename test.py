from base.scene import scene


def test():
    player = scene.add_player()
    scene.add_enemy()
    player.cast_skill(101002, 1)
    for _ in range(32):
        scene.process()
    print(player)


if __name__ == '__main__':
    test()
