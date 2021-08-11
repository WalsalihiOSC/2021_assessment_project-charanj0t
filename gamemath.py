class Window1:
   #declaring variables
   name = ""
   age = 0
   year_level = 0
   window = ''
   mainFrame = ''
   TYPE_ = 0
   list_entry_add, list_entry_sub, list_entry_div, list_entry_mul = [],[],[],[]
   addAns, subAns, divAns, mulAns  = [],[],[],[]
   score = 0
   
   #default constructor, calls when an object is created
   def __init__(self, root, Name):
      self.window = root
      root.title(Name)
      #initializing variables with string type 
      self.name = tk.StringVar()
      self.age = tk.StringVar()
      self.year_level = tk.StringVar()
      self.TYPE_ = tk.StringVar()
      self.score = tk.StringVar()

      #create a mainframe widget
      self.mainFrame = Frame(self.window,bg="#4A86E8")
      self.mainFrame.pack(fill="both")

      #creating all frame widgets that are needed
      self.frame0 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame1 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame2 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame3 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame4 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame5 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame6 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame7 = Frame(self.mainFrame,bg="#4A86E8")
      self.frame8 = Frame(self.mainFrame,bg="#4A86E8")

      #showing the frame0, when we pack any frame, it shows on screen
      self.frame0.pack(fill="x")
      
      #logo on the top left side of window
      img = Image.open("logo.jpg")  #abc.png is the name of logo, you can change it
      img = img.resize((100,40))
      logoImage = ImageTk.PhotoImage(img)
      labelLogo = Label(self.frame0,image=logoImage,bg="#4A86E8")
      labelLogo.image = logoImage
      labelLogo.pack(side=LEFT,padx=5,pady=5)

      #######################frame 1##################
      #label Student information
      lbl_stdInfo = Label(self.frame1,text='Student Information',bg="#4A86E8",fg="white",font = "Arial 14 bold")
      lbl_stdInfo.grid(row=0,column=0,columnspan=2,pady=40)

      #label Name
      labelName = Label(self.frame1,text="Name",bg="#4A86E8",fg="white",font = "Arial 12 bold")
      labelName.grid(row=1,column=0,sticky="w",padx=5)

      #input feild for Name
      entry_name = Entry(self.frame1,textvariable= self.name,width="15",bg="lightgrey", font = "Arial 12 bold")
      entry_name.grid(row=1,column=1,pady=5)

      #label Age
      labelAge = Label(self.frame1,text="Age",bg="#4A86E8",font = "Arial 12 bold", fg="white",justify="left")
      labelAge.grid(row=2,column=0, sticky="w",padx=5)
      #inout feild for Age
      entry_Age = Entry(self.frame1,textvariable=self.age, width="15",bg="lightgrey", font = "Arial 12 bold")
      entry_Age.grid(row=2,column=1,pady=5)

      #label Year Level
      labelYear_level = Label(self.frame1,text="Year Level",bg="#4A86E8",fg="white",font = "Arial 12 bold")
      labelYear_level.grid(row=3,column=0, sticky="w",padx=5)
      #input feild  Year Level
      entry_Year_level = Entry(self.frame1,textvariable= self.year_level,width="15",bg="lightgrey", font = "Arial 12 bold")
      entry_Year_level.grid(row=3,column=1,pady=5)

      #button Continue
      btn_coninue = Button(self.frame1, text="Continue", bg="#6AA84F", command=self.continueCall,font = "Arial 10 bold")
      btn_coninue.grid(row=4,column=6,padx=(220,5),pady=(170,15))

      #pack frame1
      self.frame1.pack(fill="x",padx=(250,0))
      #end frame1

      #######################frame 2##################
      #label How to Play
      lbl_stdInfo = Label(self.frame2,text='How to Play',bg="#4A86E8",fg="white",font = "Arial 14 bold")
      lbl_stdInfo.grid(row=0,column=0,columnspan=5,pady=40)

      #point 1
      labelName = Label(self.frame2,text="-  You will get a question like '7+7= ----' you have to \nclick in the box and write down your answer.",bg="#4A86E8",fg="white",font = "Arial 16 bold")
      labelName.grid(row=1,column=2,sticky="w",padx=(30,5),pady=(20,0),columnspan=2)
      #point 2
      labelName = Label(self.frame2,text="-  You have to fill in the all boxes ---- to answer.",bg="#4A86E8",fg="white",font = "Arial 16 bold")
      labelName.grid(row=2,column=2,sticky="w",padx=30,columnspan=2)
      #point 3
      labelName = Label(self.frame2,text="-  When done click next and it will take you to the \n results page where it will say your results.",bg="#4A86E8",fg="white",font = "Arial 16 bold")
      labelName.grid(row=3,column=2,sticky="w",padx=30,columnspan=2)

      #button to go on previous page
      btn_back = Button(self.frame2, text="Back", bg="#FF9912", command=self.goBackToInfo,font = "Arial 10 bold")
      btn_back.grid(row=4,column=0,sticky=W,padx=20,pady=5)

      #button to go on next window
      btn_coninue = Button(self.frame2, text="Next", bg="#6AA84F", command=self.callChooseWindow,font = "Arial 10 bold")
      btn_coninue.grid(row=4,column=4,padx=70,pady=110)
      #end frame2
