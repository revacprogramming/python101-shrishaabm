# Lists

filename = "dataset/romeo.txt"
a=open(filename)
b = list()                       
for i in a:                   
    word= i.rstrip().split()    
    for j in word:               
        if j in b:       
            continue               
        else :                    
            b.append(j)         
b.sort()                     
print (b)
