class Kalkulator(object):
    angkaSatu = 0
    angkaDua = 0

    def __init__(self, a, b):
        self.angkaSatu = a
        self.angkaDua = b

    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(self, a, b):
        return a - b

# Inisiasi object
kal = Kalkulator(20, 10)
c = kal.penjumlahan(20,10)
print(c)