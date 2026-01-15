#for clearing terminal
import os
#Binary Search Tree function
class BinarySearchTree:
    #Creating Nodes
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    #Creating the BST
    def __init__(self):
        self.root = None

    #Inserting values
    def Insert(self, value):
        new_node = self.Node(value)
        #If tree is empty
        if not self.root:
            self.root = new_node
            return self
        #Traversing the tree and inserting the value
        current_node = self.root
        while value != current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self
    
    #Checking if a value exists in the tree
    def Contains(self, value):
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                #This means we found the value
                return True
        #Value not found
        return False
    
    #Removing a value from the tree
    def Remove(self, value):
        #Initializing the node to remove and its parent
        current_node = self.root
        parent_node = None
        #Finding the node to remove
        while current_node and current_node.value != value:
            parent_node = current_node
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        #Handling the case where the value is not found
        try:
            if not current_node:
                raise Exception("Value not found in the tree")
        except Exception as e:
            print(e)
            return self
        #Determining the number of children
        has_left = current_node.left is not None
        has_right = current_node.right is not None
        #Removing based on the number of children
        if not has_left and not has_right:
            return self.remove_leaf_node(current_node, parent_node)
        elif has_left and not has_right:
            return self.remove_node_with_one_child(current_node, parent_node)
        elif not has_left and has_right:
            return self.remove_node_with_one_child(current_node, parent_node)
        else:
            return self.remove_node_with_two_children(current_node)
        
    #Removing Node With No Children
    def remove_leaf_node(self, node, parent):
        if parent is None:
            self.root = None
        elif parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None
        else:
            #If we reach here, something went wrong
            try:
                raise NotImplementedError("RemoveNoChildren is not implemented")
            except NotImplementedError as e:
                print(e)
                return self
        print(f"Removed leaf node with value: {node.value}")
        return self
    
    #Removing Node With One Child
    def remove_node_with_one_child(self, node, parent):
        #Determine the child node
        child = node.left if node.left else node.right
        #Re-link the parent to the child
        if parent is None:
            self.root = child
        elif parent.left == node:
            parent.left = child
        elif parent.right == node:
            parent.right = child
        else:
            #If we reach here, something went wrong
            try:
                raise NotImplementedError("RemoveOneChild is not implemented")
            except NotImplementedError as e:
                print(e)
                return self
        print(f"Removed node with one child with value: {node.value}")
        if parent:
            print(f"And relinked its child ({child.value}) to parent ({parent.value})")
        return self
        
    #Removing Node With Two Children
    def remove_node_with_two_children(self, node):
        #Finding the in-order successor (smallest in the right subtree)
        successor_parent = node
        successor = node.right
        predecessor_parent = node
        predecessor = node.left
        original_node = node.value
        #Finding successor and predecessor
        while successor.left:
            successor_parent = successor
            successor = successor.left
        while predecessor.right:
            predecessor_parent = predecessor
            predecessor = predecessor.right
        #Deciding whether to use predecessor or successor
        if (original_node - predecessor.value) < (successor.value - original_node):
            node.value = predecessor.value
            if predecessor_parent.left == predecessor:
                predecessor_parent.left = predecessor.left
            elif predecessor_parent.right == predecessor:
                predecessor_parent.right = predecessor.right
            else:
                #If we reach here, something went wrong
                try:
                    raise NotImplementedError("RemoveTwoChildren is not implemented")
                except NotImplementedError as e:
                    print(e)
                    return self
            print(f"Removed node with two children with value: {original_node}, replaced with predecessor value: {predecessor.value}")
        else:
            node.value = successor.value
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            elif successor_parent.right == successor:
                successor_parent.right = successor.right
            else:
                #If we reach here, something went wrong
                try:
                    raise NotImplementedError("RemoveTwoChildren is not implemented")
                except NotImplementedError as e:
                    print(e)
                    return self
            print(f"Removed node with two children with value: {original_node}, replaced with successor value: {successor.value}")
        return self
    
    #Displaying the tree in InOrder Traversal
    def InOrder(self):
        result = []
        def _inorder(n):
            if not n:
                return
            _inorder(n.left)
            result.append(n.value)
            _inorder(n.right)
        _inorder(self.root)
        print("InOrder:", result)

#Helper function to parse input
def tryparse(value):
    try:
        return int(value)
    except ValueError:
        return None

#Main program loop
if __name__ == "__main__":
    #Creating the BST instance
    bst = BinarySearchTree()
    cont = "Y"
    #Looping until user decides to stop
    while cont == "Y":
        #Input validation loop
        while True:
            choice = input("What do you want to do:\n1. Insert\n2. Contains\n3. Remove\n4. Display\nEnter choice (1-4): ")
            choice = tryparse(choice)
            if choice is None or choice < 1 or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            #Valid choice
            else:
                #Insert value
                if choice == 1:
                    while True:
                        val = input("Enter value to insert: ")
                        val = tryparse(val)
                        if val is None:
                            print("Invalid input. Please enter an integer value.")
                        else:
                            bst.Insert(val)
                            print(f"{val} inserted.")
                            break
                    break
                #Contains value
                elif choice == 2:
                    while True:
                        val = input("Enter value to check: ")
                        val = tryparse(val)
                        if val is None:
                            print("Invalid input. Please enter an integer value.")
                        else:
                            if bst.Contains(val):
                                print(f"{val} is in the tree.")
                            else:
                                print(f"{val} is not in the tree.")
                            break
                    break
                #Remove value
                elif choice == 3:
                    while True:
                        val = input("Enter value to remove: ")
                        val = tryparse(val)
                        if val is None:
                            print("Invalid input. Please enter an integer value.")
                        else:
                            bst.Remove(val)
                            break
                    break
                #Display tree
                elif choice == 4:
                    bst.InOrder()
                    break
                #Invalid choice (should not reach here)
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        #Asking if user wants to continue, either Y or y, if any other input, exit
        cont = input("Type (Y) to continue: ").upper()
        #Clear the terminal for better readability
        os.system('cls')
    