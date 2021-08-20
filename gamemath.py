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

      #######################frame 3##################      
      lbl_stdInfo = Label(self.frame3,text='Choose Math Game',bg="#4A86E8",fg="white",font = "Arial 13 bold")
      lbl_stdInfo.grid(row=0,column=1,padx=220,pady=40)

      self.btn_addition = Button(self.frame3,anchor="w",text="Addition +",width=12, bg="lightgrey", command=self.additionPress,font = "Arial 10 bold")      
      self.btn_addition.grid(row=1,column=1,padx=250,pady=5,sticky=W)

      self.btn_subtraction = Button(self.frame3,anchor="w",text="Subtraction -",width=12, bg="lightgrey", command=self.subtractionPress,font = "Arial 10 bold")  
      self.btn_subtraction.grid(row=2,column=1,padx=250,pady=5,sticky=W)
      
      self.btn_division = Button(self.frame3,anchor="w", text="Division "+chr(247),width=12, bg="lightgrey", command=self.divisionPress,font = "Arial 10 bold")      
      self.btn_division.grid(row=3,column=1,padx=250,pady=5,sticky=W)

      self.btn_multiplication = Button(self.frame3,anchor="w", text="Multiplication X",width=12, bg="lightgrey", command=self.multiplicationPress,font = "Arial 10 bold")      
      self.btn_multiplication.grid(row=4,column=1,padx=250,pady=5,sticky=W)
      
      btn_back = Button(self.frame3, text="Back", bg="#FF9912", command=self.goBackToHowTo,font = "Arial 10 bold")
      btn_back.grid(row=5,column=0,sticky=W,padx=20,pady=5)
                        
      btn_coninue = Button(self.frame3, text="Start", bg="#6AA84F", command=self.callGameplay,font = "Arial 10 bold")
      btn_coninue.grid(row=5,column=2,padx=30,pady=120)
      #end frame3

      #######################frame 4 Addition##################
      #declare and initialize variables with empty strings
      addition = ""
      subtraction = ""
      multiplication = ""
      division = ""
      
      #Label Addition +
      lbl_heading_quiz = Label(self.frame4,text='Addition +',bg="#4A86E8",fg="white")
      lbl_heading_quiz.config(font=("Arail", 16))
      lbl_heading_quiz.grid(row=0,columnspan=4,pady=(5,15))

      #Loop (create label from Random, and align using grid to the left to right) as mention in documentation
      for row in range(1,9):     #outer for loop
          col = []
          for column in range(0,3):    #inner for loop
              question = str(row+5)+"+"+str(column+2)+"="   #question that shown e.g 2+3
              add = (row+5)+(column+2)
              self.addAns.append(add)                       #appned in a list to store the answers of current questions
              #label
              labelQuestion = Label(self.frame4,text=question,bg="#4A86E8",fg="white")
              labelQuestion.config(font=("Arail", 16))
              labelQuestion.grid(row=row,column=column,padx=5,pady=5,sticky="nsew")
              #input feild for user answer
              entry_ans = Entry(self.frame4,width="5",bg="lightgrey", font = "Arial 12 bold",justify="center")
              entry_ans.grid(row=row,column=column,sticky=E,padx=30)
              self.frame4.grid_columnconfigure(column,weight=1)
              col.append(entry_ans)   #append in a 1D list and then append in a 2D list to make a 2D list of answers
          self.list_entry_add.append(col)


      
      btn_back = Button(self.frame4, text="Back", bg="#FF9912", command=self.goToChooseMenu1,font = "Arial 10 bold")
      btn_back.grid(row=9,column=0,sticky=W,padx=20,pady=5)

      btn_next = Button(self.frame4, text="Next", bg="#6AA84F", command=self.nextAddGo,font = "Arial 10 bold")
      btn_next.grid(row=9,column=3,sticky=E,padx=20,pady=5)
      #end frame4

      #######################frame 5 Subtraction##################
      #same as above , except change sign to -
      addition = ""
      subtraction = ""
      multiplication = ""
      division = ""
      
      
      lbl_heading_quiz = Label(self.frame5,text='Subtraction -',bg="#4A86E8",fg="white")
      lbl_heading_quiz.config(font=("Arail", 16))
      lbl_heading_quiz.grid(row=0,columnspan=4,pady=(5,15))


      for row in range(1,9):
          col = []
          for column in range(0,3):
              question = str(row+5)+"-"+str(column+2)+"="
              sub = (row+5)-(column+2)
              self.subAns.append(sub)
              labelQuestion = Label(self.frame5,text=question,bg="#4A86E8",fg="white")
              labelQuestion.config(font=("Arail", 16))
              labelQuestion.grid(row=row,column=column,padx=5,pady=5,sticky="nsew")
              entry_ans = Entry(self.frame5,width="5",bg="lightgrey", font = "Arial 12 bold",justify="center")
              entry_ans.grid(row=row,column=column,sticky=E,padx=30)
              self.frame5.grid_columnconfigure(column,weight=1)
              col.append(entry_ans)
          self.list_entry_sub.append(col)

