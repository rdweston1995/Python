#Finding the sum of all the even fibinocci numbers up to 4000000
first = 1
second = 2
sum = 2

while second <= 4000000:
    third  = first + second
    if(third % 2 == 0):
        sum += third

    first = second
    second = third
    
    

print (sum)
