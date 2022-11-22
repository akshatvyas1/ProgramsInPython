r = float(input())
convertChoice = input()
if convertChoice == "F":
    tempOut = (r * 1.8) + 32
    print(tempOut)
else:
    tempOut = ((r - 32)*5)/9
    print(tempOut)
