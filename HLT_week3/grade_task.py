S_marks = int(input("Please enter your marks: "))
grade_list = ["A","B","C","D","E","F"]
def Mark_Grade(marks):
    if marks > 92:
     grade = "A"
    elif marks> 80 and marks<= 92: 
     grade = "B"
    elif marks>70 and marks<= 80:
     grade = "C"
    elif marks>60 and marks<= 70:
     grade = "D"
    elif marks>50 and marks<= 60:
     grade = "E"
    else:
     grade = "F"
    
    return grade

     

s_grade=Mark_Grade(S_marks)
print(s_grade)

T_grade = input("Please enter your target grade: ")

if T_grade > s_grade:
 print("Well Done!")
elif T_grade == s_grade:
 print("You are doing well")
else:
 print("You need to work harder")

