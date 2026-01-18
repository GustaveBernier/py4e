# User inpout
scr = input("Enter score:")

# Test for number
try:
    s = float(scr)
except:
    print("Score must be a number.")
    quit()

# Test for number range
if s < 0.0 or s > 1.0 :
    print("Score must be between 0.0 and 1.0")
else:
    if s >= 0.9:
        print("A")
    elif s >= 0.8:
        print("B")
    elif s >= 0.7:
        print("C")
    elif s >= 0.6:
        print("D")
    elif s < 0.6:
        print("F")