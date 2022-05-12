"""
Given a string '19216811', return a the possible combination of the ip address. 

An ip addres, has four parts, with 3 period. and each number is i < 256

'19216811'
Design:
first you design a functions that check if the given number is valid number. i.e if the number i < 256,
speacial case '00' this is invalid, however '0' is valid

second you want to find a way to split your string into diffrent combinations of strings
'1.9.2.16811' , invalid
19.216.8.11, invalid
1.9.2.

"""

def ip_converter(str):
    def is_valid_number(s):
        return len(s) == 1 or (s[0] != '0' and int(s) < 256)
    
    result, parts = [], [''] *4 

    for i in range(1, min(4, len(str))):
        parts[0] = str[:i]
        if is_valid_number(parts[0]):
            for j in range(1, min(4, len(str)-i)):
                parts[1] = str[i:i+j]
                if is_valid_number(parts[1]):
                    for k in range(1, min(4, len(str) -j-i)):
                        parts[2], parts[3] = str[i+j:i+j+k], str[i+j+k:]
                        if is_valid_number(parts[2]) and is_valid_number(parts[3]):
                            result.append('.'.join(parts))
    
    return result

print(ip_converter('19216811'))