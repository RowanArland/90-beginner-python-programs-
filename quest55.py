exp55list = list()
for i in range(0,8):
  exp55list.append(int(input("Enter Integer Value : ")))
def unique(exp55list): 
	uniquelist = list() 
	for i in exp55list: 
		if i not in uniquelist: 
			uniquelist.append(i) 
	print(uniquelist)
unique(exp55list)
