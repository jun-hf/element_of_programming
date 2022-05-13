"""
Given a string "Hello_World!"

Which translate to 
  e       _      l
H   l   o   W   r   d
      l       o       !

You need to return from left-right from top to bottom

return = 'e_lHloWrdlo!'

Design:
If you have notice you just for every 4 letter for top, you print the number, for middle is every , and bottom is 4
"""

def snake_string(str):
    return str[1::4] + str[::2] + str[3::4]