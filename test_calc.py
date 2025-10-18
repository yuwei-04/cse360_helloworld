from src.calc import add, subtract, mul

def test_add():
    assert add(2,3)==5

def test_subtract():
    assert subtract(5,3)==2

def test_mul():
    assert mul(4,3)==12
