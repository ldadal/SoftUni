yearly_fee = int(input())
shoes = yearly_fee - yearly_fee * 0.4
clothes = shoes - shoes * 0.2
ball = clothes * 0.25
other = ball * 0.2
total = yearly_fee + shoes + clothes + ball + other
print(total)
