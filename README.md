8月项目

使用网络编程与线程做的一个类似内网通的聊天系统

涉及模块:socket, pymysql, tkinter, openpyxl, threading, json

功能: 登录账号, 注册账号, 实现单聊, 创建聊天群及实现聊天

实现: 

      1.使用tkinter搭建各个界面

      2.注册以及登录, 使用tcp套接字以及json传输数据并使用pymysql保存信息及查询信息
      
      3.单聊 使用tcp套接字传输聊天信息
      
      4.创建聊天群及实现聊天, 创建udp套接字 json传输一个列表包含群里所有人的ip以及要发送的信息
      
        创建udp服务器接收json字符串并遍历ip一个一个转发信息
