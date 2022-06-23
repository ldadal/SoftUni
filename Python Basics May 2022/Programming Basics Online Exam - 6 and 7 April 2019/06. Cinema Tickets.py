total_tickets = 0
movie_name = ""
standart_count = 0
student_count = 0
kid_count = 0
tickets_count = 0
seat = ""
movie_name = input()
free_tickets = int(input())
while movie_name != "Finish":
    count_free_tickets = free_tickets
    while count_free_tickets > 0 and seat != "End":
        seat = input()
        if seat == "standard":
            standart_count += 1
            total_tickets += 1
            tickets_count += 1
            count_free_tickets -= 1
        elif seat == "student":
            student_count += 1
            total_tickets += 1
            tickets_count += 1
            count_free_tickets -= 1
        elif seat == "kid":
            kid_count += 1
            total_tickets += 1
            tickets_count += 1
            count_free_tickets -= 1
    print(f"{movie_name} - {tickets_count / free_tickets * 100:.2f}% full.")
    tickets_count = 0
    seat = ""
    movie_name = input()
    if movie_name=="Finish":
        break
    free_tickets = int(input())
print(f"Total tickets: {total_tickets}")
print(f"{student_count / total_tickets * 100:.2f}% student tickets.")
print(f"{standart_count / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_count / total_tickets * 100:.2f}% kids tickets.")
