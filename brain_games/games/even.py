import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculation():
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    result = is_even(random_number)
    return question, result


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
