import pytest
from calc import add, subtract, mul, square, divide, mod, power

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_mul():
    assert mul(4, 3) == 12

def test_square():
    assert square(5) == 25

def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_mod():
    assert mod(10, 3) == 1

def test_power():
    assert power(2, 3) == 8
