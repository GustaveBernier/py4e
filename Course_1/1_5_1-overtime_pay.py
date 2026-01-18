# User input
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try :
    h = float(hrs)
    r = float(rate)
except :
    print("Inputs must be numbers!")

# Calculate payout
bh = 40

# Overtime
if h > bh :  
    pay = (bh * r) + (h - bh) * r * 1.5

# Regular time
else :
    pay = h * r

# All done
print(pay)