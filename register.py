from tkinter import *
from tkinter import messagebox as m
import client


def register():
    tk = Toplevel()

    def fun():
        name, password, nickname = ent.get(), ent1.get(), ent2.get()
        if name == '' or password == '' or nickname == '':
            m.showwarning('error', '用户名密码以及邮箱地址不能为空')
        else:
            list1 = ['0', name, password, nickname]
            a = client.main(list1)
            if a[0] == '注册成功':
                m.askyesno("YesNo", "注册成功")
                tk.destroy()
            else:
                m.showerror("错误", a)

    # tk = Tk()
    tk.geometry('500x400')

    lab = Label(tk, text='欢迎注册在聊天', font=('', 20))
    lab.place(relx=0.5, rely=0.1)
    lab = Label(tk, text='每一天,乐在沟通。', font=('', 15))
    lab.place(relx=0.5, rely=0.25)
    photo = PhotoImage(file=r'图片\1.png')
    lab = Label(tk, image=photo)
    lab.place(relx=0, rely=0)

    ent = Entry(tk)
    ent.place(relx=0.6, rely=0.4)
    ent1 = Entry(tk)
    ent1.place(relx=0.6, rely=0.5)
    ent2 = Entry(tk)
    ent2.place(relx=0.6, rely=0.6)

    lab = Label(tk, text='用户名')
    lab.place(relx=0.5, rely=0.4)
    lab = Label(tk, text='密码')
    lab.place(relx=0.51, rely=0.5)
    lab = Label(tk, text='昵称')
    lab.place(relx=0.51, rely=0.6)

    btn = Button(tk, text='立即注册', command=fun, bg='#3487ff', fg='white', font=('', 15), width=20)
    btn.place(relx=0.48, rely=0.7)

    tk.mainloop()


if __name__ == '__main__':
    register()
