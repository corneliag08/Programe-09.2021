Zile = [ 'Luni' , 'Marti' , 'Miercuri' , 'Joi' , 'Vineri' , 'Sambata' , 'Duminica' ]
y=[250,300,400,250,100,270,405]
x=max(y)
print (max(y))
x1=min(y)
print (min(y))
xmare=[]
xmic=[]
for i in range (len(Zile)):
    if y[i]== xmare:
        xmare.extend(Zile[i]):
for i in range (len(Zile)):
    if y[i]==xmic:
        xmic.extend(Zile[i])
print ("Venitul saptamanal al intreprinderii este :", sum(y) )
print ("Media venitului zilnic este :" , sum (y)//7 )
print ("Ziua cu cel mai mare venit :",xmare)
print ("Ziua cu cel mai mare veni", xmic)