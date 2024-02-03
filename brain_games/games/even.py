import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    result = 'yes' if random_number % 2 == 0 else 'no'
    return question, result
