from aoc23.day2 import count_cubes, day2

def test_day2_get_num():
    test = "1 blue, 2 green; 3 green".split(', ')
    print(count_cubes(test))
    
    assert 1 == 1

def test_day2():

    res = day2("aoc23/d2/data")
    assert res == 2169