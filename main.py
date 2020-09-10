import json
from tkinter import *
import time

with open("js0n.json", "r") as f:
    data = json.load(f)

m = []
for name in data:
    m.append(name)

root1 = Tk()
root1.geometry('225x220')
root1.title('LoginSys')

def loginsys():
    root = Toplevel(root1)
    root.geometry('240x220')
    def get_password():
        pass1 = entry_login2.get()
        user1 = entry_login.get()
        if user1 in m:
            if pass1 == data[f'{user1}']['password']:
                label4 = Label(root, text='Login success', fg='green')
                label4.grid(row=6, column=1)
                entry_login.delete(0, END)
                entry_login2.delete(0, END)
                loginsucces = Toplevel(root)
                loginsucces.geometry('700x650')
                loginsucces.title('bruh')

            else:
                entry_login.delete(0, END)
                entry_login2.delete(0, END)
                label4 = Label(root, text='Invalid Input!', fg='red')
                label4.grid(row=6, column=1)
        else:
            entry_login.delete(0, END)
            entry_login2.delete(0, END)
            label4 = Label(root, text='Invalid Input!', fg='red')
            label4.grid(row=6, column=1)
    # defining ui shit
    label1 = Label(root, text='Username')
    entry_login = Entry(root, width=35, borderwidth=5)
    label3 = Label(root, text='____________________________________________')
    label2 = Label(root, text='Password')
    entry_login2 = Entry(root, width=35, borderwidth=5, show='*')
    buttonbruhv = Button(root, text='Login', pady=7, padx=17, bg='gray', command=get_password)

    # grid sys shit
    entry_login2.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    label2.grid(row=3, column=1)
    label3.grid(row=2, column=1)
    entry_login.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    label1.grid(row=0, column=1)
    buttonbruhv.grid(row=5, column=1)


def registersys():
    def save_data():
        if len(entry_loginup.get()) > 5 and len(entry_login2po.get()) > 5:
            if len(entry_loginup.get()) < 20 and len(entry_login2po.get()) < 20:
                data[f'{entry_loginup.get()}'] = {}
                data[f'{entry_loginup.get()}']["password"] = f"{entry_login2po.get()}"
                entry_loginup.delete(0, END)
                entry_login2po.delete(0, END)
                with open("js0n.json", "w") as f2:
                    json.dump(data, f2, indent=2)
                labelbrtuhvy = Label(root3, text='You\'ve succesfully registered!', fg='green')
                labelbrtuhvy.grid(row=6, column=1)
            elif len(entry_loginup.get()) > 20 and len(entry_login2po.get()) > 20:
                labelbrtuhvo = Label(root3, text='Password or name is too long!', fg='red')
                labelbrtuhvo.grid(row=6, column=1)
        elif len(entry_loginup.get()) < 5 and len(entry_login2po.get()) < 5:
            labelbrtuhv = Label(root3, text='Password or name is too short!', fg='red')
            labelbrtuhv.grid(row=6, column=1)

    root3 = Toplevel(root1)
    root3.geometry('240x220')
    # defining ui shit
    label1 = Label(root3, text='Username')
    entry_loginup = Entry(root3, width=35, borderwidth=5)
    label3 = Label(root3, text='____________________________________________')
    label2 = Label(root3, text='Password')
    entry_login2po = Entry(root3, width=35, borderwidth=5)
    buttonbruhv = Button(root3, text='Register', pady=7, padx=17, bg='gray', command=save_data)

    # grid sys shit
    entry_login2po.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    label2.grid(row=3, column=1)
    label3.grid(row=2, column=1)
    entry_loginup.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    label1.grid(row=0, column=1)
    buttonbruhv.grid(row=5, column=1)


label3n = Label(root1, text='____________________________________________')
label3np = Label(root1, text='')
label2p = Label(root1, text='Select an option')
buttonb2 = Button(root1, text='Register', pady=7, padx=86, bg='gray', command=registersys)
buttonb1 = Button(root1, text='Login', pady=7, padx=92, bg='gray', command=loginsys)
buttonb1.grid(row=4, column=0)
buttonb2.grid(row=6, column=0)
label2p.grid(row=2, column=0)
label3n.grid(row=3, column=0)
label3np.grid(row=5, column=0)


mainloop()
