from pydorr.client import *

#client = Client(code='00000', echo="n")

class commands:
    """Załadowanie wszystkich komend"""


    def Term(self, code: Client.clientcodes, prefix=None, inputy=None):

        self.prefix = prefix
        Client.clientcodes.get(int(code))
        
        if prefix == None:
            while True:
                inputy = input(f"PyDorr Terminal>> ?")

        else:
            while True:
                inputy = input(f"PyDorr Terminal>> {self.prefix}")

#comms = commands()
#comms.App(code='00000', prefix="?")