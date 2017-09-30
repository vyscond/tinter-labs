from Tkinter import *

import tk_tab_panel

class main_window(object):

    def __init__(self):
    
        self.root_window = Tk()
        
        self.tabbed_panel = tk_tab_panel.TabPanel(self.root_window)
        
        #--- tab1
        
        self.tab1 = Frame(self.tabbed_panel.get_frame(), background='yellow')
        
        Label(self.tab1,text='hello').grid(row=0,column=0)
        
        self.tabbed_panel.add_pane('tab1', self.tab1)

        #--- tab2
        
        self.tab2 = Frame(self.tabbed_panel.get_frame(), background='blue')
        
        Label(self.tab2,text='hellow').grid(row=0,column=0)
        
        self.tabbed_panel.add_pane('tab2', self.tab2)        
        
        self.tabbed_panel.build(self.root_window).grid(row=0,column=0)
        
        self.button_quit = Button(self.root_window, text="f10 surrender", relief=FLAT, command=exit)
        
        #--- pack
        
        self.button_quit.grid(row=1,column=0)
        
        
    def run(self):
    
        self.root_window.mainloop()
        
if __name__ == '__main__':

    mw = main_window()
    
    mw.run()
