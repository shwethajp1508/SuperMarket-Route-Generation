import collections
class path(object):
    """docstring for path"""
    def __init__(self,roads):
        super(path, self).__init__()
        self.roads = roads	
    def Dijkstra(self,source, dest):
        inf =float('inf')
        distance ={}
        done ={}
        pred = {}
        for i in self.roads:
        # // Unknown distance function from source to i
            distance[i] =inf
            pred[i] = 0
            done[i] =False

    # // Distance from source to source = 0
        distance[source]=0   
        for x in self.roads:
            minDist=inf
            closest=None
            for  j in self.roads: 
                if done[j]==False:
                    if distance[j] <= minDist:
                        minDist = distance[j]
                        closest = j
            done[closest] = True
            if closest==dest:
                break
            neighbors =self.roads[closest]
            for nb in neighbors:
                w = nb[1]
                if done[nb[0]]==False:
                    if (distance[closest] + w < distance[nb[0]]):
                        distance[nb[0]]=distance[closest] + w
                        pred[nb[0]] = closest
        i= dest
        if distance[i]<inf:
            return distance[i]
        else:
            return inf

    def supermarket(self,s):
        items=s
        order ="start"
        startPoint="start"
        sum=0
        while items!=[]:
            minDist = 10000000000
            ClosestItem=None
            for i in items:
                r= self.Dijkstra(startPoint, i)
                if r < minDist:
                    minDist = r
                    ClosestItem = i
            startPoint = ClosestItem
            sum=sum+minDist
            order =order + " --> "+startPoint
            items.remove(startPoint)
        print(order)
        return order,sum

    def allpossibility(self,s,start):
        items=s
        startPoint=start
        sum=0
        while items!=[]:
            minDist = 10000000000000
            ClosestItem=None
            u=collections.defaultdict(list)
            for i in range(len(items)):
                r= self.Dijkstra(startPoint, items[i])
                if r<=minDist:
                    minDist=r
                    u[minDist].append(items[i])
                    ClosestItem = items[i]
            if len(u[minDist])==1:
                sum=sum+minDist
                startPoint = ClosestItem
                items.remove(startPoint)
            else:
                w=1000000000
                o=None
                for x in u[minDist]:
                    s=[]
                    for y in items:
                        if y!=u[minDist]:
                            s.append(y)
                    q=self.allpossibility(s,x)
                    if w>q:
                        w=q
                        ClosestItem=x
                sum=sum+w
                startPoint = ClosestItem
                items.remove(ClosestItem)
            return sum

def main():
    print("Enter the input file from directory (input1.txt,input2.txt,input3.txt,input4.txt,input5.txt,input6.txt) ")
    C=input() # input1.txt
    G={}
    file=open(C,'r') # reading the corresponding input file
    for line in file:
        line=line.strip()
        adjacentVertices=[]
        first=True
        k=None
        for edge in line.split(' '):
            if first:
                k=edge
                first=False
            else:
                a = edge.split(',')
                adjacentVertices.append([str(a[0]),int(a[1])])
        G[str(k)]=adjacentVertices
    file.close()
    h=path(G)
    p=set()
    s=[]
    w=set()
    for x in G:
        if x!='start':
            p.add(x)
            s.append(x)
            w.add(x)
    print("========================================================================================================================================================")
    print("")
    print("SUPERMARKET COMPLETE PATH")
    print("")
    W,v=h.supermarket(s)
    print("")
    print("========================================================================================================================================================")
    print("")
    print("ENTER REQUIRED ITEMS")
    print("")
    items=[]
    d=0	
    while d!=-1 and len(w)!=0:
        print(w)
        k=False
        while k==False:
            print("")
            print("Add item or press -1 for exit")
            t=input() # Enter the item name from list provided
            u=str(t)
            if u=="-1":
                k=True
                d=-1
            elif u.lower() not in p:
                print("Incorrect item entered!! Please enter again from list of items")
            else:
                k=True
                items.append(u)
                w.remove(u.lower())
    print("")
    print("Items Selected :")
    print(items)
    print("")
    if len(w)==0:
        print(W,v)
    else:
        order ="start"
        startPoint="start"
        sum=0
        while items!=[]:
            minDist = 1000000000000
            ClosestItem=None
            u=collections.defaultdict(list)
            for i in range(len(items)):
                r= h.Dijkstra(startPoint, items[i])
                if r <= minDist:
                    minDist = r
                    u[minDist].append(items[i])
                    ClosestItem = items[i]
            if len(u[minDist])==1:
                sum=sum+minDist
                startPoint = ClosestItem
                order += " --> "+startPoint
                items.remove(startPoint)
            else:
                w=1000000000
                o=None
                for x in u[minDist]:
                    s=[]
                    for y in items:
                        if y!=u[minDist]:
                            s.append(y)
                    q=h.allpossibility(s,x)
                    if w>q:
                        w=q
                        ClosestItem=x

                sum=sum+minDist
                # print("closest item is: ",ClosestItem,minDist)
                startPoint = ClosestItem
                order += " --> "+startPoint
                items.remove(startPoint)
                # print(items)
        print("HERE IS YOUR PATH")
        print(order)
        print("It takes ",sum," metres")
        print("-------------------------------------     THANK YOU.. VISIT US AGAIN     -----------------------------------------")
main()