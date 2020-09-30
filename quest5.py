num1= int(input("Enter a number:"))
num2= int(input("Enter a number:"))
def switch(num1,num2):
    num1, num2 = num2 , num1
    print(num1,num2)
switch(num1,num2)
