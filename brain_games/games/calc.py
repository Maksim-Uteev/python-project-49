import random

GAME_TASK = 'What is the result of the expression?'


def calculation():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    math_operator = random.choice(['+', '-', '*'])
    question = f'{number_1} {math_operator} {number_2}'
    result = str(eval(question))
    return question, result
