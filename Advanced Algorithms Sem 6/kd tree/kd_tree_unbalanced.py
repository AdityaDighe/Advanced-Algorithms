class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None
       
def newNode(point):
    return Node(point)
   
def insertRec(root, point, depth):
    if not root:
        return newNode(point)
 
    cd = depth % k
 
    if point[cd] < root.point[cd]:
        root.left = insertRec(root.left, point, depth + 1)
    else:
        root.right = insertRec(root.right, point, depth + 1)
 
    return root
   
def insert(root, point):
    return insertRec(root, point, 0)

def printTree(root, depth=0, prefix="Root:"):
    if root:
        print("  " * depth + prefix, root.point)
        printTree(root.left, depth + 1, "L:")
        printTree(root.right, depth + 1, "R:")
   
if __name__ == '__main__':
    root = None
    k = int(input("Enter the dimension of the tree: "))
    points = []
 
    n = int(input("Enter the number of nodes: "))
   
    print("\nEnter the nodes:")
    for i in range(n):
        temp = []
        print(f"\nFor node {i}:")
        for j in range(k):
            temp.append(int(input(f"Enter the {j+1}th dimension: ")))
        points.append(temp)
        root = insert(root, points[i])
   
    print("\nTree nodes:")
    printTree(root)
