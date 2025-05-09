from Card import Card
from random import getrandbits

from .consts import PlayerState


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = []
        self.state = PlayerState.ACTIVE


    def __str__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += str(card)

        result = f"name: {self.name}\n"\
            + f"cards: {cards}\n"\
            + f"score: {self.score()}"
        return result
    


    def score(self) -> int:
        total_score = 0
        for card in self.cards:
            total_score += card.score()

        if total_score > 21:
            self.state = PlayerState.FAILED

        return total_score


    def is_active(self) -> bool:
        return self.state == PlayerState.ACTIVE
    

    def decide(self) -> bool:
        decision = bool(getrandbits(1))

        if not decision:
            self.state = PlayerState.STOPPED
        
        return decision


    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.score()
