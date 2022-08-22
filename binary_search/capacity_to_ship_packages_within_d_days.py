'''
There are n packages that needs to be transported from one city to another, and you need to transport
them there within d days. For the ith package, the weight of the package is weights[i].
You are required to deliver them in order with a rental truck. The rental trucks come in different sizes.
The bigger trucks have greater weight capacity but cost more to rent. To minimize cost, you want to deliver
the packages in one truck once per day, with a weight capacity as small as possible to save on rental cost.
What is the minimum weight capacity of the truck that is required to deliver all packages within d days?

Inputs:
weights: A list of packages and their weights.
d: The number of days to deliver all packages.

Output:
The minimum weight capacity of the truck.

Examples

Input:
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 5
Output: 15

Explanation:
The first day we deliver the first 5 package.
The second day we deliver the next 2, and for each following days, we deliver 1.
The maximum weight delivered on each day is 15, so we can have a truck with a capacity of 15.
This value is the minimum.
'''

from typing import List


def is_weight_feasible(weights: List[int], d: int, possible_weight: int) -> bool:
    req_days = 1
    capacity = possible_weight
    i = 0

    while i < len(weights):
        if weights[i] <= capacity:
            capacity -= weights[i]
            i += 1
        else:
            capacity = possible_weight
            req_days += 1
    return req_days <= d


def min_max_weight(weights: List[int], d: int) -> int:
    # Create list with possible truck weights
    min_weight = max(weights)
    max_weight = sum(weights)
    possible_truck_capacities = list(range(min_weight, max_weight+1))

    # Set up for bisection algorithm
    left_index, right_index = 0, len(possible_truck_capacities)-1
    target_index = 0

    while left_index <= right_index:
        midpoint_index = (left_index+right_index)//2
        if is_weight_feasible(weights, d, possible_truck_capacities[midpoint_index]):
            target_index = midpoint_index
            right_index = midpoint_index-1
        else:
            left_index = midpoint_index+1

    return possible_truck_capacities[target_index]


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)
