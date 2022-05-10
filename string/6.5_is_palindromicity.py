"""
Given a string "Hello, I am beth" check if the string is a palidrome. 

For a solution that uses constant space you can use two pointer one at the end and one at the front and onlyu compare aplabet charcters
ones the front and back is not aline, you return false
"""

def is_pand(str):
    pointer_i, pointer_j = 0, len(str) -1

    while pointer_i > pointer_j:
        while not str[pointer_i].isalnum() and pointer_i < pointer_j:
            pointer_i += 1
        while not str[pointer_j].isalnum() and pointer_i < pointer_j:
            pointer_j -= 1
        
        if str[pointer_i] != str[pointer_j]:
            return False
        
        pointer_i += 1
        pointer_j -= 1
    return True