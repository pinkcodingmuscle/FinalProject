from string import ascii_letters, digits

CIPHER_KEY = "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
ALPHABET = digits + ascii_letters

def encode_message(message) -> str:
    # iterate through message
    cipher_text = ""
    for i in message:
        if i in ALPHABET:
            position = ALPHABET.index(i) # 17
            result = CIPHER_KEY[position]
            cipher_text += result
        else:
            cipher_text += i
    return cipher_text

def decode_message(cipher_text) -> str:
    message = ""
    for i in cipher_text:
        if i in CIPHER_KEY:
            position = CIPHER_KEY.index(i)
            result = ALPHABET[position]
            message += result
        else:
            message += i
    return message    