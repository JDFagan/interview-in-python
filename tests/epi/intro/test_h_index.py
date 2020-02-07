import pytest
from epi.intro.h_index import get_h_index


@pytest.fixture
def research_papers1() -> list:
    return [1, 4, 1, 4, 2, 1, 3, 5, 6]


def test_1(research_papers1):
    assert get_h_index(research_papers1) == 4
