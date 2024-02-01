import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculation():
    question = random.randint(1, 100)
    result = is_even(question)
    return question, result


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
