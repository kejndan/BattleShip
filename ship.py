

class Ship(object):
    __block = 'N'

    def __init__(self, player, field, len, x_start, y_start, x_end):
        for i in range(len):
            if x_start == x_end:
                add_x = i
                add_y = 0
                vec = 'v'

            else:
                add_x = 0
                add_y = i
                vec = '>'
            if self.__check_aoe(field, y_start + add_x, x_start + add_y, i, vec):
                field[y_start + add_x][x_start + add_y] = self.__block
                player.log.append((y_start+add_x, x_start + add_y))

            else:
                for j in range(i):
                    if x_start == x_end:
                        add_x = j
                        add_y = 0
                    else:
                        add_x = 0
                        add_y = j
                    field[y_start + add_x][x_start + add_y] = ' '
                    player.log.pop()
                break

    def __check_aoe(self, field, y, x, start, vec):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                try:
                    if x+j == -1 or y+i == -1:
                        raise IndexError
                    if field[y+i][x+j] == self.__block:
                        if not ((vec and i == -1 and j == 0 and start) or (vec and i == 0 and j == -1 and start)):
                            return False
                except IndexError:
                    pass
        return True


if __name__ == '__main':
    print('This is ship model')