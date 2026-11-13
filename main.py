import json,os,urllib.request
E=os.environ.get("MAKEFUN_ENV_URL")or exit("no env")
V=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33)
KI=(-17,-16,-15,-1,1,15,16,17)
DB=(-17,-15,15,17)
DR=(-16,-1,1,16)
T=(0,"kkkkkkkklmmggmmlljikkijlkkkookkkllmppmllmmoqqommuuuuuuuukkkkkkkk","aceeeecacgkllkgcelmnnmleeknoonkeelnoonleekmnnmkecgkkkkgcaceeeeca","giiiiiigilkkkkliimmmmmmiikmmmmkiillmmlliiklmmlkiikkkkkkigiiiiiig","kkkllkkkjkkkkkkjjkkkkkkjjkkkkkkjjkkkkkkjjkkkkkkjlmmmmmmlkkkkkkkk","giijjiigiklkkkkiilllllkikkllllkjjkllllkjikllllkiikkkkkkigiijjiig","oqmkkmqoookkkkooiggggggigeecceegeccaacceeccaacceeccaacceeccaacce")
b=[0]*128
w=1
ca=0
ep=-1
Kw=4
Kb=116
C=0
NB=90000
TT={}
KL=[[0,0]for _ in range(64)]
CM=[15]*128
for s,v in((4,12),(7,14),(0,13),(116,3),(119,11),(112,7)):CM[s]=v
def atk(s,q):
 o=(-15,-17)if q else(15,17)
 for x in(s+o[0],s+o[1]):
  if 0<=x<128 and b[x]==(1 if q else 7):return 1
 for o in KN:
  x=s+o
  if 0<=x<128 and not x&136 and b[x]==(2 if q else 8):return 1
 for o in KI:
  x=s+o
  if 0<=x<128 and not x&136 and b[x]==(6 if q else 12):return 1
 for o in DB:
  x=s+o
  while 0<=x<128 and not x&136:
   y=b[x]
   if y:
    if y==(3 if q else 9)or y==(5 if q else 11):return 1
    break
   x+=o
 for o in DR:
  x=s+o
  while 0<=x<128 and not x&136:
   y=b[x]
   if y:
    if y==(4 if q else 10)or y==(5 if q else 11):return 1
    break
   x+=o
 return 0
def pm(s,x):
 return[s|(x<<7)|((q if w else q+6)<<14)for q in(5,4,3,2)]
def gen():
 ms=[]
 for s in range(128):
  if s&136:continue
  c=b[s]
  if not c or(c<7)!=w:continue
  t=c if c<7 else c-6
  if t==1:
   d=16 if w else-16
   x=s+d
   if not b[x]:
    if(s>>4)==(6 if w else 1):ms+=pm(s,x)
    else:
     ms.append(s|(x<<7))
     if(s>>4)==(1 if w else 6)and not b[s+2*d]:ms.append(s|((s+2*d)<<7))
   for o in(d-1,d+1):
    x=s+o
    if 0<=x<128 and not x&136:
     y=b[x]
     if y and(y<7)!=w or x==ep:
      if(s>>4)==(6 if w else 1):ms+=pm(s,x)
      else:ms.append(s|(x<<7))
  else:
   oo,sl=((KN,0),(DB,1),(DR,1),(DB+DR,1),(KI,0))[t-2]
   for o in oo:
    x=s+o
    while 0<=x<128 and not x&136:
     y=b[x]
     if not y:ms.append(s|(x<<7))
     else:
      if(y<7)!=w:ms.append(s|(x<<7))
      break
     if not sl:break
     x+=o
   if t==6:
    for z,r,ee,pp,g in(((1,7,(5,6),(4,5,6),6),(2,0,(1,2,3),(4,3,2),2))if w else((4,119,(117,118),(116,117,118),118),(8,112,(113,114,115),(116,115,114),114))):
     if ca&z and b[r]==(4 if w else 10)and all(not b[x]for x in ee)and all(not atk(x,not w)for x in pp):ms.append(s|(g<<7))
 return ms
def mk(m):
 global w,ca,ep,Kw,Kb
 f=m&127;t=(m>>7)&127;p=(m>>14)&15;c=b[f];v=b[t];u=[m,v,ca,ep,0]
 if c in(1,7)and t==ep and not v:
  e=t-16 if w else t+16;u[4]=b[e];b[e]=0
 b[f]=0;b[t]=p or c
 if c==6:Kw=t
 elif c==12:Kb=t
 if c in(6,12)and abs(t-f)==2:b[f-4 if t<f else f+3]=0;b[f-1 if t<f else f+1]=4 if c==6 else 10
 ca&=CM[f]&CM[t]
 ep=(f+t)//2 if c in(1,7)and abs(t-f)==32 else-1
 w=not w
 return u
def un(u):
 global w,ca,ep,Kw,Kb
 m,v,ca,ep,e=u
 f=m&127;t=(m>>7)&127;p=(m>>14)&15
 w=not w
 c=b[t]
 b[f]=p and(1 if w else 7)or c
 b[t]=v
 if e:b[t-16 if w else t+16]=e
 if c==6:
  Kw=f
  if f==4 and t in(2,6):b[5 if t==6 else 3]=0;b[7 if t==6 else 0]=4
 elif c==12:
  Kb=f
  if f==116 and t in(114,118):b[117 if t==118 else 115]=0;b[119 if t==118 else 112]=10
