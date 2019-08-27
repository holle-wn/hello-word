from socket import *
import json, threading


def send_mess(udp_socket):
    while True:
        message, adder = udp_socket.recvfrom(1024)
        res = json.loads(message.decode('utf8'))
        list1 = [0, res[1], res[-1]]
        print(list1)
        json_str = json.dumps(list1)
        if res[0] == '0':
            udp_socket.sendto(json_str.encode('utf8'), (res[1], 8080))


if __name__ == '__main__':
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 7789))
    t1 = threading.Thread(target=send_mess, args=(udp_socket,))
    t1.start()
