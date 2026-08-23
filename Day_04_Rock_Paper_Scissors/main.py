import random
rock=("""
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
""")

# Paper
paper=("""
     ___
---'    _)_
           __)
          ___)
         ___)
---.____)
""")

# Scissors
scissors=("""
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
""")
choices=[rock, paper, scissors]
computer = random.randint(0,2)
user_choice=int(input("enter 0 for rock,  1 for 'paper',2 for 'scissors':"))
print(choices[user_choice])
print(choices[computer])
if user_choice == computer:
    print("Draw")
elif user_choice == 0 and computer== 2:
    print("You win")
elif user_choice == 1 and computer== 0:
    print("You win")

elif user_choice == 2 and computer== 1:
    print("You win")
else:
    print("You lose")