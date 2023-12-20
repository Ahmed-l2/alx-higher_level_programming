#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    def __init__(self, data, next_node=None):
        """Constructor.

        Args:
            data: Node data of type integer
            next_node: pointer to next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """String representation of the linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return ('\n'.join(result))
