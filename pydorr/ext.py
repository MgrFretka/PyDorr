from client import *
from events.error import *

class Commands:
    """Zebranie wszystkich klas z innych modułóœ i poskładanie w proste komendy"""
    
    code = Client.clientcodes
    echo = 'y' or 'n'
    token = Client(code=None, echo='n', token='973/mn#nx7Pvv+o\_&(Nw3')

    def __init__(self) -> None:
        pass

    def Up(client: Client(code=code, echo=echo, token=token)):
        if Error.KeyError(key=client):
            print("To sie nie uda")

