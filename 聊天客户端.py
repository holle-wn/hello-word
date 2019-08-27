from tkinter import *
import tkinter.font as tkFont
import time, socket, threading, json


def main(mess: list):
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((mess[1], 8080))

    def get_send():
        mess.pop()
        message = inputtext.get('1.0', END)
        mess.append(message)
        res = json.dumps(mess)
        theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        receive_text.insert(END, mess[0] + theTime + '说:\n')
        receive_text.insert(END, '' + message + '')
        tcp_client.send(res.encode('utf8'))
        inputtext.delete(0.0, END)

    def client_socket():
        while True:
            serverMsg = tcp_client.recv(1024).decode('utf8')
            res = json.loads(serverMsg)
            theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            receive_text.insert(END, res[0] + theTime + '说:\n')
            receive_text.insert(END, res[1])

    def close():
        tk.destroy()

    tk = Tk()
    tk.geometry('800x600')

    f = Frame(tk)
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
    lab = Label(f2, text='asdf', height=2)
    lab.pack(fill=BOTH)
    f2.pack(expand=1, fill=BOTH)
    input_Scrollbar = Scrollbar(f2)
    input_Scrollbar.pack(side=RIGHT, fill=Y)
    ft1 = tkFont.Font(family='Fixdsys', size=11)
    inputtext = Text(f2, width=70, height=8, font=ft1)
    inputtext['yscrollcommand'] = input_Scrollbar
    inputtext.pack(expand=1, fill=BOTH)

    sendButton = Button(f3, text='发送', width=10, command=get_send)
    sendButton.pack(expand=1, side=BOTTOM and RIGHT, padx=15, pady=8)
    sendButton = Button(f3, text='关闭', width=10, command=close)
    sendButton.pack(expand=1, side=RIGHT, padx=15, pady=8)
    f3.pack(expand=1, fill=BOTH)
    t1 = threading.Thread(target=client_socket)
    t1.start()
    tk.mainloop()


if __name__ == '__main__':
    main(['人生如梦', '192.168.1.13'])
