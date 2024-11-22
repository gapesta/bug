import sys, subprocess
import bug

#menampilkan semua akun
def display_akun(daftar_akun):
    for akun in daftar_akun:
        print("="*5+f" datar akun "+"="*5)
        print(f"nama : {akun['nama']}")
        print(f"server : {akun['server']}")
        print(f"port: {akun['port']}")
        print(f"uuid: {akun['uuid']}")
        print(f"alterId: {akun['alterId']}")
        print(f"cipher: {akun['cipher']}")
        print(f"tls: {akun['tls']}")
        print(f"skip-cert-verify: {akun['skip-cert-verify']}")
        print(f"servername: {akun['servername']}")
        print(f"network: {akun['network']}")
        print(f"ws-opts: {akun['ws-opts']}")
        print(f"  path: {akun['path']}")
        print(f"  headers: {akun['headers']}")
        print(f"    host: {akun['host']}")
        print(f"udp: {akun['udp']}")
        print("="*22+"\n")

#menambah akun baru
def new_akun():
    nama = input("Nama : ")
    port = input("port : ")
    type = input("type : ")
    uuid = input("uuid : ")
    tls = input("tls : ")

    network = input("network : "
                    )
    path = input("path : ")

    host = input("host : ")
    akun = {
    "nama": nama,
    "server": host,
    "port": port,
    "type": type,
    "uuid": uuid,
    "alterId": "0",
    "cipher": "auto",
    "tls": tls,
    "skip-cert-verify": "true",
    "servername": host,
    "network": network,
    "ws-opts":"",
    "path": path,
    "headers":"",
    "host": host,
    "udp": "true"
    }
    return akun

#bersihan layar terminal
def clear():
    os = sys.platform
    if os == 'linux' or os == 'darwin':
        subprocess.run('clear', shell=True)
    elif os == 'win32':
        subprocess.run('cls', shell=True)
    else:
        print("system tidak bisa membersikan layar")

