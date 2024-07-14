num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Press 1. for Addition \nPress 2. for Substraction \nPress 3. for Multiplication \nPress 4. for Division")

choice = int(input("Enter A Chioce:"))

if choice==1:
    print("Addition",num1+num2)
elif choice==2:
    print("Substraction",num1-num2)
elif choice==3:
    print("Multipliction",num1*num2)
elif choice==4:
    print("Division",num1/num2)
else:
    print("Invalid Input")