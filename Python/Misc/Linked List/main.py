class Node:
    def __init__(self, data, current=None, next=None):
        self.data = data
        self.current = current
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        ll_rep = ''
        curr = self.head
        while curr:
            ll_rep += str(curr.get_data()) + ' -> '
            curr = curr.get_next()
        ll_rep += 'None'
        return ll_rep

    def at(self, index):
        value = None
        if index < self.size():
            curr_i = 0
            curr = self.head
            found = False
            while found is False:
                if curr_i == index:
                    value = curr.get_data()
                    found = True
                else:
                    curr = curr.get_next()
                    curr_i += 1
        return value

    def prepend(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        if curr:
            for i in range(self.size()-1):
                curr = curr.get_next()
            curr.set_next(new_node)
        else:
            self.head = new_node

    def size(self):
        counter = 0
        curr = self.head
        while curr:
            counter += 1
            curr = curr.get_next()
        return counter

    def remove(self, val):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == val:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

if __name__ == '__main__':
    # Define empty singly linked list
    LL = LinkedList()

    # Testing singly linked list
    print(LL.at(0))
    LL.append(12)
    LL.prepend(23)
    LL.append(34)
    LL.prepend(4)
    print(LL.at(1))
    print(LL)
    LL.remove(23)
    LL.remove(4)
    print(LL)
