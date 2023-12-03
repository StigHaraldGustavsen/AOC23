myfile = open("aoc23/d3/test", "r")
#myfile = open("aoc23/d3/data", "r")

myline = myfile.readline()

while myline:
    myline = myfile.readline()

def find_distinct_symbols(file):
    """
    returns a list of symbol charchters that is not number or '.'
    """
    myfile = open(file, "r")
    myline = myfile.readline()
    symbol_string = ""
    while myline:
        for i in range(10):
            myline = myline.replace(str(i),'.')
        
        symbol_string += (myline.replace('.','')).replace('\n','')
        myline = myfile.readline()        

    return list(set(symbol_string))

def map_out_symbols(file):
    list_of_symbols = find_distinct_symbols(file) 

    myfile = open(file, "r")
    myline = myfile.readline()
    list_of_symbol_posistions = []
    line_number = 0
    
    while myline:
        for i in range(10):
            myline = myline.replace(str(i),'.')
        
        for i in range(len(myline)):
            if myline[i] in list_of_symbols:
                list_of_symbol_posistions.append((line_number,i))
        
        line_number += 1        
        myline = myfile.readline()
    
    return list_of_symbol_posistions

def find_numbers(string):
    """returns a list of numbers, with number and position of the number

    Args:
        string (str): string such as "..35..633." should return string[(line_index,col_index)]
    """
    string = string.replace('\n','')
    string = string+'.'
    list_of_numbers = []
    idx = 0
    new_number = False
    number_string = ""
    for i in range(len(string)):
        
        if string[i] !='.':
            
            if new_number == False:
                new_number = True
                idx = i          
                for j in range(i,len(string)):

                    #check the lengt of the number
                    if string[j] != '.':
                        number_string += string[j]
                    else:
                        #print(number_string)
                        break
            elif new_number:
                next
        
        if (new_number and string[i] == '.'):
            #print(number_string)
            list_of_numbers.append((int(number_string),idx))
            number_string = ""
            new_number = False
        else:
            True

    return list_of_numbers

def day3(file):
    list_of_symbols = find_distinct_symbols(file) #list of distict symbols
    list_of_symbol_positions = map_out_symbols(file) #list of tuple coords [(line_nr,idx)]
    print(list_of_symbol_positions)
    #print(list_of_symbol_positions)

    new_file = ""
    clean_line = ""
    myfile = open(file, "r")
    myline = myfile.readline()
    line_nr = 0
    adjacent_number_to_symbol = []

    while myline:
        clean_line = myline
        for symbol in list_of_symbols:
            #removes symbols form string and runs them into '.'
            myline = myline.replace(symbol,'.') 
        
        numbers_list = find_numbers(myline)
        print(str(line_nr)+' | '+str(numbers_list))

        for number, num_start in numbers_list:
            #check if there is a symbol nearby
            added = False
            for symbol_line_nr, symbol_idx in list_of_symbol_positions:
                
                if line_nr-1 <= symbol_line_nr <= line_nr+1 and num_start-1 <= symbol_idx < num_start+len(str(number))+1 and added != True:
                    adjacent_number_to_symbol.append(number)
                    clean_line = clean_line[:num_start] + '.'*len(str(number)) + clean_line[num_start+len(str(number)):]
                    #clean_line = clean_line.replace(str(number),"."*len(str(number)),1)
                    added = True
        new_file += clean_line
        line_nr += 1
        myline = myfile.readline()
    
    #print(adjacent_number_to_symbol)
    #print(adjacent_number_to_symbol)
    f = open('clean','w')
    f.write(new_file)
    sum = 0
    for num in adjacent_number_to_symbol:
        sum += num
    return sum

# find all symbols and store in index
# convert all symbols to dots.
# loop thorugh and find numbers and number length
# search for if there is a symbol nearby 
# store to a list if there is a symbol nearby


# 530495
# 534200
# 538934
# 529673 is to low
# 529673
# 538112
# 538112 is to high.. 

if __name__ == '__main__':
    #print(find_distinct_symbols('aoc23/d3/data'))
    #print(map_out_symbols('aoc23/d3/test'))
    #print(find_numbers('..35..633.'))
    #print(find_numbers('..35..633.555'))
    #print(find_numbers('467..114..'))
    #print(day3('aoc23/d3/test'))
    print(day3('aoc23/d3/data'))