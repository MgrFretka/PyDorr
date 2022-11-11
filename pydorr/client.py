
class Client:

    clientcodes = {37654: 'advdev', 73645: 'begdev', 00000: 'newclient'}

    def __init__(self, token, code=None, echo=None):

        self.echo = echo
        self.code = code #print(Client.clientcodes.get(int(code)))
        self.token = token

    def check_echo(self):
        """Sprawdzanie czy echo ma być włączone"""
        if self.echo == "n":
            #print("Echo off!")
            pass
        else:
            #print("Echo on!")
            pass
    
    def run(self=None):
        with open('pydorr/data/tokens.txt', 'r') as rtf:
            if self.token == rtf:
                print('Good!')
            if self.token != rtf:
                print("NONONNONNONO")

#ma = Client(code="00001", echo="n")
#Client.check_echo(ma)