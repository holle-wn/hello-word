# from socket import *
# import json, threading
#
#
# # 接收的格式 ['用户名', [ip], '消息']
# #             不动      遍历   不动
# def send_mess(udp_socket):
#     while True:
#         message, adder = udp_socket.recvfrom(1024)
#         res = json.loads(message.decode('utf8'))
#         json_str = json.dumps(res)
#         if res[0] == 1:
#             for i in res[2]:
#                 udp_socket.sendto(json_str.encode('utf8'), (res[i], 8081))
#         elif res[0] == 0:
#             for i in res[2]:
#                 udp_socket.sendto(json_str.encode('utf8'), (res[i], 8081))
#
#
# if __name__ == '__main__':
#     udp_socket = socket(AF_INET, SOCK_DGRAM)
#     udp_socket.bind(('', 7789))
#     t1 = threading.Thread(target=send_mess, args=(udp_socket,))
#     t1.start()
