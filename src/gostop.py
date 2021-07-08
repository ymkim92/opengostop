import card
import user

class GsGame:
    #   0 1 2 3 4 5 6 7 8 9 a b
    # 0 
    # 1
    # 2
    # 3
    card_set = (
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    )     
    def __init__(self, gs_users, gs_cards, num_user_cards, num_badak_cards):
        
        pass

if __name__ == '__main__':
    gs_cards = card.Cards()
    gs_users = user.Users()
    gs_game = GsGame(gs_users, gs_cards, 2, 4)