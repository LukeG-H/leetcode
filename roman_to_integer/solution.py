#!/usr/bin/python3

NUMERALS = {
   "I": 1,
   "V": 5,
   "X": 10,
   "L": 50,
   "C": 100,
   "D": 500,
   "M": 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        print(f"\nRoman Numeral: {s}")
        values_seen = {}
        result = 0

        n = len(s)
        prev_value = 0  # initialise ptr to keep track of prev value
        for i in range(n-1, -1, -1): # loop through string backwards -> smalles to largest numbers
            numeral = s[i]
            value = NUMERALS[numeral]

            if value < prev_value:
                match (value, prev_value):
                    case (1, 5 | 10):
                        values_seen[prev_value - 1] = values_seen.pop(prev_value)
                    case (10, 50 | 100):
                        values_seen[prev_value - 10] = values_seen.pop(prev_value)
                    case (100, 500 | 1000):
                        values_seen[prev_value - 100] = values_seen.pop(prev_value)
                continue

            if value not in values_seen.keys():
                values_seen[value] = 0
            values_seen[value] += 1
            prev_value = value

        for value, multiplier in values_seen.items():
            print(f"+ {value} * {multiplier}")
            result += value * multiplier
            print(f"Running total = {result}")
        
        print(f"{s} = {result}")
        return result


if __name__ == '__main__':
    tests = {
        1: {"s": "III"},
        2: {"s": "LVIII"},
        3: {"s": "MCMXCIV"},
        4: {"s": "MMXXIV"},
    }

    ans1 = Solution().romanToInt(tests[1]["s"])
    ans2 = Solution().romanToInt(tests[2]["s"])
    ans3 = Solution().romanToInt(tests[3]["s"])
    ans4 = Solution().romanToInt(tests[4]["s"])

"""
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
"""
