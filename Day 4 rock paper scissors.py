# ## Rock Paper Scissors

# # Instructions

# #Make a rock, paper, scissors game. 

# Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

# Start the game by asking the player:

# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out: 
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player. 

# You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)


# # Solution

# [https://replit.com/@appbrewery/rock-paper-scissors-end](https://replit.com/@appbrewery/rock-paper-scissors-end)


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

#Write your code below this line 👇
import random
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
computer = random.randint(0,3)
if int(user) == 0:
    if computer == 0:
        print("You tied!")
    elif computer == 1:
        print("You lost!")
    elif computer == 2:
        print("You win")
if int(user) == 1:
    if computer == 0:
        print("You win!")
    elif computer == 1:
        print("You tied!")
    elif computer == 2:
        print("You lost")
if int(user) == 2:
    if computer == 0:
        print("You win!")
    elif computer == 1:
        print("You lost!")
    elif computer == 2:
        print("You tied")