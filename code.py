# Store the images to each choice
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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choices = [rock,paper,scissors]
num_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if num_user<0 or num_user>2:
  print("You entered an invalid number")
else:
 user_choice = choices[num_user]
 print(user_choice)
 num_computer = random.randint(0,2)
 computer_choice = choices[num_computer]
 print("Computer chose:")
 print(computer_choice)
 if num_user == 0:
   if num_computer == 0:
     print("It's a draw.")
   elif num_computer == 1:
     print("You lose.")
   else:
     print("You won!")
 if num_user == 1:
   if num_computer == 0:
     print("You won!")
   elif num_computer == 1:
     print("It's a draw.")
   else:
     print("You lose.")
 if num_user == 2:
   if num_computer == 0:
     print("You lose.")
   elif num_computer == 1:
     print("You won!")
   else:
     print("It's a draw.")
