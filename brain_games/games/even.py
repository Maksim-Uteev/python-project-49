import prompt
import random


def find_correct_answer():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if is_even(random_number) == user_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{is_even(random_number)}'.")
            print(f"Let's try again, {user_name}!")
            break


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
