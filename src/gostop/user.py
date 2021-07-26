from card import Cards

class User:
    def __init__(self, id:int, h:Cards):
        self.id = id
        self.cards_in_hand = h
        self.cards_earned = Cards()
        self.score = 0

    def select_card(self, cards, index):
        pass

    def select_go_stop(self):
        pass
    
    def __str__(self):
        ret = 'Cards in hand:'
        pass