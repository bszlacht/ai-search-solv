#TODO: Typowanie
#TODO: Zdefiniować klasę `State`
#TODO: Uogólniamy klasę `State` czy będzie ona zdefioniowana pod każdy problem w swoim folderze? => Inspiracja z linku numer jeden <- README.md

"""
`State` inicjalizacyjnie powinien zamienić nam naszego startowego configa na stan początowy.
"""

class State(object):
    def __init__(self, parent, *args):
        self.parent = parent

    def __str__(self) -> str:
        return "Current state " + str(self.parent)