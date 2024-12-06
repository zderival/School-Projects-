# This Python program is designed to calculate a student's final grade based on their performance in different categories: labs, assignments, and exams. 
# This program demonstrates the coder's ability to apply basic programming concepts (loops, functions, conditionals, etc.) 
# In this program, this is one out of three questions that the user was given to complete in his final exam. This is what was done in a 100 minute timespan. 
labGrades = []
for number in range(1,14):
    lab = int(input('Enter grade for lab '+ str(number)+': '))
    labGrades.append(lab)
assignGrades =[]
for number in range(1,8):
    assignments = int(input('Enter grade for assignment '+ str(number)+': '))
    assignGrades.append(assignments)
midtermExam = int(input('Enter your midterm exam grade: '))
finalExam = int(input('Enter your final exam grades: '))
def calculate_average(list):
    list.sort()
    list = list[1:]
    return sum(list) / len(list)
if __name__ == '__main__':
     calculate_average(labGrades)
     print('Lab Average (after dropping the lowest score):', calculate_average(labGrades))
     calculate_average(assignGrades)
     print('Assignment Average (after dropping the lowest score):',calculate_average(assignGrades))
     if finalExam > midtermExam:
         midtermExam = finalExam
lab_ave = round(float(calculate_average(labGrades) * 0.1),1)
print('Labs (10%):',lab_ave)
assignments_ave = round(float(calculate_average(assignGrades) * 0.4),1)
print('Assignments (40%):',assignments_ave)
midterm_grade = midtermExam * 0.2
print('Midterm/Final Exam (20%):', midterm_grade)
final_grade = float(finalExam * 0.3)
print('Final Exam (30%):',final_grade)
class_grade = assignments_ave + lab_ave + midterm_grade + final_grade
print('Final Numeric Grade:', class_grade)
if class_grade >= 89.5:
    print('Letter Grade: A')
elif class_grade >= 79.4:
    print('Letter Grade: B')
elif class_grade >= 69.4:
    print('Letter Grade: C')
elif class_grade >= 59.4:
    print('Letter Grade: D')
else:
    print('Letter Grade: F')
