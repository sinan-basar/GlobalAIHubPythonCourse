# Day2 - HomeWorks 2/2

while True:
    n = int(input("Enter a single digit integer(>=0):"))
    if( n >= 0 and n <= 9 ):
     break

for i in range(n+1):
    if i%2 == 0:
        print("Even number(s):",i)
