def angkaMax(daftar):
    maksimal=0
    for x in daftar:
        if x > maksimal:
            maksimal=x
        return maksimal

jumlahAngka=[]
while True:
    nilai=int(input("Masukan Angka : "))
    jumlahAngka.append(nilai)
    if nilai == 0:
        break
print("angka maksimum : ", angkaMax(jumlahAngka)
      )







