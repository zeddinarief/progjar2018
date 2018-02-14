class Kalkulator(object):

    angkaSatu = 0
    angkaDua = 0

    def __init__(self,a,b):
        self.angkaSatu = a
        self.angkaDua = b

    def penjumlahan(self):
        return self.angkaSatu + self.angkaDua
    
    def pengurangan(self):
        return self.angkaSatu - self.angkaDua

kal = Kalkulator(100, 10)
print( kal.penjumlahan() )