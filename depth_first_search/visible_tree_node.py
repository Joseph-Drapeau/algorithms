class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_tree_node(root: Node) -> int:
    def dfs(root: Node, greatest_value: int) -> int:
        if root is None:
            return 0

        is_visible: bool = False
        if greatest_value <= root.val:
            greatest_value = root.val
            is_visible = True

        left_value: int = dfs(root.left, greatest_value)
        right_value: int = dfs(root.right, greatest_value)

        return is_visible + left_value + right_value

    return dfs(root=root, greatest_value=root.val - 1)


# this function build a tree from input
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
