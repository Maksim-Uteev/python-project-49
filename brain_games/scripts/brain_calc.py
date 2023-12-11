import prompt
import random


def say_welcome():
    print('Welcome to the Brain Games!')


say_welcome()


def welcome_user():
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


welcome_user()


def find_correct_answer():
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        i += 1
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        math_operator = random.choice(['+', '-', '*'])
        math_expression = f'{number_1} {math_operator} {number_2}'
        result_expression = eval(math_expression)
        print(f'Question: {math_expression}')
        user_answer = int(prompt.string('Your answer: '))
        if user_answer == result_expression:
            print('Correct!')
        else:
            print(
                f"{user_answer} is wrong answer ;(. Correct answer was {result_expression}.\nLet's try again, {user_name}!")
            break
    print(f'Congratulations, {user_name}!')


find_correct_answer()
