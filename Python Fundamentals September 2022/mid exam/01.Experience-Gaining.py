needed_exp = float(input())
battles = int(input())
exp_earn_per_battle = float(input())
count = 0
while battles > 0:
    battles -= 1
    count += 1

    if count % 3 == 0:
        exp_earn_per_battle = exp_earn_per_battle + exp_earn_per_battle * 15 / 100
    if count % 5 == 0:
        exp_earn_per_battle = exp_earn_per_battle - exp_earn_per_battle * 10 / 100
    if count % 15 == 0:
        exp_earn_per_battle = exp_earn_per_battle + exp_earn_per_battle * 5 / 100
    needed_exp -= exp_earn_per_battle
    if needed_exp <= 0:
        print(f"Player successfully collected his needed experience for {count} battles.")
        break

    if battles == 0 and needed_exp > 0:
        print(f"Player was not able to collect the needed experience, {needed_exp:.2f} more needed.")
        break
    exp_earn_per_battle = float(input())