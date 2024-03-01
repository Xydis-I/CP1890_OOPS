from binarytree import build, bst
import treelib

nodes = [10, 5, 4, 20, 47, 67]

# building the binary tree
binary_tree_build = build(nodes)
binary_tree_bst = bst(height=4, is_perfect=True)

print("Binary Tree from the list:\n", binary_tree_bst)
