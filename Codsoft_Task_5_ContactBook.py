from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as sql


def addContact():
    if len(Contact) == 0:
        count = 0
    else:
        Cursor.execute('SELECT sr FROM Contact ORDER BY sr DESC LIMIT 1')
        count = Cursor.fetchone()
        count = count[0]
    count = count + 1
    ContactString = contactField.get()
    NoString = NoField.get()
    mailString = mailField.get()
    AddressString = AddressField.get()
    if len(ContactString) == 0:
        messagebox.showerror('Error', 'Name Field is Empty!!!\n Enter the Contact Name.')
    elif len(NoString) == 0:
        messagebox.showerror('Error', 'Field is Empty!!!\n Enter the Contact Phone No.')
    elif len(mailString) == 0:
        messagebox.showerror('Error', 'Field is Empty!!!\n Enter the Contact Mail Id.')
    elif len(AddressString) == 0:
        messagebox.showerror('Error', 'Field is Empty!!!\n Enter the Contact Address.')
    else:
        Contact.append(ContactString)
        Cursor.execute('insert into Contact values (?,?,?,?,?)',
                       (count, ContactString, NoString, mailString, AddressString))
        updateList()
        clearField()


def findContact():
    ContactString = contactField.get()
    NoString = NoField.get()
    flag = 0
    if len(ContactString) == 0 and len(NoString) == 0:
        messagebox.showerror('Error', 'Field is Empty!!!\n Enter the Contact Name or Phone No.')
    else:
        Cursor.execute('SELECT * FROM Contact')
        rows = Cursor.fetchall()
        if len(ContactString) != 0:
            for contact in rows:
                if ContactString in contact:
                    messagebox.showinfo('Contact Information',
                                        f'Name         :   {contact[1]}\n'
                                        f'Phone No. :   {contact[2]}\n'
                                        f'Mail ID       :   {contact[3]}\n'
                                        f'Address     :   {contact[4]}')
                    flag = 1
                    break
                else:
                    continue
            if flag == 0:
                messagebox.showinfo('Error', 'contact is not there...')
        else:
            for contact in rows:
                if NoString in contact:
                    messagebox.showinfo('Contact Information',
                                        f'Name         :   {contact[1]}\n'
                                        f'Phone No. :   {contact[2]}\n'
                                        f'Mail ID       :   {contact[3]}\n'
                                        f'Address     :   {contact[4]}')
                    flag = 1
                    break
                else:
                    continue
            if flag == 0:
                messagebox.showinfo('Error', 'contact is not there...')
        clearField()


def view():
    window1 = Tk()
    table = ttk.Treeview(window1, columns=("sr", "name", "phone", "mail", "add"),
                         show="headings")

    table.heading('sr', text="Sr No")
    table.heading("name", text="Name")
    table.heading("phone", text="Phone No.")
    table.heading("mail", text="Email ID")
    table.heading("add", text="Address")
    table.pack()
    Cursor.execute('SELECT * FROM Contact')
    rows = Cursor.fetchall()
    for contact in rows:
        table.insert("", 'end', values=contact)


def updateList():
    clearList()
    Cursor.execute('SELECT * FROM Contact')
    rows = Cursor.fetchall()
    for contact in rows:
        table.insert("", 'end', values=contact)


def removeContact():
    selected = table.selection()
    if selected:
        item_id = table.item(selected[0])['values']
        table.delete(selected[0])
        Cursor.execute("DELETE FROM Contact WHERE sr=?", (item_id[0],))
        updateList()
    else:
        messagebox.showinfo('Error', 'No contact Selected. Cannot Delete.')


def deleteContact():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        while len(Contact) != 0:
            Contact.pop()
        Cursor.execute('delete from Contact')
        updateList()


def clearList():
    table.delete(*table.get_children())


def clearField():
    contactField.delete(0, 'end')
    NoField.delete(0, 'end')
    mailField.delete(0, 'end')
    AddressField.delete(0, 'end')


def exitApp():
    print(Contact)
    window.destroy()


def database():
    while len(Contact) != 0:
        Contact.pop()
    for row in Cursor.execute('select * from Contact'):
        Contact.append(row[0])


