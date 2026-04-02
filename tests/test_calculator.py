from app.calculator import sum, resta

def test_sum() -> None:
    assert sum(2, 3) == 5
    
def test_resta() -> None:
    assert resta(5, 3) == 1

def test_fail() -> None:
    assert False, "This test is meant to fail"

