Num = int(input('Enter Your Loop'))
NumTotal = []
print('Enter Your Data:')
for i in range(Num):
    data = int(input(''))
    NumTotal += [data]
print(NumTotal,end='')
NumTotal.sort()
print("---> ",end='')
print("Min -> ",NumTotal[0])
print("Max -> ",NumTotal[-1])