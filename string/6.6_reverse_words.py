"""
Given a string (array) "Hello I am You", return the reverse string "You I am Hello"

Desgin:
You can first reverse the whole string to "uoY ma I olleH"

Then you can reverse the individuals string

input: ['H', 'e', 'l', 'l', ' ', 'I', ' ', 'C', 'a','t']
def reverseStr(arr):
    # define a functions that take in a str arr and start and finish index and reverse it
    def reverse():
        pass

    # call reverse() to reverse the whole array
    # ['t', 'a', 'C', ' ', 'I', ' ', ' ', 'l', 'l', 'e', 'H']
    # [Cat ]

    # reverse individual words and use ' ' as a separator

"""

def reverseString(arr):
    def reverse(arr_strings, start, end):
        while start < end:
            arr_strings[start], arr_strings[end] = arr_strings[end], arr_strings[start]
            start += 1
            end -= 1
    
    # reverse the whole array
    reverse(arr, 0, len(arr) -1 )

    # reverse individuals words
    start = 0 
    while True:
        finish = start
        while finish < len(arr) and arr[finish] != " ":
            print(start, finish)
            finish += 1
        if finish == len(arr):
            break

        reverse(arr, start, finish -1)
        start = finish + 1
    print(start)
    reverse(arr, start, len(arr) -1 )
    return arr
print(reverseString(['H', 'e', 'l', 'l', ' ', 'I', ' ', 'C', 'a','t']))
