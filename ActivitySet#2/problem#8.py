class Menu:
    def __init__(self):
        self.items=dict() as hi 
    def __add__(self, item):
        dick[item[0]] = item[1]
        return self

    def __setitem__(self, a, b):
        dick[a] = b

    def __str__(self):
        f = " \n".join(" ".join(k, str(v)) for k, v in dick.items())

        return f


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)