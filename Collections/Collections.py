def calcLetterGrade(grade):
    letter = ""
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

name = input("Please enter your name: ")
grade_1 = int(input("Please enter grade #1: "))
grade_2 = int(input("Please enter grade #2: "))
grade_3 = int(input("Please enter grade #3: "))
grade_4 = int(input("Please enter grade #4: "))
grade_5 = int(input("Please enter grade #5: "))
avg_grade = (grade_1 + grade_2 + grade_3 + grade_4 + grade_5) / 5.0
letter_grade = calcLetterGrade(avg_grade)

print(f"Name: {name}\nAverage: {avg_grade}\nLetter Grade: {letter_grade}")



