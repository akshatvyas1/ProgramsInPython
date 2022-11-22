import random

#generates a float number between 0 and 1.

n = random.random()  
print(n)

#Generating a Number within a Given Range

m = random.randint(0, 50)
print(m)

# Using for loop

rand_list = []  
for i in range(0,10):  
    n = random.randint(1,50)  
    rand_list.append(n)  
print(rand_list)

#using Sample

random_list = random.sample(range(10, 40), 6)  
print(random_list)  
