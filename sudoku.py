from random import  randrange
def affichage(a):
  for y in range(9):
    if(y%3==0):
      print(' ------------------------')
    print(f' | {a[y][0] if (a[y][0]!=0) else "_"} {a[y][1] if (a[y][1]!=0) else "_"} {a[y][2] if (a[y][2]!=0) else "_"} | {a[y][3] if (a[y][3]!=0) else "_"} {a[y][4] if (a[y][4]!=0) else "_"} {a[y][5] if (a[y][5]!=0) else "_"} | {a[y][6] if (a[y][6]!=0) else "_"} {a[y][7] if (a[y][7]!=0) else "_"} {a[y][8] if (a[y][8]!=0) else "_"} |')
  print(' ------------------------')
def casPossibleGeneral(donne,i,j):
  casLigne=[ii for ii in range(1,10) if ii not in donne[i]]
  casColonne=[iii for iii in range(1,10) if iii not in [ii[j] for ii in donne]]
  casPossible=[ii for ii in casLigne if ii in casColonne]
  xx=(i//3)*3
  yy=(j//3)*3
  carre=[donne[m][n] for m in range(xx,xx+3) for n in range(yy,yy+3)]
  carre=[ii for ii in range(1,10) if ii not in carre]
  casPossible=[ii for ii in casPossible if (ii in carre)]
  return casPossible
def casPossibleSurLeCase(donne,x,y):
  m=[casPossibleGeneral(donne,y,i) for i in range(0,len((donne[y])))]
  isa=[len([1 for a in m[x+1:] if n in a]) for n in m[x]]
  if len(isa)==0:
    return []
  minimum=min(isa)
  casPossible=[i for i in m[x] if (len([1 for a in m[x+1:] if i in a])==minimum)]
  return casPossible
def casPossibleSurLeCase1(donne,x,y):
  m=[casPossibleGeneral(donne,y,i) for i in range(9)]
  isa=[len([1 for a in m for n in m[x] if (n in a)])]
  if len(isa)==0:
    return []
  minimum=min(isa)
  casPossible=[i for i in m[x] if (len([1 for a in m if i in a])==minimum)]
  return casPossible
def ajoutCas1(a):
  for y in range(9):
    for x in range(9):
      nb=casPossibleSurLeCase1(a,x=x,y=y)
      if(len(nb)==1 and a[y][x]==0):
        return nb[0],x,y
      if(len(nb)>1 and a[y][x]==0):
        print(nb)
  return None,None,None

def genererLesChiffres():
  quite=True
  while quite:
    quite=False
    data=[[0 for a in range(9)] for b in range(9)]
    for i in range(9):
      for j in range(9):
        casPossible=casPossibleSurLeCase(data,y=i,x=j)
        if(len(casPossible)!=0):
          data[i][j]=casPossible[randrange(len(casPossible))]
        else:
          quite=True
          break
      if quite:
        break
  return data
a=[[6, 9, 7, 5, 8, 1, 3, 4, 2], [1, 8, 4, 2, 3, 9, 6, 5, 7], [3, 5, 2, 4, 6, 7, 8, 1, 9], [5, 4, 1, 9, 7, 6, 2, 3, 8], [8, 7, 9, 3, 2, 5, 1, 6, 4], [2, 6, 3, 8, 1, 4, 9, 7, 5], [4, 3, 5, 6, 9, 2, 7, 8, 1], [7, 2, 6, 1, 4, 8, 5, 9, 3], [9, 1, 8, 7, 5, 3, 4, 2, 6]]
a=genererLesChiffres()
print("resultat")
affichage(a)


print("sujet")
for m in range(70):
  x,y=randrange(9),randrange(9)
  nb=a[y][x]
  a[y][x]=0
  casP=casPossibleSurLeCase1(a,x=x,y=y)
  a[y][x]=0 if (len(casP)<=1) else nb
# a=[[6, 9, 7, 0, 8, 1, 3, 0, 2], [0, 8, 4, 0, 3, 9, 0, 5, 7], [0, 5, 0, 0, 0, 0, 8, 1, 0], [0, 0, 0, 9, 7, 0, 0, 0, 0], [8, 0, 0, 0, 0, 5, 1, 6, 4], [0, 6, 3, 0, 0, 0, 0, 0, 5], [0, 3, 0, 0, 0, 2, 0, 0, 1], [7, 2, 6, 0, 4, 0, 0, 0, 0], [9, 1, 0, 7, 5, 3, 0, 0, 6]]

# affichage(a)
k=0
while 0 in [j for i in a for j in i]:
  nb,x,y=ajoutCas1(a)
  if nb is not None:
    a[y][x]=nb
  k+=1
  if k==200:
    break
affichage(a)
  


#  7 9 6 | 3 4 1 | 2 8 5
#  5 2 3 | 8 7 6 | 1 4 9
#  1 8 4 | 2 5 9 | 7 3 6
# ----------------------
#  2 3 7 | 1 6 8 | 5 9 4
#  9 6 8 | 4 2 5 | 3 1 7
#  4 5 1 | 7 9 3 | 8 6 2
# ----------------------
#  6 1 9 | 5 3 7 | 4 2 8
#  3 4 5 | 9 8 2 | 6 7 1

#  8 7 2 | 6 1 4 | 9 5 3
