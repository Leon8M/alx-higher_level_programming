#!/usr/bin/python3
"""
Module that contains the Node class.
"""


class Node:
    """
    Class that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the linked list.

        Raises:
            TypeError: If data is not an integer.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node.

        Returns:
            int: The data value of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list.

        Returns:
            Node: The next node.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If value is not None or a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a singly linked list instance with an empty head.

        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position.

        Args:
            value (int): The value to insert.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.

        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
