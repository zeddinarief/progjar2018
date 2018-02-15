def penjumlahan(a,b):
    sum = 0
    for i in range(0, len(a)-1):
        sum = sum + (a[i] * b[i])
    return sum

a = [2,3,0]
b = [1,1,2]
print(penjumlahan(a,b))