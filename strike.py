class Strike(object):
    def __init__(self):
        self.point_hit = 'X'

    def __check_aoe(self, field, y, x):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                try:
                    if x+i == -1 or y+j == -1:
                        raise IndexError
                    if field[y+j][x+i] != ' ' and field[y+j][x+i] != 'X':
                        return True
                except IndexError:
                    pass
        return False

    def hit(self, self_field, field_enemy, y, x):
        if self_field != 0:
            self_field[x][y] = 'X'
        if field_enemy[x][y] == 'N':
            field_enemy[x][y] = 'X'
            if self.__check_aoe(field_enemy, x, y):
                print('Hit')
                return 'H'
            else:
                print('Killed')
                return 'K'
        else:
            field_enemy[x][y] = 'X'
            print('Missed')
            return 'M'


if __name__ == '__main':
    print('This is strike model')
