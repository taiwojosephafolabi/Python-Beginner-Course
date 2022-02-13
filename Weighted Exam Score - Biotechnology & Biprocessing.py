# Weighted Exam Score Average for Biotechnology & Bioprocessing module
number_of_exams = int(input("Enter number of exams: "))
total_credits = int(input("Enter total number of credits for exams: "))
average = 0
for exam in range(number_of_exams):
    score = int(input("enter exam score: "))
    exam_credits = int(input("Enter credits for this exam: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)
