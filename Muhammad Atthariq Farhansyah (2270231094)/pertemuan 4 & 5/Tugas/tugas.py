print("========== Nasi Goreng Maknyuss  ==========")
pembeli = input("Masukkan nama Pembeli: ")
alamat = str(input("Masukan Alamat Pelanggan: "))
telpon = int(input("Masukan Nomor Telepon: "))
tanggal = str(input("Masukan Tanggal: "))


def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 18000")
   print("2. Mie Goreng - Rp 15000")
   print("3. Kwetiau - Rp 15000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*18000
       print (porsi," porsi Nasi Goreng = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*15000
       print (porsi," porsi Mie Goreng = Rp", totalmkn)
       mkn=("Mie Goreng")
   elif nomor==3:
       totalmkn=porsi*15000
       print (porsi, " porsi Kwetiau = Rp", totalmkn)
       mkn=("Kwetiau")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 5000")
   print("2. Es jeruk - Rp 7000")
   print("3. Es kopi - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*7000
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========= S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("alamat\t\t:",alamat)
print ("NoTelp\t\t:",telpon)
print ("tanggal\t\t:",tanggal)
print ("Pesanan\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("========== TERIMA KASIH ==========")
print("==================================")