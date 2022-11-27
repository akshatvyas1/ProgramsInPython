x = int(input())
if x % 400 == 0 or ( x % 100 != 0 and x % 4 == 0):
    print("Leap Year")
else:
    print("not a leap year")
    
