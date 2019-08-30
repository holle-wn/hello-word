from tkinter import *
from tkinter import messagebox as m
import openpyxl, register, client, home_page


def fun1(event):
    register.register()


def fun2():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'sheet1'
    user_name = ent.get()
    user_password = ent1.get()
    if user_name and user_password:
        list1 = ['1', user_name, user_password]
        a = client.main(list1)
        if a[0] == '登录成功':
            for i in a[1]:
                sheet.append(i)
            print(a)
            wb.save(r'用户信息\信息.xlsx')
            m.askyesno('提示', a[0])
            tk.destroy()
            for i in a[1]:
                if user_name in i:
                    home_page.main(i[2])
        else:
            m.showerror('错误', a)
    else:
        m.showerror('错误', '用户名密码不能为空')


tk = Tk()
tk.geometry('400x250')
ent = Entry(tk)
ent.place(relx=0.35, rely=0.3)
lab = Label(tk, text='用户名:')
lab.place(relx=0.23, rely=0.3)

ent1 = Entry(tk)
ent1.place(relx=0.35, rely=0.4)
lab1 = Label(tk, text='密码:', )
lab1.place(relx=0.25, rely=0.4)

lab2 = Label(tk, text='注册账号')
lab2.place(relx=0, rely=0.9)
lab2.bind('<Button-1>', fun1)
btn = Button(tk, text='立即登录', command=fun2)
btn.place(relx=0.45, rely=0.55)

tk.mainloop()
