#myfile = open("aoc23/d2/test", "r")
myfile = open("aoc23/d2/data", "r")
myline = myfile.readline()


possible_games = []

def count_cubes(cubes):
    blue = 0
    red = 0
    green = 0

    for cube in cubes:
        
        if 'blue' in cube:
            blue = int(cube.split(" ")[0])
        if 'red' in cube:
            red = int(cube.split(" ")[0])
        if 'green' in cube:
            green = int(cube.split(" ")[0])

    result = {
            'blue':blue,
            'red':red,
            'green': green
              }
    return result

def day2(file):
    myfile = open(file, "r")
    myline = myfile.readline()
    while myline:
        string_list = myline.split(': ')
        game_possible = True

        try:
            game_nr = int(string_list[0].replace("Game ","").replace("Game ",""))
        except:
            print('error after game number :'+str(game_nr))
        
        games = string_list[1].split('; ')
        for game in games:
            cubes = game.split(', ')
            crates = count_cubes(cubes)
            if crates['red'] > 12:
                game_possible = False
            if crates['green'] > 13:
                game_possible = False
            if crates['blue'] > 14:
                game_possible = False

        if game_possible:
            possible_games.append(game_nr)
    
        myline = myfile.readline()

    sum = 0
    for game_nr in possible_games:
        sum += game_nr

    print(sum)
    return sum


if __name__ == '__main__':
    True
    day2("aoc23/d2/data")