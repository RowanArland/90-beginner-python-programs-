num1 = int(input("Enter First Number:"))
num2 =int(input("Enter Second Number:"))
def swapp(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    print("First Number:",num1)
    print("Second Number:",num2)
swapp(num1,num2)
