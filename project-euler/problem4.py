#Finding the largest palindrome number thats a product of a two three digit numbers
products = []

for i in range(900, 999):
    for k in range(900, 999):
        pro = i * k
        products.append(pro)
for i in range (len(products)):
    temp = str(products[i])
    if temp[0] == temp[5] and temp[1] == temp[4] and temp[2] == temp[3]:
        print(temp)

        
