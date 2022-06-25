locations = int(input())
while locations >= 1:
    expected_average = float(input())
    days = int(input())
    count = days
    average = 0
    while count >= 1:
        gold_for_day = float(input())
        average += gold_for_day
        count -= 1
    average = average / days
    if average >= expected_average:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {(expected_average - average):.2f} gold.")
    locations -= 1
