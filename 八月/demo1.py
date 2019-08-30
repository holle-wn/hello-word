from tkinter import *
import tkinter.font as tkFont
import time, socket, threading, json


# 格式 [1, '用户名', 群名, [群聊里的ip], '要说的话']
# 格式 [2, '用户名', ip, '要说的话']

def main(mess):
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_send():
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = inputtext.get('1.0', END)
        mess.append(message)
        res = json.dumps(mess)
        theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        receive_text.insert(END, mess[1] + '  ' + theTime + '说:\n')
        receive_text.insert(END, '' + message + '')
        if mess[0] == 1:
            tk.title(mess[2])
            for i in mess[3]:
                send_socket.sendto(res.encode('utf8'), (i, 8080))
        elif mess[0] == 2:
            send_socket.sendto(res.encode('utf8'), (mess[2], 8080))
        send_socket.close()
        inputtext.delete(0.0, END)
        mess.pop()
        # tk.destroy()
        # udp_client.close()

    def client_socket():
        udp_client.bind(('', 8081))
        while True:
            try:
                serverMsg, adder = udp_client.recvfrom(1024)
                res = json.loads(serverMsg)
                theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                receive_text.insert(END, res[1] + '  ' + theTime + '说:\n')
                receive_text.insert(END, res[-1])
            except:
                pass

    def close():
        tk.destroy()
        udp_client.close()

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
