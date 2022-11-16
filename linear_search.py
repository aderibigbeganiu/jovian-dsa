# from jovian.pythondsa import evaluate_test_cases

def linear_search(cards, query):
    """LINEAR SEARCH"""
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
    return -1