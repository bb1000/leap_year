import pytest

@pytest.mark.parametrize(
    'year,expected',
    [(2000, True), (1999, False), (1998, False), (1996, True), (1900, False),
     (1800, False), (1600, True)
    ]
)
def test_leap_year(year, expected):
     assert is_leap_year(year) == expected


def is_leap_year(year):
    if year % 100 == 0:
       return year % 400 == 0
    return year % 4 == 0
