import random

min_val=1
max_val=6

Start_rolling = "Y"
Stop_rolling = "N" 

while Start_rolling == "Y" :
    print("Let's Roll The Dise:")
    print("The Value Is:")
    print(random.randint(min_val,max_val))

    Start_rolling = input("Want To Roll The Dice Again??")

while Start_rolling=="N":
    Stop_rolling=input("Stop Game !")