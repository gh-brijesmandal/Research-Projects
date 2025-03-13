message = input("Enter a string message to decode: ")
encode_value = int(input("Enter a value to encode this message: "))
result = ""


for i in message:
    if i.isalpha():
        if i.isupper():
            # range 65-90
            value = ord(i) + encode_value
            if value > 90:
                value = 64+(value - 90)
                result = result + chr(value)
            else:
                result = result + chr(value)
        else:
            # range 97 - 122
            value = ord(i) + encode_value
            if value > 122:
                value = 96+(value - 122)
                result = result + chr(value)
            else:
                result = result + chr(value)
    else:
        result = result + i  

print("The encoded string is ",result)