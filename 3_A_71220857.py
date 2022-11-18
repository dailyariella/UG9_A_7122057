#Test 3
import math
p = int (input("Masukkan panjang: "))
l = int (input("Masukkan lebar: "))
r = int (input("Masukkan jari-jari: "))
luaslingkaran =float(((math.pi)*(r**2))/2)
luaspp =float(p*l)
jumlahkaleng =float(((luaslingkaran+luaspp)/15))
print ("Area tersebut membutuhkan",math.ceil(jumlahkaleng),"kaleng cat")
