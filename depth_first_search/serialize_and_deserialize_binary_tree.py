from typing import Optional, List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Optional[Node]) -> str:
    tree_as_list_string: List[str] = []
    NONE_STRING: str = "x"

    def dfs(node: Optional[Node]):
        if node is None:
            tree_as_list_string.append(NONE_STRING)
            return None

        tree_as_list_string.append(str(node.val))
        dfs(node=node.left)
        dfs(node=node.right)

    dfs(node=root)

    return " ".join(tree_as_list_string)


def deserialize(tree_as_string: str) -> Node:
    def dfs(tree_as_iterable: iter):
        node_value: str = next(tree_as_iterable)
        if node_value == "x":
            return None
        left_node: Optional[Node] = dfs(tree_as_iterable)
        right_node: Optional[Node] = dfs(tree_as_iterable)
        return Node(val=int(node_value), left=left_node, right=right_node)

    tree_as_iterable: iter = iter(tree_as_string.split())
    return dfs(tree_as_iterable)


if __name__ == "__main__":

    def build_tree(nodes):
        val = next(nodes)
        if not val or val == "x":
            return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur

    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)

    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(" ".join(print_tree(new_root)))
