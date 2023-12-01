#myfile = open("aoc23/d1/day1_test", "r")
#myfile = open("aoc23/d1/day1_2_test", "r")
myfile = open("aoc23/d1/day1", "r")
myline = myfile.readline()
numbers = []
numbers_p2 = []


def get_num(cal_string):
    number_string = ""
    for charcakter in cal_string:
        try:
            int(charcakter)
            number_string = number_string + str(int(charcakter))
        except:
            next
    if len(number_string) == 0:
        return 0
    elif len(number_string) == 0:
        return int(number_string+number_string)
    else:
        first = number_string[:1]
        last = number_string[len(number_string)-1]
        return int(first+last)
    

while myline:

    numbers.append(get_num(myline))

    myline = myline.replace("one","o1e")
    myline = myline.replace("two","t2o")
    myline = myline.replace("three","th3ee")
    myline = myline.replace("four","fo4ur")
    myline = myline.replace("five","fi5ve")
    myline = myline.replace("six","si6x")
    myline = myline.replace("seven","sev7en")
    myline = myline.replace("eight","eig8ht")
    myline = myline.replace("nine","ni9ne")
    #print(myline)
    numbers_p2.append(get_num(myline))

    myline = myfile.readline()
myfile.close()

print(numbers)
sum = 0
for number in numbers:
    sum += number

print('result')
print(sum)

print(numbers_p2)
sum2 = 0
for number in numbers_p2:
    sum2 += number

print('result for part 2')
print(sum2)
print('\n')
if __name__ == '__main__':
    #simple test
    print(get_num("sf1ffv2fgdf3dfs45"))
    test = 'asdfghgdf43ninee'
    print(get_num(test))
    test = test.replace("nine","9")
    print(test)
    print(get_num(test))