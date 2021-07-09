class User:
    def __init__(self, id, h, m):
        self.id = id
        self.cards_in_hand = h
        self.money = m
        self.cards_earned = []

    def select_card(self, cards, index):
        pass

    def select_go_stop(self):
        pass
    
    def __str__(self):
        ret = 'Cards in hand:'
        pass