'''
Given an integer, find its square root without using the built-in square root function.
Only return the integer part (truncate the decimals).

Input: 16
Output: 4

Input: 8
Output: 2

Explanation: square root of 8 is 2.83..., return integer part 2
'''


def square_root(n: int) -> int:
    if n == 0:
        return 0
    left_index, right_index = 1, n
    boundary_index = -1

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        if (mid_index * mid_index) <= n:
            boundary_index = mid_index
            left_index = mid_index+1
        else:
            right_index = mid_index-1

    return boundary_index


if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
