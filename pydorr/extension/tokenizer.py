"""TEST"""

import string
import secrets
import os

class Tokenizer:

    token = ''

    def __init__(self) -> None:
        pass

    def MadeToken():

        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        Mtoken = letters + digits + symbols

        token_lenght = 22

        for i in range(token_lenght):
            Tokenizer.token += ''.join(secrets.choice(Mtoken))

        #print(Tokenizer.token)

    def save_token_in_file():

        with open('pydorr/data/tokens.txt', 'w') as tf:
            tf.write(Tokenizer.token)

    def read_token():

        with open('pydorr/data/tokens.txt', 'r') as rtf:
            read = rtf.read()
            print(read)

#Tokenizer.MadeToken()
#Tokenizer.save_token_in_file()