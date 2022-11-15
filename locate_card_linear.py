from jovian.pythondsa import evaluate_test_cases

def locate_card_linear(cards, query):

    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
    return -1


tests = [
    {"input": {"cards": [1, 4, 5, 6, 7, 9, 10, 24], "query": 5}, "output": 2},
    {"input": {"cards": [1, 4, 5, 5, 6, 7, 9, 10, 24], "query": 5}, "output": 2},
    {"input": {"cards": [], "query": 5}, "output": -1},
]

evaluate_test_cases(locate_card_linear, tests)