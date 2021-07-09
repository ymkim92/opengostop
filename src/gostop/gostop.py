import card
import user

INIT_MONEY = 1000
INIT_NUM_USER_CARDS = 8
INIT_NUM_BADAK_CARDS = 6
NUM_USERS = 2


class GsGame:
    def __init__(self, num_users, gs_cards, num_user_cards, num_badak_cards, money_list, play_order_list):
        self.current_player = 0
        self.play_order = play_order_list
        self.gs_users = []
        self.badak_cards = gs_cards.get_cards_in_random(num_badak_cards)
        for i in range(num_users):
            user_cards = gs_cards.get_cards_in_random(num_user_cards)
            self.gs_users.append(user.User(i, user_cards, money_list[i]))

    def start(self):
        pass

def gostop(num_users, play_order_list, money_list):
    while True:
        gs_cards = card.GameCards()
        gs_game = GsGame(NUM_USERS, gs_cards, INIT_NUM_USER_CARDS, INIT_NUM_BADAK_CARDS, money_list, play_order_list)
        gs_game.start()
        print(gs_game.badak_cards)
        print(sorted(gs_game.badak_cards))
        print(gs_cards)
        print(len(gs_cards))
        break

if __name__ == '__main__':
    play_order_list = []
    for i in range(NUM_USERS):
        play_order_list.append(i)

    gostop(NUM_USERS, play_order_list, [INIT_MONEY, INIT_MONEY])