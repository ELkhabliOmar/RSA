import random

dic = {' ':10, 'A':11, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18,
    'I':19, 'J':20, 'K':21, 'L':22, 'M':23, 'N':24, 'O':25, 'P':26, 'Q':27, 'R':28,
    'S':29, 'T':30, 'U':31, 'V':32, 'W':33, 'X':34, 'Y':35, 'Z':36,}


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Euclide(a, b):     # algo d'Euclide
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = Euclide(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = Euclide(a, m)
    if y < 0: y = congru(y,1,m)
    if g != 1:
        raise Exception('modulo inverse n\'exist pas !')
    else:
        return x % m

def congru(a,p,n):
    return(a**p-((a**p)//n)*n)

def exp_rapide(b,e,m):
    d = {}
    d[1] = b
    y = congru(b,2,m)
    x = 2
    d[x] = y
    while x*2 < e:
        x = x*2
        y = congru(y,2,m)
        if y == 1: return y
        d[x] = y
    
    while x < e:
        k = e-x
        if k == 1:
            pass
        else:
            i = 1
            while 2*i < k:
                i = i * 2
            k = i
        x = x+k
        y = congru(y*d[k],1,m)
        if y == 1: return y
        
    #print(d)
    del d
    return y

def cle(k):
    for x in dic.keys():
        if dic[x] == k:
            return x


############## programme #####################
p = 3182227225630079723
q = 9803760009659795503
n = p * q
phi_n = (p-1) * (q-1)
e = 44344829669746450844892891211
g = pgcd(e, phi_n)
while g != 1:
     e = random.randrange(1, phi_n)
     g = pgcd(e, phi_n)

d = modinv(e,phi_n)

message_E = input("donner le message à chiffrée : ")
message_E = message_E.upper()

txt = ""
for i in message_E:
    txt = txt + str(dic[i])

ind=0
L=[]
while ind<len(txt)-1:
    if ind+10 < len(txt):
        L.append(txt[ind:ind+10])
    else:
        L.append(txt[ind:len(txt)])
    ind+=10

for j in range(len(L)):
    x = exp_rapide(int(L[j]),e,n)
    L[j] = x
    
print("blocs des messages chiffrée sont :",L)

txt2 =""
for x in L:
    txt2+= str(exp_rapide(x,d,n))
print("message reçu sous form des nombre est :",txt2)
message=""
for i in range(0,len(txt2)-1,2):
    k = cle(int(txt2[i:i+2]))
    message+= k.lower()

print("message reçu sous form de texte est :",message)