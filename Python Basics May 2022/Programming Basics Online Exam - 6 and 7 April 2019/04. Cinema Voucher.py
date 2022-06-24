voucher = int(input())
count_tickets = 0
count_other = 0
purchase = ""
if voucher == 0:
    purchase = "End"
while purchase != "End":
    purchase = input()
    if purchase == "End":
        break
    else:
        if len(purchase) > 8:
            order = ord(purchase[0]) + ord(purchase[1])
            if order <= voucher:
                voucher -= order
                count_tickets += 1
            else:
                break
        elif len(purchase) <= 8:
            order = ord(purchase[0])
            if order <= voucher:
                voucher -= order
                count_other += 1
            else:
                break
print(count_tickets)
print(count_other)
