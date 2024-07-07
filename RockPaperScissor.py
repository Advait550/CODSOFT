import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Image = [rock , paper , scissor]
print(rock)
print(paper)
print(scissor)
print("Choose Number Corresponding to Its Role From Menu Below...")
print("  Menu")
print("1 : Rock")
print("2 : Paper")
print("3 : Scissor")
Uchoice = int(input("Enter Your Choice: "))
if (Uchoice > 3 or Uchoice < 1):
    print("You Lost Due to Penalty of Invalid Choice!")
else:
    print("\n\n\nYour Choice: ")
    print(Image[Uchoice - 1])
    Cchoice = random.randint(1 , 3)
    print("Computer's Choice: ") 
    print(Image[Cchoice - 1])
    
    # Conditions To Check Who Wins And Displaying The Final Message
    if(Uchoice == 1):
        if(Cchoice == 1):
            print("Tie Match! You Both Chose The Same.\n\n")
        elif(Cchoice == 2):
            print("You Lost! Better Luck Next Time.\n\n")
        else:
            print("Congratulations! You Won.\n\n")
    elif(Uchoice == 2):              
        if(Cchoice == 1):
            print("Congratulations! You Won.\n\n")
        elif(Cchoice == 2):
            print("Tie Match! You Both Chose The Same.\n\n")
        else:
            print("You Lost! Better Luck Next Time.\n\n")
    else:
        if(Cchoice == 1):
            print("You Lost! Better Luck Next Time.\n\n")
        elif(Cchoice == 2):
            print("Congratulations! You Won.\n\n")
        else:
            print("Tie Match! You Both Chose The Same.\n\n")