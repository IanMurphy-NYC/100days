#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('This is a tip calculator.\n');

bill = float(input('What was the total bill?\n'));

ways = int(input('How many ways will the bill be split?\n'));

tip = int(input('Input an integer to represent the tip percentage.\n'));

amount = round((bill / ways) * (1+tip), 2);

print('Each person owes: ' + amount);
