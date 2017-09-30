from tkinter import *

class App:

    def __init__(self, master):

        master.config(background="black")

        frame = Frame(master, bg="black")
        frame.pack()

       

        self.flat = Button(frame, text="Hello", command=self.say_hi, relief=FLAT, background="#D27278")
        self.flat.grid(row=0, column=0, padx=5, pady=5)

        self.raised = Button(frame, text="Hello", command=self.say_hi, relief=RAISED, background="#D27278")
        self.raised.grid(row=1, column=1, padx=5, pady=5)

        self.sunken = Button(frame, text="Hello", command=self.say_hi, relief=SUNKEN, background="#D27278")
        self.sunken.grid(row=2, column=2, padx=5, pady=5)

        self.groove = Button(frame, text="Hello", command=self.say_hi, relief=GROOVE, background="#D27278")
        self.groove.grid(row=3, column=3, padx=5, pady=5)

        self.ridge = Button(frame, text="Hello", command=self.say_hi, relief=RIDGE, background="#D27278")
        self.ridge.grid(row=4, column=4, padx=5, pady=5)

        self.quitter = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quitter.grid(row=4, column=5, padx=5, pady=5)
        

    def say_hi(self):
        print ("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()