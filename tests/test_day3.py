from aoc23.day3 import day3, find_numbers, map_out_symbols , find_distinct_symbols, day3_2

file = "aoc23/d3/test"

def test_find_numbers():
    res = find_numbers('..35..633.')
    assert res[0][0] == 35
    assert res[0][1] == 2
    assert res[1][0] == 633
    assert res[1][1] == 6

def test_day3():
    res = day3("aoc23/d3/test")
    assert res == 4361

def test_day3():
    res = day3_2("aoc23/d3/test")
    assert res == 467835