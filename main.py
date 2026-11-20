import lzma,base64,struct,os
import json as J
from itertools import count as C,accumulate
from collections import namedtuple as T
CT={"Content-Type":"application/json"}
from urllib.request import *
Rr,Uo=Request,urlopen
M=30000
A,H,B,G=91,98,21,28
P=list(accumulate(struct.unpack("<720i",lzma.decompress(base64.b85decode("{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;0r$h?p*)?Zh;J?x3#DtA;;&7(;LTYWdZ@NNSR#rXktDOr-jwP^)xGpA&HaaS)_<T$KShblx})&Y7zqbQG@ZyQonB&XA#BwFx)EDKWw%*8buEV8XO>Bu_~WLcaSbhJsQhx@L05s+S3S|PYx#MX0OZaL0w-~aaVfRG#II;6>BgFcmlO--JrDp9bN8S(L0||`(!SIrSdDku<`x#giiHQyz}q7oGH3A9|c08Go5e=iM6J^sPG=62rQ>75wGUSCUx@U)Pc2NDr-C+NgbuI>&_zOMQ!HW;_$?n2_C4OveGA9%ps;OY%Raw00000l@Dhws`jl100D{uz!m@i$AMUAvBYQl0ssI200dcD")))))
pst={k:P[i*120:(i+1)*120] for i,k in enumerate("PNBRQK")}
N,E,S,W=-10,1,10,-1
Q=(N,E,S,W,N+E,S+E,S+W,N+W)
d={'P':(N,2*N,N+W,N+E),'N':(2*N+E,N+2*E,S+2*E,2*S+E,2*S+W,S+2*W,N+2*W,2*N+W),'B':(N+E,S+E,S+W,N+W),'R':Q[:4],'Q':Q,'K':Q}
F=T("F","b s w c e k")
def iu(i):r,f=divmod(i-A,10);return chr(f+97)+str(1-r)
class Z(F):
 def gm(o):
  for i,p in enumerate(o.b):
   if not p.isupper():continue
   for D in d[p]:
     for j in C(i+D,D):
      q=o.b[j]
      if q in' \n':break
      if q=='K' and(i==A and o.w[0] or i==H and o.w[1]):yield (j,j-2) if i==A else (j,j+2)
      if q.isupper():break
      if p=='P' and D in(N+W,N+E)and q=='.'and j not in(o.e,o.k):break
      if p=='P'and D in(N,2*N)and q!='.':break
      if p=='P'and D==2*N and(i<A+N or o.b[i+N]!='.'):break
      yield (i,j)
      if p in'PNK':break
      if q.islower():break
 ro=lambda o:Z(o.b[::-1].swapcase(),-o.s,o.c,o.w,119-o.e,119-o.k)
 def va(o,m):
  i,j=m;p,q=o.b[i],o.b[j];sc=pst[p][j]-pst[p][i]
  if q.islower():sc+=pst[q.upper()][j]
  if abs(j-o.k)<2:sc+=pst['K'][j]
  if p=='K' and abs(i-j)==2:sc+=pst['R'][(i+j)//2]-pst['R'][A if j<i else H]
  if p=='P'and B<=j<=G:sc+=pst['Q'][j]-pst['P'][j]
  if p=='P'and j==o.e:sc+=pst['P'][j+S]
  return sc
 def mv(o,m):
  i,j=m;pt=lambda b,i,p:b[:i]+p+b[i+1:]
  p,q=o.b[i],o.b[j]
  w,b,ep,kp=o.w,o.c,0,0
  sc=o.s+o.va(m);bd=o.b
  bd=pt(bd,j,bd[i]);bd=pt(bd,i,'.')
  if i==A:w=(0,w[1])
  if i==H:w=(w[0],0)
  if j==B:b=(b[0],0)
  if j==G:b=(0,b[1])
  if p=='K':
   w=(0,0)
   if abs(j-i)==2:kp=(i+j)//2;bd=pt(bd,A if j<i else H,'.');bd=pt(bd,kp,'R')
  if p=='P':
   if B<=j<=G:bd=pt(bd,j,'Q')
   if j-i==2*N:ep=i+N
   if j-i in(N+W,N+E)and q=='.':bd=pt(bd,j+S,'.')
  return Z(bd,sc,w,b,ep,kp).ro()
def fp(fen):
 p=fen.split();P9=' '*9
 s=P9+'\n'+P9+'\n'+''.join(' '+''.join('.'*int(c)if c.isdigit()else c for c in r)+'\n' for r in p[0].split('/'))+P9+'\n'+P9+' '
 o=Z(s,0,('K' in p[2],'Q' in p[2]),('k' in p[2],'q' in p[2]),0,0)
 if p[1]=='b':o=o.ro()
 return o
tp={}
def bo(o,g,x):
 global NN;NN+=1;e=tp.get(o)
 if e and e[0]>=x and(e[1]<e[2]and e[1]<g or e[1]>=e[2]and e[1]>=g):return e[1]
 if abs(o.s)>=M:return o.s
 null=-bo(o.ro(),1-g,x-3) if x>0 else o.s
 if null>=g:return null
 best,bm=-3*M,0
 for m in sorted(o.gm(),key=o.va,reverse=1):
  if x<1 and o.va(m)<150:break
  sc=-bo(o.mv(m),1-g,x-1)
  if sc>best:best=sc;bm=m
  if sc>=g:break
 if x<1 and best<null:return null
 if x>0 and best<=-M and null>-M:best=0
 if not e or x>=e[0]and best>=g:
  tp[o]=x,best,g,bm
  if len(tp)>4e5:tp.clear()
 return best
def se(o,mx):
 global NN;NN=0;sc=0;BM=0
 for x in range(1,99):
  lo,up=-3*M,3*M
  while lo<up-3:
   g=(lo+up+1)//2;sc=bo(o,g,x)
   if sc>=g:lo=sc
   else:up=sc
  e=tp.get(o)
  if e and e[3]:BM=e[3]
  if NN>=mx or abs(sc)>=M:break
 return BM,sc
def ok(p,m):return isinstance(m,tuple)and'k'not in[p.mv(m).b[m2[1]] for m2 in p.mv(m).gm()]
def c0(fen):
 p=fp(fen);m,sc=se(p,55000)
 if m is None or not ok(p,m):m=next(m2 for m2 in sorted(p.gm(),key=p.va,reverse=1)if ok(p,m2))
 i,j=m
 if fen.split()[1]=='b':i,j=119-i,119-j
 return iu(i)+iu(j)
U=os.environ["MAKEFUN_ENV_URL"]
def a0(p,b):return J.load(Uo(Rr(U+p,data=J.dumps(b).encode(),headers=CT),timeout=60))
if __name__=="__main__":
 while 1:
  g=a0("/game",{})
  while g["status"]=="your_move":g=a0("/move",{"game":g["game"],"move":c0(g["fen"]) or iu(min(Z.gm(fp(g["fen"]))))})
  if g["status"]=="done":break
