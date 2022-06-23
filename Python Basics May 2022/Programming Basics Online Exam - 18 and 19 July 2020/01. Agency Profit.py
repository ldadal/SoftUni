company_name = input()
normal_tickets = int(input())
kid_tickets = int(input())
ticket_price = float(input())
taxes = float(input())
total_sum = kid_tickets * ticket_price * 0.3 + kid_tickets * taxes + normal_tickets * taxes + normal_tickets * ticket_price
print(f"The profit of your agency from {company_name} tickets is {total_sum * 0.2:.2f} lv.")
