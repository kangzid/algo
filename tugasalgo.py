bukuSudahDibaca = []
bukuBelumDibaca = []

def sudahDibaca(b):
    bukuSudahDibaca.append(b)

def belumDibaca(b):
    bukuBelumDibaca.append(b)

def rakBuku():
    return {
        "bukuSudahDibaca": bukuSudahDibaca,
        "bukuBelumDibaca": bukuBelumDibaca
    }

def hitungTotalBuku():
    return len(bukuSudahDibaca) + len(bukuBelumDibaca)

def tampilkanSemuaBuku():
    rak = rakBuku()
    semuaBuku = rak["bukuSudahDibaca"] + rak["bukuBelumDibaca"]
    print("|=======================================|")
    print("Semua buku di rak: ")
    for buku in semuaBuku:
        print("- ", buku)
    print("|=======================================|")

while True:
    
    print("  |}=====  MENU SYSTEM RAK BUKU ====={|")
    print("=======================================")
    print("| 1.|]  Memasukkan buku ke rak         [|")
    print("| 2.|]  Lihat semua buku               [|")
    print("| 3.|]  Lihat buku yang sudah dibaca   [|")
    print("| 4.|]  Lihat buku yang belum dibaca   [|")
    print("| 5.|]  Hitung total buku di rak       [|")
    print("| 6.|]  Tampilkan semua buku           [|")
    print("| 7.|]  Keluar                         [|")
    print("=======================================")

    pilihMenu = int(input("         Pilih menu (1-7): "))
    print(".")
    if pilihMenu == 1:
        print("|==================================|")
        buku = input("Masukkan judul buku: ")
        cek = input("Buku sudah dibaca/belum? (sudah/belum): ").lower()
        if cek == "sudah":
            sudahDibaca(buku)
            print("|==================================|")
            print("  Buku sudah dibaca: ", bukuSudahDibaca)
            print("|==================================|")
        elif cek == "belum":
            belumDibaca(buku)
            print("|=======================================|")
            print("  Buku belum dibaca: ", bukuBelumDibaca)
            print("|=======================================|")
        else:
            print("Pilihan tidak valid.")
    elif pilihMenu == 2:
        rak = rakBuku()
        print("|=========================|")
        print("Semua buku: ", rak["bukuSudahDibaca"] + rak["bukuBelumDibaca"])
        print("|=========================|")
    elif pilihMenu == 3:
        rak = rakBuku()
        print("|=======================================|")
        print("Buku yang sudah dibaca: ", rak["bukuSudahDibaca"])
        print("|=======================================|")
    elif pilihMenu == 4:
        rak = rakBuku()
        print("|=======================================|")
        print("Buku yang belum dibaca: ", rak["bukuBelumDibaca"])
        print("|=======================================|")
    elif pilihMenu == 5:
        totalBuku = hitungTotalBuku()
        print("|=========================|")
        print("   Total buku di rak: ", totalBuku )
        print("|=========================|")
    elif pilihMenu == 6:
        tampilkanSemuaBuku()
    elif pilihMenu == 7:
        print("|=========================|")
        print("|}   - Sampai jumpa -    {|")
        print("|=========================|")
        break
    else:
        print("Pilihan tidak valid.")
