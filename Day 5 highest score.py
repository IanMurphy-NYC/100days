# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

def find_highest_value(student_scores):
    if not student_scores:  # Check if the list is empty
        return None

    highest = student_scores[0]  # Initialize with the first element

    for value in student_scores:
        if value > highest:
            highest = value

    return highest

highest_score = find_highest_value(student_scores)
print("The highest score is:", highest_score)