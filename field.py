from ship import Ship

class Field(object):

    A = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    __len_ships = (4, 3, 2, 1)
    num_ships = 4
    def __init__(self, size):
        self.size = size
        self.field = [[' ']*self.size for i in range(self.size)]
        self.list_ships = {}

    def draw(self, name):
        print("{}'s field".format(name))
        for i in range(self.size):
            print(' {} '.format(self.A[i]), end='')
        print()
        for i in range(self.size):
            print('|', end='')
            for j in range(self.size):
                print(' {}|'.format(self.field[i][j]), end='', sep='')
            print(' {}'.format(i+1))
            print('—'*2*self.size)

    def add_ships(self, player):
        for i in range(self.num_ships):
            self.draw(player.player_name)
            flag = True
            while flag:
                l = int(input('Enter len of the ship\n'))
                start = str(input('Enter the front of the ship\n'))
                end = str(input('Enter the back of the ship\n'))
                if start[0] == end[0]:
                    if int(start[1]) > int(end[1]):
                        start, end = end, start
                else:
                    if self.A.index(start[0]) > self.A.index(end[0]):
                        start, end = end, start
                if not (str(l) in self.list_ships):
                    self.list_ships[str(l)] = []
                if len(self.list_ships[str(l)]) < self.__len_ships[l-1]:
                    prev = self.check_points(player.field.field)
                    self.list_ships[str(l)].append(Ship(player, player.field.field, l,
                                                        self.A.index(start[0]),
                                                        int(start[1:])-1,
                                                        self.A.index(end[0])
                                                        ))
                    now = self.check_points(player.field.field)
                    if prev < now:
                        flag = False
                    else:
                        print("You can't put a ship in here")
                        self.list_ships[str(l)].pop()
                else:
                    print('Too many length ships {}'.format(l))

    def check_points(self,field):
        count = 0
        for i in range(len(field[0])):
            for j in range(len(field[0])):
                if field[i][j] == 'N':
                    count += 1
        return count


if __name__ == '__main__':
    print('This is field model')