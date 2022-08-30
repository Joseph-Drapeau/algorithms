from typing import Tuple, Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced_tree_helper(node: Optional[Node]) -> Tuple[bool, int]:
    if node is None:
        return True, 0

    left_bal, left_height = balanced_tree_helper(node.left)
    right_bal, right_height = balanced_tree_helper(node.right)

    return (left_bal and right_bal and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1)


def is_balanced(node: Optional[Node]) -> bool:
    return balanced_tree_helper(node)[0]


# this function builds a tree from input
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == "__main__":
    node = build_tree(iter(input().split()), int)
    res = is_balanced(node)
    print("true" if res else "false")
