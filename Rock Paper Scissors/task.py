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
images= [rock, paper, scissors]
user_choice=int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
 print(images[user_choice])
comp_choice=random.randint(0,2)
print("Computer chose:")
print(images[comp_choice])

if user_choice >=3 or user_choice < 0:
    print("you typed an invalid number. you lose!")
elif user_choice==0 and comp_choice==2:
    print("you wins!")
elif user_choice==2 and comp_choice== 0:
    print("you lose!")
elif comp_choice > user_choice:
   print("you lose !")
elif user_choice > comp_choice:
    print("you wins!")
elif comp_choice == user_choice:
    print("its a tie!")
