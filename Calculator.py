print("\n    Welcome to Simple Calculator...\n\n")

a = float(input("Enter First Number : "))

b = float(input("Enter Second Number : "))

print("Select Operation :")

print("1 : Addition")
print("2 : Subtraction")
print("3 : Multiplication")
print("4 : Division")

s = int(input("\nEnter Choice : "))

if(s > 4 or s < 1):
    print("Invalid Choice")
print("\n\n Calculating Result...")

# Declaring a Flag Variable for verifying In division if denominator is Zero or Not.

flg = 0  

if(s == 1):
    res = a + b
    symbol = "+"
elif(s == 2):
    res = a - b
    symbol = "-"
elif(s == 3):
    res = a * b
    symbol = "*"
elif(s == 4):
    if(b == 0):
        print("Invalid Input... Can Not Perform Operaation.")
        flg = 1

    else:
        res = a / b
        symbol = "/"

if(flg == 0):
    print("\n " ,a , symbol , b , " = " , res , "\n\n\n")