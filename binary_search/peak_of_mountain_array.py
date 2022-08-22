'''
A mountain array is defined as an array that:

1) has at least 3 elements

2) has an element with the largest value called "peak", with index k.
The array elements monotonically increase from the first element to A[k],
and then monotonically decreases from A[k + 1] to the last element of the array.
Thus creating a "mountain" of numbers.

3) That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k.
Note that the peak element is neither the first nor the last element of the array.

Find the index of the peak element. Assume there is only one peak element.

Input: 0 1 2 3 2 1 0
Output: 3
Explanation: the largest element is 3 and its index is 3.
'''

from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    left_index, right_index = 0, len(arr)-1
    target_index = -1

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        if arr[mid_index-1] <= arr[mid_index]:
            target_index = mid_index
            left_index = mid_index+1
        else:
            right_index = mid_index-1

    return target_index


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
