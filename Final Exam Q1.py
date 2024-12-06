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
    gradesinlist = len(list)
    sumofgrades = sum(list)
    ave = float((sumofgrades) / (gradesinlist) - 1)
    return ave
if __name__ == '__main__':
     calculate_average(labGrades)
     print('Lab Average (after dropping the lowest score):', calculate_average(labGrades))
     calculate_average(assignGrades)
     print('Assignment Average (after dropping the lowest score):',calculate_average(assignGrades))
     if finalExam > midtermExam:
         midtermExam = finalExam
lab_ave = float(calculate_average(labGrades) * 0.1)
print('Labs (10%):',lab_ave)
assignments_ave = float(calculate_average(assignGrades) * 0.4)
print('Assignments (40%):',assignments_ave)
midterm_grade = midtermExam * 0.2
print('Midterm/Final Exam (20%):', midterm_grade)
final_grade = float(finalExam * 0.3)
print('Final Exam (30%):',final_grade)
class_grade = assignments_ave + lab_ave + midterm_grade + final_grade
print('Final Numeric Grade:', class_grade)
if class_grade >= 89.5:
    print('Letter Grade: A')
elif class_grade <= 89.4:
    print('Letter Grade: B')
elif class_grade >= 79.4:
    print('Letter Grade C')
elif class_grade <= 69.4 :
    print('Letter Grade D')
else:
    print('Letter Grade: F')