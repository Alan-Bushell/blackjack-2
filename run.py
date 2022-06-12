"""
BlackJack 2.0
"""

# Global Elements
suits = ["♠", "♥", "♣", "♦"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
         "K"]
card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
               "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
deck = []

for s in suits:
    for c in cards:
        print(c, s)
        deck.append([c, s])


print(deck)
