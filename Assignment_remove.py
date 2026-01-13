class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def Insert(self, value):
        new_node = Node(value)
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
        parent_node = None
        current_node = self.root

        if value < self.root.value:
            while current_node and current_node.value != value:
                parent_node = current_node
                if value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
        
        elif value > self.root.value:
            while current_node and current_node.value != value:
                parent_node = current_node
                if value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

        if not current_node:
            return self

        if current_node.left and current_node.right:
            successor_parent = current_node
            successor = current_node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            current_node.value = successor.value
            current_node = successor
            parent_node = successor_parent
            
        child = current_node.left if current_node.left else current_node.right

        if not parent_node:
            self.root = child
        elif parent_node.left == current_node:
            parent_node.left = child
        else:
            parent_node.right = child
        
        return self
    
    def display(self):
        if not self.root:
            print("Tree is empty.")
            return
        node_list = [self.root]
        
        display_list = []

        while node_list:
            node = node_list.pop()

            display_list.append(node.value)

            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
        
        print("Binary Search Tree:", display_list)
            
                
cont = "Y"
bst = BinarySearchTree()
while cont == "Y":
    choice = int(input("What do you want to do:\n1. Insert\n2. Contains\n3. Remove\n4. Display\nEnter choice (1-4): "))
    if choice == 1:
        val = int(input("Enter value to insert: "))
        bst.Insert(val)
        print(f"{val} inserted.")
    elif choice == 2:
        val = int(input("Enter value to check: "))
        if bst.Contains(val):
            print(f"{val} is in the tree.")
        else:
            print(f"{val} is not in the tree.")
    elif choice == 3:
        val = int(input("Enter value to remove: "))
        bst.Remove(val)
        print(f"{val} removed if it was present.")
    elif choice == 4:
        bst.display()
    
    cont = input("Type (Y) to continue: ")
