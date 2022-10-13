import pytest
# There are no masterpieces made by lazy artists

@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2*4", 8), ("6*9", 45)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
