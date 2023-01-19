
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

#(3:28:41) Modules & Pip
print('\n\t\t\t\t\t\tModules & Pip import func from another file'.upper())

import main_Copy_for_import

print(main_Copy_for_import.monthConversions)

from student import student
student1 = student('Jim','Art',3.1, False)
student2 = student('Pam','Business',2.1, False)
student3 = student('Bob','Art',5.0, True)
print(student1.gpu)
print(student3.name)

# todo    (3:57:37) Building a Multiple Choice Quiz !!!!! you should understand it
#(3:57:37) Building a Multiple Choice Quiz !!!!! you should understand it
print('\n\t\t(3:57:37) Building a Multiple Choice Quiz !!!!! you should understand it'.upper())

question_promts=[
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]

from question import Question

questions=[
    Question(question_promts[0],'a'),
    Question(question_promts[1],'c'),
    Question(question_promts[2],'c')
]


'''score = 0
for question in questions:
    print(question.prompt)
    answer = input('Enter your answer: ')
    if answer == question.answer:
        print("Correct answer!")
        score+=1
'''

'''#better
def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer==question.answer:
            score+=1
    #print('You got '+ str(score)+'/'+str(len(questions))+' correct')
    print(f'You got {score}/{len(questions)} correct')

run_test(questions)
'''
print(student1.on_honor_roll())

#    (4:12:37) Inheritance class
print('\t\t\t\t Inheritance'.upper())

from Chef_4_12_Inheritance import Chef

myChef = Chef()
myChef.make_special_dish()

#TASKS

#implement the calculate_profit function that accepts 3 parameters:
# amount — the initial amount that we deposit;
# percent — annual interest rate;
# period — the number of years (the time for which the money is deposited).
# The function should calculate and return the total net profit for the entire period.
def calculate_profit(amount: int, percent: float, period: int) -> float:
    # write your code here

    if period == 0:
        return 0

    else:
        base_amount = amount
        full_income = 0
        for i in range(period):
            full_income = amount + amount * percent / 100
            amount = full_income

        return full_income - base_amount

print(calculate_profit(12500, 3, 12))

# Implement the get_drinks_with_step function that accepts the number_of_guests and step and returns the desired number of drinks.
# if step = 1, then, as before, each incoming guest says a toast;
# if step = 2, then 1st, 3rd, 5th, and so on;
# if step = 3, then 1st, 4th, 7th, 10th, and so on.

def get_drinks_with_step(number_of_guests: int, step: int) -> int:
    # write your code here
    if number_of_guests > 0:
        start = 1
    else:
        start = 0
    total = 0
    for i in range(start, number_of_guests + 1, step):
        total +=i
    return(total)

print(get_drinks_with_step(10, 3))

# Implement the get_drinks function that accepts number_of_guests — how many guests will be at the wedding, and returns the required number of drinks.
# when the first guest arrives — we need only 1 drink;
# when the second one comes — we need 2 more drinks;
# the third — 3 more drinks and so on.
# If there are 5 guests, then we need 15 drinks in total (1 + 2 + 3 + 4 + 5).
# If 10, then 55 drinks (1 + 2 + 3 + ... + 10).

def get_drinks(number_of_guests: int) -> int:
    # write your code here
    total = 0
    for i in range(number_of_guests + 1):
        total +=i
    return(total)
print(get_drinks(6))

# Complete function print_numbers that accepts integer n and prints numbers form 0 to n - 1 inclusive.
def print_numbers(n: int) -> None:
    #  write your code here
    for i in range(n):
        print(i)
print_numbers(3)

# Write the remove_vowels function that accepts the document string and returns a string with all the letters from the document except the vowels.

def remove_vowels(document: str) -> str:
    # write your code here
    new_text = ''
    for char in document:
        if char.lower() not in 'aeiouy':
            new_text += char
        else:
            new_text = new_text
    return(new_text)
print(remove_vowels("I like my boss"))

