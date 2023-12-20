#!/usr/bin/python3
"""Singly linked list module"""

class Node:
    def __init__(self, data, next_node=None):
        """Constructor.

        Args:
            data (int): Node data of type integer.
            next_node (Node, optional): Pointer to the next node in the list.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data from node

        Returns: returns the data from the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): New value for the data.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node or None: Retrieve the next node in the list.

        Returns: the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Args:
            value (Node or None): New value for the next node.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        """Constructor for SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): Value for the new Node.
        """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """String representation of the linked list.

        Returns:
            str: String representation of the linked list.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

