# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pick = random.uniform(0,len(names))
print(names[int(pick)]+' is going to guy the meal today!')
