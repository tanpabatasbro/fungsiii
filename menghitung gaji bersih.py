print(f"{'PROGRAM PENGHITUNG GAJI BERSIH': ^40}")
print(f"{'='*40 : ^40}")

nama  = input("Masukkan Nama :")
gaji = int(input("Masukkan Jumlah Gaji/Bulan:"))
alpha = int(input("Masukkan JUmmlah Alpa Kerja :"))
print()
if alpha >5:

    potongan = 25000 * alpha
    pajak = gaji - 2.5/100
    hasil = pajak - potongan
    print(f"Nama\t\t\t\t : {nama}")
    print(f"Gaji DiPotong Pajak 2.5%\t : {pajak}")
    print(f"Gaji DiPotongan Alpa Kerja\t : {potongan}")
    print(f"Jumlah gaji ahkir\t\t : {hasil}")
else:
    pajak = gaji - 2.5/100
    print(f"Nama\t : {nama}")
    print(f"Gaji DiPotong pajak 2.5%\t : {pajak}")
