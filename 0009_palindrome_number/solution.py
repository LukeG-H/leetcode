#!/usr/bin/python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        start = 0 
        end = len(string) - 1

        while start < end:
            if not string[start] == string[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    tests = {
        1: {"x": 121},
        2: {"x": -121},
        3: {"x": 10},
        4: {"x": 1001},
        5: {"x": 101010},
        6: {"x": 1010101},
    }

    ans1 = Solution().isPalindrome(tests[1]["x"])
    ans2 = Solution().isPalindrome(tests[2]["x"])
    ans3 = Solution().isPalindrome(tests[3]["x"])
    ans4 = Solution().isPalindrome(tests[4]["x"])
    ans5 = Solution().isPalindrome(tests[5]["x"])
    ans6 = Solution().isPalindrome(tests[6]["x"])
    print(f"Expected: True  | Result: {ans1}")
    print(f"Expected: False | Result: {ans2}")
    print(f"Expected: False | Result: {ans3}")
    print(f"Expected: True  | Result: {ans4}")
    print(f"Expected: False | Result: {ans5}")
    print(f"Expected: True  | Result: {ans6}")
