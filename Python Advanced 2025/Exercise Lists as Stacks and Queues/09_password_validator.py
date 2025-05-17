def pass_checker(password):
    count = 0
    symbol_checker = 0
    for sym in password:
        s = ord(sym)
        if sym.isdigit():
            count += 1
        if sym.isalnum():
            symbol_checker += 1
    if 6 > len(password) or len(password) > 10:
        print("Password must be between 6 and 10 characters")
    if symbol_checker < len(password):
        print("Password must consist only of letters and digits")
    if count < 2:
        print("Password must have at least 2 digits")
    if len(password) >= 6 and len(password) <= 10 and symbol_checker == len(password) and count >= 2:
        print("Password is valid")


password = input()
pass_checker(password)
