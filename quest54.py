exp54list = list()
for i in range(0,8):
  exp54list.append(int(input("Enter Integer Value : ")))
print("My List :",exp54list)
def secLargest(exp54list): 
    length = len(exp54list) 
    exp54list.sort()
    print("Sorted List :" ,exp54list)
    print("Second Largest element is:", exp54list[length-2])  
secLargest(exp54list) 
