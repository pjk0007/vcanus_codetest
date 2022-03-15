num = 1
for i in range(1,1000001):
    num *= i
    if(i%10000==0) : print(i)
print(num)