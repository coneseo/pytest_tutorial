import pytest


@pytest.fixture(params=[1,2,3])
def make_double_value(request):
    return (request.param, request.param * 2)


def test_double_value(make_double_value):
    assert make_double_value[1] == (make_double_value[0] * 2 ) -1