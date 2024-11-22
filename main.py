from akun import daftar_akun
import program

daftar_akun.append({
    "nama": "khusus nontls",
    "server": "bug.com",
    "port": "80",
    "type": "vmess",
    "uuid": "894347-938983494-94400",
    "alterId": "0",
    "cipher": "auto",
    "tls": "false",
    "skip-cert-verify": "true",
    "servername": "cah.contoh.com",
    "network": "ws",
    "ws-opts":"",
    "path": "/vmess",
    "headers":"",
    "host": "cah.gapesta.com",
    "udp": "true"
})
daftar_akun.append({
    "nama": "khusus tls",
    "server": "cah.contoh.com",
    "port": "443",
    "type": "vmess",
    "uuid": "894347-938983494-94300",
    "alterId": "0",
    "cipher": "auto",
    "tls": "true",
    "skip-cert-verify": "true",
    "servername": "bug.com",
    "network": "ws",
    "ws-opts":"",
    "path": "/vmess",
    "headers":"",
    "host": "cah.contoh.com",
    "udp": "true"
})

# Menu program
while True:
    print("# Menu")
    print("1. Daftar akun")
    print("2. Tambah akun")
    print("3. Hapus akun")
    print("4. Cari akun")
    print("5. menu config")
    print("0. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        program.display_akun(daftar_akun)
        print("="*28)
        print(f"  akun berhasil ditampilkan\n\ttotal akun {len(daftar_akun)}")
        print("="*28)
    elif menu == "2":
        akun = program.new_akun()
        daftar_akun.append(akun)
        print("="*28)
        print(f"  akun berhasil ditambahakan\n\ttotal akun {len(daftar_akun)}")
        print("="*28)
    elif menu == "3":
        program.hapus_akun(daftar_akun)
    elif menu == "4":
        program.cari_akun(daftar_akun)
    elif menu == "5":
        program.menu_config(daftar_akun)
    else:
        print("Menu tidak tersedia")
program.clear()
print("clear")
print("="*32)
print("Program selesai, sampai jumpa")
print("="*32)
    

