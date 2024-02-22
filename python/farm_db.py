import pickle
from farm.models import Farm

with open("ml/new_farm.p","rb") as fr:
    data = pickle.load(fr)

for name, values in data.items() :
    f = Farm(name=name, address=values[0], coord=values[1])
    f.save()