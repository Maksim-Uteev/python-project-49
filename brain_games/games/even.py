import prompt
import random


def find_correct_answer():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if ((user_answer == 'yes') and (number % 2 == 0)) or ((user_answer == 'no') and (number % 2 != 0)):
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user_name}!')
        elif user_answer != 'yes' and number % 2 == 0:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {user_name}!")
            break
        elif user_answer != 'no' and number % 2 != 0:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!")
            break
