import random

class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x:x}{self.y}'

CARD_KW = CARD_KWANG = 0        # 광    3 cards = 3 points
CARD_YK = CARD_YEOLKKEUS = 1    # 열끗  6 cards = 1 point
CARD_TI = CARD_TTI = 2          # 띠    6 cards = 1 point
CARD_PI = 3                     # 피    10 cards = 1 point
CARD_SP = CARD_SSANGPI = 4      # 쌍피 

class Cards:

    card_set = (
        (CARD_KW, CARD_TI, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_KW, CARD_TI, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_KW, CARD_YK, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_YK, CARD_TI, CARD_PI, CARD_PI),
        (CARD_KW, CARD_SP, CARD_PI, CARD_PI),
        (CARD_KW, CARD_YK, CARD_TI, CARD_SP),
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
        if len(self)==0:
            return None
        i = random.randint(0, len(self)-1)
        return self.available_cards.pop(i)

    def get_cards_in_random(self, n):
        if len(self) < n:
            return None
        ret = []
        for _ in range(n):
            ret.append(self.get_card_in_random())
        
        return ret

    def __str__(self):
        return str(self.available_cards)
    
    def __len__(self):
        return len(self.available_cards)

    def __getitem__(self, key):
        return self.available_cards[key]

class GameCards(Cards):
    def __init__(self):
        super().__init__()
        for i in range(len(self.card_set)):
            for j in range(len(self.card_set[0])):
                self.available_cards.append((i, j))

if __name__ == '__main__':
    gs_cards = GameCards()
    print(gs_cards)
    print(gs_cards.get_cards_in_random(5))
    print(gs_cards)
