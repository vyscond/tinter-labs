try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here


class App:

    def __init__(self, master):

        

        master.config(background="black")

        frame = Frame(master, bg="black")

        frame.pack()

        self.frame_s = Frame(frame, bg="yellow", width=500, height=500)
       

        #--- additional frames

        self.frame1 = Frame(self.frame_s, bg="white", width=500, height=500)


        self.frame_list = {'frame1' : self.frame1}



        self.flat = Button(frame, text="Hello", command= lambda  : self.swicth_tab('frame1'), relief=FLAT, background="#D27278")
        self.flat.grid(row=0, column=0, padx=5, pady=5)

        self.raised = Button(frame, text="Hello", command=self.say_hi, relief=RAISED, background="#D27278")
        self.raised.grid(row=0, column=1, padx=5, pady=5)

        self.sunken = Button(frame, text="Hello", command=self.say_hi, relief=SUNKEN, background="#D27278")
        self.sunken.grid(row=0, column=2, padx=5, pady=5)

        self.groove = Button(frame, text="Hello", command=self.say_hi, relief=GROOVE, background="#D27278")
        self.groove.grid(row=0, column=3, padx=5, pady=5)

        self.ridge = Button(frame, text="Hello", command=self.say_hi, relief=RIDGE, background="#D27278")
        self.ridge.grid(row=0, column=4, padx=5, pady=5)

        self.frame_s.grid(row=1,column=0, columnspan=5)

        self.quitter = Button(frame, text="QUIT", fg="red", command=exit)
        self.quitter.grid(row=2, column=0, padx=5, pady=5,columnspan=5 , stick=W+E+N+S)
        

    def say_hi(self):
        
        print ("hi there, everyone!")

    def swicth_tab(self, msg):

        print ( self.frame_list.get(msg) )

        print (self.frame_s)
        
        self.frame_s = self.frame_list.get(msg)
        self.frame_s.grid(row=1,column=0, columnspan=5)
        #self.frame_list.get(msg).grid(row=1,column=0, columnspan=5)

root = Tk()

app = App(root)

root.geometry("%dx%d%+d%+d" % (600, 600, 0, 0))

root.mainloop()
