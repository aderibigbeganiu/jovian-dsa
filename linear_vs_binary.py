import binary_search
import linear_search
from jovian.pythondsa import evaluate_test_case

l = list(range(0, 100000000))
large_test = {"input": {"cards": l, "query": 99999998}, "output": 99999998}

print("Binary search")
evaluate_test_case(binary_search.binary_search, large_test)
print("Linear search")
evaluate_test_case(linear_search.linear_search, large_test)