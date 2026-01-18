def computepay(h, r):
    bh = 40
    # Overtime
    if h > bh :  
        pay = (bh * r) + (h - bh) * r * 1.5
    # Regular time
    else :
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rt = input("Enter rate:")
h = float(hrs)
r = float(rt)
p = computepay(h, r)
print("Pay", p)