#hapus akun
def hapus_akun(daftar_kontak):
    nama = input("nama akun yang akan dihapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        akun = daftar_kontak[i]
        if nama == akun["nama"]:
            index = i 
            break

    if index == -1:
        print("="*28)
        print(f"Data akun dengan nama: {nama} tidak ditemukan")
        print("="*28)
    else:
        del daftar_kontak[index]
        print("="*30)
        print(f"Berhasil menghapus data akun dengan nama: {nama}")
        print("="*30)

#cari akun
def cari_akun(daftar_kontak):
    nama_yg_dicari = input("Nama yang dicari : ")

    for akun in daftar_kontak:
        nama = akun["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("="*3+f" tampilkan akun yang di cari "+"="*3)
            print(f"nama : {akun['nama']}")
            print(f"server : {akun['server']}")
            print(f"port: {akun['port']}")
            print(f"uuid: {akun['uuid']}")
            print(f"alterId: {akun['alterId']}")
            print(f"cipher: {akun['cipher']}")
            print(f"tls: {akun['tls']}")
            print(f"skip-cert-verify: {akun['skip-cert-verify']}")
            print(f"servername: {akun['servername']}")
            print(f"network: {akun['network']}")
            print(f"ws-opts: {akun['ws-opts']}")
            print(f"  path: {akun['path']}")
            print(f"  headers: {akun['headers']}")
            print(f"    host: {akun['host']}")
            print(f"udp: {akun['udp']}")
            print("="*22+"\n")
        else:
            print("="*22+"\n")
            print(f"akun dengan nama: {nama_yg_dicari} tidak di temukan")
            print("="*22+"\n")

#fungsi bikin file
def bikin_file(nama_file):
    try:
        f = open(nama_file, "x")
                    
        print(f"file {nama_file} berhasil di buat")
            
    except:
        print(f"file {nama_file} gagal di buat")
        print("buatlah nama file yang lain")
    finally:
        f.close()
        sts = f.closed()
        print(f"status file {sts}")

#menampilakan bug
def tampilkan_bug():
    print("menampilkan bug")
    print("="*20)
    for key, vel in bug.kumpulan_bug.items():
        print(key)
    print("="*20)

#tambah bug
def tambah_bug():
    nama = input("masukan nama bug: ")
    bag = input("masukan nama bug: ")
    bug.kumpulan_bug.update({nama : bag})
    print(f"menambah bug dengan nama {nama} dan nama bug {bag} berhasil")



#menu config
def menu_config(akun):
    while True:
        print("="*32)
        print("# Menu config")
        print("1. bikin file")
        print("2. bikin config")
        print("3. tambah bug")
        print("0. Keluar dari menu config")
        #mencari nomer yang di pilih
        inp = input("menu config: ")
        if inp == "1":
            #manggil fungsi bikin file
            print("silakan bikin nama file Contoh: configku.yaml")
            nama_file = input()
            bikin_file(nama_file)
            break
        elif inp == "2":
            #menayakan apakah sudah bikin file
            print("apakah anda sudah bikin file?")
            print("yes atau y jika sudah dan no atau n jika belum")
            msk = input()
            if msk.lower() == "yes" or msk.lower() == "y":
                 print("="*32)
                 print("masukan nama file yang akan diisi config")
                 nama_file = input()
                 print("="*32)
                 print("menampilkan nama akun")
                 for index in akun:                     
                     nama = index["nama"]
                     print(f"ada akun nama: {nama}")
                 print("="*20)
                 print("masukan nama akun yang mau di pake")
                 ipt = input()
                 for index in akun:
                     nama = index["nama"]
                     if ipt.lower() == nama.lower():
                         tulis = open(nama_file, 'a')
                         port = index['port']
                         type = index['type']
                         uuid = index['uuid']
                         tls = index['tls']
                         network = index['network']
                         path = index['path']
                         host = index['host']
                         #menampilkan bug
                         tampilkan_bug()
                         print("masukan bug yang ingin di pake")
                         put = input()
                         kum_bug = bug.kumpulan_bug[put]
                         if put == "vidio nontls":                             
                             print("proxies:",file=tulis)
                             for bugnya in kum_bug:
                                 print(f"  - name: {nama}-",file=tulis)
                                 print(f"    server: {bugnya}",file=tulis)
                                 print(f"    port: {port}",file=tulis)
                                 print(f"    type: {type}",file=tulis)
                                 print(f"    uuid: {uuid}",file=tulis)
                                 print("    alterId: 0",file=tulis)
                                 print("    cipher: auto",file=tulis)
                                 print("    skip-cert-verify: true",file=tulis)
                                 print(f"    tls: {tls}",file=tulis)
                                 print(f"    servername: {host}",file=tulis)
                                 print(f"    network: {network}",file=tulis)
                                 print("    ws-opts:",file=tulis)
                                 print(f"      path: {path}",file=tulis)
                                 print("      headers:",file=tulis)
                                 print(f"        Host: {host}",file=tulis)
                                 print("    udp: true",file=tulis)
                         elif put == "vidio bb":
                             print("proxies:",file=tulis)
                             for bugnya in kum_bug:
                                 print(f"  - name: {nama}-",file=tulis)
                                 print(f"    server: {host}",file=tulis)
                                 print(f"    port: {port}",file=tulis)
                                 print(f"    type: {type}",file=tulis)
                                 print(f"    uuid: {uuid}",file=tulis)
                                 print("    alterId: 0",file=tulis)
                                 print("    cipher: auto",file=tulis)
                                 print("    skip-cert-verify: true",file=tulis)
                                 print(f"    tls: {tls}",file=tulis)
                                 print(f"    servername: {host}",file=tulis)
                                 print(f"    network: {network}",file=tulis)
                                 print("    ws-opts:",file=tulis)
                                 print(f"      path: {path}",file=tulis)
                                 print("      headers:",file=tulis)
                                 print(f"        Host: {bugnya}",file=tulis)
                                 print("    udp: true",file=tulis)
                         elif put == "vidio tls":
                             print("proxies:",file=tulis)
                             for bugnya in kum_bug:
                                 print(f"  - name: {nama}-",file=tulis)
                                 print(f"    server: {host}",file=tulis)
                                 print(f"    port: {port}",file=tulis)
                                 print(f"    type: {type}",file=tulis)
                                 print(f"    uuid: {uuid}",file=tulis)
                                 print("    alterId: 0",file=tulis)
                                 print("    cipher: auto",file=tulis)
                                 print("    skip-cert-verify: true",file=tulis)
                                 print(f"    tls: {tls}",file=tulis)
                                 print(f"    servername: {host}",file=tulis)
                                 print(f"    network: {network}",file=tulis)
                                 print("    ws-opts:",file=tulis)
                                 print(f"      path: {path}",file=tulis)
                                 print("      headers:",file=tulis)
                                 print(f"        Host: {bugnya}",file=tulis)
                                 print("    udp: true",file=tulis)
                         else:
                             print(f"maaf bug dengan nama: {put} tidak tersedia")
                             
                         tulis.close()
                         print("="*32)
                         print("\tconfig berhasil di bikin")
                         print(f"silakan cek file dengan nama: {nama_file}")
                         print("="*32)
                         break
                     elif len(ipt) <= 8:
                         break
                     elif ipt == "":
                         break
                     elif len(ipt) >= 8:
                         continue
                     else:
                         print("="*32)
                         print(f"akun dengan nama: {ipt} tidak tersedia")
                         print("="*32)
                         
            #jika belum bikin file panggil fungsi bikin file
            elif msk.lower() == "no" or msk.lower() == "n":
                 print("="*32)
                 print("silakan bikin nama file Contoh: configku.yaml")
                 print("="*32)
                 nama_file = input()
                 bikin_file(nama_file)
                 break
            #jika inputnya ngaco jalankan ini
            else:
                 print("="*32)
                 print(f"printah {msk} tidak tersedia")
                 print("="*32)
                 break
        elif inp == "3":
            tambah_bug()
        elif inp == "0":
             break
        
        else:
             print("="*32)
             print(f"nomer {inp} tidak tersedia")
             print("="*32)
             break



            



