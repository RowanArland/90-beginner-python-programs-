number = int(input("Enter the number to check whether it is  even or odd :"))
def check(number):
        if((number%2)==0):
                print("{0} is even ".format(number))
        else:
                print("{0} is odd".format(number))
check(number)
