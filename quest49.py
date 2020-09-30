import itertools
a = list()
a = ["a","r","e"]
b = list()
b = ["a",5,1]
c = list()
c = ["i","s"]
d = list()
d = ["h","e","r","e"]
exp49list = [a,b,c,d]
print("Initial List : ",exp49list)
Flattenedlist = list(itertools.chain(*exp49list))
print("List after merger(Flattning) is :",Flattenedlist)
