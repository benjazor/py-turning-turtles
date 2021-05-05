from random import randint


def enter_int(msg="Enter a number"):
    tmp = input(msg)
    try:
        int(tmp)
    except:
        return enter_int(msg)
    else:
        return int(tmp)


class Coin:
    def __init__(self, state):
        self.__State = None;
        self.construct(state)

    def construct(self, state):
        self.set_state(state)

    def __str__(self):
        if self.get_state():
            return "H"
        else:
            return "T"

    def get_state(self):
        return self.__State

    def set_state(self, value):
        if isinstance(value, bool):
            self.__State = value

    def flip(self):
        self.set_state(not self.get_state())


class Row:
    def __init__(self, length, coins=None):
        self.__Length = None
        self.__Coins = None
        self.construct(length, coins)

    def construct(self, length, coins):
        self.set_length(length)
        if coins is None:
            tmp = []
            for i in range(length):
                if randint(0, 1) == 0:
                    tmp.append(Coin(True))
                else:
                    tmp.append(Coin(False))
            self.set_coins(tmp)
        elif len(coins) == length:
            self.set_coins(coins)

    def __str__(self):
        tmp1, tmp2 = "", ""
        for i,coin in enumerate(self.get_coins()):
            tmp1 += str(coin) + " "
            tmp2 += str(i+1) + " "
        return tmp1 + "\n" + tmp2

    def get_length(self):
        return self.__Length

    def set_length(self, value):
        if value != 0:
            self.__Length = abs(int(value))

    def get_coins(self):
        return self.__Coins

    def set_coins(self, value):
        if len(value) == self.get_length():
            self.__Coins = value

    def print(self):
        print(str(self))

    def check(self):
        tmp = True
        for coin in self.get_coins():
            tmp = tmp and not coin.get_state()
        return tmp


class Player:
    def __init__(self, name):
        self.__Name = None
        self.construct(name)

    def construct(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__Name

    def set_name(self, value):
        if isinstance(value, str):
            self.__Name = value


class TurningTurtles:
    def __init__(self, length):
        self.__Players = None
        self.__Row = None
        self.construct(length)

    def construct(self, length):
        self.set_row(Row(length))
        tmp = []
        for i in range(2):
            tmp.append(Player(input("Player " + str(i + 1) + " enter your name: ")))
        self.set_players(tmp)

    def get_players(self):
        return self.__Players

    def set_players(self, value):
        self.__Players = value

    def get_row(self):
        return self.__Row

    def set_row(self, value):
        self.__Row = value

    def choose_head(self):
        tmp = int(enter_int("Choose a head: ")) - 1
        while not self.get_row().get_coins()[tmp].get_state():
            tmp = int(enter_int("This is not a head, please choose a head: ")) - 1
        return tmp

    def first_move(self):
        tmp = self.choose_head()
        self.get_row().get_coins()[tmp].flip()
        return tmp

    def choose_coin(self, index):
        if index > 0:
            tmp = int(enter_int("Choose a coin: ")) - 1
            while not (tmp < index):
                tmp = int(enter_int("Choose another coin: ")) - 1
            return tmp

    def second_move(self, index):
        if index > 0:
            self.get_row().get_coins()[self.choose_coin(index)].flip()

    def anotherMove(self, index):
        if index > 0:
            tmp = enter_int("Would you like to play again? (0: yes - 1: no) --> ")
            while tmp != 0 and tmp != 1:
                tmp = enter_int("Would you like to play again? (0: yes - 1: no) --> ")
            if tmp == 0:
                self.second_move(index)

    def play(self):
        current_player = True
        while True:
            print("\n" + str(self.get_row()) + "\n")
            if current_player:
                print(self.get_players()[0].get_name() + " to play")
            else:
                print(self.get_players()[1].get_name() + " to play")

            tmp = self.first_move()

            if self.get_row().check():
                if current_player:
                    print("\nThe winner is " + self.get_players()[0].get_name())
                else:
                    print("\nThe winner is " + self.get_players()[1].get_name())
                break

            self.anotherMove(tmp)

            if self.get_row().check():
                if current_player:
                    print("\nThe winner is " + self.get_players()[0].get_name())
                else:
                    print("\nThe winner is " + self.get_players()[1].get_name())
                break

            current_player = not current_player


class MockTurtles(TurningTurtles):
    def __init__(self, length):
        super(MockTurtles, self).__init__(length)

    def anotherMove(self, index):
        if index > 0:
            tmp1 = enter_int("Would you like to play again? (0: yes - 1: no) --> ")
            while tmp1 != 0 and tmp1 != 1:
                tmp1 = enter_int("Would you like to play again? (0: yes - 1: no) --> ")
            if tmp1 == 0:
                self.second_move(index)
                if not self.get_row().check():
                    tmp1 = enter_int("Would you like to play again? (0: yes - 1: no) --> ")
                    while tmp1 != 0 and tmp1 != 1:
                        tmp1 = enter_int("Would you like to play again? (0: yes - 1: no) --> ")
                    if tmp1 == 0:
                        self.second_move(index)

while True:
    tmp1 = enter_int("You can play a game!\n\n0: TurningTurtles \n1: MockTurtles \n\nGame: ")
    tmp2 = enter_int("Choose a lenght: ")
    print("\n\n")
    if tmp1 == 0:
        print("Let's play TurningTurtles")
        game = TurningTurtles(tmp2)
        break
    if tmp1 == 1:
        print("Let's play MockTurtles")
        game = MockTurtles(tmp2)
        break

game.play()