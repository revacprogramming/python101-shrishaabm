

class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.items=[]

    def add(self,item,quant):
        self.items.append((item,quant))
    
    def show(self):
        for a,b in self.items:
            print(a,b)


m = Menu()  # Menu is a class
m = m + ("idly", 10) + ("vada", 20)
m.show()

