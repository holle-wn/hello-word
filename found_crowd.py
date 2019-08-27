import openpyxl
from tkinter import *
from tkinter import messagebox as m

wb = openpyxl.load_workbook(r'存储信息\信息.xlsx')
sheet = wb['sheet1']


def fun1(lib, lib1):
    for i in lib.curselection():
        lib1.insert(0, lib.get(i))


def fun2(lib1):
    for i in lib1.curselection():
        lib1.delete(i)


def fun3(tk, lib1, ent):
    s = set()
    for i in lib1.get(0, END):
        s.add(i)
    with open(r'存储信息\{}.txt'.format(ent.get()), 'a', encoding='utf8') as f:
        for i in s:
            split_str = i.split(':')
            f.write(sheet[int(split_str[0])][1].value + '\n')
    m.askyesno('Yes or No', '创建成功')
    tk.destroy()


def main():
    tk = Toplevel()
    tk.geometry('400x400')
    tk.title('创建聊天室')
    list1 = []
    for i in range(1, sheet.max_row + 1):
        list1.append(str(i) + ':' + sheet[i][2].value)
    lib = Listbox(tk)
    lib1 = Listbox(tk)
    for i in list1:
        lib.insert(0, i)
    lib.place(relx=0, rely=0.1)
    lab = Label(tk, text='输入聊天室名称:')
    lab.place(relx=0.25, rely=0)
    ent = Entry(tk, width=20)
    ent.place(relx=0.5, rely=0)
    btn = Button(tk, text='添加>>', command=lambda: fun1(lib, lib1), width=20)
    btn1 = Button(tk, text='删除<<', command=lambda: fun2(lib1), width=20)
    btn2 = Button(tk, text='确定', command=lambda: fun3(tk, lib1, ent), width=20)
    btn.place(relx=0.3, rely=0.6)
    btn1.place(relx=0.3, rely=0.7)
    btn2.place(relx=0.3, rely=0.8)
    lib1.place(relx=0.6, rely=0.1)

    tk.mainloop()


if __name__ == '__main__':
    main()
