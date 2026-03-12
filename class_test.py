from Counter import Count
import json

p1 = Count

save = json.dumps(p1.to_dict())

print(save)