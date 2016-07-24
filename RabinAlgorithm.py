import random
import math
import time

def numrize(shuru):
    num=ord(shuru)
    if(num>=ord('0') and num<=ord('9')):
        return num-ord('0')
    elif(num>=ord('a')and num<=ord('z')):
        return num-ord('a')+10
    elif(num>=ord('A')and num<=ord('Z')):
        return num-ord('A')+36
    else:
        return 62
    

def denumrize(shuru):
    table='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ   '
    ##     012345678911234567892123456789312345678941234567895123456789612
    return table[shuru]

def getst(a,b):
    flag=0
    r2=a
    s1=1
    t1=0
    r1=b
    s=0
    t=1
    q=a/b
    r=a-b*q
    while(r!=0):
        s2=s1
        t2=t1
        r2=r1
        s1=s
        t1=t
        r1=r
        s=s2-q*s1
        t=t2-q*t1
        q=r2/r1
        r=r2-q*r1
    return s,t
##  st(p,q)  ->  sp*tq=1
##  return (s,t)
    
def chineseresidue(b1,b2,p,q):
    a=getst(p,q)
    s=a[0]%q
    t=a[1]%p
    n=p*q
    r1=(s*p*b2+t*q*b1)%n
    r2=(s*p*b2-t*q*b1)%n
    r3=(-s*p*b2+t*q*b1)%n
    r4=(-s*p*b2-t*q*b1)%n
    res=(r1,r2,r3,r4)
    return res
##  chineseresidue(b1,b2,p,q)  x=b1%p;x=b2%q
##  return(x1,x2,x3,x4)

def digitalize(a):
    b=[]
    c=[]
    if(a==''):
        a='Communication Skill Mathematical Fundation of Information Security 201201001 5130369064 000001'
        print a
    length=len(a)
    residue=6-length%6 ##" "residue
    a=a+residue*' '
    block=len(a)/6
    for i in range(block):
        b.append(a[i*6:i*6+6])
    print b
    for j in b:
        res=0
        for k in j:
            res=res*64
            res=res+numrize(k)
        res=res*64+63
        res=res*64+63
        res=res*64+63
        c.append(res)
    print '\n',"the word(c) is:",'\n',c,'\n'
    return c
##return (1234434545,423432432234,24343232432,4243324234)

def dedigital(i):
    res=''
    i=i/64
    i=i/64
    i=i/64
    for j in range(6):
        char=i%64
        res=''+denumrize(char)+res
        i=i/64
    return res

def mopingfang(a,b,c):
    aa=1
    bb=a
    while(b!=0):
        if(b%2==1):
            aa=aa*bb%c;
        bb=bb*bb%c
        b=b/2
    return aa
##a^b mod c=aa
##return aa

def test(p):
    for i in range(8):
        b=random.randint(2,200)
        a=mopingfang(b,p-1,p)
        if(a!=1):
            return 0
    return 1
##test p
##return 1 0

def pq():
    flag=0
    while(flag!=1):
        res=random.randrange(268435457,536870911,2)
        if(test(res)==1 and res%4==3):
            flag=1
    ##print res
    return res
##create 2^28< p <2^29
##return p

def sqroot(c,p):
    res=mopingfang(c,(p+1)/4,p)
    res=res%p
    return res
##calculate the square root, x^2=c mod p
##return abs x

def reprocess(s):
    for i in s:
        res=''
        x1=i%64
        i=i/64
        x2=i%64
        i=i/64
        x3=i%64
        i=i/64
        if(x1==63 and x2==63 and x3==63):
            for j in range(6):
                char=i%64
                res=''+denumrize(char)+res
                i=i/64
            return res

def main():
    string=raw_input('plz give me the message u want to encrypt or u will encrypt the arranged:\n')
    string2=raw_input('if u wanna C the decode message please press"1":\n')
    p=pq();
    q=pq();
    if(p<q):
        pqp=p
        p=q
        q=pqp
    n=p*q                   ##produce p q
    print 'p:',p
    print 'q:',q
    print 'n:',n,'\n'
    m=digitalize(string)    ##digitalize get message:M
    c=[]
    for i in m:
        c.append(i*i%n)     ##encrypt get code:C
    print 'the code(m) is:','\n',c
    d=''
    c1=''
    ##for j in c:
      ##  c1=''+c1+dedigital(j);
    ##print "\nthe encypted message is:",'\n',c1
    if(string2=='1'):
        print '\n','if u decode M, u will get this:'
    for j in c:
        b1=sqroot(j,p)
        b2=sqroot(j,q)
        s=chineseresidue(b1,b2,p,q)##decode calculate
        if(string2=='1'):
            print s
        d=d+reprocess(s)    ##decode and dedigitalize
        #print j
        #print b1,b2,p,q
    while(d[-1]==' '):
        d=d[0:-1]
    print '\n','after decode:','\n',d,'\n'
    print 'the window will only exist 20 seconds'
    time.sleep(20)
    
main()
