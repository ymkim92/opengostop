class User:
    def __init__(self, h, g, m):
        self.cards_in_hand = h
        self.cards_earned = g
        self.money = m

    def select_card(self, cards, index):
        pass

    def select_go_stop(self):
        pass
    
    def __str__(self):
        ret = 'Cards in hand:'
        pass