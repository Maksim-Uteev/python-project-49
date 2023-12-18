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
        number_1 = random.randint(0, 20)
        length_progression = 10
        step_progression = random.randint(0, 10)
        progression = [number_1 + i
                       * step_progression for i in range(length_progression)]
        mutable_element = random.randint(0, 9)
        new_progression = progression.copy()
        new_progression[mutable_element] = '..'
        result_new_progression = ' '.join(map(str, new_progression))
        print(f'Question: {result_new_progression}')
        user_answer = int(prompt.string('Your answer: '))
        if user_answer == progression[mutable_element]:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(
                f"{user_answer} is wrong answer ;(. Correct answer was {progression[mutable_element]}.\nLet's try again, {user_name}!")
            break


find_correct_answer()
