#the base for the pokemon so I don't have to repeat myself
class Pokemon:
    
    def __init__(self, name, level, colors):
        self.name = name
        self.level = level
        self.colors = colors
    
    def to_dict(self):
        return {'name': self.name, 'level': self.level, 'colors': self.colors}