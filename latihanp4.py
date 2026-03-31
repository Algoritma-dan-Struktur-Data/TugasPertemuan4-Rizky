#Program konversi detik ke hari, jam, menit, dan detik

total_detik = int(input("Masukkan total detik: "))

hari = total_detik // 86400
sisa_hari = total_detik % 86400

jam = sisa_hari // 3600
sisa_jam = sisa_hari % 3600

menit = sisa_jam // 60 
detik = sisa_jam % 60

print("Hasil konversi", total_detik, "detik adalah,", hari, "Hari,", jam, "Jam,", menit, "Menit,", detik, "Detik")