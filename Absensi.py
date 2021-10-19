import matplotlib
import re
import datetime
i = 0
while i < 9:
    i = i + 1
    nama_mahasiswa = ["Bima Prasetya Nurhidayat".lower(),
                  "Naufal Rfiqi Habibie".lower(),
                  "Gamal Muhammad Ramadhan Firdaus".lower(),
                  "Dimas Akhmad Sobari".lower(),
                  "Andi Naufal Hidayaturrahman".lower(),
                  "Matheo Nigel".lower(),
                  "Ridinta Nabila".lower(),
                  "Muhammad Ichsan Ghifari".lower(),
                  "Mohammad Dzaky Arditya".lower()]

    name = input("please enter your name: ").lower()
    while name not in nama_mahasiswa:
        print("Nama tidak terdaftar silahkan coba lagi")
        name = input("please enter your name: ").lower()
    else:

        print('selamat datang ' +name)

    NRP = input("please enter your NRP: ")
    nomor_nrp = ['02311940000091',
             '02311940000135',
             '02311940000163',
             '02311940000164',
             '02311940000027',
             '02311940000073',
             '02311940000038',
             '02311940000139',
             '02311940000105']

    while NRP not in nomor_nrp:
        print("NRP tidak terdaftar silahkan coba lagi")
        NRP = input("please enter your NRP: ").lower()
    else:
        print("successfully logged in!, hello " + name)
    d = datetime.datetime.now()
    file = open('absensi.txt', "a+")
    file.write('       '+ name + ' ')
    file.write(NRP + ' ')
    file.write(str(d) + '''.
    ''')
    file.close()

    print (name, NRP)
    print (d)

else:
    print('selesai')


