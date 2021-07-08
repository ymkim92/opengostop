class Score:
    blue_tti = ((0,1), (2,1))
    red_tti = ((0,1), (2,1))
    godori = ((0,1), (2,1))
    double_pi = ((0,1), (2,1))

    def __init__(self):
        pass

    def get_score(self, cards):
        self.get_score_kwang(cards)
        self.get_score_10(cards)
        self.get_score_tti(cards)
        self.get_score_pi(cards)