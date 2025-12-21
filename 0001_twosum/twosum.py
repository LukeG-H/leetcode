#!/usr/bin/python3

class Solution:
    def two_sum(self, nums: list[int], target: int) -> tuple[int, int]|None:
        compliments = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in compliments.keys():
                return compliments[compliment], i

            compliments[num] = i
        return


if __name__ == '__main__':
    nums = [2, 4, 7, 5]
    target = 6
    solved = Solution().two_sum(nums, target)
    print(solved)
