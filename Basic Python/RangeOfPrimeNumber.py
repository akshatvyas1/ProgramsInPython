low, high = map(int, input().split())
count = 0
for i in range(low, high + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            count = count + 1
print("Count of Prime Number: ",count)
