from jovian.pythondsa import evaluate_test_cases, evaluate_test_case


def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif mid_number > query:
        return "left"
    else:
        return "right"

def locate_card_binary(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1

tests = [
    {"input": {"cards": [1, 4, 5, 6, 7, 9, 10, 24], "query": 5}, "output": 2},
    {"input": {"cards": [1, 4, 5, 5, 6, 7, 9, 10, 24], "query": 5}, "output": 2},
    {"input": {"cards": [], "query": 5}, "output": -1},
]

evaluate_test_cases(locate_card_binary, tests)
