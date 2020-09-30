exp57list = list()
for i in range(0,8):
  exp57list.append(int(input("Enter Integer Value between 0 & 100: ")))
def listrange(exp57list , min, max):
	counter = 0
	for x in exp57list:
		if min <= x <= max:
			counter += 1
	return counter
print("Entered List : " , exp57list)
print("List after defining range (20 ,50 )is : " ,listrange(exp57list, 20, 50))

