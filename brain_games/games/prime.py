import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculation():
    random_number = random.randint(-1, 40)
    question = f'{random_number}'
    result = is_prime(random_number)
    return question, result


def is_prime(number):
    if number <= 1:
        return 'no'
    else:
        for i in range(2, number):
            if number % i == 0:
                return 'no'
        return 'yes'
