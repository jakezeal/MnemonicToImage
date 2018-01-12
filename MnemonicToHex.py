#!/usr/bin/env python

import sys
import base64


def get_argument_inputs():
    # TODO: Take other inputs (.txt files, etc.)
    return sys.argv[1:]


def list_to_string(word_list):
    return ' '.join(word_list)


def hash_word_list(words_string):
    # words_hash = hashlib.sha256(words_string).hexdigest()
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(words_string, AES.MODE_CFB, iv)
    words_hash = iv + cipher.encrypt(b'Attack at dawn')
    words_hash.encode("hex")

    return words_hash

def add_zeros_to_hex(words_hex):
    # TODO: Add 2 zeros if there are 12 words, or 0 zeros if there are 24 words
    words_hex = "00" + words_hex
    return words_hex

def hex_to_hex_codes_list(hex_string):
    # Every six characters, create an array of hex color values
    hex_colors = []
    empty_string = ""
    counter = 0

    for character in hex_string:

        empty_string += character
        counter += 1

        if counter % 6 == 0:
            hex_colors.append(empty_string)
            empty_string = ""
        
    return hex_colors

# convert string to hex
def string_to_hex(string):
   return string.encode("hex")

# convert hex repr to string
def hex_to_string(string):
    return string.decode("hex")


if __name__ == '__main__':
    # Get mnemonic seed
    mnemonic_list = get_argument_inputs()

    # Convert mnemonic to string
    mnemonic_string = list_to_string(mnemonic_list)
    print '\nmnemonic input string:', mnemonic_string

    # Convert mnemonic string to hex
    mnenonic_hex = string_to_hex(mnemonic_string)
    print '\nmnenonic in hex:', mnenonic_hex

    # Convert mnemonic hex back to string (for testing)
    mnemonic_string = hex_to_string(mnenonic_hex)
    print '\nmnemonic string from hex (for testing):', mnemonic_string

    # Add zeros to hex (if necessary such as with 12 words) in order to have complete list
    final_mnenonic_hex = add_zeros_to_hex(mnenonic_hex)
    print '\nnmnenonic in hex with zeros:', final_mnenonic_hex

    # Create list of hex codes that can be used as colors
    hex_codes_list = hex_to_hex_codes_list(final_mnenonic_hex)
    print '\nmnemonic hex codes (can be used for colors):', hex_codes_list
    print '\nNumber of hex codes:', len(hex_codes_list)

# Notes:
# - Case insensitive

# TODO: 
# - Add PyPNG library to create and save image from hex values
