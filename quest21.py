def compare(temp):
    if(temp < -273.15):
        print("Temperature is Invalid!")
    elif(-273.15 == temp):
        print("Temperature is Absolute zero!")
    elif(-273.15<temp<0):
        print("Temperature is below Freezing point!")
    elif(temp==0):
        print("Temperature is at Freezing point!")
    elif(0<temp<100):
        print("Temperature is in normal range!")
    elif(temp==100):
        print("Temperature is at boiling point!")
    elif(temp>100):
        print("Temperature is above Boiling point!")
temp = float(input("Enter Temperature(Celsius):"))
compare(temp)
