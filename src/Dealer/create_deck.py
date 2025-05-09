from typing import List
from Card import Card

from Card import CardSuit, CardValue

def create_deck() -> List[Card]:
    deck = []
    
    for suit in CardSuit:
        for value in CardValue:
            card = Card(suit, value)
            deck.append(card)
    
    return deck