numbers_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())
total_for_book = numbers_of_pages // pages_per_hour
hours_per_day = total_for_book // days
print(hours_per_day)