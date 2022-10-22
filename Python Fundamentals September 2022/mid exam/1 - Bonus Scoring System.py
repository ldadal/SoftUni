number_of_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attended = 0
for i in range(number_of_students):
    student_attended = int(input())
    total_bonus = student_attended / total_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attended = student_attended
print(f"Max Bonus: {max_bonus:.0f}.\nThe student has attended {max_attended} lectures.")
