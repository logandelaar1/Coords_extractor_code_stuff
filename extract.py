import socket
import re
import threading
import datetime

# Function to extract latitude, longitude, and heading from the given dat
def handle_connection(host, port):
    filename = f"{host}_{port}_all_GAME.txt"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        with open(filename, 'a') as f:
            while True:
                data = s.recv(1024).decode('utf-8')
                if not data:
                    break
                f.write(f"{data}\n")
                f.flush()
                print(f"Data saved to {filename}")

# Main function to handle multiple IP addresses
def main():
    ip_addresses = [
        '192.168.1.31',
        '192.168.1.51',
        '192.168.1.91',
        '192.168.1.81',
        '192.168.1.71',
        '192.168.1.101'
    ]
    
    port = 8003

    threads = []

    for ip in ip_addresses:
        thread = threading.Thread(target=handle_connection, args=(ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
