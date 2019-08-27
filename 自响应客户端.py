from tkinter import *
import tkinter.font as tkFont
import time, socket, threading, json

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 8080))
tcp_socket.listen(5)


def send_Message(new_socket, inputtext, receive_text, user_name):
    mess = inputtext.get('1.0', END)
    message = [user_name, mess]
    message = json.dumps(message)
    new_socket.send(message.encode('utf8'))
    theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    receive_text.insert(END, user_name + theTime + '说:\n')
    receive_text.insert(END, '' + mess + '')
    inputtext.delete(0.0, END)


def recv_Message(new_socket, receive_text, message, user_name):
    theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    receive_text.insert(END, message[0] + theTime + '说:\n')
    receive_text.insert(END, message[1])
    while True:
        try:
            mess = new_socket.recv(1024).decode('utf8')
            print(mess)
            if mess:
                res = json.loads(mess)
                theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                receive_text.insert(END, res[0] + theTime + '说:\n')
                receive_text.insert(END, res[1])
            else:
                new_socket.close()
        except:
            tcp_server(user_name)


def close(tk):
    tk.destroy()


def tcp_server(user_name):
    while True:
        try:
            new_socket, adder = tcp_socket.accept()
            message = new_socket.recv(1024).decode('utf8')
            message = json.loads(message)
            if message:
                threading.Thread(target=tcp_gui, args=(new_socket, message, user_name)).start()
        except:
            print('取消')


def tcp_gui(new_socket, message, user_name):
    tk = Tk()
    tk.title(user_name)
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
                        command=lambda: send_Message(new_socket, inputtext, receive_text, user_name))
    sendButton.pack(expand=1, side=BOTTOM and RIGHT, padx=15, pady=8)
    sendButton = Button(f3, text='关闭', width=10, command=lambda: close)
    sendButton.pack(expand=1, side=RIGHT, padx=15, pady=8)
    f3.pack(expand=1, fill=BOTH)
    t1 = threading.Thread(target=recv_Message, args=(new_socket, receive_text, message, user_name))
    t1.start()
    tk.mainloop()


if __name__ == '__main__':
    tcp_server('hhhh')
