from .node import Node


class Sequenceable(object):
    def __init__(self):
        self.start = None 
        self.end = None

    def get_elements(self):
        element_list = []
        the_node = self.start
        
        while the_node is not None:
            element_list.append(the_node.value)
            the_node = the_node.next 
        return element_list


class Appendable(object):
    def append(self, element):
        the_input = Node(element)
        
        if self.start is not None:
            self.end.next = the_input
        else: 
            self.start = the_input
        self.end =  the_input #I don't understand this self.end = the_input
        

class Popable(object):
    def pop(self):
        if self.start is None:
            raise IndexError
        answer = self.start.value
        self.start=self.start.next
        return answer
        
        

class Pushable:
    def push(self, element):
        some_node = Node(element)
        
        if self.start is None:
            self.start = some_node
            self.end = self.start #by setting self.end to self.start (which is = None) is it making sure you don't add n2, n3?
        else:
            some_node.next = self.start #is this setting the next value to None so it doesn't append n1,n2,n3?
            self.start = some_node