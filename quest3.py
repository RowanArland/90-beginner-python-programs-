num1= float(input("Enter a number:"))
num2= float(input("Enter a number:"))
num3= float(input("Enter a number:"))
def calculation(num1,num2,num3):
    s=((num1+num2+num3)/2)
    si=(s*(s-num1)*(s-num2)*(s-num3))**0.5
    print('area is:',s)
    print('semi perimeter is:',si)
calculation(num1,num2,num3)
