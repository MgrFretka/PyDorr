class Error:

    def __init__(self) -> None:
        pass

    def KeyError(self, key):
        self.key = key

        if key == '':
            key = 'i cant found error'

        keyerrormsg = f"KeyError:-> {key}"

        raise KeyError(keyerrormsg)