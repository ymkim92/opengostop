# PYTHONPATH=src/gostop poetry run pytest

import pytest
from rule import check_4cards

def test_check_4cards():
    ll = [(1,1), (1,3)]
    ret = check_4cards(ll)
    assert(ret == -1)
    ll = [(1,0), (1,2), (1,1), (1,3)]
    ret = check_4cards(ll)
    assert(ret == 1)
    ll = [(1,0), (1,2), (0, 3), (11, 1), (1,1), (1,3)]
    ret = check_4cards(ll)
    assert(ret == 1)