# In this task, implement the make_abbr function that accepts the words string and returns an uppercase abbreviation.
# The words string contains one or more words separated by a single space. And if the words does not have any character, return an empty string.
def make_abbr(words: str) -> str:
    # write your code here
    if len(words) > 0:
        text = words[0].upper()
        for index, char in enumerate(words):
            if char == ' ':
                text+=words[index+1].upper()

    else:
        text= ''
    return(text)
print(make_abbr("national aeronautics space administration"))

# Create the is_werewolf function that accepts the target string and returns True if it's a werewolf or False if it isn't.
# A werewolf is a word or sentence that you can read the same in both directions (left to right and vice versa), ignoring case, spaces, and punctuation.
def is_werewolf(target: str) -> bool:
    # write your code here
    text= ''
    for char in target:
        if char not in ' ,!?.':
            text +=char.lower()
        else:
            text = text
    return(text==text[::-1])
print(is_werewolf("red rum sir is murder"))

# Implement the parity_checker function that:
#
# using the input function, reads a number entered by a user;
# prints the "Even" string if the number is even or "Odd" if the number is odd.
# In the input function, pass the "What number do you want to check?" message to make it clear to the user what information they need to enter.
#
# Please note:
#
# if a user entered 0 — print "Even";
# the function should not return anything, so use only print.

def parity_checker() -> None:
    # write your code here
    number = input("What number do you want to check?")
    print ('Odd' if int(number)%2 >0 else 'Even')

# LIST
# write the is_sorted function that accepts the list of numbers — box_numbers, and returns True if all numbers are in ascending order or False otherwise.
#
# Please note: numbers in the list can be repeated.
def is_sorted(box_numbers: list) -> bool:
    # write your code here
    return(True if sorted(box_numbers) == box_numbers else False)
print(is_sorted([1, 2, 3, 4, 5]))

# For example, we have the coordinates = [2, 1] and commands = ["left", "back", "back"] lists:
#
# coordinates after the first command — [1, 1] (1 step left);
# coordinates after the second command — [1, 0] (1 step back);
# coordinates after the third command — [1, -1] (1 step back);
# the result is the [1, -1] list.

def get_location(coordinates: list, commands: list) -> list:
    # write your code here
    for command in commands:
        if command == "right":
            coordinates[0] += 1
        elif command == "left":
            coordinates[0] -= 1
        elif command == "forward":
            coordinates[1] += 1
        elif command == "back":
            coordinates[1] -= 1
    return coordinates
print(get_location([2, 3], ["back", "back", "back", "right"]))

# the goal for the next month is based on the previous month.
#
# If the number of robots is a fraction, round it down using the math.floor
# the first goal is 200 + 50% = 300 robots;
# the second is 300 + 50% = 450 robots;
# and the third one is 450 + 50% = 675 robots.
# The resulting list is [300, 450, 675].
import math


def get_plan(current_production: int, month: int, percent: int) -> list:
    # write your code here
    result=[]
    for i in range(month):
        result.append(math.floor(current_production * (1+percent/100)))
        current_production = math.floor(current_production * (1+percent/100))
    return(result)
print(get_plan(1000, 6, 20))

# Implement the get_speed_statistic function, that accepts the test_results list of robots' speeds and returns statistics as a list with 3 numbers:
#
# the first one is the lowest speed;
# the second is the highest speed;
# the last one is the average speed, rounded down (use math.floor).
# Please note: if the test_results list is empty, return [0, 0, 0].

def get_speed_statistic(test_results: list) -> list:
    # write your code here
    if len(test_results) >=1:
        lowest = test_results[0]
        highest = test_results[0]
        summ = 0
    for index, elem in enumerate(test_results):
        if elem > highest:
            highest = elem
        if elem < lowest:
            lowest = elem
        summ = summ + elem
        avg = math.floor(summ/len(test_results))
    return([0,0,0] if len(test_results) ==0 else [lowest,highest,avg])





