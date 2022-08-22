'''
Given a sorted array of integers and a target integer, find the first occurrence of the target
and return its index. Return -1 if the target is not in the array.

Input:

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
Output: 1

Explanation: First occurrence of 3 is at index 1.

Input:

arr = [2, 3, 5, 7, 11, 13, 17, 19]
target = 6
Output: -1

Explanation: 6 does not exists in the array.
'''

from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    left_index, right_index = 0, len(arr)-1
    boundary_index = -1

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        if arr[mid_index] == target:
            boundary_index = mid_index
            right_index = mid_index-1
        elif arr[mid_index] > target:
            right_index = mid_index-1
        else:
            left_index = mid_index+1

    return boundary_index


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
