def calculate_average(scores):
    # Calculate the total of the scores
    total = sum(scores)
    # Calculate the average by dividing the total by the number of scores
    average = total / len(scores)
    return average

# Read scores and names from the file
with open("records.txt", "r") as file:
    lines = file.readlines()

student_scores = {}
for line in lines:
    # Split each line into name and score, handling potential errors
    try:
        name, score = line.strip().split(",")
        score = float(score)

        if name in student_scores:
            # If the student's name already exists in the dictionary, append the score
            student_scores[name].append(score)
        else:
            # If the student's name doesn't exist in the dictionary, create a new entry with the score
            student_scores[name] = [score]
    except ValueError:
        # Skip the line if it doesn't contain the expected format
        print(f"Ignoring invalid line: {line}")

# Calculate average grades and store in grades.txt
with open("grades.txt", "w") as file:
    for name, scores in student_scores.items():
        # Calculate the average grade for each student
        average_grade = calculate_average(scores)
        # Write the student's name and average grade to the file
        file.write(f"{name}: {average_grade}\n")

# Ask the teacher if they want to display the student grades
choice = input("Do you want to display the student grades? (y/n): ")

if choice.lower() == "y":
    # Read the grades from grades.txt and display them
    with open("grades.txt", "r") as file:
        grades = file.read()
    print(grades)
else:
    print("Thank you. Have a nice day!")
