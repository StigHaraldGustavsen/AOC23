from aoc23.day2 import count_cubes, day2, day2_2

def test_day2_get_num():
    test = "1 blue, 2 green, 4 red".split(', ')
        
    assert count_cubes(test)['green'] == 2
    assert count_cubes(test)['red'] == 4

def test_day2():

    res = day2("aoc23/d2/test")
    assert res == 8

def test_day2_2():

    res = day2_2("aoc23/d2/test")
    assert res == 2286