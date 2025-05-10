from Game21 import Game21

from Player import Player

players = [
    Player("Ваня"),
    Player("Петя"),
    Player("Игорь"),
    Player("Вася"),
    Player("Лёша"),
    Player("Стёпа"),
    Player("Кирилл"),
]

game21 = Game21(players)

game21.run()
