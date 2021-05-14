from tkinter import*
import random
import time
from tkinter import messagebox
window = Tk()
window.geometry("820x1000")
window.title("Guess The Number")


logo1 = PhotoImage(file="UpArrow.png")
logo1= logo1.subsample(7)

logo2 = PhotoImage(file="DownArrow.png")
logo2 = logo2.subsample(7)

logo3 = PhotoImage(file="Bravo.png")
logo3 = logo3.subsample(7)

turns=0
def randomnumber():
    global yy,turns
    label3.configure(image = "")
    turns = 0
    entry.delete(0, "end")
    yy = random.randint(1,100)
    for i in range(8):
        label4.configure(text=random.randint(1, 100))
        label4.update()
        time.sleep(0.2)
    label4.configure(text="Ready!")

def end():
    if turns>=10:
        messagebox.showinfo("Your Score\n", "Your score was:"+str(turns)+" turns   "+", better luck next time!    ")
    elif turns<10 and turns>=7:
        messagebox.showinfo("Your Score\n", "Your score was: "+str(turns)+ " turns "+ ", good, you are an amateur!       ")
    elif turns<7 and turns>3:
        messagebox.showinfo("Your Score\n", "Your score was: " + str(turns) + " turns " + ", pretty good, you are an intermediate!     ")
    elif turns < 3 and turns > 1:
        messagebox.showinfo("Your Score\n", "Your score was: " + str(turns) + " turns " + ", amazing, you are an expert!     ")
    else:
        messagebox.showinfo("Your Score\n","Your score was: " + str(turns) + " turn " + ", you are the boss!")

def start(event):
    global turns
    turns=turns+1
    if int(entry.get())<yy:
        label3.configure(image = logo1)
    elif int(entry.get())>yy:
        label3.configure(image = logo2)
    else:
        label3.configure(image = logo3)
        end()
    entry.delete(0, "end")

label1= Label(window,text = "Guess The Number",font = ('Times', 40, 'bold'))
label1.grid(column = 0,row = 0,columnspan = 2, pady = 3, padx = 40)
label2=Label(window,text="We have picked a secret number.\nYour purpose is to guess what number it is!\nIf your guess is too high or too low,\nyou will be given a hint.\nPress Enter to start!",
             font=('Times', 30, 'bold'))
label2.grid(column = 0,row = 2,columnspan = 2, pady = 30, padx = 40)
entry=Entry(window,font=('Times', 40, 'bold'),width=10)
entry.grid(column = 0,row = 3, pady = 45, columnspan=2,padx=0)
label3 = Label(window, text="", bg='black')
label3.grid(column = 1,row = 3, pady = 45)
label4 = Label(window, text = "")
label4.grid(column = 0,row = 3, padx = 1)

btnre = Button(window, text="Reset",width=9,bg="Light blue",font=('Times', 20, 'bold'),command=randomnumber)
btnre.grid(column = 0, row = 4,columnspan = 2)
btne = Button(window, text = "Exit",width = 9,bg = "Green",font=('Times', 20, 'bold'),command = window.destroy)
btne.grid(column = 0, row = 5,columnspan=2,pady=4)

for i in range(8):
    label4.configure(text = random.randint(1,100))
    label4.update()
    time.sleep(0.2)
label4.configure(text = "Ready!")

window.bind("<Return>",start)

randomnumber()
window.mainloop()