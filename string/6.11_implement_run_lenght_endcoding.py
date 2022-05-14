"""
Messages decode and encoding.

"3e2c" = "eeecc"
"eeecc" = "3e2c"

"""
def decoder(str):
    count, s = 0, []
    for i in range(len(str)):
        if str[i].isdigit():
            count = int(str[i])
        else:
            s.append(count*str[i])
            count = 0
    return ''.join(s)

def encode(st):
    count, result , char = 0, [], st[0]
    for i in range(len(st)):
        if st[i] == char:
            count += 1
        else:
            result.append(str(count) + char)
            count = 1
            char = st[i]
    result.append(str(count) + char)
    return ''.join(result)

print(type([]))



print(decoder('2d3c'))
print(encode('eeecc'))


