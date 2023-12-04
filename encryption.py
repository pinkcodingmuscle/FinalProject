"""
Final Project   
=======================
Course:   CS 5001

This module contains functions that deal with the encoding and decoding of messages.
"""

from string import ascii_letters, digits
# randomly generated cipher key 
CIPHER_KEY = "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
ALPHABET = ascii_letters + digits

def encode_message(message) -> str:
    """This function will encode a given string using the alphabet and cipher_key.
    Examples:
        >>> encode_message('Hello World')
        'nw11f cfq1D'

        >>> encode_message('An old silent pond..., A frog jumps into the pond—')
        'KQ f1D gz1wQb NfQD..., K Iqfr YZ7Ng zQbf bGw NfQD—'

        >>> encode_message("Santa's elevs at north pole!")
        "M0Qb0'g w1wHg 0b QfqbG Nf1w!"

    Args:
        message
    Returns:
        str: string containing the encoded text
    """
    # declare an empty string variable
    cipher_text = ""
    # iterate through message
    for i in message:
        if i in ALPHABET:
            position = ALPHABET.index(i) 
            result = CIPHER_KEY[position]
            cipher_text += result
        else:
            # takes into account punctuation
            cipher_text += i
    return cipher_text

def decode_message(cipher_text) -> str:
    """This function will decode a given string the cipher_key and alphabet.
    
    Examples:
        >>> decode_message("s8 M0Qb0'g w1Hwg 0b QfqbG Nf1w!")
        "13 Santa's elves at north pole!"

        >>> decode_message('K1fG0! - cfq1D')
        'Aloha! - World'

    Args:
        filename
    Returns:
        str: string containing the decoded text
    """
    # declare an empty string variable
    message = ""
    # iterate through the cipher text
    for i in cipher_text:
        if i in CIPHER_KEY:
            position = CIPHER_KEY.index(i)
            result = ALPHABET[position]
            message += result
        else:
            # takes into account punctuation
            message += i
    return message

if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)