from Pokemon_class import Pokemon
import json

p1 = Pokemon("Bulbasaur", 5, "whole body green")

save = json.dumps(p1.to_dict())

print(save)