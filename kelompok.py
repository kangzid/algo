bukuSudahDibaca = []
bukuBelumDibaca = []


def sudahDibaca(b):
    bukuSudahDibaca.append(b)


def belumDibaca(b):
    bukuBelumDibaca.append(b)


def lihatSemuaBuku(semuaBuku):
    for kunci, sb in semuaBuku.items():
        for s in sb:
            print("  |   ~  " + s)


def rakBuku():
    return {"bukuSudahDibaca": bukuSudahDibaca, "bukuBelumDibaca": bukuBelumDibaca}


def hitungTotalBuku(bukuList):
    if not bukuList:
        return 0
    else:
        return 1 + hitungTotalBuku(bukuList[1:])


while True:
    print("  |====================================|")
    print("  {             𝚁𝙰𝙺 𝙱𝚄𝙺𝚄               }")
    print("  |====================================|")
    print("  |====================================|")
    print("  |               ᴍᴇɴᴜ                 |")
    print("  |===|================================|")
    print("  | 1.| Memasukkan buku ke rak         |")
    print("  | 2.| Lihat semua buku               |")
    print("  | 3.| Lihat buku yang sudah dibaca   |")
    print("  | 4.| Lihat buku yang belum dibaca   |")
    print("  | 5.| Hitung total buku di rak       |")
    print("  | 6.| Keluar                         |")
    print("  |===|================================|")

    rak = rakBuku()
    pilihMenu = int(input("  |   |    Pilih menu (1-6):           |                                   :"))
    print("  |===|================================|")
    if pilihMenu == 1:
        buku = input(" Masukkan judul buku: ")
        cek = input("Buku sudah dibaca/belum? (sudah/belum): ").lower()
        if cek == "sudah":
            sudahDibaca(buku)
            print("  |====================================|")
            print("  | Buku sudah dibaca: ", bukuSudahDibaca)
            #print("  |====================================|")
        elif cek == "belum":
            belumDibaca(buku)
            print("  |====================================|")
            print("  | Buku belum dibaca: ", bukuBelumDibaca)
            #print("  |====================================|")
        else:
            print("     Maaf Pilihan tidak valid.")
    elif pilihMenu == 2:
        print("  |====================================|")
        print("  |            Semua Buku :            |")
        print("  |------------------------------------|")
        lihatSemuaBuku(rak)
        
    elif pilihMenu == 3:
        print("  |====================================|")
        print("  |         buku sudah dibaca :        |")
        print("  |====================================|")
        for bsd in bukuSudahDibaca:
            print(bsd.rjust(10))
            
        #print(bsd)
        
        
    elif pilihMenu == 4:
        print("  |====================================|")
        print("  |         buku belum dibaca :        |")
        print("  |====================================|")
        for bbd in bukuBelumDibaca:
            print(bbd.rjust(10))
        
    elif pilihMenu == 5:
        print("  |====================================|")
        print(
            "  |         Total buku di rak:  ",
            hitungTotalBuku(rak["bukuSudahDibaca"] + rak["bukuBelumDibaca"]),
        )
        print("  |====================================|")
    elif pilihMenu == 6:
        print("  {          𝑺𝒂𝒎𝒑𝒂𝒊 𝑱𝒖𝒎𝒑𝒂              }")
        print("  |====================================|")
        
        break
    else:
        print("  |    Maaf Pilihan Anda tidak valid   |")