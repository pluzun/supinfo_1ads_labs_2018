# Partie 1
x = int(input("nbr line : "))
z = "1"
for i in range(1,x+1) :
    print(i*z,"*",i*z,"=",int(z*i)**2)

print('\n\n')

# Partie 2
x = int(input("nbr line : "))
z = "1"
y=1
j=''
for i in range(1,x+1) :
    y+=1
    j = j + str(i)
    print(x,"*",j,"+",y,"=",z*(i+1))

print('\n\n')

# Partie 3
b,c="1","1"
for _ in range(1,x+1):
    print((x-1),"*",b,"+",c,"=",(x-1)*int(b)+int(c))
    b+= c
    b=str(int(b)+1)
    c=str(int(c)+1)

print('\n\n')

# Partie 4
table=int(input("Saisissez un nombre de lignes : "))
a,b,c=str(table),int(table-2),str(table)
for _ in range(1,table):
    print(table,"*",c,"+",b,"=",table*int(c)+int(b))
    a=str(int(a)-1)
    c+=a
    b-=1
