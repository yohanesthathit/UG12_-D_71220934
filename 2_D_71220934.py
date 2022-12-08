print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
x = 1
b = input("Masukkan model matematika yang diinginkan 1/2 : ")
a = int(input("Menampilkan table matematika dari angka: "))
if(b == "1"):    
    while x <= 10:
        print(a, 'x', x, '=', a*x)
        x = x+1
        if x == 11:
            break
elif(b == "2"):
    while x <= 10:
        print(a, ':', x, '=', a/x)
        x = x+1
        if x == 11:
            break
else:
    print("Pilihan tidak tersedia, jangan ngasal!")