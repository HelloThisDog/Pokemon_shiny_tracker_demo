#the base for the pokemon so I don't have to repeat myself

class Pokemon:
    
    def __init__(self, name, level, colors):
        self._name = name
        self._level = level
        self._colors = colors