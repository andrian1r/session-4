import random

batu = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

kertas = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

gunting = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''

gambar =[batu,kertas,gunting]


pengguna_memilih =int (input("0 untuk batu, 1 untuk kertas, 2 untuk gunting! "))


if pengguna_memilih >= 3 or pengguna_memilih < 0:
    print("kamu salah ngetik, kamu kalah")

else:
    print("pilihanmu:")
    print(gambar[pengguna_memilih])

    pilihan_komputer = random.randint(0, 2)
    print("pilihan_komputer:")
    print(gambar[pilihan_komputer])


if pengguna_memilih == 0 and pilihan_komputer == 2:
    print("kamu menang!")
elif pilihan_komputer == 0 and pengguna_memilih ==2:
    print("kamu kalah!")
elif pilihan_komputer > pengguna_memilih:
    print("kamu kalah")
elif pengguna_memilih > pilihan_komputer:
    print("kamu menang")
elif pilihan_komputer == pengguna_memilih:
    print("kamu seri")







