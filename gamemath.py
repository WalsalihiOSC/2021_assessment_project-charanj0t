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