par= 0
odd= 0
array = [1,2,3,4,5,6,7,8,9,10]
for i in range (0, len(array)):
    if array[i] % 2 == 0:
        par+= 1
    else:
        odd+= 1
        
print (par,"tantos pares", odd," tantos impares")
