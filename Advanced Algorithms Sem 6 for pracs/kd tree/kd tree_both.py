class Node:
    def __init__(self,point):
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
        root.left = insertRec(root.left, point, depth+1)
    else:
        root.right = insertRec(root.right,point,depth+1)

    return root

def insert(root, point):
    return insertRec(root,point,0)

def printTree(root, depth=0, prefix='Root:'):
    if root:
        print("  "*depth + prefix,root.point)
        printTree(root.left,depth+1,"L:")
        printTree(root.right,depth+1,"R:")

def median(points,axis):
    sorted_points = sorted(points, key = lambda x: x[axis])
    median_index = len(sorted_points)//2
    return sorted_points[median_index],median_index

def build_balanced_kd_tree(points,depth=0):
    if not points:
        return None
    
    axis = depth%k
    median_point, median_index = median(points,axis)
    node= Node(median_point)
    node.left = build_balanced_kd_tree(points[:median_index],depth+1)
    node.right = build_balanced_kd_tree(points[median_index+1:],depth+1)

    return node

if __name__ =='__main__':
    root = None
    k=int(input("Enter the dimension of the tree: "))
    points = []

    n=int(input("Enter the number of nodes to be inserted: "))
    print("Enter the nodes:")
    for i in range(n):
        temp=[]
        print("For node ",i,": ")
        for j in range(k):
            temp.append(int(input(f'Enter the {j+1}th dimension: ')))
        points.append(temp)
        root = insert(root,points[i])

    print("Unbalanced KD tree: ")
    printTree(root)    


    points.sort()
    root = build_balanced_kd_tree(points)
    print("\nBalanced KD tree: ")
    printTree(root)
