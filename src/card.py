import random

class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, card_tuple):
        self.x = card_tuple[0]
        self.y = card_tuple[1]

    def __str__(self):
        return f'{self.x:x}{self.y}'

class Cards:

    card_set = (
        (0, 1, 3, 3),
        (0, 1, 2, 3),
        (0, 1, 2, 3),
    )     

    def __init__(self):
        self.available_cards = []

    def get_card_type(self, x, y):
        return self.card_set(x, y)

    def get_total_number_of_cards(self):
        return sum(len(items) for items in self.card_set)
 
    def get_card(self, x, y):
        if (x, y) in self.available_cards:
            self.available_cards.remove((x, y))
            return True
        else:
            return False

    def get_card_in_random(self):
        i = random.randint(0, len(self)-1)
        return self.available_cards.pop(i)

    def __str__(self):
        return str(self.available_cards)
    
    def __len__(self):
        return len(self.available_cards)

class GameCards(Cards):

    def __init__(self):
        super().__init__()
        for i in range(len(self.card_set[0])):
            for j in range(len(self.card_set)):
                self.available_cards.append((i, j))

if __name__ == '__main__':
    gs_cards = GameCards()
    print(gs_cards.get_total_number_of_cards())
    print(len(gs_cards))
    print(gs_cards.available_cards)
    print(gs_cards.get_card(0,1))
    print(gs_cards.available_cards)
    print(gs_cards.get_card_in_random())
    print(gs_cards.get_card_in_random())
    print(gs_cards.available_cards)
    print(gs_cards)