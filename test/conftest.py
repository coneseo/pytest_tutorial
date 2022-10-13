from test.test_foocompare import Foo
import pytest


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val)
        ]


@pytest.fixture
def square_10():
    return 10 * 10

