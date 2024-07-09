import random

Letters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q'
          'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
Digits = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
Symbols = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '+' , '(' , ')' , '-' , '=' , '/' , '?' , '>' , '<']

print("  \n\nWelcome To The Password Generator!")

print("\nEnter The Details You Need In Your Password.")
Lcount = int(input("Number Of Letters: "))
Dcount = int(input("Number Of Digits :"))
Scount = int(input("Number Of Symbols: "))

print("\n\nGenerating Password...")

Pwd = []
        
for char in range(0 , Lcount):
    RandLet = random.choice(Letters)
    Pwd.append(RandLet);

for char in range(0 , Scount):
    Randsym = random.choice(Symbols)
    Pwd.append(Randsym);
    
for char in range(0 , Dcount):
    Randnum = random.choice(Digits)
    Pwd.append(Randnum);
    
P1 = ""
for char in Pwd:
    P1 += char
P2 = ""

random.shuffle(Pwd)
for char in Pwd:
    P2 += char
    
print("\n\nPassword Suggestions Are: ")
print(" " , P1 , "                 " , P2 , "\n\n")