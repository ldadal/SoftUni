name = input()
goals = int(input())
max_score = 0
player_max_score = ""
while name != "END":
    if goals >= 10:
        max_score = goals
        player_max_score = name
        break
    if max_score < goals:
        max_score = goals
        player_max_score = name
    name = input()
    if name == "END":
        break
    goals = int(input())
if max_score >= 10:
    print(f"""{player_max_score} is the best player!
He has scored {max_score} goals and made a hat-trick !!!""")
elif max_score >= 3 and max_score < 10:
    print(f"""{player_max_score} is the best player!
He has scored {max_score} goals and made a hat-trick !!!""")
else:
    print(f"""{player_max_score} is the best player!
He has scored {max_score} goals.""")
