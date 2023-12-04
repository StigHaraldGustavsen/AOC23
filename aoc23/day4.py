#myfile = open("data/d4/test", "r")
myfile = open("data/d4/data", "r")

myline = myfile.readline()

Cards = []
card_nr = 1

#list_of_number_of_wins = []
games = []
while myline:
    myline = myline.replace('\n','')
    Game_num_strings =  (myline.split(': ')[1]).split(' | ')
    this_round = []
    for Game_num_string in Game_num_strings:
        
        Game_num_string = Game_num_string.replace('  ',' ')
        if Game_num_string[0] ==' ':
            Game_num_string = Game_num_string[1:]
        game_num_list = Game_num_string.split(' ')
        this_round.append(list(map(int, game_num_list)))
        #print(game_num_list)
        #for game_num_str in game_num_list:
            #print(game_num_str)
            #int(num) for num in game_num_str        
            #Game to int[]

    games.append(this_round)
    #print(list_of_number_of_wins)
    #print(myline)
    myline = myfile.readline()

#print(games)

list_of_number_of_wins = []

for i, game in enumerate(games):
    #print(game)
    winning_numbers = 0
    for number in game[0]:
        if number in game[1]:
            winning_numbers += 1
            #print(str(number) +' in : '+str(game[1]),'now found '+str(winning_numbers)+' number in game: '+str(i))
    
    num = 0
    if winning_numbers != 0:
        num = 1
        for i in range(winning_numbers-1):
            num = num*2

    list_of_number_of_wins.append(num)


print(list_of_number_of_wins)
sum = 0
for number in list_of_number_of_wins:
    sum += number

print(sum)