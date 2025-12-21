#!/usr/bin/python3

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #count = 0
        #for i, num in enumerate(nums):
        #    if num == val:
        #        count += 1
        count = nums.count(val)  # does same as above anyway
        for _ in range(count):
            nums.remove(val)
        return len(nums) 


class Solution_2:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)


if __name__ == '__main__':
    tests = {
        1: {"nums": [3,2,2,3], "val": 3},
        2: {"nums": [0,1,2,2,3,0,4,2], "val": 2},
        3: {"nums": [3,2,2,3], "val": 3},
        4: {"nums": [0,1,2,2,3,0,4,2], "val": 2},
    }

    print("SOLUTION 1")
    print(f"Nums before: {tests[1]["nums"]}")
    print(f"Nums before: {tests[2]["nums"]}")
    ans1 = Solution().removeElement(**tests[1])
    ans2 = Solution().removeElement(**tests[2])
    print(f"Nums after: {tests[1]["nums"]}")
    print(f"Nums after: {tests[2]["nums"]}")

    print("SOLUTION 2")
    print(f"Nums before: {tests[3]["nums"]}")
    print(f"Nums before: {tests[4]["nums"]}")
    ans3 = Solution_2().removeElement(**tests[3])
    ans4 = Solution_2().removeElement(**tests[4])
    print(f"Nums after: {tests[3]["nums"]}")
    print(f"Nums after: {tests[4]["nums"]}")
