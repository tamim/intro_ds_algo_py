class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node is not None:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = Node(None, node)
            return

        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node

    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def insert(self, data, new_data):
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break
            current_node = current_node.next 

    def search(self, item):
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next
        while current_node is not None:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return None
        
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next
