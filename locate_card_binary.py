from jovian.pythondsa import evaluate_test_cases

def locate_card_binary(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        mid_number = cards[mid]
        print(
        "lo: ",
        lo,
        "\n" "hi: ",
        hi,
        "\n" "mid: ",
        mid,
        "\n" "mid_number: ",
        mid_number,
    )

        if query == mid_number:
            return mid
        elif query < mid_number:
            hi = mid - 1
        elif query > mid_number:
            lo = mid + 1
    return -1

tests = [
    {"input": {"cards": [1, 4, 5, 6, 7, 9, 10, 24], "query": 5}, "output": 2},
    {"input": {"cards": [1, 4, 5, 5, 6, 7, 9, 10, 24], "query": 5}, "output": 2},
    {"input": {"cards": [], "query": 5}, "output": -1},
]

evaluate_test_cases(locate_card_binary, tests)
