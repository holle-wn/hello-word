from tkinter import *
import tkinter.font as tkFont
import time, socket, threading, json

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('', 8080))
dict_ip = {}


def send_message(inputtext, receive_text, message, user_name, adder):
    # 发送
    # 格式 [1, '用户名', 群名, [群聊里的ip], '要说的话']
    # 格式 [2, '用户名', '要说的话']

    # 获取本机电脑名
    myname = socket.gethostname()
    # 获取本机ip
    myaddr = socket.gethostbyname(myname)
    mess = inputtext.get('1.0', END)
    if message[0] == 1:
        message_send = [1, user_name, message[2], message[3], mess]
        print(message)
        for i in message[3]:
            if i == myaddr:
                continue
            message_send = json.dumps(message_send)
            udp_socket.sendto(message_send.encode('utf8'), (i, 8081))
    elif message[0] == 2:
        message_send = [2, user_name, mess]
        message_send = json.dumps(message_send)
        udp_socket.sendto(message_send.encode('utf8'), (adder[0], 8081))
    theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    receive_text.insert(END, user_name + ' ' + theTime + '说:\n')
    receive_text.insert(END, '' + mess + '')
    inputtext.delete(0.0, END)


def recv_message(receive_text, message, user_name):
    # 接收
    # 格式 [1, '用户名', 群名, [群聊里的ip], '要说的话']
    # 格式 [2, '用户名', ip, '要说的话']
    theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    receive_text.insert(END, message[1] + ' ' + theTime + '说:\n')
    receive_text.insert(END, message[-1])
    while True:
        try:
            mess, adder = udp_socket.recvfrom(1024)
            if mess:
                res = json.loads(mess.decode('utf8'))
                theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                receive_text.insert(END, res[1] + theTime + '说:\n')
                receive_text.insert(END, res[-1])
        except:
            tcp_server(user_name)


def close(tk, user_name):
    tk.destroy()
    tcp_server(user_name)


def tcp_server(user_name):
    # 接收一次跳转 recv_Message
    while True:
        try:
            message, adder = udp_socket.recvfrom(1024)
            message = json.loads(message.decode('utf8'))
            if message[0] == 0:
                # 创建文件
                with open(r'用户信息\群聊\{}.txt'.format(message[1]), 'w', encoding='utf8') as f:
                    for i in message[2]:
                        f.write(i + '\n')
            else:
                tcp_gui(message, user_name, adder)
        except:
            print('取消')


def tcp_gui(message, user_name, adder):
    tk = Tk()
    tk.geometry('800x600')
    f = Frame(tk)
    f1 = Frame(tk)
    f2 = Frame(tk)
    f3 = Frame(tk)
    # 显示消息的滚动条
    receive_scr = Scrollbar(f)
    receive_scr.pack(side=RIGHT)
    ft = tkFont.Font(family='Fixdsys', size=11)
    receive_text = Listbox(f, width=70, height=18, font=ft)
    receive_text['yscrollcommand'] = receive_scr.set
    receive_text.pack(expand=1, fill=BOTH)
    receive_scr['command'] = receive_text.yview()
    f.pack(expand=1, fill=BOTH)

    # 发送消息的滚动条
    lab = Label(f1, text='asdf', height=2)
    lab.pack(fill=BOTH)
    f1.pack(expand=1, fill=BOTH)
    input_Scrollbar = Scrollbar(f2)
    input_Scrollbar.pack(side=RIGHT, fill=Y)
    ft1 = tkFont.Font(family='Fixdsys', size=11)
    inputtext = Text(f2, width=70, height=8, font=ft1)
    inputtext['yscrollcommand'] = input_Scrollbar
    inputtext.pack(expand=1, fill=BOTH)
    input_Scrollbar['command'] = receive_text.yview()
    f2.pack(expand=1, fill=BOTH)

    sendButton = Button(f3, text='发送', width=10,
                        command=lambda: send_message(inputtext, receive_text, message, user_name, adder))
    sendButton.pack(expand=1, side=BOTTOM and RIGHT, padx=15, pady=8)
    sendButton = Button(f3, text='关闭', width=10, command=lambda: close(tk, user_name))
    sendButton.pack(expand=1, side=RIGHT, padx=15, pady=8)
    f3.pack(expand=1, fill=BOTH)
    t1 = threading.Thread(target=recv_message, args=(receive_text, message, user_name))
    t1.start()
    tk.mainloop()


if __name__ == '__main__':
    tcp_server('hhhh')
