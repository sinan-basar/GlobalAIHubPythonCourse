# HW4 - Homework
lower_lim = 0
upper_lim = 100

if lower_lim < 0:
    lower_lim=0

if upper_lim < 1:
    upper_lim = 1
    
for i in range(lower_lim,upper_lim+1):
    if i==0:
        continue
    isPrime = True
    for k in range(2,i):
        if (i%k) == 0:
            isPrime = False
            break
        
    if isPrime == True:
        print("Prime:",i)
