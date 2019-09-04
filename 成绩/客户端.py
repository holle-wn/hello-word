import socket, json


def data():
    while True:
        name = input('姓名:')
        one = input('选择题:')
        two = input('判断题:')
        there = input('填空题:')
        four = input('简答题:')
        five = input('翻译题:')
        total_points = input('总分:')
        judge_name = input('判卷人:')
        res = [name, one, two, there, four, five, total_points, judge_name]
        a = True
        for i in res:
            if i is '' or ' ' in i:
                a = False
        if a:
            return res
        print('格式错误, 不能为空加空字符')


def main():
    res = data()
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('192.168.1.13', 7788))
    res_json = json.dumps(res)
    tcp_socket.send(res_json.encode('utf8'))
    tcp_socket.close()


if __name__ == '__main__':
    main()
