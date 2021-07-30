from card import create_image, GameCards
import cmd2 as cmd
import rule
import user

INIT_MONEY = 1000
INIT_NUM_USER_CARDS = 10
INIT_NUM_BADAK_CARDS = 8
NUM_USERS = 2

class GsGame:
    def __init__(self, num_users, play_order_list):
        self.current_player = 0
        self.play_order = play_order_list
        self.gs_users = []
        self.num_users = num_users
        for i in range(num_users):
            self.gs_users.append(user.User(i))

    def prepare_game(self, gs_cards, num_user_cards, num_badak_cards):
        self.badak_cards = gs_cards.get_cards_in_random(num_badak_cards)
        for i in range(self.num_users):
            user_cards = gs_cards.get_cards_in_random(num_user_cards)
            self.gs_users[i].set_cards(user_cards)

    def start(self):
        winner = -1
        self.current_player = self.get_first_player()
        for _ in range(NUM_USERS):
            player = self.get_next_player()
            if rule.check_4cards(player.cards_in_hand) >= 0:
                player.score = 7
                
        while True:
            # TODO add cmd2 console here
            pass
            # self.gs_users[self.current_player].select_card()
        
        return winner

    def get_first_player(self):
        # TODO: replace 0 to winner
        return 0

    def get_next_player(self):
        i = self.current_player
        self.current_player += 1
        return self.gs_users[i]

def gostop(num_users, play_order_list, money_list):
    gs_id = 0
    gs_game = GsGame(NUM_USERS, play_order_list)

    while True:
        gs_cards = GameCards()
        gs_game.prepare_game(gs_cards, INIT_NUM_USER_CARDS, INIT_NUM_BADAK_CARDS)
        # TODO 
        # - check if any card set has all 4 set cards.
        # - money_list

        print(len(gs_cards))
        create_image(sorted(gs_game.badak_cards), image_name="../html/badak.png", overlap=0)
        create_image(sorted(gs_game.gs_users[gs_id].cards_in_hand), 
            image_name="../html/user_in_hand.png", number=True)

        for i in range(NUM_USERS):
            create_image(sorted(gs_game.gs_users[i].cards_earned), 
                image_name=f"../html/cards_earned{i}.png", number=True, overlap=0)

        gs_game.start()
        break

if __name__ == '__main__':
    play_order_list = []
    for i in range(NUM_USERS):
        play_order_list.append(i)

    gostop(NUM_USERS, play_order_list, [INIT_MONEY]*NUM_USERS)