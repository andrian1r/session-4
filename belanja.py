belanja = []
harga = []


item1 = input("masukan barang pertama")
harga1 = int(input("masukan harga barang pertama"))
belanja.append(item1)
harga.append(harga1)

item2 = input("masukan barang kedua")
harga2 =int(input("masukan harga barang kedua"))
belanja.append(item2)
harga.append(harga2)

item3 = input ("masukan barang ketiga")
harga3 =int(input("masukan harga barang ketiga"))
belanja.append(item3)
harga.append(harga3)


print("\nDaftar belanja")
print("1.", belanja[0], "- Rp", harga[0])
print("2.", belanja[1], "- Rp", harga[1])
print("3.", belanja[2], "- Rp", harga[2])

total = harga[0] + harga[1] + harga[2]
print("\nTotal belanja: Rp", total)





















































