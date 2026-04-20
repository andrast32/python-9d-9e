def helo():
    print('halo dunia')

helo()

# def -> define 
# helo -> nama fungsi
# (): -> menunjukan fungsi ini tidak punya parameter / tidak butuh input
# : -> menunjukan bahwa setelahnya adalah isi dari fungsi
# helo() -> cara untuk menjalankan fungsi

# parameter itu apa?
# parameter adalah tempat penampung input

def sapa(nama):
    print("hallo", nama)

sapa("iqbal")
sapa("bani")

# return
# return adalah perintah dalam fungsi python untuk mengembalikan nilai hasil perhitungan ke luar fungsi
# nilai yang dikembalikan bisa disimpan dalam variabel atau dipakai dalam operasi lain

# perbedaan return dengan print
# print => hanya menampilkan hasil di layar, tapi ga bisa dipakai lagi
# return => menyimpan hasil agar bisa digunakan kembali di program

# contoh
def tambah_print(a, b):
    print(a+b)

def tambah_return(a, b):
    return a + b

hasil1 = tambah_print(3,4)
print("hasil1 =", hasil1)

hasil2 = tambah_return(3,4)
print("hasil2 =", hasil2) 

# question
def luas_lingkaran(r):
    pi = 3.14
    return pi * r * r

def hitung_keliling(r):
    return 2 * pi

print(luas_lingkaran(7))

# jawaban challenge
pi = 3.14

def hitung_luas(r):
    return pi * r *r

def hitung_keliling(r):
    return 2 * pi * r

def main():
    print("Menu:")
    print("1 hitung luas lingkaran")
    print("2 hitung keliling lingkaran")

    pilihan = int(input("pilih menu 1/2: "))
    r = float(input("masukan jari jari: "))

    if pilihan == 1:
        print("luas lingkaran =", hitung_luas(r))
    elif pilihan == 2:
        print("keliling lingkaran =", hitung_keliling(r))
    else:
        print("pilihan tidak valid")
main()