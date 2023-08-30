#!/usr/bin/python3


class Node:
    """Class that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """property to set data"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """property to retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property to set next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value



class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initializes the list"""
        self.__head = None

    def __str__(self):
        """prints nodes"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(current.data)
            current = current.next_node
        return '\n'.join(str(node) for node in nodes)

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in
        the list (increasing order)"""
        addNode = Node(value)
        if self.__head is None or value < self.__head.data:
            addNode.next_node = self.__head
            self.__head = addNode
            return
        ptr = self.__head
        while (ptr.next_node is not None and ptr.next_node.data < value):
            ptr = ptr.next_node
        addNode.next_node = ptr.next_node
        ptr.next_node = addNode
