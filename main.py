berat = float(input("Masukan berat anda (kg): "))
tinggi = float(input("Masukan tinggi anda (m): "))

print (f"berat badan anda {berat}")
print (f"tinggi badan anda {tinggi}")

bmi = berat / (tinggi ** 2)
print("BMI anda = ", round(bmi, 2))
if bmi < 18.5:
      print("Berat badan anda kurang")
elif bmi < 25:
      print("Berat badan anda ideal")
elif bmi < 30:
      print("Berat badan anda kelebihan")
else:
      print("Anda Obesitas")