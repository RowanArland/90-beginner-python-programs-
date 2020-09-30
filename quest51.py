import random
exp51lsit = list()
exp51lsitsize = int(input("Enter List Size :"))
for i in range(0,exp51lsitsize):
    exp51lsit.append(input("Enter Value to list :"))
print("Exp 51 lsit :", exp51lsit)
print("Random Item from list :",random.choice(exp51lsit))
