from binary.node import Node
from binary.binary_tree import BinaryTree
# left = Node(5)
# head = Node(9)
# right = Node(13)
#
# head.left = left
# head.right = right
#
# print(head)
# print(head.left)
# print(head.right)

# tree = BinaryTree(Node(9))
# tree.add(Node(5))
# tree.add(Node(11))
# tree.add(Node(13))
# tree.add(Node(3))
#
# tree.inorder()
# print("**____**____**")
# tree.preorder()
# print("**____**____**")
# print(tree.find(11))
# print("**____**____**")
# print(tree.find_parent(3))


tree = BinaryTree(Node(6))

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)
tree.inorder()