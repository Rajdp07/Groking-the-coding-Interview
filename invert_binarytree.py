class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    q = [root]
    while q:
        curr = q.pop(0)
        print(curr.val, end = ' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

def invertBST(root):
    q = [root]
    while q:
        curr = q.pop(0)
        # print(curr.val, end =' ')
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)



if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print('Before Inversion :- ')
    levelOrder(root)
    print('\n')
    print('After Inversion :- ')
    invertBST(root)

    levelOrder(root)

