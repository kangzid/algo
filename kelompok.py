rak = []
bukuSudahDibaca = []
bukuBelumDibaca = []


def sudahDibaca(b):
    bukuSudahDibaca.append(b)


def belumDibaca(b):
    bukuBelumDibaca.append(b)


def rakBuku():
    return {"bukuSudahDibaca": bukuSudahDibaca, "bukuBelumDibaca": bukuBelumDibaca}


def hitungTotalBuku(bukuList):
    if not bukuList:
        return 0
    else:
        return 1 + hitungTotalBuku(bukuList[1:])


while True:
    print("RAK BUKU")
    print("MENU")
    print("1. Memasukkan buku ke rak")
    print("2. Lihat semua buku")
    print("3. Lihat buku yang sudah dibaca")
    print("4. Lihat buku yang belum dibaca")
    print("5. Hitung total buku di rak")
    print("6. Keluar")

    pilihMenu = int(input("Pilih menu (1-6): "))
    if pilihMenu == 1:
        buku = input("Masukkan judul buku: ")
        cek = input("Buku sudah dibaca/belum? (sudah/belum): ").lower()
        if cek == "sudah":
            sudahDibaca(buku)
            print("Buku sudah dibaca: ", bukuSudahDibaca)
        elif cek == "belum":
            belumDibaca(buku)
            print("Buku belum dibaca: ", bukuBelumDibaca)
        else:
            print("Pilihan tidak valid.")
    elif pilihMenu == 2:
        rak = rakBuku()
        print("Semua buku: ", rak["bukuSudahDibaca"] + rak["bukuBelumDibaca"])
    elif pilihMenu == 3:
        rak = rakBuku()
        print("Buku yang sudah dibaca: ", bukuSudahDibaca)
    elif pilihMenu == 4:
        rak = rakBuku()
        print("Buku yang belum dibaca: ", bukuBelumDibaca)
    elif pilihMenu == 5:
        rak = rakBuku()
        totalBuku = hitungTotalBuku(rak["bukuSudahDibaca"] + rak["bukuBelumDibaca"])
        print("Total buku di rak: ", totalBuku)
    elif pilihMenu == 6:
        break
    else:
        print("Pilihan tidak valid.")
