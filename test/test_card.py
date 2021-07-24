# PYTHONPATH=src/gostop poetry run pytest

import pytest
from card import Card, Cards, GameCards

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
    gs_cards.get_card((0,1))
    assert(len(gs_cards) == 47)
    gs_cards.get_card_in_random()
    gs_cards.get_card_in_random()
    assert(len(gs_cards) == 45)
    ret = gs_cards.get_cards_in_random(40)
    assert(len(gs_cards) == 5)
    assert(len(ret) == 40)
    ret = gs_cards.get_cards_in_random(6)
    assert(ret == None)

def test_gscard_add():
    gs_cards = GameCards()
    ret = gs_cards.add_card((1,2))
    assert(ret==False)
    ret = gs_cards.get_card((1,2))
    assert(ret==True)
    assert(len(gs_cards) == 47)
    ret = gs_cards.add_card((1,2))
    assert(ret==True)
    assert(len(gs_cards) == 48)

def test_gscard_add_value_error():
    gs_cards = GameCards()
    with pytest.raises(ValueError): 
        gs_cards.add_card((21,2))

def test_cards_value_error():
    ll = [(1,2)]
    gs_cards = Cards(ll)

    ll = [(1,2,3)]
    with pytest.raises(ValueError): 
        gs_cards = Cards(ll)

    ll = [(1,2), (90, 2)]
    with pytest.raises(ValueError): 
        gs_cards = Cards(ll)

    ll = [(1,2), (9, 20)]
    with pytest.raises(ValueError): 
        gs_cards = Cards(ll)

