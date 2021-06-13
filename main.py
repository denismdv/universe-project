import tkinter as tk
import tkinter.ttk as ttk



def radiobutton():
    rb1 = tk.Radiobutton(root, text="сталь", variable=pol, value=1)
    rb2 = tk.Radiobutton(root, text="бронза", variable=pol, value=2)
    rb3 = tk.Radiobutton(root, text="алюминий", variable=pol, value=3)
    rb1.place(x=30, y=140)
    rb2.place(x=30, y=170)
    rb3.place(x=30, y=200)


def confirm():
    global m3, m1, m2, f, message, n, s
    a = pol.get()
    v = entry_pole1.get()
    size = ['8', '10', '12', '15', '17']
    if entry_pole.get() in size:
        d = entry_pole.get()
    else:
        d = 'Неверно задан диаметр!!!'
    if a == 1:
        message = "Информация о детали ( сталь" + ', ' + str(cb1.get()) + ', ' + d + ' мм' + ') ' + 'Ответсвенный за парттию '+v
        m1 = message
        n += 1
        s += 1
    elif a == 2:
        message = "Информация о детали ( бронза" + ', ' + str(cb1.get()) + ', ' + d + ' мм' + ') '+ 'Ответсвенный за парттию '+v
        m2 = message
        n += 1
        s += 1
    elif a == 3:
        message = "Информация о детали ( аллюминий" + ', ' + str(cb1.get()) + ', ' + d + ' мм' + ') '+ 'Ответсвенный за парттию '+v
        m3 = message
        n += 1
        s += 1
    pole1.config(text=message)
    if n == 3:
        n = 0
        f = m1 + '\n' + m2 + '\n' + m3
        pole2.config(text=f)
    h = 'Количество деталий: ' + str(s)
    pole3.config(text=h)
    if check.get() == 1:
        if int(entry_pole2.get()) > 10:
            pole4.config(text='Неверное кол-во деталей!')


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('650x450+300+200')
    root.title('Рабочее место работника приемочного контроля на заводе')
    root.resizable(False, False)
    pol = tk.IntVar()
    check = tk.IntVar()
    enter = tk.StringVar()
    radiobutton()
    n = 0 ; s = 0
    pole1 = tk.Label(root)
    pole1.place(x=30, y=20)
    pole2 = tk.Label(root)
    pole2.place(x=30, y=60)
    pole3 = tk.Label(root)
    pole3.place(x=30, y=120)
    pole4 = tk.Label(root)
    pole4.place(x=300, y=40)
    val1 = ['втулка', 'шестерня', 'вал']
    cb1 = ttk.Combobox(root, values=val1, state='readonly')
    cb1.place(x=110, y=145)
    pl = tk.Label(root, text='Задайте диаметр детали:')
    pl.place(x=270, y=145)
    entry_pole = tk.Entry(root, width=15)
    entry_pole.place(x=420, y=145)
    p2 = tk.Label(root, text='Имя рабочего:')
    p2.place(x=320, y=230)
    entry_pole1 = tk.Entry(root, width=15)
    entry_pole1.place(x=410, y=230)
    entry_pole2 = tk.Entry(root, textvariable=enter)
    entry_pole2.place(x=30, y=230)
    check_box = tk.Checkbutton(root, text='Тестирование', variable=check, onvalue=1, offvalue=0)
    check_box.place(x=200, y=230)
    button = tk.Button(root, text='Подтвердить', command=confirm)
    button.place(x=30, y=400)
    root.mainloop()

