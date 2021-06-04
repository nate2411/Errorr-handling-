from tkinter import *
from tkinter import messagebox

window_log = Tk()
window_log.title("")
window_log.geometry("400x220")
window_log["background"] = ["blue"]
window_log.resizable(False, False)

verified = {"Nathan": "123", "Ashton": "142", "Anele": "676"}

#Funtionality  of the interface.
def verification():
    username = user_entry.get()
    password = password_entry.get()

    try:
        if username in verified:
            pw = verified.get(username)
            if pw == password:
                window_log.destroy()
                import second
            else:
                wrong = messagebox.showinfo('', "Username incorrect")
        else:
            wrong = messagebox.showinfo('', "Password incorrect")
    except:
        messagebox.showinfo("","Login details are incorrect")

def clear():
    user_entry.delete(0, END)
    password_entry.delete(0, END)

def exit():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                        icon='warning')
    if msg_box == 'yes':
        window_log.destroy()



#The entries, labels and the buttons used in the interface.
#Heading of the interface.
head_label = Label(window_log, text="Please enter your Username and Password", bg="blue", font="15")
head_label.place(x=30, y=30)

#The Username details.
user_label = Label(window_log, text="Username: ", font="15", bg="blue")
user_label.place(x=50, y=80)
user_entry = Entry(window_log, width=20, highlightthickness=0)
user_entry.place(x=150, y=80)

#The Password details.
password_label = Label(window_log, text="Password: ", font="15", bg="blue")
password_label.place(x=50, y=120)
password_entry = Entry(window_log, width=20, highlightthickness=0)
password_entry.place(x=150, y=120)

#Clear, Exit and Verify buttons
verify_button = Button(window_log, text="Verify", width=10, bg="grey", highlightthickness=0, command=verification)
verify_button.place(x=40, y=160)
clear_button = Button(window_log, text="Clear", width=10, bg="grey", highlightthickness=0, command=clear)
clear_button.place(x=150, y=160)
exit_button = Button(window_log, text="Exit", width=10, bg="grey", highlightthickness=0, command=exit)
exit_button.place(x=260, y=160)


window_log.mainloop()
