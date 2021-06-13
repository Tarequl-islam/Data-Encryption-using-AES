from array import array

msg = "abcc"
msg+= "0"*10
print(msg[2:])

a = array('B', [1, 2, 3, 4, 5])
print(a[2])

ch = 'M'

# Using chr()+ord()
# prints P
x = chr(ord(ch) + 3)

print("The incremented character value is : ", end="")
print(x)

print(msg)