def ev():
 s=0;a=0;n=0
 for q in range(128):
  if q&136:continue
  c=b[q]
  if c:
   t=c if c<7 else c-6
   i=(q>>4)*8+(q&7)
   v=V[t]+(ord(T[t][i if c<7 else i^56])-107)*5
   if t==3:
    if c<7:a+=1
    else:n+=1
   s+=v if c<7 else-v
 if a>1:s+=40
 if n>1:s-=40
 return s if w else-s
def sc(m):
 t=(m>>7)&127;v=b[t]
 if not v and t==ep:v=7 if w else 1
 if v:
  z=v if v<7 else v-6;y=b[m&127];y=y if y<7 else y-6
  return 10000+V[z]*10-V[y]
 return 0
def sr(d,a,be,pl):
 global C
 C+=1
 if C>NB:return 0
 q=d<=0
 if q:
  s=ev()
  if s>=be:return be
  if s>a:a=s
 h=atk(Kw if w else Kb,not w)
 if not q and h and pl<20:d+=1
 k=(bytes(b),w,ca,ep);e=0;tm=0
 if not q:
  e=TT.get(k)
  if e:
   tm=e[3]
   if e[0]>=d:
    if e[2]==0:return e[1]
    if e[2]==1:a=max(a,e[1])
    else:be=min(be,e[1])
    if a>=be:return e[1]
 ms=gen()
 if q and not h:ms=[m for m in ms if b[(m>>7)&127]or(m>>7)&127==ep or(m>>14)&15]
 ms.sort(key=lambda m:(m==tm)*10**7+sc(m)+(m==KL[pl][0])*9000+(m==KL[pl][1])*8000,reverse=True)
 bs=a if q else-10**9;bm=0;al=a;lg=0;n=0
 for m in ms:
  t=(m>>7)&127;cp=b[t]or t==ep or(m>>14)&15
  u=mk(m)
  if atk(Kb if w else Kw,w):un(u);continue
  lg=1;n+=1
  if d>=3 and n>3 and not cp and not h:
   s=-sr(d-2,-a-1,-a,pl+1)
   if s>a:s=-sr(d-1,-be,-a,pl+1)
  else:s=-sr(d-1,-be,-a,pl+1)
  un(u)
  if C>NB:return 0
  if s>bs:bs=s;bm=m
  if s>a:a=s
  if a>=be:
   if not q and not b[(m>>7)&127]and not(m>>14)&15:KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 if not lg and(d>0 or h):return -99999+pl if atk(Kw if w else Kb,not w)else 0
 if not q and C<=NB:TT[k]=(d,bs,2 if bs<=al else 1 if bs>=be else 0,bm)
 return bs
def parse(f):
 global w,ca,ep,Kw,Kb
 b[:]=[0]*128
 p=f.split();r=7;c=0
 for ch in p[0]:
  if ch=='/':r-=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:
   v="PNBRQK".find(ch.upper())+1
   if ch.islower():v+=6
   b[r*16+c]=v
   if v==6:Kw=r*16+c
   elif v==12:Kb=r*16+c
   c+=1
 w=p[1]=='w'
 ca=('K'in p[2])+2*('Q'in p[2])+4*('k'in p[2])+8*('q'in p[2])
 ep=(ord(p[3][0])-97)+(int(p[3][1])-1)*16 if p[3]!='-'else-1
def sq(x):return"abcdefgh"[x&7]+str((x>>4)+1)
def frm(u):
 f=(ord(u[0])-97)+(int(u[1])-1)*16;t=(ord(u[2])-97)+(int(u[3])-1)*16
 return f|(t<<7)|(((2+"nbrq".find(u[4]))+(0 if w else 6))<<14)if len(u)>4 else f|(t<<7)
def uci(m):
 f=m&127;t=(m>>7)&127;p=(m>>14)&15
 return sq(f)+sq(t)+("nbrq"[(p if p<7 else p-6)-2]if p else"")
def post(p,y):
 q=urllib.request.Request(E+p,data=json.dumps(y).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(q)as r:return json.load(r)
 except Exception as e:exit(p+" "+str(e))
def best(fen,legal):
 parse(fen)
 if len(legal)==1:return legal[0]
 rm=[frm(u)for u in legal]
 global C
 C=0
 bm=rm[0]
 if len(TT)>300000:TT.clear()
 for d in range(1,33):
  if C>NB:break
  rm.sort(key=lambda m:(m!=bm,-sc(m)))
  bs=-10**9;cur=bm
  for m in rm:
   u=mk(m)
   if atk(Kb if w else Kw,w):un(u);continue
   s=-sr(d-1,-10**9,10**9,1)
   un(u)
   if C>NB:break
   if s>bs:bs=s;cur=m
  if C>NB:break
  bm=cur
  if abs(bs)>90000:break
 return uci(bm)
# DRIVER
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=post("/move",{"game":g["game"],"move":best(g["fen"],g["legal_moves"])})
