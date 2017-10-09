import time
import heapq
import random 
import itertools
from copy import deepcopy

#Goal State
f=[[1,2,3],[4,5,6],[7,8,0]]
#f =[[0,1,2],[3,4,5],[6,7,8]]
#f=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

r=[0,0,1,-1]
c=[1,-1,0,0]

class node:
    def __init__(self,x,y,matrix,parent,cost,d):
        self.x=x
        self.y=y
        self.matrix=matrix
        self.parent=parent
        self.d=d
        self.cost=cost+d
#Manhatan Distance
def cost(a): #a -pointer to node or a node 
    s=0
    for i in range(n):
        for j in range(n):
            if a.matrix[i][j] == 0:
                continue
            #remove -1 from below calculation of x,y. if Goal state starts with 0 
            x = int((a.matrix[i][j] - 1)/n) 
            y = int((a.matrix[i][j] - 1)%n) 
            s = s + abs(i-x)+abs(j-y)
    return s
#Feasiblity
def feas(i,j):
    if i<0 or i >=n or j <0 or j >= n:
        return 0
    return 1
#IF Goal state
def check(a):
    if a.matrix == f:
        return True
    return False

def printmat(parent):
        for i in range(n):
            for j in range(n):
                print(parent.matrix[i][j], end = ' ' )
            print()
        print()
#Print Path 
def printpath(parent):
    if parent == None:
        return
    printpath(parent.parent)
    printmat(parent)
#Astar   
def astar(i,j):
    root = node(i,j,b,None,0,0)
    root.cost = cost(root)
    #ctr - Tie breaker 
    ctr = 0
    q = []
    heapq.heappush(q , (root.cost,0 , root)) 
    d = {}
    while(q):
        element = heapq.heappop(q)
        parent = element[2]
        #Check for Goal 
        if check(parent):
            printpath(parent)
            print(ctr)
            return 
        #ctr+=1
        #print(ctr)
        #print(parent.matrix)
        #Check feasible moves from current state
        for k in range(4):
            x=parent.x + r[k]
            y=parent.y + c[k]
            if feas(x,y) == 0:
                continue
            matrix = deepcopy(parent.matrix)
            i,j=parent.x,parent.y
            matrix[i][j],matrix[x][y]=matrix[x][y],matrix[i][j]
            if parent.parent!= None and matrix == parent.parent.matrix:
                    continue  
            child=node(x,y,matrix,parent,0,0)
            child.d = parent.d+ 1
            child.cost = child.d+ cost(child)
            
            s=""
            for i in matrix:
                for j in i:
                    s=s+str(j)
            if s in d and d[s] < child.cost:
                continue
            d[s] = child.cost
            ctr+=1
            heapq.heappush(q,(child.cost,ctr, child))
        s=""
        for i in root.matrix:
            for j in i:
                s=s+str(j)
        d[s]=parent.cost
#Check if Solvable. Only for 3X3 
def isSolvable(matrix): 
    arr = []
    for i in range(n):
        for j in range(n):
            arr.append(matrix[i][j])
            
    inv_count = 0
    for i in range(n*n - 1 ):
        for j in range(i+1, n*n):
            if arr[i] and arr[j] and arr[i] > arr[j]:
                inv_count = inv_count + 1
    return (inv_count %2 == 0)


n=3                    

start_time = time.time()

#b=[[13,2,10,3],[1,12,8,4],[5,0,9,6],[15,14,11,7]] #2747264 nodes 213 secand 129 sec without i/o
#astar(2,1)
for i in itertools.permutations([1,2,3,4,5,6,7,8,0]):# returns tuple
    a = list(i)
    break
b=[[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        b[i][j] = a.pop()
#b=[[1,2,3],[5,6,0],[7,8,4]] #106316 nodes 12 sec 
#astar(1,2)
for i in b:
    random.shuffle(i)
for i in range(n):
    for j in range(n):
        if b[i][j]== 0 and isSolvable(b):
            print(b)
            astar(i,j)
            break
        elif b[i][j]== 0:
            print("not Solvable")
            break
print("--- %s seconds ---" % (time.time() - start_time))

