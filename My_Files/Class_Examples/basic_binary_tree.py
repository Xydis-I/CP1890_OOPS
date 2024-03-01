from dataclasses import dataclass


@dataclass
class Node:
    data: object
    left: object = None
    right: object = None


class BinaryTree:
    root: Node = None

    def add(self, data) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_node(data, self.root)

    def _add_node(self, data, node):
        if data < node.data:
            if node.left:
                self._add_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._add_node(data, node.right)
            else:
                node.right = Node(data)

    def print_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.left)
            print(node.data, end="->")
            self._view_tree(node.right)


tree = BinaryTree()
tree.add(10)
tree.add(3)
tree.add(20)
tree.add(15)
tree.add(25)

tree.print_tree()
