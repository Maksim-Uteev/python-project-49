import random
import operator

GAME_TASK = 'What is the result of the expression?'


def get_game():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)

    math_operator, operation = random.choice([
        ("+", operator.add),
        ("-", operator.sub),
        ("*", operator.mul)
    ])

    question = f'{number_1} {math_operator} {number_2}'
    correct_answer = str(operation(number_1, number_2))

    return question, correct_answer
