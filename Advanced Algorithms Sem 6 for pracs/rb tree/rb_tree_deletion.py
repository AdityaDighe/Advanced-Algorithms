class node:
    def __init__(self, value, colour, left, right, parent):
        self.value = value
        self.colour = colour
        self.left = left
        self.right = right
        self.parent = parent

def remove_node(node):
    parent = node.parent

    if node == parent.left:
        parent.left = None
    else:
        parent.right = None

def delete_node_case1(node):
    remove_node(node)

    return False # for case 1 no DB node is formed

def delete_node_case2():
    global db_node

    # just remove double black from node
    db_node = node(None, None, None, None, None)

def delete_node(value):
    global root_node
    global db_node
    current_parent = root_node
    current_value = value
    node_found = False
    node_to_delete = node(None, None, None, None, None)
    
    while not node_found: # traverse to get the node for current value, then delete
        if current_value == current_parent.value:
            node_to_delete = current_parent
            node_found = True

            # if node to delete is not a leaf node, below process happens
            # swap node value with either smallest element in its right sub-tree (inorder successor) 
            # or largest element in its left sub-tree (inorder predecessor)
            temp_node = node_to_delete
            if node_to_delete.left is not None: # inorder predecessor
                temp_node = node_to_delete.left
                while temp_node.right is not None:
                    temp_node = temp_node.right
            elif node_to_delete.right is not None: # inorder successor
                temp_node = node_to_delete.right
                while temp_node.left is not None:
                    temp_node = temp_node.left

            # swap values of nodes
            temp_node.value, node_to_delete.value = node_to_delete.value, temp_node.value
            # update node to delete
            node_to_delete = temp_node
            db_node = node_to_delete

        elif current_value < current_parent.value:
            current_parent = current_parent.left
        else:
            current_parent = current_parent.right

    db_node_exists = True # every time when we delete a node, we get a DB node, once deletion is complete DB node is gone
    is_node_deleted = False

    while db_node_exists:
        # case 1 - when node is red and leaf
        if node_to_delete.colour == 'R' and node_to_delete.left is None and node_to_delete.right is None:
            db_node_exists = delete_node_case1(node_to_delete)

        # case 2 - when root node is DB node
        elif db_node == root_node:
            db_node_exists = delete_node_case2()


def print_tree(node, indent=0, prefix="root"):
    if indent == 0:
        print()
    if node is not None:
        print("|" * indent + "--" * indent + f"{'' if indent == 0 else ' '}" + f"{prefix}: {node.value} {node.colour}")
        print_tree(node.left, indent + 1, "left")
        print_tree(node.right, indent + 1, "right")



#tree
db_node = node(None, None, None, None, None)
root_node = node(55, 'B',None,None,None)
n1 = node(27,'B',None,None,root_node)
n2 = node(66,'R',None,None,root_node)
n3 = node(19,'R',None,None,n1)
n4 = node(51,'R',None,None,n1)
n5 = node(57,'B',None,None,n2)
n6 = node(83,'B',None,None,n2)
n7 = node(72,'R',None,None,n6)

root_node.left = n1
root_node.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n6.left = n7

print("Initial tree:")
print_tree(root_node)
print()

while True:
    print("Action Menu:")
    print("1. Delete node and print tree")
    print("2. Stop")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter node value: "))
        
        delete_node(value)
        print_tree(root_node)

        print()
    elif choice == 2:
        print("Node deletion complete")
        break

    else:
        print("Invalid input!\n")
