from itertools import combinations
exp59list = list()
for i in range(0,3):
  exp59list.append(input("Enter Value: "))
print("Original list:",exp59list)

def sublist(exp59list):
	sub = list()
	for i in range(0, len(exp59list)+1):
	  subt = [list(x) for x in combinations(exp59list, i)]
	  if len(subt)>0:
	    sub.extend(subt)
	print("Sub list :" ,sub)
sublist(exp59list)
