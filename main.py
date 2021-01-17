import itertools
import requests
from vector import Vector
from lxml import html
import copy
import time

start = time.time()

def mascherati(maskedv,m):
    ris = []
    v,indir = m
    a = copy.copy(v)
    a[len(v)-1] = -1
    if nonpresente(maskedv,v):
        ris.append(m)
    if nonpresente(maskedv,a):
        tempr = a,indir
        ris.append(tempr)
    for i in range(0,len(v)-1):
        for j in range(i+1,len(v)):
            c =[]
            d =[]
            for k in range(len(v)):
                c.append(9) 
                d.append(9)
            for b in range(0,len(v)):
                if b==i or b==j:
                    c[b] = -1
                    if b==i:
                        d[b] = -1
                    else:
                        d[b] = v[b]
                else:
                    c[b]=v[b]
                    d[b]=v[b]
            if nonpresente(maskedv,c):
                tempr = c,indir
                ris.append(tempr)
        if nonpresente(maskedv,d):
            tempr = d,indir
            ris.append(tempr)
    return ris

def nonpresente(maskedv,v1):
    for v2,indi in maskedv:
        for n in range(len(v1)):
            if (v2[n]!=v1[n]):
                break
            if (n==len(v1)-1):
                return False
    return True

def copre(vet1,mask):
    for b in range(len(vet1)):
        if mask[b]!=vet1[b] and mask[b]>=0:
            return False
    return True

def uguale(v1,v2):
    for b in range(len(v1)):
        if v1[b] != v2[b]:
            return False
    return True

def trova(vettori, sample, temp, salti, rangeA):
    if rangeA>=salti:
        return -1
    a,b = temp
    if nonpresente(sample,a):
        return temp
    else:
        if b<=1:
            return -1
        else:
            temp2 = vettori[b-1],b-1
            return trova(vettori, sample, temp2, salti, rangeA+1)


f1 = open("film/film.txt")
nomi1 = f1.readlines()
f1.close()
f2 = open("attori/attori.txt")
nomi2 = f2.readlines()
f2.close()
f3 = open("journals/journals.txt")
nomi3 = f3.readlines()
f3.close()
f4 = open("scientist/scientist.txt")
nomi4 = f4.readlines()
f4.close()
f5 = open("libri/libri.txt")
nomi5 = f5.readlines()
f5.close()
f6 = open("musica/musica.txt")
nomi6= f6.readlines()
f6.close()

sites = {}
num1 = 0
for nome in nomi1:
    num1= num1+1
    sites[num1] = nome[:-1]
for nome in nomi2:
    num1= num1+1
    sites[num1] = nome[:-1]
for nome in nomi3:
    num1 = num1+1
    sites[num1] = nome[:-1]
for nome in nomi4:
    num1 = num1+1
    sites[num1] = nome[:-1]
for nome in nomi5:
    num1 = num1+1
    sites[num1] = nome[:-1]
for nome in nomi6:
    num1 = num1+1
    sites[num1] = nome[:-1]

sample = []
vector = Vector()
vettori = {}
elle = 10
salti = 50
for indirizzo in sites.keys():
    vettori[indirizzo] = vector.vettore(elle,sites.get(indirizzo))
    if (indirizzo%salti == 0.0):
        temp = vettori[indirizzo],indirizzo
        if nonpresente(sample,vettori[indirizzo]):
            sample.append(temp)
        else:
            if indirizzo==0:
                ()
            else:
                temp2 = vettori[indirizzo-1],indirizzo-1
                ristemp = trova(vettori, sample, temp2, salti, 1)
                if not ristemp==-1:
                    sample.append(ristemp)


print("sample",len(sample))
maskedv = []
for m in sample:
    maskedv.extend(mascherati(maskedv,m))

diz = {}
i = 0
for vet,ind in maskedv:
    diz[i] = vet,ind,0
    i = i + 1

for vet1 in vettori.values():
    for ide in diz.keys():
        mask, ind, num = diz.get(ide)
        if copre(vet1,mask):
            num = num+1
            diz[ide] = mask,ind,num


serv = []
for mask, ind, num in diz.values():
    serv1 = []
    serv2 = []
    if num >= 0:
        temp = mask,ind
        serv1.append(temp)
        serv1.append(num)
        serv.append(serv1)

persi = 0
ris = []
for indice in vettori.keys():
    serv.sort(key=lambda i: i[1],reverse = True)
    perso = True
    for s in serv:
        if copre(vettori.get(indice),s[0][0]):
            perso = False
            flag = 0
            for r in ris:
                if uguale(r[0][0],s[0][0]):
                    r.append(indice)
                    flag = 1
            if flag == 0:
                ris.append([s[0],indice])
            for s2 in serv:
                if (not uguale(s[0][0],s2[0][0])) and copre(vettori.get(indice),s2[0][0]):
                    s2[1] = s2[1]-1
            break
    if perso:
        persi = persi +1

giusti=0
sbagliati=0
for a in ris:
    if a[0][1]<=500:
        for b in range(1,len(a)):
            if a[b] <=500:
                giusti = giusti+1
            else:
                sbagliati = sbagliati+1
    if a[0][1]>500 and a[0][1]<=1000:
        for b in range(1,len(a)):
            if a[b] >500 and a[0][1]<=1000:
                giusti = giusti+1
            else:
                sbagliati = sbagliati+1
    if a[0][1]>1000 and a[0][1]<=1500:
        for b in range(1,len(a)):
            if a[b] >1000 and a[0][1]<=1500:
                giusti = giusti+1
            else:
                sbagliati = sbagliati+1
    if a[0][1]>1500 and a[0][1]<=2000:
        for b in range(1,len(a)):
            if a[b] >1500 and a[0][1]<=2000:
                giusti = giusti+1
            else:
                sbagliati = sbagliati+1
    if a[0][1]>2000 and a[0][1]<=2500:
        for b in range(1,len(a)):
            if a[b] >2000 and a[0][1]<=2500:
                giusti = giusti+1
            else:
                sbagliati = sbagliati+1
    if a[0][1]>2500 and a[0][1]<=3000:
        for b in range(1,len(a)):
            if a[b] >2500 and a[0][1]<=3000:
                giusti = giusti+1
            else:
                sbagliati = sbagliati+1
    
recall = giusti/(len(sites)-persi)
precision = giusti/len(sites)
fmeasure = (2*recall*precision)/(recall+precision)


print("vettori da =",8)
print("elle =",elle+1)
print("persi =",persi)
print("recall =",recall)
print("precision =",precision)
print("fmeasure =",fmeasure)

end = time.time()
print("tempo =",end-start,"secondi")

