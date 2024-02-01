import random

GAME_TASK = 'What number is missing in the progression?'


def calculation():
    number_1 = random.randint(0, 20)
    length_progression = 10
    step_progression = random.randint(0, 10)
    progression = [number_1 + i
                   * step_progression for i in range(length_progression)]
    mutable_element = random.randint(0, 9)
    new_progression = progression.copy()
    new_progression[mutable_element] = '..'
    result_new_progression = ' '.join(map(str, new_progression))
    question = f'{result_new_progression}'
    result = str(progression[mutable_element])
    return question, result
