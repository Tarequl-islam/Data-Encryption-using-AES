"""from array import array

msg = "abcc"
msg+= "0"*10

for i in range(255):
    print(chr(i), end=" ")
print(msg[2:])

a = array('B', [1, 2, 3, 4, 5])
print(a[2])

ch = 'M'

# Using chr()+ord()
# prints P
x = chr(ord(ch) + 3)

print("The incremented character value is : ", end="")
print(x)

print(msg)"""


try:
    path = input(r'Enter path of Image : ')
    key = int(input('Enter Key for encryption of Image : '))
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # open file for reading purpose
    fin = open(path, 'rb')

    # storing image data in variable "image" 
    image = fin.read()
    fin.close()

    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)
    mn = 1000
    mx = 0
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key

    print()
    # opening file for writting purpose
    fin = open(path, 'wb')

    # writing encrypted data in image
    fin.write(image)
    fin.close()
    print('Encryption Done...')
    print("min = ", mn, "max = ", mx)

except Exception:
    print('Error caught : ', Exception.__name__)
