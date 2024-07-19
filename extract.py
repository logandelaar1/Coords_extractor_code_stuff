import socket
import threading
import datetime
initial_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# Function to extract latitude, longitude, and heading from the given data
def handle_connection(host, port):
    filename = f"{host}_{port}_{initial_timestamp}_GAME.txt"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        with open(filename, 'a') as f:
            while True:
                data = s.recv(1024).decode('utf-8')
                if not data:
                    break
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"{timestamp} - {data}\n")
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
        '192.168.1.101',
        '192.168.1.111',
        '192.168.1.21',
        '192.168.1.61',
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
