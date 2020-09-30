exp53list = list()
for i in range(0,8):
  exp53list.append(int(input("Enter Integer Value : ")))
print("My List :",exp53list)
def secSmallest(exp53list): 
    length = len(exp53list) 
    exp53list.sort()
    print("Sorted List :" ,exp53list)
    print("Second Smallest element is:", exp53list[1])  
secSmallest(exp53list) 
