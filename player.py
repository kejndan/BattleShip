from field import Field


class Player(object):
    def __init__(self, name, queue, s_z):
        self.player_name = name
        self.queue = queue
        self.field = Field(s_z)
        self.field_enemy = Field(s_z)
        self.killed = 0
        self.log = []

    def check_win(self):
        if self.killed == Field.num_ships:
            return 1

    def attack(self, enemy, shoot):
        result = 'H'
        self.field.draw(self.player_name)
        self.field_enemy.draw(enemy.player_name)
        while result != 'M' and self.killed < Field.num_ships:
            point = str(input('Shoots by {}.\n'
                            'Enter the coordinates\n'.
                              format(self.player_name))
                        )
            result = shoot.hit(self.field_enemy.field, enemy.field.field, ord(point[0]) - ord('A'),
                               int(point[1]) - 1)
            self.field_enemy.draw(enemy.player_name)
            if result == 'K':
                self.killed += 1
