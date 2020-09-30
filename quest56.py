import collections
exp56list = list()
for i in range(0,8):
  exp56list.append(int(input("Enter Integer Value : ")))
print("Original List : ",exp56list)
freq = collections.Counter(exp56list)
print("Frequency of the elements in the List : ",freq)
