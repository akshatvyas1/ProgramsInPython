a = int(input())
if a > 1:
    for j in range(2, int(a/2)+1):
        if a % j == 0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("not a prime number")
