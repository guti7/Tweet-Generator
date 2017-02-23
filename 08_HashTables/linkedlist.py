 #!python
""" linked lists module."""
from __future__ import print_function


class Node(object):
    """"Node class for linked lists."""

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):
    """Linked List Class."""

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any."""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        if self.is_empty():
            return 0

        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
        # return len(self.as_list(self))

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        if self.is_empty():
            # newNode = Node(item)
            self.head = Node(item)
            self.tail = self.head
        else:  # one or many nodes
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        new_head = Node(item)
        if self.is_empty():
            self.tail = new_head
        new_head.next = self.head
        self.head = new_head

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        # check for empty linked list
        if self.is_empty():
            raise ValueError('Empty Linked List.')

        current = self.head
        # first node
        if current.data == item:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return

        # traverse nodes
        while current.next is not None:
            if current.next.data == item:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next
        # not found after traversing whole list
        return ValueError('Item was not found')

        # current = self.head
        # previous = None
        # while current:
        #     if current.data == item:
        #         if previous:  # not at the first node
        #             if current.next is None:  # current node is the tail
        #                 self.tail = previous
        #             previous.next = current.next  # set previous to next node
        #         else:  # only when you first start the traversing
        #             self.head = current.next
        #             if self.head is None:
        #                 self.tail = self.head
        #         return
        #     else:  # move to next node
        #         previous = current
        #         current = current.next
        # raise ValueError('Item not found')

    def find(self, quality):
        """Return an item from linked list satisfying the given quality."""
        # traverse
        # TODO: how to call with just a string, instead of function/lambda.
        current = self.head
        while current:
            if quality(current.data):
                return current.data
            current = current.next
        return None  # if not found


def test_linked_list():
    """Test linked list class."""
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
