#import python modules
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import math


#class
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
      btn_coninue = Button(self.frame1, text="Continue", highlightbackground="#6AA84F", command=self.continueCall,font = "Arial 10 bold")

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
      btn_back = Button(self.frame2, text="Back", highlightbackground="#FF9912", command=self.goBackToInfo,font = "Arial 10 bold")
      btn_back.grid(row=4,column=0,sticky=W,padx=20,pady=5)

      #button to go on next window
      btn_coninue = Button(self.frame2, text="Next", highlightbackground="#6AA84F", command=self.callChooseWindow,font = "Arial 10 bold")
      btn_coninue.grid(row=4,column=4,padx=70,pady=110)
      #end frame2


      #######################frame 3##################      
      lbl_stdInfo = Label(self.frame3,text='Choose Math Game',bg="#4A86E8",fg="white",font = "Arial 13 bold")
      lbl_stdInfo.grid(row=0,column=1,padx=220,pady=40)

      self.btn_addition = Button(self.frame3,anchor="w",text="Addition +",width=12, highlightbackground="lightgrey", command=self.additionPress,font = "Arial 10 bold")      
      self.btn_addition.grid(row=1,column=1,padx=250,pady=5,sticky=W)

      self.btn_subtraction = Button(self.frame3,anchor="w",text="Subtraction -",width=12, highlightbackground="lightgrey", command=self.subtractionPress,font = "Arial 10 bold")  
      self.btn_subtraction.grid(row=2,column=1,padx=250,pady=5,sticky=W)
      
      self.btn_division = Button(self.frame3,anchor="w", text="Division "+chr(247),width=12, highlightbackground="lightgrey", command=self.divisionPress,font = "Arial 10 bold")      
      self.btn_division.grid(row=3,column=1,padx=250,pady=5,sticky=W)

      self.btn_multiplication = Button(self.frame3,anchor="w", text="Multiplication X",width=12, highlightbackground="lightgrey", command=self.multiplicationPress,font = "Arial 10 bold")      
      self.btn_multiplication.grid(row=4,column=1,padx=250,pady=5,sticky=W)
      
      btn_back = Button(self.frame3, text="Back", highlightbackground="#FF9912", command=self.goBackToHowTo,font = "Arial 10 bold")
      btn_back.grid(row=5,column=0,sticky=W,padx=20,pady=5)
                        
      btn_coninue = Button(self.frame3, text="Start", highlightbackground="#6AA84F", command=self.callGameplay,font = "Arial 10 bold")
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


      
      btn_back = Button(self.frame4, text="Back", highlightbackground="#FF9912", command=self.goToChooseMenu1,font = "Arial 10 bold")
      btn_back.grid(row=9,column=0,sticky=W,padx=20,pady=5)

      btn_next = Button(self.frame4, text="Next", highlightbackground="#6AA84F", command=self.nextAddGo,font = "Arial 10 bold")
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


      
      btn_back = Button(self.frame5, text="Back", highlightbackground="#FF9912", command=self.goToChooseMenu2,font = "Arial 10 bold")
      btn_back.grid(row=9,column=0,sticky=W,padx=20,pady=5)

      btn_next = Button(self.frame5, text="Next", highlightbackground="#6AA84F", command=self.nextSubGo,font = "Arial 10 bold")
      btn_next.grid(row=9,column=3,sticky=E,padx=20,pady=5)
      #end frame5

      #######################frame 6 Division##################
      addition = ""
      subtraction = ""
      multiplication = ""
      division = ""
      
      
      lbl_heading_quiz = Label(self.frame6,text='Division '+chr(247),bg="#4A86E8",fg="white")
      lbl_heading_quiz.config(font=("Arail", 16))
      lbl_heading_quiz.grid(row=0,columnspan=4,pady=(5,15))
      for row in range(1,9):
          col = []
          for column in range(0,3):
              question = str(row+5)+chr(247)+str(column+2)+"="
              div = (row+5)/(column+2)
              self.divAns.append(div)
              labelQuestion = Label(self.frame6,text=question,bg="#4A86E8",fg="white")
              labelQuestion.config(font=("Arail", 16))
              labelQuestion.grid(row=row,column=column,padx=5,pady=5,sticky="nsew")
              entry_ans = Entry(self.frame6,width="5",bg="lightgrey", font = "Arial 12 bold",justify="center")
              entry_ans.grid(row=row,column=column,sticky=E,padx=30)
              self.frame6.grid_columnconfigure(column,weight=1)
              col.append(entry_ans)
          self.list_entry_div.append(col)


      
      btn_back = Button(self.frame6, text="Back", highlightbackground="#FF9912", command=self.goToChooseMenu3,font = "Arial 10 bold")
      btn_back.grid(row=9,column=0,sticky=W,padx=20,pady=5)

      btn_next = Button(self.frame6, text="Next", highlightbackground="#6AA84F", command=self.nextDivGo,font = "Arial 10 bold")
      btn_next.grid(row=9,column=3,sticky=E,padx=20,pady=5)
      #end frame6

      #######################frame 7 Multiplication##################
      addition = ""
      subtraction = ""
      multiplication = ""
      division = ""
      
      
      lbl_heading_quiz = Label(self.frame7,text='Multiplication *',bg="#4A86E8",fg="white")
      lbl_heading_quiz.config(font=("Arail", 16))
      lbl_heading_quiz.grid(row=0,columnspan=4,pady=(5,15))


      for row in range(1,9):
          col = []
          for column in range(0,3):
              question = str(row+5)+"X"+str(column+2)+"="
              mul = (row+5)*(column+2)
              self.mulAns.append(mul)
              labelQuestion = Label(self.frame7,text=question,bg="#4A86E8",fg="white")
              labelQuestion.config(font=("Arail", 16))
              labelQuestion.grid(row=row,column=column,padx=5,pady=5,sticky="nsew")
              entry_ans = Entry(self.frame7,width="5",bg="lightgrey", font = "Arial 12 bold",justify="center")
              entry_ans.grid(row=row,column=column,sticky=E,padx=30)
              self.frame7.grid_columnconfigure(column,weight=1)
              col.append(entry_ans)
          self.list_entry_mul.append(col)


      
      btn_back = Button(self.frame7, text="Back", highlightbackground="#FF9912", command=self.goToChooseMenu4,font = "Arial 10 bold")
      btn_back.grid(row=9,column=0,sticky=W,padx=20,pady=5)

      btn_next = Button(self.frame7, text="Next", highlightbackground="#6AA84F", command=self.nextMulGo,font = "Arial 10 bold")
      btn_next.grid(row=9,column=3,sticky=E,padx=20,pady=5)
      #end frame7

      #######################frame 8 Results##################
      #showing results to users
      lbl_stdInfo = Label(self.frame8,text='Results',bg="#4A86E8",fg="white",font = "Arial 14 bold")
      lbl_stdInfo.grid(row=0,column=0,columnspan=2,pady=40)


      labelName = Label(self.frame8,text="Name",bg="#4A86E8",fg="white",font = "Arial 12 bold")
      labelName.grid(row=1,column=0,sticky="w",padx=5)

      labelName2 = Label(self.frame8,text="Name",textvariable= self.name,bg="lightgrey",width=12,font = "Arial 12 bold",anchor="w")
      labelName2.grid(row=1,column=1,pady=5)


      labelAge = Label(self.frame8,text="Age",bg="#4A86E8",font = "Arial 12 bold", fg="white",justify="left")
      labelAge.grid(row=2,column=0, sticky="w",padx=5)

      labelAge2 = Label(self.frame8,text="Age",textvariable=self.age,font = "Arial 12 bold",bg="lightgrey",width=12,justify="left",anchor="w")
      labelAge2.grid(row=2,column=1,pady=5)
      

      labelYear_level = Label(self.frame8,text="Year Level",bg="#4A86E8",fg="white",font = "Arial 12 bold")
      labelYear_level.grid(row=3,column=0, sticky="w",padx=5)

      labelYear_level = Label(self.frame8,text="Year Level",textvariable= self.year_level,bg="lightgrey",width=12,font = "Arial 12 bold",anchor="w")
      labelYear_level.grid(row=3,column=1,pady=5)

      
      labelScore = Label(self.frame8,text="Score",bg="#4A86E8",fg="white",font = "Arial 12 bold")
      labelScore.grid(row=4,column=0, sticky="w",padx=5)

      self.labelScore2 = Label(self.frame8,text="Score", bg="lightgrey",width=12,font = "Arial 12 bold",anchor="w")
      self.labelScore2.grid(row=4,column=1,pady=5)

                        
      btn_continue = Button(self.frame8, text="Finish", highlightbackground="#FF0317", command=self.quit,font = "Arial 10 bold")
      btn_continue.grid(row=5,column=6,padx=(220,5),pady=(140,15))

      
      self.frame1.pack(fill="x",padx=(250,0))
      #end frame8

   #function to quit the quiz
   def quit(self):  
      self.window.destroy()

   #set addition quiz, if number is 1
   def additionPress(self):
      self.TYPE_.set(1)
      self.btn_addition.configure(bg= "gray",fg="white")
      self.btn_subtraction.configure(bg= "lightgrey",fg="black")
      self.btn_division.configure(bg= "lightgrey",fg="black")
      self.btn_multiplication.configure(bg= "lightgrey",fg="black")

   #set subtraction quiz, if number is 2
   def subtractionPress(self):
      self.TYPE_.set(2)
      self.btn_addition.configure(bg= "lightgrey",fg="black")
      self.btn_subtraction.configure(bg= "gray",fg="white")
      self.btn_division.configure(bg= "lightgrey",fg="black")
      self.btn_multiplication.configure(bg= "lightgrey",fg="black")

      
   #set division quiz, if number is 3
   def divisionPress(self):
      self.TYPE_.set(3)
      self.btn_division
      self.btn_addition.configure(bg= "lightgrey",fg="black")
      self.btn_subtraction.configure(bg= "lightgrey",fg="black")
      self.btn_division.configure(bg= "gray",fg="white")
      self.btn_multiplication.configure(bg= "lightgrey",fg="black")
      
   #set multiplication quiz, if number is 3
   def multiplicationPress(self):
      self.TYPE_.set(4)
      self.btn_addition.configure(bg= "lightgrey",fg="black")
      self.btn_subtraction.configure(bg= "lightgrey",fg="black")
      self.btn_division.configure(bg= "lightgrey",fg="black")
      self.btn_multiplication.configure(bg= "gray",fg="white")
      
      
   #setting up quiz frames for each type, e.g if user press addition button then, show the addition quiz etc
   def callGameplay(self):
      try:
         number = int(self.TYPE_.get()) 
         if(number == 1):
            #print(self.TYPE_.get())
            #print(self.addAns)
            self.frame3.forget()
            self.frame4.pack(fill="x")
         if(number == 2):
            #print(self.TYPE_.get())
            #print(self.subAns)
            self.frame3.forget()
            self.frame5.pack(fill="x")
         if(number == 3):
            #print(self.TYPE_.get())
            #print(self.divAns)
            self.frame3.forget()
            self.frame6.pack(fill="x")
         if(number == 4):
            #print(self.TYPE_.get())
            #print(self.mulAns)
            self.frame3.forget()
            self.frame7.pack(fill="x")
         else:
            return
      except:
         print("Please Select One of them!!")
         
   def goBackToHowTo(self):
      self.frame3.forget()
      self.frame2.pack(fill="x")

   def goBackToInfo(self):
      self.frame2.forget()
      self.frame1.pack(fill="x",padx=(250,0))

   def callChooseWindow(self):
      self.frame2.forget()
      self.frame3.pack(fill="x")

   #validate user input, if empty, show msg
   def continueCall(self):
      if (self.name.get()== '' or self.age.get()=='' or self.year_level.get()==''):
         print("Any Input, Should not be Empty!!")
         return
      
      #print(self.age.get())
      #print(self.year_level.get())
      self.frame1.forget()
      self.frame2.pack(fill="x")
      
   def goToChooseMenu1(self):
      self.frame4.forget()
      self.frame3.pack(fill="x")

   def goToChooseMenu2(self):
      self.frame5.forget()
      self.frame3.pack(fill="x")

   def goToChooseMenu3(self):
      self.frame6.forget()
      self.frame3.pack(fill="x")

   def goToChooseMenu4(self):
      self.frame7.forget()
      self.frame3.pack(fill="x")


   #function to calculate how many user questions are correct, and assign score with respect
   def nextAddGo(self):
      self.score = 0
      index1 = 0
      for row in range(0,8):
         for column in range(0,3):
            a = self.list_entry_add[row][column].get()
            b = str(self.addAns[index1])
            if(a == b):
               self.score = self.score+1
            index1 = index1+1
      #print("Total score = "+str(self.score))
      self.labelScore2.configure(text=str(self.score)+"/24")
      self.frame4.forget()
      self.frame8.pack(fill="x",padx=(280,0))

   #function to calculate how many user questions are correct, and assign score with respect   
   def nextSubGo(self):
      self.score = 0
      index2 = 0
      for row in range(0,8):
         for column in range(0,3):
            c = self.list_entry_sub[row][column].get()
            d = str(self.subAns[index2])
            #print(c)
            if(c == d):
               self.score = self.score+1
            index2 = index2+1
      #print("Total score = "+str(self.score))
      self.labelScore2.configure(text=str(self.score)+"/24")
      self.frame5.forget()
      self.frame8.pack(fill="x",padx=(280,0))

   #function to calculate how many user questions are correct, and assign score with respect   
   def nextDivGo(self):
      self.score = 0
      index3 = 0
      for row in range(0,8):
         for column in range(0,3):
            e = self.list_entry_div[row][column].get()
            f = str(math.floor(self.divAns[index3]))
            if(e == f):
               self.score = self.score+1
            index3 = index3+1
      #print("Total score = "+str(self.score))
      self.labelScore2.configure(text=str(self.score)+"/24")
      self.frame6.forget()
      self.frame8.pack(fill="x",padx=(280,0))

   #function to calculate how many user questions are correct, and assign score with respect
   def nextMulGo(self):
      self.score = 0
      index4 = 0
      for row in range(0,8):
         for column in range(0,3):
            g = self.list_entry_mul[row][column].get()
            h = str(self.mulAns[index4])
            if(g == h):
               self.score = self.score+1
            index4 = index4+1
      self.labelScore2.configure(text=str(self.score)+"/24")
      #print("Total score = "+str(self.score))
      self.frame7.forget()
      self.frame8.pack(fill="x",padx=(280,0))
            

#starting of program      
if __name__ == "__main__":
   root = Tk()                   #object of Tkinter window
   root.geometry("800x500")      #set width and height of window
   root.resizable(False,False)   #resizable false
   root.config(bg="#4A86E8")     #setting bg=background color
   Window1(root ,"Math Quiz")    #calling constructor of Class Window1
   root.mainloop()               #mainloop of tkinter window
