#operasi dan memanipulasi string

#1.menyambung stringh(concatenate)

nama_pertama = "Monkey"
nama_tengah = "D"
nama_akhir = "Luffy"

nama_lengkap = nama_pertama + nama_tengah +nama_akhir
print(nama_lengkap)

nama_lengkap = nama_pertama + "" + nama_tengah + "" +nama_akhir
print(nama_lengkap)

#2.Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang" + nama_lengkap + "adalah" + str(panjang))

#3.Operator untuk string
#cek apakah ada komponen pada sebuah string

d="d"
status = d in nama_lengkap
print("apakah" + d +"ada di" + nama_lengkap + "," + str(status))

D = "D"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", " + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x + " tidak ada di " + nama_lengkap + ", " + str(status))

# mengulang string
print("wk"*100)
print(100*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0]) # dimulai dari 0
print("index ke-6 : " + nama_lengkap[6]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-[6,8) : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,7]:" + nama_lengkap[0:10:2])#diambil index 0,2,4,6,8

#item paling kecil 
print("nilai terkecil:"+min(nama_lengkap))

#item paling besar
print("nilia terbesar:"+max(nama_lengkap))

ascii_code = ord("")
print("ASCII number dari spasi:"+str(ascii_code))
data=117
print("character dari ascii code 117:"+chr(data))

#4. operator dalam bentuk methode
data="otong surotong pararotong"
jumlah=data.count("o")
print("jumlah 0 di "+ data + " : " + str(jumlah))
