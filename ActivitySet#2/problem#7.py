class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.items=[]
    
    def add(self,item,q):
        self.items.append((item,q))

    def __add__(self,item,q):
        m=Menu()
        m.items=add()
        return m

        
    def show(self):
        for a,b in self.items:
            print(a,b)
  
m = Menu()
m =("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly