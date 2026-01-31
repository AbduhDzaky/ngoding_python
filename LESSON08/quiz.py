import sys
import random
from enum import Enum

playagain = True

while playagain: 
    print("")
    print("==========================QUIZ==========================")

    score = 0

    print("\n1. ibu kota sulawesi selatan?")
    print("a. Makassar")
    print("b. Bandung"  )
    print("c. Malang")

    jawaban1 = input("Masukkan jawaban (a, b, c): ")

    if jawaban1 == "a":
        print("✅")
        score += 1
    else:
        print("❌")

    print("\n2. Hewan yang dikenal sebagai raja hutan adalah?")
    print("a. Kadal")
    print("b. Harimau")
    print("c. Monyet")

    jawaban2 = input("Masukkan jawaban (a, b, c): ")

    if jawaban2 == "a":
        print("✅")
        score += 1
    else:
        print("❌")

    print("\n1. Hasil dari 5 + 2 adalah...")
    print("a. 3")
    print("b. 2")
    print("c. 7")

    jawaban3 = input("Masukkan jawaban (a, b, c): ")

    if jawaban3 == "a":
        print("✅")
        score += 1
    else:
        print("❌")

    print("")
    print("Jumlah benar: ", score, " Soal")
    print("")

    playagain =input("\nKerjakan Lagi? \ny for Iya atau \nq untuk Keluar \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("Terima kasih sudah bermain!")
        playagain = False

sys.exit("Dadah! 👋")

