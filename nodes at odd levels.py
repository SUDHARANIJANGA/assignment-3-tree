class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    # If empty tree
    if (root == None):
        return
 
    # If current node is of odd level
    if (isOdd):
        print(root.data, end = " ")
 
    # Recur for children with isOdd
    # switched.
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
# Driver code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)
    