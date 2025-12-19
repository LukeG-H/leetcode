#!/usr/bin/python3

class Solution:
    def dumb(self, nums: list[int], target: int) -> tuple[int, int] | None:
        """O(n^2)"""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return

    def two_sum_II(self, nums: list[int], target: int) -> tuple[int, int] | None:
        """O(n)"""
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return left, right
            elif sum > target:
                right -= 1
            else:
                left += 1
        return


if __name__ == '__main__':
    sorted_nums = [1, 3, 4, 6, 8, 11, 15]
    target = 10

    print(Solution().dumb(sorted_nums, target))
    print(Solution().two_sum_II(sorted_nums, target))

    tests = {
        1: {"numbers": [2,7,11,15], "target": 9},
        2: {"numbers": [2,3,4], "target": 6},
        3: {"numbers": [-1,0], "target": -1},
    }
    
    answer1 = Solution().two_sum_II(tests[1]["numbers"], tests[1]["target"])
    answer2 = Solution().two_sum_II(tests[2]["numbers"], tests[2]["target"])
    answer3 = Solution().two_sum_II(tests[3]["numbers"], tests[3]["target"])
    print(answer1)
    print(answer2)
    print(answer3)
