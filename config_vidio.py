vidio = ["104.17.70.206", "104.17.72.206", "104.17.71.206", "104.17.73.206", "104.17.74.206", "172.64.153.235", "172.64.155.235", "104.16.112.133", "104.16.143.237", "162.159.128.79", "104.18.43.134", "104.16.242.118", "104.18.43.123", "104.18.40.22", "172.64.151.90", "104.18.21.37", "172.64.148.245", "162.159.135.91", "172.64.155.61", "104.18.32.195", "188.114.96.3", "162.159.153.4", "172.64.155.179", "172.67.37.55", "172.64.147.209", "162.159.135.91", "104.18.40.14", "104.18.33.162", "104.18.15.182", "172.66.47.13", "104.18.24.109", "104.18.29.127", "104.18.19.109", "104.18.28.127", "104.18.18.109", "162.159.130.11", "104.16.95.80", "104.18.41.18", "104.16.20.254", "104.18.36.212", "172.64.146.238", "172.64.151.106", "172.67.5.14", "04.22.5.240", "162.159.140.159"]
bb_vidio = ["static.web.prod.vidiocdn.com", "sb.scorecardresearch.com", "token-media-vidio-com.akamaized.net", "static-quiz.prod.vidiocdn.com"]
tls_vidio = ["static.web.prod.vidiocdn.com", "sb.scorecardresearch.com", "token-media-vidio-com.akamaized.net", "static-quiz.prod.vidiocdn.com"]


def config_all_vidio(vidio, host = "cah.gapesta.my.id", uuid = "1b934a34-daa2-4c38-9816-7f265e8e5e6c"):
    print("proxies:")
    for no, bug in enumerate(vidio):
        print(f"  - name: xl-unli-{no}")
        print(f"    server: {bug}")
        print("    port: 80")
        print("    type: vmess")
        print(f"    uuid: {uuid}")
        print("    alterId: 0")
        print("    cipher: auto")
        print("    tls: false")
        print("    skip-cert-verify: true")
        print(f"    servername: {host}")
        print("    network: ws")
        print("    ws-opts:")
        print("      path: /vmess")
        print("      headers:")
        print(f"        Host: {host}")
        print("    udp: true")

def config_vidio_bb(vidio, host = "cah.gapesta.my.id", uuid = "1b934a34-daa2-4c38-9816-7f265e8e5e6c"):
    for  no, bug, in enumerate(vidio):
        print(f"  - name: xl-unli-bb-{no}")
        print(f"    server: {host}")
        print("    port: 80")
        print("    type: vmess")
        print(f"    uuid: {uuid}")
        print("    alterId: 0")
        print("    cipher: auto")
        print("    tls: false")
        print("    skip-cert-verify: true")
        print(f"    servername: {host}")
        print("    network: ws")
        print("    ws-opts:")
        print("      path: /vmess")
        print("      headers:")
        print(f"        Host: {bug}")
        print("    udp: true")

def config_all_vidio_tls(vidio, host = "cah.gapesta.my.id", uuid = "1b934a34-daa2-4c38-9816-7f265e8e5e6c"):
     for no, bug in enumerate(vidio):
            print((f"  - name: xl-unli-tls-{no}"))
            print(f"    server: {host}")
            print("    port: 443")
            print("    type: vmess")
            print(f"    uuid: {uuid}")
            print("    alterId: 0")
            print("    cipher: auto")
            print("    tls: true")
            print("    skip-cert-verify: true")
            print(f"    servername: {bug}")
            print("    network: ws")
            print("    ws-opts:")
            print("      path: /vmess")
            print("      headers:")
            print(f"        Host: {host}")
            print("    udp: true")



config_all_vidio(vidio)
config_vidio_bb(bb_vidio)
config_all_vidio_tls(tls_vidio)
    


