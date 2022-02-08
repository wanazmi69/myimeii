

# class masuk():
#     hasil = ""

#     def index(request):
#         # Saat tombol kirim ditekan
#         if request.method('POST'):

#             # tangkap nilai yang di inputkan dan ubah tipenya ke FLOAT
#             inputan = float(request.POST['masukanHarga'])

#             # tangkap jenis mata uangnya
#             mataUang = request.POST['mata_uang']

#             # dapatkan nilai mata uang terbaru yang di tuju
#             linkAPI = requests.get(
#                 'https://free.currconv.com/api/v7/convert?q={mataUang}&compact=ultra&apiKey=9006dcb72b6464e75d5d')

#             # pecah dan ambil array mata uang dari api
#             ambilMataUang = linkAPI.json()

#             # ubah tipe mata uang API menjadi FLOAT
#             nilaiMataUang = float(ambilMataUang[mataUang])

#             # hasil
#             masuk.hasil = inputan * nilaiMataUang

#         context = {
#             'iniHasilnya': masuk.hasil,
#             'title': 'Kalkulator',
#             'judul': 'Kalkulator IMEI',
#             'subjudul': 'Kalkulator Hitung Pajak HP',
#             'hasil': 'Pajak HPmu',
#         }

#         return render(request, 'index.html', context)


# def formatrupiah(uang):
#     y = str(uang)
#     if len(y) <= 3:
#         return 'Rp ' + y
#     else:
#         p = y[-3:]
#         q = y[:-3]
#         return formatrupiah(q) + '.' + p

#         print('Rp ' + formatrupiah(q) + '.' + p)


# print('Rp{: , .2f}'.format(300000))


def rupiah(nilai):
    ini = '{:,.2f}'.format(nilai)
    return ini


nilaiYen = float(input('masukan harga : ',))
kursYen_USD = float('0.008663')
kursRP = float('14386.85')
kepabeanan = nilaiYen * kursYen_USD
konversiRUPIAH = kepabeanan * kursRP
# # 37, 389, 984.5
# # 3, 738, 998.45
# # 41, 128, 983
# 4,112,898,3

bea_masuk = konversiRUPIAH * 10/100

nilai_impor = konversiRUPIAH + bea_masuk


PPN = nilai_impor * 10/100
PPH = nilai_impor * 10/100

total = bea_masuk + PPH + PPH


print('ini adalah konversi YEN-USD = $ ', rupiah(kepabeanan), '\n')
print('ini adalah konversi USD-RP = Rp. ', rupiah(konversiRUPIAH), '\n')
print('ini nilai IMPOR = Rp. ', rupiah(nilai_impor), '\n')
print('ini nilai bea masuk = Rp. ', rupiah(bea_masuk), '\n')
print(' nilai PPN = Rp. ', rupiah(PPN), '\n')
print(' nilai PPH = Rp. ', rupiah(PPH), '\n')
print('ini pajakmu = Rp. ', rupiah(total), '\n')


# nilai kepabeanan: Rp 37, 389, 984.47
# bea masuk: Rp 3, 738, 998.45
# nilai import: Rp 41, 128, 982.91
# ppn: Rp 4, 112, 898.29
# pph: Rp 4, 112, 898.29
# Total Pajak: Rp 11, 964, 795.03
