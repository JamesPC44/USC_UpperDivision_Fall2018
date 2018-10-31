from pdb import set_trace

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 1
        self.size = 1

class Tree(object):
    def __init__(self):
        self.root = None

    def insert_and_count(self, val):
        if self.root is None:
            self.root = Node(val)
            return 0
        current_node = self.root
        last_node = self.root
        count = 0
        while not current_node is None and current_node.val != val:
            last_node = current_node
            current_node.size += 1
            if val < current_node.val:
                current_node = current_node.left
            elif val > current_node.val:
                count += current_node.count
                if not current_node.left is None:
                    count += current_node.left.size
                current_node = current_node.right
        if not current_node is None:
            count += current_node.count
            if not current_node.left is None:
                count += current_node.left.size
            current_node.count += 1
            current_node.size += 1
        else:
            new_node = Node(val)
            if val < last_node.val:
                last_node.left = new_node
            if val > last_node.val:
                last_node.right = new_node

        return count

            

def main():
    n = int(input())
    tree = Tree()
    for _ in range(n):
        age = int(input())
        print(tree.insert_and_count(age))
    

if __name__ == "__main__":
    main()
