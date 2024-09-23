import tkinter

screen=tkinter.Tk()
screen.title("MyApp")
screen.geometry("400x500")
screen.config(background="lightblue")

lbl=tkinter.Label(text="Firstname:",bg="lightblue",font="Elephant 16 bold").grid(row=0,column=0)

lbl=tkinter.Label(text="lastname:",bg="lightblue",font="Elephant 16 bold").grid(row=1,column=0)
lbl=tkinter.Radiobutton(text="Male",bg="lightblue",font="Elephant 16 bold").grid(row=2,column=0)
lbl=tkinter.Radiobutton(text="feMale",bg="lightblue",font="Elephant 16 bold").grid(row=3,column=0)

screen.mainloop()