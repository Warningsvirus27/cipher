def encrypt(string):
    if len(string) < 2:
        raise Exception("Input String too small, Must be more than 2")
    result = string[-1]
    for i in string:
        while len(string) > 1:

            temp = ord(string[-1]) + ord(string[-2])
            string = string[:-2] + chr(temp)

            result = string[-1] + result

    return result[:-1] + chr(ord(result[-1]) + ord(result[0]))


def decrypt(string):
    if len(string) < 2:
        raise Exception("Input String too small, Must be more than 2")
    result = chr(ord(string[-1]) - ord(string[0]))
    string = string[:-1] + result

    for i in string:
        while len(string) > 1:

            temp = ord(string[-2]) - ord(string[-1])
            result = chr(temp) + result

            string = string[:-1]
    return result


inp_string = input("Enter the string : ")

encrypt_string = encrypt(inp_string)
print(encrypt_string)

decrypt_string = decrypt(encrypt_string)
print(decrypt_string)
