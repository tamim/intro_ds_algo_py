class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node is not None:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)

    def append(self, data):
        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return

        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node
        node.prev = current_node

    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(data, None, first_node)
        self.head.next = new_node
        if first_node is not None:
            first_node.prev = new_node

    def search(self, item):
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None

    def remove_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head.next = node.next

        if node.next is not None:
            node.next.prev = node.prev 

    def remove(self, item):
        node = self.search(item)
        if node is None:
            return
        self.remove_node(node)
