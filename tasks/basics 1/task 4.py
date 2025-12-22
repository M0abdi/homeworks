time = input("Enter time (HH:MM:SS): ")
h, m, s = map(int, time.split(":"))
if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
    print("Valid")
else:
    print("Invalid")
