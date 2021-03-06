import util.db_helper


class Node(object):  # node for each item in linked list
    def __init__(self, name=None, price=None, next_node=None):
        self.name = name
        self.price = price
        self.next_node = next_node

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, name, price):
        new_node = Node(name, price)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, name):  # search through linked list based on name
        current = self.head
        found = False
        while current and found is False:
            if current.get_name() == name:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("name not in list")
        return current

    def delete(self, name):  # deletes node and restructures list to remove node
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_name() == name:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("name not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print(self):  # print function for testing
        curr = self.head
        while curr:
            print(str(curr.name) + ": " + str(curr.price) + "\n")
            curr = curr.get_next()

    def to_lists(self):  # provides a list of the names and the prices of the items in the linked list
        curr = self.head
        info_list = []
        while curr:
            info_list.append([curr.name, curr.price])
            curr = curr.get_next()
        return info_list

    def total(self):
        # creates totals of the items in the list
        # with non taxed and taxed based on NJ sales tax(configurability coming later)
        curr = self.head
        total_value = 0
        while curr:
            total_value = total_value + float(curr.price)
            curr = curr.get_next()
        taxed_total = total_value * 1.06625
        return round(total_value, 2), round(taxed_total, 2)
