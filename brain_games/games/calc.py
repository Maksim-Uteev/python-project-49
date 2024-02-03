import random
import operator

GAME_TASK = 'What is the result of the expression?'


def get_game():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }
    random_key_operator, random_operator = random.choice(
        list(operators.items()))
    question = f'{number_1} {random_key_operator} {number_2}'
    result = str(random_operator(number_1, number_2))
    return question, result
