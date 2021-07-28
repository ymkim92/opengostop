from card import Cards

class User:
    def __init__(self, id:int, name:str=''):
        self.id = id
        self.name = name
        self.score = 0
        self.cards_in_hand = None
        self.cards_earned = None

    def set_cards(self, h:Cards) -> None:
        self.cards_in_hand = h
        self.cards_earned = Cards()

    def select_card(self, cards, index):
        pass

    def select_go_stop(self):
        pass
    
    def __str__(self):
        ret = 'Cards in hand:'
        pass