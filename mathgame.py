##CHARANJOT SINGH##

class Windowone :
    def __init__(self):
        self.welcome_frame = Frame(root,width="800",height="600")
        self.welcome_frame.grid()
        

        Label(self.welcome_frame,text="Student Information ").grid(column=3,row=1)
        Label(self.welcome_frame, text="Logo Here").grid(column=1, row=1)
        Button(self.welcome_frame, text="Continue", command=self.csc).grid(column=5, row=7)
        
        Label(self.welcome_frame, text="Name: ").grid(column=2, row=3)
        Label(self.welcome_frame, text="Age:").grid(column=2, row=4)
        Label(self.welcome_frame, text="Year Level: ").grid(column=2, row=6)

        self.name=Entry(self.welcome_frame)
        self.name.grid(column=4, row=3)
        self.age=Entry(self.welcome_frame)
        self.age.grid(column=4, row=4)
        self.year_level=Entry(self.welcome_frame)
        self.year_level.grid(column=4, row=5)

    
    def help(self,cframe):
        cframe.grid_forget()
        self.help_frame = Frame(root,width="800",height="600")
        self.help_frame.grid()
        Label(self.help_frame, text="You will get a question like “7+7= ” you have to click in the box and write down you answer. ").grid(column=3, row=3)
        Label(self.help_frame, text="You have to fill in the all the boxes to answer.").grid(column=3, row=4)
        Label(self.help_frame, text="When done click next and it will take you to the results page where it will say your results.").grid(column=3, row=5)

        Label(self.help_frame,text="Student Information ").grid(column=3,row=1)
        Label(self.help_frame, text="Logo Here").grid(column=1, row=2)
        Label(self.help_frame, text="Continue").grid(column=5, row=7)
        
        Button(self.help_frame, text="Back", command= lambda: self.backb (cframe,self.help_frame)).grid(column=1, row=7)
  
def csc(self):
    self.welcome_frame.grid_forget()
    self.csc_frame=Frame(root, width="300", height="400")
    self.csc_frame.grid()
        
    

       
