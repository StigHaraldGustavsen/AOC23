from aoc23.day1 import get_num, day1

def test_day1_get_num():
    assert get_num("sf1ffv2fgdf3dfs45") == 15
    assert get_num("sdfgsdfsds") == 0
    assert get_num("") == 0
    assert get_num("1sadfs") == 11
    assert get_num("sdf4fghfghf") == 44
    assert get_num("123456789") == 19

def test_day1():
    sum, sum2 = day1("aoc23/d1/day1_test")
    assert sum == 142

def test_day1_2():
    sum, sum2 = day1("aoc23/d1/day1_2_test")
    assert sum2 == 281
