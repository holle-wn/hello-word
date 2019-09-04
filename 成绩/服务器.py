import socket, json, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '笔试'
sheet['A1'] = '姓名'
sheet['B1'] = '选择题'
sheet['C1'] = '判断题'
sheet['D1'] = '填空题'
sheet['E1'] = '简答题'
sheet['F1'] = '翻译题'
sheet['G1'] = '总分'
sheet['H1'] = '判卷人'


def servers():
    tcp_servers = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_servers.bind(('', 7788))
    tcp_servers.listen(20)
    count = 0
    while True:
        count += 1
        new_tcp_socket, client_mes = tcp_servers.accept()
        message = new_tcp_socket.recv(1024)
        mess = message.decode('utf8')
        res = json.loads(mess)
        sheet.append(res)
        new_tcp_socket.close()
        wb.save('笔试成绩.xlsx')
        if count == 3:
            break
    tcp_servers.close()
    wb.close()


if __name__ == '__main__':
    servers()
