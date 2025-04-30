from typing import List, Dict

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    if length <= 0 or not prices or len(prices) < length:
        raise ValueError("Некоректні вхідні дані")

    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):  # довжина стрижня
        for j in range(1, i + 1):  # розріз на довжину j
            if j <= len(prices):
                if dp[i - j] + prices[j - 1] > dp[i]:
                    dp[i] = dp[i - j] + prices[j - 1]
                    cuts[i] = cuts[i - j] + [j]

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1
    }

# --- Тестування ---
def test_tabulation():
    tests = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "expected_profit": 12
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "expected_profit": 8
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "expected_profit": 12
        }
    ]

    for test in tests:
        result = rod_cutting_table(test["length"], test["prices"])
        print(f"\nСтрижень {test['length']} | Ціни: {test['prices']}")
        print(f"Макс прибуток: {result['max_profit']}")
        print(f"Розрізи: {result['cuts']}")
        print(f"К-сть розрізів: {result['number_of_cuts']}")
        assert result["max_profit"] == test["expected_profit"]

if __name__ == "__main__":
    test_tabulation()
