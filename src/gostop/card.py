import random
import logging
from PIL import Image
from build_a_image import get_concat_h, add_number

logging.basicConfig(level=logging.INFO)

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

class Cards(list):

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

    def __init__(self, l = []):
        self.check_cards_valid(l)
        super().__init__(l)

    def check_cards_valid(self, l):
        for i in l:
            if type(i) is not tuple:
                raise ValueError(l)

            self.check_card_valid(i)

    def check_card_valid(self, t):
        if len(t) != 2:
            raise ValueError(t)
        for i in range(2):
            if type(t[i]) is not int:
                raise ValueError(t) 
        if t[0] < 0 or t[0] > 11:
            raise ValueError(t)
        if t[1] < 0 or t[1] > 3:
            raise ValueError(t)

    def get_card_type(self, x, y):
        return self.card_set(x, y)

    def get_total_number_of_cards(self):
        return sum(len(items) for items in self.card_set)
 
    def add_card(self, a_card):
        self.check_card_valid(a_card)
        if a_card in self:
            logging.error(f"Card {a_card}) is in card set already")
            return False
        else:
            self.append(a_card)
            return True

    def get_card(self, a_card):
        if a_card in self:
            self.remove(a_card)
            return True
        else:
            return False

    def get_card_in_random(self):
        if len(self)==0:
            return None
        i = random.randint(0, len(self)-1)
        return self.pop(i)

    def get_cards_in_random(self, n):
        if len(self) < n:
            return None
        ret = Cards()
        for _ in range(n):
            ret.add_card(self.get_card_in_random())
        
        return ret
    
    def create_image(self, image_name="../html/gostop.png", number=False, overlap=50):
        images = []
        for i, (x, y) in enumerate(self):
            img = Image.open(f"images/{x:x}{y}.png")
            if number:
                img = add_number(img, i) 
            images.append(img)
        
        dst_image = images.pop(0)
        for i in images:
            dst_image = get_concat_h(dst_image, i, overlap)

        dst_image.save(image_name)


class GameCards(Cards):
    def __init__(self):
        super().__init__()
        for i in range(len(self.card_set)):
            for j in range(len(self.card_set[0])):
                self.add_card((i, j))


if __name__ == '__main__':
    cards = Cards()
    cards.add_card((1,2))
    cards.add_card((10,0))
    cards.add_card((10,1))
    cards.add_card((10,2))
    cards.create_image()
    cards.create_image(image_name="../html/badak.png", number=True, overlap=0)
