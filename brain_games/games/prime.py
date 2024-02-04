import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    random_number = random.randint(-1, 40)

    question = f'{random_number}'
    correct_answer = 'yes' if is_prime(random_number) is True else 'no'

    return question, correct_answer


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
