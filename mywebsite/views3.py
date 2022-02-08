from multiprocessing import context
from django.shortcuts import render
import requests


class masuk():
    r_yen = requests.get(
        'https://free.currconv.com/api/v7/convert?q=JPY_USD&compact=ultra&apiKey=9006dcb72b6464e75d5d')
    data_yen = r_yen.json()
    r_sd = requests.get(
        'https://free.currconv.com/api/v7/convert?q=SGD_USD&compact=ultra&apiKey=9006dcb72b6464e75d5d')
    data_sd = r_sd.json()
    r_rp = requests.get(
        'https://free.currconv.com/api/v7/convert?q=IDR_USD&compact=ultra&apiKey=9006dcb72b6464e75d5d')
    data_sd = r_sd.json()

    def index(request):
        yen = float(masuk.data_yen['JPY_USD'])
        sd = float(masuk.data_sd['SGD_USD'])
        rp = float(masuk.data_sd['IDR_USD'])
        r_m = request.method

        if r_m == ('POST'):
            pilihan = request.POST['mata_uang']
            user = float(request.POST['masukanHarga'])
            if pilihan == ('JPY'):
                hasil = yen * user
            elif pilihan == ('SD'):
                hasil = sd * user
            elif pilihan == ('RP'):
                hasil = rp * user

        else:
            hasil = ""

        context = {
            'iniHasilnya': hasil,
            'title': 'Kalkulator',
            'judul': 'Kalkulator IMEI',
            'subjudul': 'Kalkulator Hitung Pajak HP',
            'hasil': 'Pajak HPmu',
        }

        return render(request, 'index.html', context)


class kalk():
    pass


ini = masuk()
ini.index
