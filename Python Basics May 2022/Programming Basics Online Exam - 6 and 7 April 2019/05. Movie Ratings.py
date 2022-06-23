movies_count = int(input())
count = 0
max_r_movie = ""
max_r = 0.0
min_r_movie = ""
min_r = 0.0
sum_rating = 0.0
while count < movies_count:
    name_of_movie = input()
    rating = float(input())
    count+=1
    sum_rating+=rating
    if count==1:
        min_r=rating
        min_r_movie=name_of_movie
    if max_r < rating:
        max_r_movie = name_of_movie
        max_r = rating
    elif min_r > rating:
        min_r_movie = name_of_movie
        min_r = rating
print(f"{max_r_movie} is with highest rating: {max_r:.1f}")
print(f"{min_r_movie} is with lowest rating: {min_r:.1f}")
print(f"Average rating: {sum_rating/movies_count:.1f}")
