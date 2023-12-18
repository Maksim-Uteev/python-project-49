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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(-1, 8)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if is_prime(random_number) == user_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(
                f"{user_answer} is wrong answer ;(. Correct answer was {is_prime(random_number)}.\nLet's try again, {user_name}!")
            break


def is_prime(number):
    if number <= 1:
        return "no"
    else:
        for i in range(2, number):
            if number % i == 0:
                return "no"
        return "yes"


find_correct_answer()
