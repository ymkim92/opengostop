# PYTHONPATH=src poetry run pytest

import pytest
from gostop.card import Card, GameCards

def test_card_str():
    for i in range(12):
        for j in range(4):
            card = Card(i, j)
            assert(str(card) == f'{i:x}{j}')

def test_gscard_init():
    gs_cards = GameCards()
    assert(gs_cards.get_total_number_of_cards() == 48)
    assert(len(gs_cards) == 48)
    assert(gs_cards[4] == (1, 0))
    gs_cards.get_card(0,1)
    assert(len(gs_cards) == 47)
    gs_cards.get_card_in_random()
    gs_cards.get_card_in_random()
    assert(len(gs_cards) == 45)
    ret = gs_cards.get_cards_in_random(40)
    assert(len(gs_cards) == 5)
    assert(len(ret) == 40)
    ret = gs_cards.get_cards_in_random(6)
    assert(ret == None)