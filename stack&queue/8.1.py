class ArrayStack:
    """LIFO Stack implementation using Python list as underlying storage"""

    def __init__(self):
        "Create an empty stack."
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        "Return True if stakc is empty."
        return len(self._data) == 0
    
    def push(self, e):
        "Add element e to the top of the stack."
        self._data.append(e)
    
    def top(self):
        "Return the top of the element."
        return self._data[-1]
    
    def pop(self):
        "Remove the top of the stack."
        return self._data.pop()