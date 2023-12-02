
# Advent of Code 2023

![Tests](https://github.com/StigHaraldGustavsen/AOC23/actions/workflows/tests.yml/badge.svg)


```bash
poetry install
```

```bash
poetry run pytest
```

## reusable boilerplate


```bash
mkdir aoc23/d{x}
touch aoc23/d{x}/day{x}_test
touch aoc23/d{x}/day{x}_2_test
touch aoc23/d{x}/day{x}

touch aoc23/day{x}.py
touch tests/test_day{x}.py
```

### dayX.py
```python
myfile = open("aoc23/d1/day1", "r")
myline = myfile.readline()
```

### test_dayX.py
```python
from aoc23.day{x} import get_num, day{x}

def test_day{x}():
    assert 1 == 1
```