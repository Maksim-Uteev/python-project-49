import random

GAME_TASK = 'What number is missing in the progression?'
LENGHT_PROGRESSION = 10


def get_question_and_answer():
    start_number = random.randint(0, 20)
    step_progression = random.randint(1, 10)
    stop_number = start_number + LENGHT_PROGRESSION * step_progression
    hidden_index = random.randrange(LENGHT_PROGRESSION)

    progression = list(range(
        start_number, stop_number, step_progression))

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
