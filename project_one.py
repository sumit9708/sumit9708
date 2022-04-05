# print all the prime number in range of 1 to 1000.

start = int(input('enter the starting range'))
end = int(input('enter the ending number'))
print("prime number in the range of",start,'to',end,'is')

# coding part

for i in range(start,end+1):
    flag = 0
    for j in range(2,i):
        if (i % j==0):
            flag=1
            break

    if (flag == 0):
        print(i, end =' ')
