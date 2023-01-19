# This is a sample Python script.
from builtins import print


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('Hello world')
print('   /|')
print('  / |')
print(' /  |')
print('/___|')

character_name = "John"
character_age = 35
isMale = True

print(f'There once was a man named {character_name},')
print(f'he was {character_age} years old.')
character_name = 'Mike'
print('He really liked the name ' + character_name + ',')
print(f'but didn\'t like being {character_age}.')

# 27.10 Strings
print('\n\t\t\t\t\t\tStrings'.upper())
print("Giraffe Academy")
print("Giraffe \nAcademy")
print("Giraffe \'Academy")

phrase = "Giraffe Academy"
print(phrase)
print(phrase + 'is cool!')
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.lower().islower())
print(len(phrase))
print(phrase[0])
print(phrase[5:9])
print(phrase[5:9:2]) # step
print(phrase[::-1])
print(phrase.count('a'))
print(phrase.index('a'))
print(phrase.index('Acad'))
print(phrase.replace('Giraffe', 'Elephant'))
print(phrase.split())
print(phrase.split('a'))


# 38.30 Numbers
print('\n\t\t\t\t\t\tnumber'.upper())
print(2)
print(-2.22342)
print(3+4.5)
print(3*4.5)
print(3*4+5)
print(3*(4+5))
print(10%3) # reminder rest
print(10/3)
print(10//3) # without the rest
my_num = 5
print(my_num)
print(str(my_num) + ' - is my favourite number.')
my_num = -5
print(abs(my_num))
print(my_num.__abs__())
print(pow(my_num,3))
print(my_num**3)
vo_num = [2,3,4,5,9]
print(max(2,3,4,5,9))
print(max(vo_num))
print(min(vo_num))
print(round(3.7))
from math import *
print(sqrt(35345))
print(isqrt(35345))
print(floor(3.7))
print((3.7).__ceil__())

'''
# 50:00 Input
print('\n\t\t\t\t\t\tInput command'.upper())
name = input('Enter your name:')
age = input('Enter your age:')
print(f'Hello {name}! You are {age}.')
'''

'''
# 53:00 Basic calculator
print('\n\t\t\t\t\t\tBasic calculator'.upper())
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
result = float(num1) + float(num2)
print(result)
'''

# 1:00:00 Basic calculator
print('\n\t\t\t\t\t\tMad Libs Game'.upper())

print('Roses are red ')
print('Violets are blue')
print("I love you")

'''color = input('Enteer a color: ')
plural_noun = input('Enteer a Plural Noun: ')
celebrity = input('Enteer a celebrity: ')


print(f'Roses are {color}')
print(f'{plural_noun} are blue')
print(f'I love {celebrity}')
'''

# 1:04:00 LISTS
print('\n\t\t\t\t\t\tLISTS'.upper())
friends = ['Kevin', 'Karen', 'Jim']
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[::-1])
print(friends.count('Jim'))
friends.extend(['John'])
print(friends)

lucky_numbers = [42,8,15,16,23,4]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']

print(friends)
# friends.extend(lucky_numbers)
print(friends)
friends.append('Kreed')
print(friends)
friends.insert(1,'Kelly')
print(friends)
friends.remove('Jim')
print(friends)
#friends.clear()
print(friends)
friends.pop(-2)
print(friends)
print(friends*2)
print(friends.index('Oscar'))
friends.sort()
print(friends)
lucky_numbers.sort()
print(friends)
friends.reverse()
print(friends)

# 1:04:00 TUPLES
print('\n\t\t\t\t\t\tTUPLES'.upper())
coordinates = (4,5)
print(coordinates[0])

coordinates = [(4,5), (6,7), (80,34)]
print(coordinates[0])

# 1:24:00 FUNCTIONS
print('\n\t\t\t\t\t\tFUNCTIONS'.upper())

def say_hi():
    print('Hello user!')
print('Top')
say_hi()
print('Bottom')

def say_hi(name, age):
    print(f'Hello {name}! You are {age}.')

#say_hi(input('Enter your name: '), input('Enter your age: '))
say_hi('Mike', 3)

# 1:34:00 RETURN STATEMENT
print('\n\t\t\t\t\t\tRETURN STATEMENT'.upper())
def cube(num):
    return num*num*num

print(cube(3))
result = cube(4)
print(result)

