import socket, json


def main(res):
    res = json.dumps(res)
    # 创建套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 链接服务器
    tcp_client.connect(('192.168.1.13', 7788))
    # 发送数据
    tcp_client.send(res.encode('utf8'))
    # 接收服务器返回的数据
    message = tcp_client.recv(1024)
    decode_message = message.decode('utf8')
    if len(decode_message) < 10:
        res_recv = [decode_message]
    else:
        res_recv = json.loads(decode_message)

    # 关闭链接
    tcp_client.close()
    return res_recv


if __name__ == '__main__':
    main('sad')
