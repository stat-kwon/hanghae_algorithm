class Node:
    def __init__(self, data):
        self._data = data
        self._next = None


node = Node(3)
first_node = Node(4)
node._next = first_node

print(node._data)
print(node._next._data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print("cur is ", cur.data)
        cur.next = Node(data)

    def print_all(self):
        print("hihihi")
        cur = self.head
        while cur is not None:
            print(cur.data, end='')
            cur = cur.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()

