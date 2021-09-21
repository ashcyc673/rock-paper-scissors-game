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
print("********RPS game start********")
player_choice = input("0 for rock, 1 for paper, 2 for scissors. ---> ")

if player_choice == "0":
  print(rock)
elif player_choice == "1":
  print(paper)
else:
  print(scissors)

print("computer's choice: ")
choice = ['0','1','2']
ran_choice = random.choice(choice)

if ran_choice == '0':
  print(rock)
elif ran_choice == '1':
  print(paper)
else:
  print(scissors)




