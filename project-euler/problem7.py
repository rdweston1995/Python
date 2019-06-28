#Finding the 10001st prime number
#Make a blank array
#For loop to fill the blank array with prime numbers
    #Check in the for loop for the array size to check when it gets to 10001

n = []
for i in range(1, 11):
    n.append(i)

for k in range(len(n)):
    for i in range(len(n)):
        if n[i] % k == 0 and n[i] != k:
            
