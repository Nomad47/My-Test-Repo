# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 08:17:19 2022

@author: mathr
"""

class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)

class LList(object):
    def __init__(self):
        self.head = None
        self.current = None
        self.size = 0

    def insert(self, node):
        if self.head is not None:
            # set new node's pointer to old head
            node.nextNode = self.head
        self.head = node
        self.size += 1

    def __len__(self):
        return self.size

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        current = self.current
        if current is None:
            raise StopIteration
        else:
            self.current = current.nextNode
            return current

    def printLL(self):
        for i, node in enumerate(self, 1):
            print(node, i)

    # print the list backwards
    def reverse_print(self):
        c = len(self)
        for node in reversed(list(self)):
            print(node, c)
            c -= 1


# main program
mylist = LList()
mylist.insert(Node("NJ"))
mylist.insert(Node("NR"))
mylist.insert(Node("OH"))

print(len(mylist))

# print forwards
mylist.printLL()

#print the nodes using a list comprehension
print([str(node) for node in mylist])

#print in reverse
mylist.reverse_print()
