
from tkinter import *
from tkinter import messagebox

window_log = Tk()
window_log.title("")
window_log.geometry("400x175")
window_log["background"] = ["blue"]
window_log.resizable(False, False)

#Funtionality  of the interface.
def check():
    try:
        if int(password_entry.get()) > 3000:
            messagebox.showinfo("", "You going to Malaysia")
        else:
            messagebox.showinfo("", "You can't go to Malaysia")
    except:
        messagebox.showinfo("", "That's not right")
def clear():
    password_entry.delete(0, END)

def close():
    msg_box = messagebox.askquestion('Close Application', 'Are you sure you want to close the application', icon='warning')
    if msg_box == 'yes':
        window_log.destroy()



#The entries, labels and the buttons used in the interface.
#Heading of the interface.
head_label = Label(window_log, text="Please enter your balance", bg="blue", font="15")
head_label.place(x=100, y=30)

#The Password details.
password_label = Label(window_log, text="Balance: ", font="15", bg="blue")
password_label.place(x=70, y=70)
password_entry = Entry(window_log, width=20, highlightthickness=0)
password_entry.place(x=150, y=70)

#Clear, Exit and Verify buttons
verify_button = Button(window_log, text="Check", width=10, bg="grey", highlightthickness=0, command=check)
verify_button.place(x=40, y=120)
clear_button = Button(window_log, text="Clear", width=10, bg="grey", highlightthickness=0, command=clear)
clear_button.place(x=150, y=120)
exit_button = Button(window_log, text="Exit", width=10, bg="grey", highlightthickness=0, command=close)
exit_button.place(x=260, y=120)
