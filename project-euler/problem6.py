#Finding the difference of the Sum of the Squares and
#The Square of the sums of 1-100
sumSquare = 0
squareSum = 0

for i in range(1, 101):
    sumSquare += i ** 2
    squareSum += i

print("Square of the Sum: ", squareSum, " ^ 2 = ", (squareSum ** 2))
print("Sum of the Squares: ", sumSquare)
print((squareSum ** 2) - sumSquare)
