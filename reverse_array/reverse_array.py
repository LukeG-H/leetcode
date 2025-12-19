#!/usr/bin/python3
import copy

class Solution:
    def reverse_array(self, array: list[int]) -> list[int]:
        length = len(array)
        start = 0 
        end = (length - 1)

        while start < end:
            tmp = array[start]
            array[start] = array[end]
            array[end] = tmp
            start += 1
            end -= 1

        return array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    array_copy = copy.deepcopy(array)

    print(f"Array before:      {array}")
    print(f"Luke's solution:   {Solution().reverse_array(array)}")

    print(f"Array Copy before: {array_copy}")
    array_copy.reverse()
    print(f"Python's solution: {array_copy}")
