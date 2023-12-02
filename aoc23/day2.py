#myfile = open("aoc23/d2/test", "r")
myfile = open("aoc23/d2/data", "r")
myline = myfile.readline()




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
    possible_games = []
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



def day2_2(file):
    myfile = open(file, "r")
    myline = myfile.readline()
    game_score_sum =  0
    while myline:
        string_list = myline.split(': ')
        game_possible = True

        try:
            game_nr = int(string_list[0].replace("Game ","").replace("Game ",""))
        except:
            print('error after game number :'+str(game_nr))
        
        games = string_list[1].split('; ')

        red = 0
        green = 0
        blue = 0

        for i, game in enumerate(games):
            cubes_string = game.split(', ')
            cubes = count_cubes(cubes_string)

            if i == 0: #initsialize
                red = cubes['red']
                green = cubes['green']
                blue = cubes['blue']
            else:
                True

            if cubes['red'] > red:
                red = cubes['red']
            if cubes['blue'] > blue:
                blue = cubes['blue']
            if cubes['green'] > green:
                green = cubes['green']
        
        game_score_sum +=  red*blue*green  

        red = 0
        green = 0
        blue = 0
        myline = myfile.readline()


    return game_score_sum



if __name__ == '__main__':
    
    #day2("aoc23/d2/test")
    print(day2_2("aoc23/d2/data"))