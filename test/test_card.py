# PYTHONPATH=src poetry run pytest

import pytest
from card import Card

@pytest.fixture
def my_card():
    return Card(0,0)

def test_card_str():
    for i in range(12):
        for j in range(4):
            card = Card(i, j)
            assert(str(card) == f'{i:x}{j}')