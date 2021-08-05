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