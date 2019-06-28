sum = 0

i = 1


while i < 1000:
    if i % 5 == 0:
        sum += i
        #print (sum)
    elif i % 3 == 0:
        sum += i
        #print (sum)
    i += 1


print (sum)
