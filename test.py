from base.monitor import monitor


def test():
    player = monitor.add_player()
    enemy = monitor.add_enemy()
    player.learn_skill_level(100994, 14, player.id)
    for i in range(320):
        print(f"Frame {i}")
        monitor.process()
        player.cast_skill(101015, 1)
        player.cast_skill(101009, 1)
        player.cast_skill(101005, 1)
        # player.cast_skill(101003, 1)
        # player.cast_skill(101004, 1)
        player.cast_skill(101002, 1)
        # print(player.buff_map)
        # print(player.cd_map)
        # print(player.timer_map)
        print("-------------------")
    print(player)


if __name__ == '__main__':
    test()
