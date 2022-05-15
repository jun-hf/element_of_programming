class LinkedStack:
    """
    LIFO Stack implementation using a singly linked list for storage.
    """

    # nested _Node class
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    # stack methods
    def __init__(self):
        """
        Create an empty stack
        """
        self._head = None
        self._size = 0
    
    def __len__(self):
        """
        Return the number of elements in the stack.
        """
        return self._size

    def is_empty(self):
        """
        Return if the stack is empty
        """
        return self._size == 0
    
    def push(self, e):
        """
        Add element e to the top of the stack
        """
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """
        Return the top of the element of the stack
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self._head._element

class Empty(Exception):
    """
    Empyt class to raise message you put into Empty
    """

    def __init__(self, message):
        """
        Create an empty class
        """
        self.message = message


L1 = LinkedStack()
L1.top()