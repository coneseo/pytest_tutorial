import pytest

# Python Framework에서는 입력 인자를 Fixture로 명명하여 관리할 수 있다.
# Fixture를 사용하면 코드가 간결해지고, 재활용할 수 있어 효율적인 테스트를 할 수 있다.
# Fixture는 데코레이터(@pytest.fixture)를 활용하여 사용한다.

# Fixture를 활용하여 함수를 변수처럼 사용하기
@pytest.fixture
def square_10():
    return 10 * 10


def test_square(square_10):
    assert square_10 == 100
    assert square_10 == 121