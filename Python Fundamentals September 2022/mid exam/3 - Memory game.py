sequence = input().split()
guess = input()
count = 0
while guess != "end":
    first, second = [int(x) for x in guess.split()]
    # first = int(first)
    # second = int(second)
    count += 1
    if not sequence:
        count -= 1
        print(f"You have won in {count} turns!")
        break
    if not 0 <= first < len(sequence) or not 0 <= second < len(sequence) or first == second:
        print("Invalid input! Adding additional elements to the board")
        sequence.insert(int(len(sequence) / 2), f"-{count}a")
        sequence.insert(int(len(sequence) / 2), f"-{count}a")
    elif sequence[first] == sequence[second]:
        print(f"Congrats! You have found matching elements - {sequence[first]}!")
        del sequence[first]
        if first<second:
            second-=1
        del sequence[second]
        # if first > second:
        #     del sequence[first]
        #     del sequence[second]
        # else:
        #     del sequence[second]
        #     del sequence[first]
    else: # sequence[first] != sequence[second]:
        print("Try again!")
    guess = input()
if sequence:
    print("Sorry you lose :(")
    print(*sequence)
