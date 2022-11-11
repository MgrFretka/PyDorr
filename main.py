#import pydorr
from pydorr.client import Client
from pydorr.extension.commands import commands
from pydorr.extension.tokenizer import Tokenizer
import unittest

class TestPyDorr(unittest.TestCase):

    def maintest(self):
        client = Client(code="00000", echo="n", token='973/mn#nx7Pvv+o\_&(Nw3')
        Client.check_echo(client)
        comman = commands()

        Tokenizer.read_token()

        comman.Term(code='00000')
        client.run()

if __name__ == '__main__':
    unittest.main()