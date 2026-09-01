import time
from itertools import chain
from sage.all import *


def DoubleCircuits(M,IngletonMain=False):
    #input: a matroid M
    #       a boolean indicating whether Ingleton-Main is checked or not (then Dress-Lovasz is checked)
    #output: for each double circuit CC:
    #          the double circuit degree d, 
    #          the number of points to be added to the intersection
    #          the circuit closures of the double circuit
    #          the intersection of these circuits
    Md = M.dual()
    for F in Md.flats(Md.full_rank() - 2):
        Mdm = Md.contract(F)
        d=Mdm.simplify().size()
        if IngletonMain:
            goodDegree = (d == 3)
        else:
            goodDegree = (d >= 3)
        if goodDegree:
            circs = [M.closure(C) for C in Mdm.cocircuits()]
            inter = M.groundset()
            for C in circs:
                inter = inter.intersection(C)
            ir = M.rank(inter)
            if d-2 - ir <= 0:
                continue
            yield d, circs, inter
 
 
def DressLovaszExtensions(M, CC):
    #input: a matroid M
    #       a list of circuit closures CC
    #output: the subsets that i must lie in the closure of so that i lies in all circuit closures of CC, and the new element i
    E = M.groundset()
    i = -1
    while i in E:
        i -= 1
    
    return [list(c) for c in CC if len(c) < M.size()], i
 
def RecursiveDressLovaszCondition(M,depth=1,IngletonMain=False):
    #input: a matroid M
    #       an integer depth
    #       a boolean indicating whether Ingleton-Main is checked or not (then Dress-Lovasz is checked)
    #output: the Dress-Lovasz (or Ingleton-Main) condition at depth 'depth' for M
    
    if depth==0:
        return True
    
    for dCC in DoubleCircuits(M,IngletonMain):
        d, CC, inter = dCC
        subsets, i = DressLovaszExtensions(M,CC)
        principal = M.extension(element=i,subsets=subsets)
        if depth == 1:
            DLE = (principal,)
        else:
            DLE = chain((principal,), M.extensions(element=i,subsets=subsets))
        goodCC = False
        for N in DLE:
            if N.rank(inter.union([i])) == N.rank(inter):
                continue
            if RecursiveDressLovaszCondition(N,depth-1,IngletonMain):
                goodCC = True
                break
        if not goodCC:
            return False
    return True
 

C1 = Matroid(groundset = set(range(13)), revlex = '0********0****0******0****0**0**************0*****0**00*************************************************0*******0**********0*******************************0************0************0*******0*****0********0**0**0000*0**0**0**0******0**0*****00000*0**0***************0*0**0*********0****00********0**0***************0*****00*****************0***000**00****0******0*0******00000**000****0********0*****0********0**0*********0*****0********0**0**00000000*0**0******0*0**0*0*0****0******************0****0****00****00000**************0***000**00**000***0****************0000000***0**0**************0*********0*********0**0**0*********0****00*0*0*******000***************0**00**000********0000*******0*******0*0**********', rank=4)

t = time.time()
print(RecursiveDressLovaszCondition(C1, depth=4, IngletonMain=True))
print(time.time() - t)

C2 = Matroid(groundset = set(range(13)), revlex = '0********0****0******0****0**0**************0*****0**00*************************************************0*******0**********0*******************************0************0************0*******0*****0********0**0**0000*0**0**0**0******0**0*****00000*0**0***************0*0**0*********0****00********0**0***************0*****00*****************0***000**00****0******0*0******00000**000****0********0*****0********0**0*********0*****0********0**0**00000000*0**0******0*0**0*0*0****0******************0****0****00****00000**************0***000**00**000***0****************0000000***0**0**0***********0*********0*********0**0**0*********0****00*0*0*******000***************0**00**000********0000*******0*******0*0**********', rank=4)


t = time.time()
print(RecursiveDressLovaszCondition(C2, depth=4, IngletonMain=True))
print(time.time() - t)

C3 = Matroid(groundset = set(range(13)), revlex = '0********0****0******0****0**0**************0*****0**00*************************************************0*******0**********0*******************************0************0************0*******0*****0********0**0**0000*0**0**0**0******0**0*****00000*0**0***************0*0**0*********0****00********0**0***************0*****00*****************0***000**00****0******0*0******00000**000****0********0*****0********0**0*********0*****0********0**0**00000000*0**0******0*0**0*0*0****0******************0****0****00****00000**************0***000**00**000***0****************0000000***0**0*0************0*********0*********0**0**0*********0****00*0*0*******000*0*0***********0**00**000********0000*******0*******0*0**********', rank=4)
t = time.time()
print(RecursiveDressLovaszCondition(C3, depth = 4, IngletonMain =True))
print(time.time() - t)