# 1:40:00 IF STATEMENT
print('\n\t\t\t\t\t\tIF STATEMENT 1:40:00'.upper())
'''I wake up
If I'm hungry
I eat breakfast

I leave my house
if it's cloudy
I bring an umbrella
otherwise
I bring sunglasses

I'm at a restaurant
if I want meat
I order a steak
otherwise if I want pasta
I order a spagetti & meatballs
otherwise
I order a salad'''

is_male=True
is_tall=False
if is_male and is_tall:
    print('You\'re a tall male')
elif is_male and not is_tall:
    print('You\'re a short male')
elif is_male or is_tall:
    print('You\'re a male or tall or both')
else:
    print('You\'re neither male nor tall')

# 1:54:00 IF STATEMENT
print('\n\t\t\t\t\t\tIF STATEMENT AND COMPARISON 1:54:00'.upper())
def max_num(num1, num2, num3):
    if num1 >=num2 and num1 >=num3:
        return num1
    elif num2 >=num2 and num2 >=num3:
        return num2
    else:
        return num3
print(f'max num = {max_num(3,40,5)}')

# 2:00:00 better calculator
print('\n\t\t\t\t\t\tbetter calculator'.upper())

'''num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
op = input('Enter operatop: ')

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '/':
    print(num1/num2)
elif op == '*':
    print((num1*num2).__round__(4))
    #print(num1*num2)
else:
    print('Invalid operator!')
'''

# 2:07:00 Dictionaries
print('\n\t\t\t\t\t\tDictionaries'.upper())
monthConversions={
    'Jan':'January',
    'Feb':'February',
    'Mar':'March',
    'Apr':'April',
    'May':'May',
    6:'June',
    7:'July',
    8:'August',
    'Sep':'September',
    'Oct':'October',
    'Nov':'November',
    'Dec':'December',
    'winter':['December','January','February']
}
    #show
print(monthConversions['Feb'])
print(monthConversions.get('Feb'))
print(monthConversions.items())

print(monthConversions.keys())
for key in monthConversions.keys():
    print(monthConversions[key])

# 2:14:00 WHILE LOOP
print('\n\t\t\t\t\t\tWHILE LOOP'.upper())
i = 1
while i<=10:
    print(i)
    i+=1
# 2:20:00

'''secret_wors = 'giraffe'
guess = ''
limit = 3
while guess != secret_wors and limit !=0:
    guess = input("Enter guess: ")
    limit -= 1
    if guess == secret_wors:
        print("You win!")
    elif limit == 0:
        print("You lose!")
'''

# 2:33:00 for loop
print('\n\t\t\t\t\t\tfor loop'.upper())
for letter in 'Giraffe Academy':
    print(letter.upper())

for index in range(10):
    print(index)

# 2:41:00 Exponent Function
print('\n\t\t\t\t\t\tExponent Function'.upper())
'''# var1
def rise_to_power (base_num, pow_num):
    result = base_num
    for index in range(1,pow_num+1):
        if index == 1:
            result = result
        else:
            result = result*base_num
    return result
print(rise_to_power(float(input('Input base number:')), int(input('Input power number:'))))
'''

# var2 better
def rise_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result
print(rise_to_power(2,3))

# todo   (2:47:13) 2D Lists & Nested Loops
print('\n\t\t\t\t\t\t2D Lists & Nested Loops'.upper())
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0])
print(number_grid[1][0])

for row in number_grid:
    print(row)
    print(f'row lengh - {len(row)}')
    for col in row:
        print(col)

# (2:52:41) Building a Translator
print('\n\t\t\t\t\t\tBuilding a Translator'.upper())

'''def translate (phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation += letter
    return translation

print(translate(input('Enter a phrase: ')))'''

#  (3:04:17) Try / Except
print('\n\t\t\t\t\t\tTry / Except'.upper())
'''
number = int(input('Enter a number: ')) # try enter text
print(number)
'''
try:
    value = 10/0
    number = int(input('Enter a number: ')) # try enter text
    print(number)
except ZeroDivisionError:
    print('Devided by zero.')
except ValueError:
    print('Invalid value.')

#(3:12:41) Reading Files
print('\n\t\t\t\t\t\tReading Files'.upper())
file = open('employees.txt','r')

print(file.readable())
print(file.readline())
print(file.readline())
#print(file.readlines())

for employee in file.readlines():
    print(employee)

file.close()

#(3:22:41) Writing Files
print('\n\t\t\t\t\t\tWriting Files'.upper())
file = open('employees.txt','a')
#file.write('\nObi-Wan Kenobi')

file2 = open('employees.txt2','w')

file.close()
file2.close()