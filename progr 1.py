x=[6,1,8,4,2]
y=x
produs=1
print ("Suma primelor trei componente este " , sum (x[0:3]))
print ("Suma tuturor componentelor este " , sum (y))
for element in range (0,len(x)):
    produs*=x[element]
print("Produsul acestor componente este :", produs)