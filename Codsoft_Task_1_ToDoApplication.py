from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


def addTask():
    taskString = taskField.get()
    if len(taskString) == 0:
        messagebox.showerror('Error', 'Field is Empty!!!\n Enter the task.')
    else:
        tasks.append(taskString)
        Cursor.execute('insert into tasks values (?)', (taskString,))
        updateList()
        clearField()


def findTask():
    taskString = taskField.get()
    if len(taskString) == 0:
        messagebox.showerror('Error', 'Field is Empty!!!\n Enter the task.')
    else:
        if taskString in tasks:
            messagebox.showinfo('', 'Task is there in ToDo List')
        else:
            messagebox.showinfo('Error', 'Task is not there in ToDo List')
        clearField()


def updateList():
    clearList()
    for task in tasks:
        listbox.insert('end', task)


def removeTask():
    try:
        the_value = listbox.get(listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            updateList()
            Cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')


def deleteTasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        while len(tasks) != 0:
            tasks.pop()
        Cursor.execute('delete from tasks')
        updateList()


def clearList():
    listbox.delete(0, 'end')


def clearField():
    taskField.delete(0, 'end')


def exitApp():
    print(tasks) # This is optional
    window.destroy()


def database():
    while len(tasks) != 0:
        tasks.pop()
    for row in Cursor.execute('select title from tasks'):
        tasks.append(row[0])


if __name__ == "__main__":
    window = Tk()
    window.title("To-Do Application ")
    window.geometry("665x500+550+250")
    window.resizable(0, 0)
    window.configure(bg="#B5E5CF")

    connection = sql.connect('listOfTasks.db')
    Cursor = connection.cursor()
    Cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    frame = Frame(window, bg="#acc9ff")

    frame.pack(side="top", expand=True, fill="both")
    Title = Label(frame, text="TO-DO APPLICATION",
                  font=("arial", "20", "bold"),
                  background="#acc9ff",
                  foreground="BLUE"
                  )
    taskLabel = Label(frame, text="Enter the Task:",
                      font=("arial", "14", "bold"),
                      background="#acc9ff",
                      foreground="#001743"
                      )

    taskField = Entry(
        frame,
        font=("Arial", "14"),
        width=42,
        foreground="black",
        background="white",
    )

    addB = Button(
        frame,
        text="Add",
        width=12,
        bg='#0058fc', font=("arial", "12", "bold"),
        foreground="#ffffff",
        command=addTask,

    )
    findB = Button(frame, text="Find",
                   width=12,
                   bg='#0058fc', font=("arial", "12", "bold"),
                   foreground="#ffffff",
                   command=findTask,
                   )

    removeB = Button(
        frame,
        text="Remove",
        width=12,
        bg='#0058fc', font=("arial", "12", "bold"),
        foreground="#ffffff",
        command=removeTask,
    )
    del_allB = Button(
        frame,
        text="Delete All",
        width=12,
        font=("arial", "12", "bold"),
        bg='#0058fc',
        foreground="#ffffff",
        command=deleteTasks
    )

    exitB = Button(
        frame,
        text=" Exit ",
        width=11,
        bg='#321096', font=("arial", "12", "bold"),
        foreground="WHITE",
        command=exitApp
    )

    listbox = Listbox(
        frame,
        width=57,
        height=10,
        font="bold",
        selectmode='SINGLE',
        background="WHITE",
        foreground="BLACK",
        selectbackground="#B5E5CF",
        selectforeground="#4e4e4e",
    )
    Title.place(x=210, y=10)
    taskLabel.place(x=20, y=70)
    taskField.place(x=180, y=70)
    addB.place(x=20, y=120, )
    findB.place(x=190, y=120)
    removeB.place(x=350, y=120)
    del_allB.place(x=515, y=120)
    listbox.place(x=17, y=180)
    exitB.place(x=280, y=450)

    database()
    updateList()
    window.mainloop()
    connection.commit()
    Cursor.close()
