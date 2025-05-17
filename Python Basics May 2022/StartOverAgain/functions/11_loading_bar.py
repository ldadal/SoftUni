def loading(percentage):
    p=percentage//10
    if percentage != 100:
        print(percentage,"% [","%" * p,"." * (10 - p),"]", sep='')
        print("Still loading...")
    if percentage == 100:
        print(f"100% Complete!")
        print("[","%" * p,"]",sep='')


n = int(input())
loading(n)