if __name__ == "__main__":
    window = Tk()
    window.title("Contact Book ")
    window.geometry("765x700+550+250")
    window.resizable(0, 0)
    window.configure(bg="#B5E5CF")

    the_connection = sql.connect('listOfContact.db')
    Cursor = the_connection.cursor()
    Cursor.execute('create table if not exists Contact (Sr INTEGER,name text,phone INTEGER(10),mail TEXT,address TEXT)')

    Contact = []

    frame = Frame(window, bg="#acc9ff")

    frame.pack(side="top", expand=True, fill="both")
    Title = Label(frame, text="Contact Book",
                  font=("arial", "20", "bold"),
                  background="#acc9ff",
                  foreground="BLUE"
                  )
    name = Label(frame, text="Enter the Name         :",
                 font=("arial", "14", "bold"),
                 background="#acc9ff",
                 foreground="#001743"
                 )
    phoneNo = Label(frame, text="Enter the Phone No. :",
                    font=("arial", "14", "bold"),
                    background="#acc9ff",
                    foreground="#001743"
                    )
    email = Label(frame, text="Enter the Email         :",
                  font=("arial", "14", "bold"),
                  background="#acc9ff",
                  foreground="#001743"
                  )
    address = Label(frame, text="Enter the Address    :",
                    font=("arial", "14", "bold"),
                    background="#acc9ff",
                    foreground="#001743"
                    )
    contactField = Entry(
        frame,
        font=("Arial", "14"),
        width=45,
        foreground="black",
        background="white",
    )
    NoField = Entry(
        frame,
        font=("Arial", "14"),
        width=45,
        foreground="black",
        background="white",
    )
    mailField = Entry(
        frame,
        font=("Arial", "14"),
        width=45,
        foreground="black",
        background="white",
    )
    AddressField = Entry(
        frame,
        font=("Arial", "14"),
        width=45,
        foreground="black",
        background="white",
    )

    addB = Button(
        frame,
        text="Add",
        width=10,
        bg='#0058fc', font=("arial", "12", "bold"),
        foreground="#ffffff",
        command=addContact,

    )
    viewB = Button(
        frame,
        text="View",
        width=10,
        bg='#0058fc',
        font=("arial", "12", "bold"),
        foreground="#ffffff",
        command=view
    )
    findB = Button(frame, text="Find",
                   width=10,
                   bg='#0058fc', font=("arial", "12", "bold"),
                   foreground="#ffffff",
                   command=findContact,
                   )

    removeB = Button(
        frame,
        text="Remove",
        width=10,
        bg='#0058fc', font=("arial", "12", "bold"),
        foreground="#ffffff",
        command=removeContact,
    )
    del_allB = Button(
        frame,
        text="Delete All",
        width=10,
        font=("arial", "12", "bold"),
        bg='#0058fc',
        foreground="#ffffff",
        command=deleteContact
    )

    exitB = Button(
        frame,
        text=" Exit ",
        width=11,
        bg='#321096', font=("arial", "12", "bold"),
        foreground="WHITE",
        command=exitApp
    )

    table = ttk.Treeview(frame, columns=("sr", "name", "phone", "mail", "add"),
                         show="headings", height=15)
    # table["columns"] = ("sr", "name", "phone", "mail", "add")

    table.heading('sr', text="Sr No")
    table.heading("name", text="Name")
    table.heading("phone", text="Phone No.")
    table.heading("mail", text="Email ID")
    table.heading("add", text="Address")
    table.column('sr', width=50)
    table.column("name", width=120)
    table.column("phone", width=100)
    table.column("mail", width=200)
    table.column("add", width=250)

    Title.place(x=280, y=10)

    name.place(x=20, y=70)
    phoneNo.place(x=20, y=110)
    email.place(x=20, y=150)
    address.place(x=20, y=190)

    contactField.place(x=230, y=70)
    NoField.place(x=230, y=110)
    mailField.place(x=230, y=150)
    AddressField.place(x=230, y=190)

    addB.place(x=20, y=240, )
    viewB.place(x=170, y=240)
    findB.place(x=320, y=240)
    removeB.place(x=480, y=240)
    del_allB.place(x=630, y=240)
    table.place(x=17, y=300)
    exitB.place(x=320, y=645)

    database()
    updateList()
    window.mainloop()
    the_connection.commit()
    Cursor.close()
