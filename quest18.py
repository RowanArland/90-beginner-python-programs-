num1 = int(input("Enter a Number:"))
num2 = int(input("Enter a Number that you want to divide the previous number with:"))
def div(num1,num2):
    if num1==0 or num2==0:
        print("Incorrect values")
    elif (num1%num2==0):
        print("Numbers are completely divisible")
    else:
        print("Numbers are not completely divisible")
div(num1,num2)
