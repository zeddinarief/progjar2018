inputan = input("Masukkan angka : ")
angka = int(inputan)

counter = 0
for i in range(1,angka+1):
    if angka % i == 0 :
        counter=counter+1

if counter == 2:
    print("Bilangan Prima")
else :
    print("Bilangan bukan prima")
