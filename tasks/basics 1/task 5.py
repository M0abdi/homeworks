

r = float(input("Enter radius: "))
x, y = map(float, input("Enter point (x y): ").split())
if x*x + y*y <= r*r:
    print("Inside circle")
else:
    print("Outside circle")
