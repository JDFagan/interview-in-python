import pytest
from epi.intro.h_index import get_h_index


@pytest.fixture
def research_papers1() -> dict:
    return {
        'A': 1,
        'B': 4,
        'C': 1,
        'D': 4,
        'E': 2,
        'F': 1,
        'G': 3,
        'H': 5,
        'I': 6,
        }


def test_1(research_papers1):
    assert get_h_index(research_papers1) == 4
