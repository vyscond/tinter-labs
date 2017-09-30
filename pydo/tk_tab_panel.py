
#TODO --- resolver a referencia de endereco ali no fim no metodo de filling/creation dos buttons

from Tkinter import *

class TabPanel(object):

    def __init__(self, master):
    
        self.frame = Frame(master)
        
        self.select_tab_frame = Frame(self.frame, background='black' , width=200 , height=200)
        
        self.available_frames = []
        
        self.tab_labels = []
        
        self.tab_buttons = []
        
        self.callbacks = []
        
    def get_frame(self):
    
        return self.frame
        
    def add_pane(self, tab_name, frame):
    
        self.available_frames.append( frame )
        
        self.tab_labels.append( tab_name )
    
    def show_frame(self, index):
        
        print '<show me frame><'+str(index)+'>'
    
        print '<frame received>' + str (self.available_frames[index])

        self.select_tab_frame.grid_forget()
        
        self.select_tab_frame = self.available_frames[index]
        
        print '<select_tab>'+str(self.select_tab_frame)

        #.grid(row=1,column=0,sticky=E+W+N+S, columnspan=len(self.tab_labels))
        self.select_tab_frame.grid(row=1,column=0, columnspan=len(self.tab_labels))
        self.select_tab_frame.grid_propagate( False )
    
    def build(self, master):
        
        self.select_tab_frame.grid(row=1,column=0, columnspan=len(self.tab_labels))

        self.select_tab_frame.grid_propagate(False)
            
        for label in self.tab_labels :
            
            index = self.tab_labels.index(label)

            self.tab_buttons.append( Button(self.frame) )
            
            self.tab_buttons[index].configure( command = lambda i = index : self.show_frame(i) , text=label )

            self.tab_buttons[index].grid(row=0,column=index)
            
        print index
        
        return self.frame
