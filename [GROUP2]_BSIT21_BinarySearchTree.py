import os
class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def Insert(self, value):
        new_node = self.Node(value)
        if not self.root:
            self.root = new_node
            return self
        
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
    
    def Contains(self, value):
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False
    
    def Remove(self, value):
        current_node = self.root
        parent_node = None

        while current_node and current_node.value != value:
            parent_node = current_node
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        try:
            if not current_node:
                raise Exception("Value not found in the tree")
        except Exception as e:
            print(e)
            return self
        has_left = current_node.left is not None
        has_right = current_node.right is not None

        if not has_left and not has_right:
            return self.remove_leaf_node(current_node, parent_node)
        elif has_left and not has_right:
            return self.remove_node_with_one_child(current_node, parent_node)
        elif not has_left and has_right:
            return self.remove_node_with_one_child(current_node, parent_node)
        else:
            return self.remove_node_with_two_child(current_node, parent_node)
        
    def remove_leaf_node(self, node, parent):
        if parent is None:
            self.root = None
        elif parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None
        else:
            try:
                raise NotImplementedError("RemoveNoChildren is not implemented")
            except NotImplementedError as e:
                print(e)
                return self
        print(f"Removed leaf node with value: {node.value}")
        return self
    
    def remove_node_with_one_child(self, node, parent):
        child = node.left if node.left else node.right
        if parent is None:
            self.root = child
        elif parent.left == node:
            parent.left = child
        elif parent.right == node:
            parent.right = child
        else:
            try:
                raise NotImplementedError("RemoveOneChild is not implemented")
            except NotImplementedError as e:
                print(e)
                return self
        print(f"Removed node with one child with value: {node.value}")
        return self
        
    
    def remove_node_with_two_child(self, node, parent):
        successor_parent = node
        successor = node.right

        while successor.left:
            successor_parent = successor
            successor = successor.left

        node.value = successor.value

        if successor_parent.left == successor:
            successor_parent.left = successor.right
            return self
        else:
            successor_parent.right = successor.right
            return self
        try:
            raise NotImplementedError("RemoveTwoChildren is not implemented")
        except NotImplementedError as e:
            print(e)
            return self
        print(f"Removed node with two children with value: {node.value}")
        return self
    
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

def tryparse(value):
    try:
        return int(value)
    except ValueError:
        return None

if __name__ == "__main__":
    bst = BinarySearchTree()
    cont = "Y"
    while cont == "Y":
        while True:
            choice = input("What do you want to do:\n1. Insert\n2. Contains\n3. Remove\n4. Display\nEnter choice (1-4): ")
            choice = tryparse(choice)
            if choice is None or choice < 1 or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
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
                elif choice == 4:
                    bst.InOrder()
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        cont = input("Type (Y) to continue: ").upper()
        os.system('cls')
    