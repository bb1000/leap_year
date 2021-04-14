def test_leap_year():
     assert is_leap_year(2000) == True
     assert is_leap_year(1999) == False
     assert is_leap_year(1998) == False
     assert is_leap_year(1996) == True
     assert is_leap_year(1900) == False
     assert is_leap_year(1800) == False
     assert is_leap_year(1600) == True


def is_leap_year(year):
    if year % 100 == 0:
       if year % 400 == 0:
          return True
       else:
          return False
    if year % 4 == 0:
        return True
    else:
        return False