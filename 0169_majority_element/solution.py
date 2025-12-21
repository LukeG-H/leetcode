#!/usr/bin/python3

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            if num not in counts.keys():
                counts[num] = 0
            counts[num] += 1
        return max(counts)

    def test_results(self, expected: int, actual: int) -> None:
        print(f"Expected: {expected}, Actual: {actual}")
        assert expected == actual


if __name__ == '__main__':
    tests = {
        1: {"nums": [3,2,3], "expected": 3},
        2: {"nums": [2,2,1,1,1,2,2], "expected": 2},
    }

    ans1 = Solution().majorityElement(tests[1]["nums"])
    ans2 = Solution().majorityElement(tests[2]["nums"])
    Solution().test_results(tests[1]["expected"], actual=ans1)
    Solution().test_results(tests[2]["expected"], actual=ans2)
