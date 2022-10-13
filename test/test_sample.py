# Assertion error test,
# we can simply add error message like below
def test_even():
    a = 11
    assert a % 2 == 0, 'value was odd, should be even'
