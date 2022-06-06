


def get_cs():
    a=input("enter")
    return a

def cs_to_lot(cs):
    """convert connected string to list of strings"""
    b=tuple()
    l=cs.split(";")
    c=[]
    for i in l:
        c.append(tuple(i.split("=")))
    print (c)

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)



main()
