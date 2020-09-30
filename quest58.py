exp58list = list()
for i in range(0,8):
  exp58list.append(int(input("Enter Integer Value : ")))
print("Main List :",exp58list)
  
exp58list1 = list()
for i in range(0,3):
  exp58list1.append(int(input("Enter Integer Value : ")))
print("Second List:",exp58list1)

sub = "false"
if(set(exp58list1).issubset(set(exp58list))): 
    sub = "true"
       
if (sub == "true") : 
    print ("Second list is subset of the Main List.") 
else : 
    print ("Second list is not subset of the Main List.") 
