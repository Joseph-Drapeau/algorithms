from typing import Optional
import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: Optional[Node]) -> bool:
    def dfs(node: Optional[Node], min_value: int, max_value: int) -> bool:
        if node is None:
            return True

        if min_value <= node.val <= max_value:
            left_bool: bool = dfs(node=node.left, min_value=min_value, max_value=node.val)
            right_bool: bool = dfs(node.right, min_value=node.val, max_value=max_value)
            return left_bool and right_bool
        else:
            return False

    return dfs(node=root, min_value=-math.inf, max_value=math.inf)


# this function builds a tree from input
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print("true" if res else "false")
