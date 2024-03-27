def compute_grades(input_file, output_file):
    with open('input_file.txt', 'r') as input_f, open('output_file', 'w') as output_f:
        lines = input_f.readlines()
        output_f.write("Student Name\t\tQuiz Scores\tAverage Score\n")
        
        for line in lines:
            data = line.strip().split()
            last_name = data[0]
            first_name = data[1]
            quiz_scores = list(map(int, data[2:]))
            num_quizzes = len(quiz_scores)
            total_score = sum(quiz_scores)
            average_score = total_score / 10
            
            output_f.write(f"{last_name}, {first_name}\t")
            output_f.write(' '.join(str(score) for score in quiz_scores))
            output_f.write('\t\t')
            output_f.write(f"{average_score:.2f}\n")
            
            # If the student missed quizzes, append zeroes to calculate average
            if num_quizzes < 10:
                missing_quizzes = 10 - num_quizzes
                output_f.write(f"Missed quizzes: {missing_quizzes}\n")
                output_f.write(f"{'0 ' * missing_quizzes}\t\t")
                output_f.write(f"{average_score:.2f}\n")

        # Copy contents of output file to input file
        output_f.seek(0)
        input_f.writelines(output_f.readlines())

    print("Grades computed and saved successfully!")

# Usage
input_file = 'input.txt'  # Replace with your input file path
output_file = 'output.txt'  # Replace with your output file path
compute_grades(input_file, output_file)
