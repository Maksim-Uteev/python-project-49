import random

GAME_TASK = 'What number is missing in the progression?'
LENGHT_PROGRESSION = 10


def get_game():
    start_number = random.randint(0, 20)
    step_progression = random.randint(1, 10)
    stop_number = start_number + LENGHT_PROGRESSION * step_progression
    progression = list(range(
        start_number, stop_number, step_progression))
    mutable_element = random.randint(0, LENGHT_PROGRESSION - 1)
    new_progression = progression.copy()
    new_progression[mutable_element] = '..'
    result_new_progression = ' '.join(map(str, new_progression))
    question = f'{result_new_progression}'
    result = str(progression[mutable_element])
    return question, result
