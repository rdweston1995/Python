#Finding that smallest number divisible by 1-20 with no remainder

for i in range(200000000, 250000000):
    if(
        i % 2 == 0 and i % 3 == 0 and
        i % 4 == 0 and i % 5 == 0 and
        i % 6 == 0 and i % 7 == 0 and
        i % 8 == 0 and i % 9 == 0 and
        i % 10 == 0 and i % 11 == 0 and
        i % 12 == 0 and i % 13 == 0 and
        i % 14 == 0 and i % 15 == 0 and
        i % 16 == 0 and i % 17 == 0 and
        i % 18 == 0 and i % 19 == 0 and
        i % 20 == 0
       ):
        print(i)



#2 = 4 = 6 = 8 = 10 = 12 = 14 = 16 = 18 = 20
#3 = 6 = 9 = 12 = 15 = 18
#4 = 8 = 12 = 16 = 20
#5 = 10 = 15 = 20
#6 = 12 = 18
#7 = 14
#8 = 16
#9 = 18
#10 = 20
#11
#12
#13
#14
#15
#16
#17
#18
#19
#20
