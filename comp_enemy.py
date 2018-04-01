from random import randint, choice
from strike import Strike
from ship import Ship
from field import Field
class Enemy(object):
    __coords = ((0, 1), (0, -1), (1, 0), (-1, 0))
    def __init__(self, comp, s_z):
        self.complexity = comp
        self.size = s_z
        self.list_attack = []

    def add_ships(self, player):
        ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
        for ship in ships:
            x_start = 0
            y_start = 0
            x_end = -1
            y_end = -1
            flag = True
            while flag:
                while not ((0 <= x_end <= self.size-1) and (0 <= y_end <=self.size-1)):
                    x_start = randint(0,self.size-1)
                    y_start = randint(0,self.size-1)
                    vector = choice(self.__coords)
                    x_end = x_start + vector[0] * ship
                    y_end = y_start + vector[1] * ship
                if x_start > x_end or y_start > y_end:
                    x_start, x_end = x_end, x_start
                    y_start, y_end = y_end, y_start
                if not (str(ship) in player.field.list_ships):
                    player.field.list_ships[str(ship)] = []
                print('({}, {}), ({}, {})'.format(x_start,y_start,x_end,y_end))
                prev = player.field.check_points(player.field.field)
                player.field.list_ships[str(ship)].append(Ship(player,player.field.field, ship,
                                                                x_start,
                                                                y_start,
                                                                x_end
                                                                )
                                                        )

                now = player.field.check_points(player.field.field)
                if prev < now:
                    flag = False
                else:
                    player.field.list_ships[str(ship)].pop()
                    x_start = 0
                    y_start = 0
                    x_end = -1
                    y_end = -1

    def AI_attack(self, player, shoot, point_attack):
            if not point_attack:
                random_num = randint(1,100)
                if (self.complexity == 'easy' and random_num <= 10 or
                        self.complexity == 'medium' and random_num <= 25 or
                        self.complexity == 'hard' and random_num <= 40):
                    point = choice(player.log)

                else:
                    y = randint(0, self.size-1)
                    x = randint(0, self.size-1)
                    point = (y, x)
                if point in player.log:
                    del player.log[player.log.index(point)]
                result = shoot.hit(0, player.field.field, point[1], point[0])
                if result == 'H':
                    while result != 'K':
                        add_coord = choice(self.__coords)
                        new_point_attack = (point[1]+add_coord[1], point[0] + add_coord[0])
                        if player.field.field[new_point_attack[0]][new_point_attack[1]] != 'X':
                            result = shoot.hit(0, player.field.field, new_point_attack[1], new_point_attack[0])
                            if result == 'M':
                                return point
                            elif result == 'H':
                                point = new_point_attack
                    return 'K'
                elif result == 'M':
                    return 'M'
                else:
                    return 'K'
            else:
                result = 0
                point = point_attack
                while result != 'K':
                    for add_coord in self.__coords:
                        new_point = (point[1]+add_coord[1], point[0]+add_coord[0])
                        if point in player.log:
                            del player.log[player.log.index(point)]
                            result = shoot.hit(0, player.field.field, point[1], point[0])
                            point = new_point
                    # add_coord = choice(self.__coords)
                    # new_point_attack = (point[1] + add_coord[1], point[0] + add_coord[0])
                    # if player.field.field[new_point_attack[0]][new_point_attack[1]] != 'X':
                    #     result = shoot.hit(0, player.field.field, new_point_attack[1], new_point_attack[0])
                    #     if result == 'M':
                    #         return point
                    #     elif result == 'H':
                    #         point = new_point_attack
                return 'K'













