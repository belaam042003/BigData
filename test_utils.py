from utils import sumar, restar


def test_sumar():
    assert sumar(2, 4) == 6
    assert sumar(1, 4) == 5
    assert sumar(2, 2) == 4


def test_restar():
    assert restar(6, 4) == 2
    assert restar(1, 4) == -3
    assert restar(2, 2) == 0
    
