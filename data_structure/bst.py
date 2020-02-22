class Node(object):
    def __init__(self, key:int):
        self.left_node = None
        self.right_node = None
        self.parent_node = None
        self.key = key

class BST(object):
    def __init__(self, root:Node):
        self.root = root
    
    def add_node(self, node:Node):
        current_node = self.root
        while True:
            if node.key == current_node.key:
                raise Exception('same key value is not allow !')
            elif node.key < current_node.key:
                if current_node.left_node:
                    current_node = current_node.left_node
                else:
                    node.parent_node = current_node
                    current_node.left_node = node
                    break
            elif node.key > current_node.key:
                if current_node.right_node:
                    current_node = current_node.right_node
                else:
                    node.parent_node = current_node
                    current_node.right_node = node
                    break

            
