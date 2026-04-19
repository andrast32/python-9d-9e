while True:
    print("\n--- Kalkulator Sederhana ---")
    print("Masukan Angka Pertama")
    pertama = int(input("= "))
    
    print("Masukan Angka Kedua")
    kedua = int(input("= "))
    
    print("Masukan Operator (+, -, *, /, //)")
    OP = input("= ")
    
    if OP == "+":
        print("Hasil:", pertama + kedua)
    elif OP == "-":
        print("Hasil:", pertama - kedua)
    elif OP == "*":
        print("Hasil:", pertama * kedua)
    elif OP == "/":
        if kedua != 0:
            print("Hasil:", pertama / kedua)
        else:
            print("Error: Tidak bisa dibagi dengan nol!")
    elif OP == "//":
        if kedua != 0:
            print("Hasil:", pertama // kedua)
        else:
            print("Error: Tidak bisa dibagi dengan nol!")
    else:
        print("Operator Error")
        
    while True:
        print("\nMau Ulang ?")
        ulang = input("y / n = ").lower() 
        
        if ulang == "y":
            break
        elif ulang == "n":
            print("Bye!")
            exit() 
        else:
            print("Error: Masukkan 'y' untuk ya atau 'n' untuk tidak.")