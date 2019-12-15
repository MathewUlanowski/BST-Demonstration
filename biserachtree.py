# class for creating nodes with only an integer required
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val = key

# inserts a value into the BST as a node with null left and right pointers
def Insert(node, InsertingNode):
    if InsertingNode > node.val:
        if node.right is None:
            node.right = Node(InsertingNode)
        else:
            Insert(node.right, InsertingNode)
    elif InsertingNode < node.val:
        if node.left is None:
            node.left = Node(InsertingNode)
        else:
            Insert(node.left, InsertingNode)

# this is the node search function that seraches all of the children of the node for a given number
def BiSearch(number, node):
    if node.val == number:
        return True
    else:
        if number > node.val:
            if node.right is None:
                return False
            return BiSearch(number, node.right)
        elif number < node.val:
            if node.left is None:
                return False
            return BiSearch(number, node.left)
        return False


# class for creating the binary search tree
class BST:
    def __init__(self, rootval):
        self.root = Node(rootval)
    def Add(self, val):
        Insert(self.root, val)
    def search(self, val):
        return BiSearch(val, self.root)

newBST = BST(46)

# print(newBST.root.val)


# puts in some values from an arra
insertArr = [21,45,65,85,95,12,66,45,75,82]
for indexVal in insertArr:
    newBST.Add(indexVal)


# puts in all of the odd numbers from 1 to 1000 into the tree
for i in range(1,1000,2):
    newBST.Add(i)
    # print(i)

inputy = int(input("put in the value you want to search for\nvalue: "))
print(newBST.search(inputy))

