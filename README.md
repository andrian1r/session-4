# session-4
A beginner Python project combining a text-based adventure game and a simple shopping list program using conditionals, lists, and user input.
# 🐍 Python Beginner Project  
## 🛒 Shopping List & ✊ Rock Paper Scissors Game

## 📖 Overview

This project contains two beginner-friendly Python programs:

1. 🛒 Shopping List Total Calculator  
2. ✊ Rock Paper Scissors Game  

The goal of this project is to practice Python fundamentals such as:

- Lists
- User input handling
- Type conversion
- Conditional statements
- Random module usage
- Basic game logic

---

# 🛒 Part 1: Shopping List Program

## 📝 Description

This program allows users to:

- Enter 3 shopping items
- Enter their prices
- Display the shopping list
- Calculate and display the total cost

## 🧠 Concepts Used

- Lists (`append()`)
- Integer conversion using `int()`
- List indexing
- Arithmetic operations
- Output formatting

---

# ✊ Part 2: Rock Paper Scissors Game

## 🎮 Description

A simple Rock-Paper-Scissors game where:

- The user selects a number (0, 1, or 2)
- The computer randomly selects a choice
- The program determines the winner

## 🧠 Concepts Used

- `random` module
- `randint()`
- Conditional logic (`if`, `elif`, `else`)
- ASCII art display
- Input validation

---

# 💻 Full Code

```python
# ===============================
# Shopping List Program
# ===============================

belanja = []
harga = []

item1 = input("masukan barang pertama")
harga1 = int(input("masukan harga barang pertama"))
belanja.append(item1)
harga.append(harga1)

item2 = input("masukan barang kedua")
harga2 = int(input("masukan harga barang kedua"))
belanja.append(item2)
harga.append(harga2)

item3 = input("masukan barang ketiga")
harga3 = int(input("masukan harga barang ketiga"))
belanja.append(item3)
harga.append(harga3)

print("\nDaftar belanja")
print("1.", belanja[0], "- Rp", harga[0])
print("2.", belanja[1], "- Rp", harga[1])
print("3.", belanja[2], "- Rp", harga[2])

total = harga[0] + harga[1] + harga[2]
print("\nTotal belanja: Rp", total)


# ===============================
# Rock Paper Scissors Game
# ===============================

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

gambar = [batu, kertas, gunting]

pengguna_memilih = int(input("0 untuk batu, 1 untuk kertas, 2 untuk gunting! "))

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
    elif pilihan_komputer == 0 and pengguna_memilih == 2:
        print("kamu kalah!")
    elif pilihan_komputer > pengguna_memilih:
        print("kamu kalah")
    elif pengguna_memilih > pilihan_komputer:
        print("kamu menang")
    else:
        print("kamu seri")
```

---

# 🛠 Requirements

- Python 3.x

---

# 👤 Author

Andrian Wijaya

---

# 📜 License

This project is created for educational purposes.
