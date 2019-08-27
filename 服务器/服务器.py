import socket, pymysql, json
from multiprocessing import Pool


def mysql_statement(text):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='248548', db='class')
    cursor = conn.cursor()
    cursor.execute(text)
    row = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return row


def servers():
    # 创建套接字
    tcp_servers = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口 7788
    tcp_servers.bind(('', 7788))
    # 监听TCP
    tcp_servers.listen(5)
    # 等待客户端链接
    while True:
        new_tcp_socket, client_mes = tcp_servers.accept()
        ip, post = client_mes
        # 将客户端的数据写入到数据库中
        message = new_tcp_socket.recv(1024)
        if message:
            a = message.decode('utf8')
            res = json.loads(a)
            if res[0] == '1':
                row = mysql_statement(
                    "select * from userinfo where user_name = '%s'and user_password='%s'" % (res[1], res[2]))
                if len(row) == 1:
                    all_userinfo = mysql_statement("select user_name, ip, nickname from userinfo")
                    json_all = json.dumps(['登录成功', all_userinfo])
                    new_tcp_socket.send(json_all.encode('utf8'))
                    new_tcp_socket.close()
                else:
                    new_tcp_socket.send('用户名或者密码错误'.encode('utf8'))
                    new_tcp_socket.close()
            elif res[0] == '0':
                mysql_statement('select user_name from userinfo')
                try:
                    mysql_statement(
                        "insert into userinfo values ('%s', '%s', '%s', '%s')" % (res[1], res[2], ip, res[3]))
                    new_tcp_socket.send('注册成功'.encode('utf8'))
                    new_tcp_socket.close()
                except Exception:
                    new_tcp_socket.send('用户名已存在'.encode('utf8'))
                    new_tcp_socket.close()
            elif res[0] == '2':
                all_userinfo = mysql_statement("select user_name, ip, nickname from userinfo")
                json_all = json.dumps(['登录成功', all_userinfo])
                new_tcp_socket.send(json_all.encode('utf8'))
                new_tcp_socket.close()
        else:
            new_tcp_socket.close()
            break

    tcp_servers.close()


if __name__ == '__main__':
    servers()
