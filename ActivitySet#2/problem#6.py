

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
m.add("idly", 10)
m.add("vada", 20)
m.show()

