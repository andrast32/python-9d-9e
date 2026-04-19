# Nested if sederhana nya if didalam if

# if kondisi1: 
#     if kondisi2:
#         print("kondisi 2 benar")
#     else:
#         print("jika hanya kondisi 1 yang benar")
# else:
#     print("jika kondisi1 salah")

# contoh
# matematika = 75
# inggris = 55

# if matematika >= 70:  kondisi 1
#     if inggris >= 60: kondisi 2
#         print("Lulus semua ujian") ini adalah hasil jika nilai matematika dan nilai inggris melampaui ketentuan
#     else:
#         print("matematika lulus, tapi inggris tidak lulus") ini adalah hasil jika matematika melampaui ketentuan tapi inggris tidak
# else:
    #print("kedua ujian tidak ada yang lulus") ini kalau ga ada sama sekali

# praktek
print("masukan nilai matematika")
matematika = int(input("= "))
print("masukan nilai bahasa inggris")
inggris = int(input("= "))
print("masukan nilai ipa")
ipa = int(input("= "))

rata = (matematika + inggris + ipa) / 3
print("Rata rata nilai = ", rata)

if rata >= 70:
    if matematika >= 60 and inggris >= 60 and ipa >= 60:
        print("Lulus semua mata pelajaran")
    else:
        print("rata rata cukup tapi ada nilai yang kurang")
else:
    print("tidak lulus")