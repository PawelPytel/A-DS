import random
import time
import sys
sys.setrecursionlimit(500000)
class macierz_sasiedztwa:
    def __init__(self,n):
        self.macierz=[]
        self.V=n
        self.default_E= n * (n - 1) // 4
        self.E=0
        for i in range(n):
            self.macierz.append([])
            for j in range(n):
                self.macierz[i].append(0)

    def __str__(self):
        string=""
        for i in self.macierz:
            string+=str(i)+"\n"
        return string
    def clean(self):
        for i in range(self.V):
            for j in range(self.V):
                self.macierz[i][j]=0
        self.E=0
    def set_connection(self,poprzednik,nastepnik):
        if poprzednik>=self.V or nastepnik>=self.V:
            return "Nieprawidłowe wierzchołki"
        if self.macierz[poprzednik][nastepnik]==0:
            self.macierz[poprzednik][nastepnik]=1
            self.E+=1
    def delete_connection(self,poprzednik,nastepnik):
        if poprzednik>=self.V or nastepnik>=self.V:
            return "Nieprawidłowe wierzchołki"
        if self.macierz[poprzednik][nastepnik] == 1:
            self.macierz[poprzednik][nastepnik]=0
            self.E-=1

    def fill(self):
        self.clean()
        ones = self.default_E
        zeros=0
        helper = []
        for i in range(self.V):
            for j in range(i + 1, self.V):
                helper.append([i, j])
        for i in range(self.V-1):
            row=i
            col=random.randrange(i+1,self.V)
            self.macierz[row][col]=1
            ones-=1
            position = 0
            for i in range(row):
                position += self.V-1 - i
            position += col - row - 1-zeros
            del helper[position]
            zeros+=1
        while ones!=0:
            coordinates = random.choice(helper)
            row=coordinates[0]
            col=coordinates[1]
            self.macierz[row][col]=1
            position = 0
            for i in range(coordinates[0]):
                position += self.V-1 - i
            position += col - row - 1 - zeros
            del helper[position]
            ones -= 1
            zeros += 1
        self.E=self.default_E
    def find_next(self,indeks):
        if indeks>=self.V:
            return "Nieprawidłowy wierzchołek"
        for next in range(self.V):
            if self.macierz[indeks][next]==1:
                return next
        return "Nie znaleziono następnika"
    def find_all_next(self,indeks):
        result=[]
        if indeks>=self.V:
            return "Nieprawidłowy wierzchołek"
        for next in range(self.V):
            if self.macierz[indeks][next]==1:
                result.append(next)
        #if result==[]:
            #return "Nie znaleziono następnika"
        return result
    def connection(self,poprzednik,nastepnik):
        if poprzednik>=self.V or nastepnik>=self.V:
            return "Nieprawidłowe wierzchołki"
        return self.macierz[poprzednik][nastepnik]==1
    def count_edges(self):

        count=0
        for i in self.macierz:
            for j in i:
                if j==1:
                    count+=1
        return count
    def DFS_sort(self):
        def DFS(i):
            visited[i]=True
            for j in self.find_all_next(i):
                if not visited[j]:
                    DFS(j)

        visited=[]
        for i in range(self.V):
            visited.append(False)
        result=[]
        for i in range(self.V):
            if  not visited[i]:
                DFS(i)
            result.append(i)
        return result
    """def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in range(self.V):
            for j in range(self.V):
                if self.macierz[i][j]==1:
                    result[j]+=1
        return result"""
    def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in range(self.V):
            for j in self.find_all_next(i):
                result[j]+=1
        return result
    def BFS_sort(self):
        unsorted=self.V
        result=[]
        poprz=self.poprzednicy()
        while unsorted!=0:
            for i in range(len(poprz)):
                if poprz[i]==0 and i not in result:
                    result.append(i)
                    unsorted-=1
                    for j in self.find_all_next(i):
                        poprz[j]-=1
        return result

class tabela_krawedzi:

    def __init__(self):
        self.tabela=[]
        self.E=0
        self.V=0
    def __str__(self):
        string=""
        for i in self.tabela:
            string+=str(i)+"\n"
        return string
    def clean(self):
        self.tabela=[]
        self.E=0
        self.V=0
    def fill(self,macierz):
        self.clean()
        self.E=macierz.E
        self.V=macierz.V
        for poprzednik in range(macierz.V):
            for nastepnik in range(macierz.V):
                if macierz.macierz[poprzednik][nastepnik]==1:
                    self.tabela.append([poprzednik,nastepnik])

    def find_next(self,indeks):
        for i in self.tabela:
            if i[0]==indeks:
                return i[1]
        return "Nie znaleziono następnika"
    def find_all_next(self,indeks):
        result=[]
        for i in self.tabela:
            if i[0]==indeks:
                result.append(i[1])

        return result
    def connection(self,poprzednik,nastepnik):
        for i in self.tabela:
            if i[0]==poprzednik:
                if i[1]==nastepnik:
                    return True
        return False
        #return [poprzednik,nastepnik] in self.tabela
    def count_V(self):
        zbior=[]
        for i in self.tabela:
            for j in i:
                if j not in zbior:
                    zbior.append(j)
        return len(zbior)

    def set_connection(self,poprzednik,nastepnik):
        self.tabela.append([poprzednik,nastepnik])
        self.E+=1
        self.V=self.count_V()
    def delete_connection(self,poprzednik,nastepnik):
        if [poprzednik,nastepnik] in self.tabela:
            self.tabela.remove([poprzednik,nastepnik])
            self.E-=1
        self.V=self.count_V()
    def DFS_sort(self):
        def DFS(i):
            visited[i]=True
            for j in self.find_all_next(i):
                if not visited[j]:
                    DFS(j)
        visited=[]
        for i in range(self.V):
            visited.append(False)
        result=[]
        for i in range(self.V):
            if  not visited[i]:
                DFS(i)
            result.append(i)

        return result
    """def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in self.tabela:
            result[i[1]]+=1
        return result"""
    def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in range(self.V):
            for j in self.find_all_next(i):
                result[j]+=1
        return result
    def BFS_sort(self):
        unsorted = self.V
        result = []
        poprz = self.poprzednicy()
        while unsorted != 0:
            for i in range(len(poprz)):
                if poprz[i] == 0 and i not in result:
                    result.append(i)
                    unsorted -= 1
                    for j in self.find_all_next(i):
                        poprz[j] -= 1
        return result

class next:
    def __init__(self,first_data):
        self.data=first_data
        self.next=None
class lista_nastepnikow:
    def __init__(self):
        self.tabela=[]
        self.V=0
        self.E=0
    def __str__(self):
        string=""
        for i in range(self.V):
            string+=str(i)+": "+str(self.find_all_next(i))+"\n"
        return string
    def clean(self):
        self.tabela=[]
        self.V=0
        self.E=0
    def fill(self,macierz):
        self.clean()
        self.V=macierz.V
        self.E=macierz.E
        for x in range(macierz.V):
            self.tabela.append(None)
        for i in range(macierz.V):
            for j in range(macierz.V):
                if macierz.macierz[i][j]==1:
                    if self.tabela[i]==None:
                        self.tabela[i]=next(j)
                    else:
                        temp=self.tabela[i]
                        while temp.next:
                            temp=temp.next
                        temp.next=next(j)
    def find_next(self,indeks):
        if indeks>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[indeks]:
            return self.tabela[indeks].data
        else:
            return "Nie znaleziono następnika"
    def find_all_next(self,indeks):
        result=[]
        if indeks>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        temp=self.tabela[indeks]
        while temp:
            result.append(temp.data)
            temp=temp.next
        return result
    def DFS_sort(self):
        def DFS(i):
            visited[i]=True
            for j in self.find_all_next(i):
                if not visited[j]:
                    DFS(j)
        visited=[]
        for i in range(self.V):
            visited.append(False)
        result=[]
        for i in range(self.V):
            if  not visited[i]:
                DFS(i)
            result.append(i)
        return result


    def connection(self,poprzednik,nastepnik):
        if poprzednik>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[poprzednik]:
            temp=self.tabela[poprzednik]
            found=False
            while temp and not found:
                if temp.data==nastepnik:
                    found=True
                temp=temp.next
            return found
        else:
            return "Nie znaleziono następnika"
    def set_connection(self,poprzednik,nastepnik):
        while poprzednik>=len(self.tabela) or nastepnik>=len(self.tabela):
            self.tabela.append(None)
            self.V+=1
        if  nastepnik not in self.find_all_next(poprzednik):
            if self.tabela[poprzednik] == None:
                self.tabela[poprzednik] = next(nastepnik)
            else:
                temp = self.tabela[poprzednik]
                while temp.next:
                    temp = temp.next
                temp.next = next(nastepnik)
    def delete_connection(self,poprzednik,nastepnik):
        if poprzednik>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[poprzednik]:
            temp=self.tabela[poprzednik]
            previous=None
            found=False
            while temp and not found:
                if temp.data==nastepnik:
                    found=True
                else:
                    previous=temp
                    temp=temp.next
            if temp:
                if temp.next:
                    if previous:
                        previous.next=temp.next
                    else:
                        self.tabela[poprzednik]=temp.next
                else:
                    if previous:
                        previous.next=None
                    else:
                        self.tabela[poprzednik]=None
                self.E-=1
            else:
                return "Nie znaleziono następnika"
        else:
            return "Nie znaleziono następnika"
    def BFS_sort(self):
        unsorted = self.V
        result = []
        poprz = self.poprzednicy()
        while unsorted != 0:
            for i in range(len(poprz)):
                if poprz[i] == 0 and i not in result:
                    result.append(i)
                    unsorted -= 1
                    for j in self.find_all_next(i):
                        poprz[j] -= 1
        return result
    def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in range(self.V):
            for j in self.find_all_next(i):
                result[j]+=1
        return result
class lista_poprzednikow:
    def __init__(self):
        self.tabela=[]
        self.V=0
        self.E=0
    def __str__(self):
        string=""
        for i in range(self.V):
            string+=str(i)+": "+str(self.find_all_previous(i))+"\n"
        return string
    def clean(self):
        self.tabela=[]
        self.V=0
        self.E=0
    def fill(self,macierz):
        self.clean()
        self.V=macierz.V
        self.E=macierz.E
        for x in range(macierz.V):
            self.tabela.append(None)
        for i in range(macierz.V):
            for j in range(macierz.V):
                if macierz.macierz[i][j]==1:
                    if self.tabela[j]==None:
                        self.tabela[j]=next(i)
                    else:
                        temp=self.tabela[j]
                        while temp.next:
                            temp=temp.next
                        temp.next=next(i)
    def find_previous(self,indeks):
        if indeks>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[indeks]:
            return self.tabela[indeks].data
        else:
            return "Nie znaleziono następnika"
    def find_all_previous(self,indeks):
        result=[]
        if indeks>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        temp=self.tabela[indeks]
        while temp:
            result.append(temp.data)
            temp=temp.next
        return result



    def connection(self,poprzednik,nastepnik):
        if nastepnik>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[nastepnik]:
            temp=self.tabela[nastepnik]
            found=False
            while temp and not found:
                if temp.data==poprzednik:
                    found=True
                temp=temp.next
            return found
        else:
            return "Nie znaleziono następnika"
    """def set_connection(self,poprzednik,nastepnik):
        while poprzednik>=len(self.tabela) or nastepnik>=len(self.tabela):
            self.tabela.append(None)
            self.V+=1
        if  nastepnik not in self.find_all_next(poprzednik):
            if self.tabela[poprzednik] == None:
                self.tabela[poprzednik] = next(nastepnik)
            else:
                temp = self.tabela[poprzednik]
                while temp.next:
                    temp = temp.next
                temp.next = next(nastepnik)
    def delete_connection(self,poprzednik,nastepnik):
        if poprzednik>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[poprzednik]:
            temp=self.tabela[poprzednik]
            previous=None
            found=False
            while temp and not found:
                if temp.data==nastepnik:
                    found=True
                else:
                    previous=temp
                    temp=temp.next
            if temp:
                if temp.next:
                    if previous:
                        previous.next=temp.next
                    else:
                        self.tabela[poprzednik]=temp.next
                else:
                    if previous:
                        previous.next=None
                    else:
                        self.tabela[poprzednik]=None
                self.E-=1
            else:
                return "Nie znaleziono następnika"
        else:
            return "Nie znaleziono następnika"
    def BFS_sort(self):
        unsorted = self.V
        result = []
        poprz = self.poprzednicy()
        while unsorted != 0:
            for i in range(len(poprz)):
                if poprz[i] == 0 and i not in result:
                    result.append(i)
                    unsorted -= 1
                    for j in self.find_all_next(i):
                        poprz[j] -= 1
        return result
    def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in range(self.V):
            for j in self.find_all_next(i):
                result[j]+=1
        return result"""
class lista_braku:
    def __init__(self):
        self.tabela=[]
        self.V=0
        self.E=0
    def __str__(self):
        string=""
        for i in range(self.V):
            string+=str(i)+": "+str(self.find_all(i))+"\n"
        return string
    def clean(self):
        self.tabela=[]
        self.V=0
        self.E=0
    def fill(self,macierz):
        self.clean()
        self.V=macierz.V
        self.E=macierz.E
        for x in range(macierz.V):
            self.tabela.append(None)
        for i in range(macierz.V):
            for j in range(i,macierz.V):
                if macierz.macierz[i][j]==0 and macierz.macierz[j][i]==0:
                    if self.tabela[j]==None:
                        self.tabela[j]=next(i)
                    else:
                        temp=self.tabela[j]
                        while temp.next:
                            temp=temp.next
                        temp.next=next(i)
                    if i!=j:
                        if self.tabela[i]==None:
                            self.tabela[i]=next(j)
                        else:
                            temp=self.tabela[i]
                            while temp.next:
                                temp=temp.next
                            temp.next=next(j)
    def find(self,indeks):
        if indeks>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        if self.tabela[indeks]:
            return self.tabela[indeks].data
        else:
            return "Nie znaleziono następnika"
    def find_all(self,indeks):
        result=[]
        if indeks>=len(self.tabela):
            return "Nie ma takiego wierchołka"
        temp=self.tabela[indeks]
        while temp:
            result.append(temp.data)
            temp=temp.next
        return result

class macierz_grafu:
    def __str__(self):
        string=""
        for i in self.macierz:
            string+=str(i)+"\n"
        return string
    def __init__(self,n):
        self.V=n
        self.E=0
        self.macierz=[]
        for i in range(self.V):
            self.macierz.append([])
            for j in range(self.V+3):
                self.macierz[i].append(0)
    def clean(self):
        for i in range(self.V):
            for j in range(self.V+3):
                self.macierz[i][j]=0
    def poprzednicy(self):
        result=[]
        for i in range(self.V):
            result.append(0)
        for i in range(self.V):
            for j in self.find_all_next(i):
                result[j]+=1
        return result
    def BFS_sort(self):
        unsorted=self.V
        result=[]
        poprz=self.poprzednicy()
        while unsorted!=0:
            for i in range(len(poprz)):
                if poprz[i]==0 and i not in result:
                    result.append(i)
                    unsorted-=1
                    for j in self.find_all_next(i):
                        poprz[j]-=1
        return result
    def DFS_sort(self):
        def DFS(i):
            visited[i]=True
            for j in self.find_all_next(i):
                if not visited[j]:
                    DFS(j)

        visited=[]
        for i in range(self.V):
            visited.append(False)
        result=[]
        for i in range(self.V):
            if  not visited[i]:
                DFS(i)
            result.append(i)
        return result
    def fill(self,macierz):
        self.E=macierz.E
        help_poprz=lista_poprzednikow()
        help_nast=lista_nastepnikow()
        help_brak=lista_braku()
        help_brak.fill(macierz)
        help_nast.fill(macierz)
        help_poprz.fill(macierz)

        for i in range(self.V):
            nxt=help_nast.find_all_next(i)
            pre=help_poprz.find_all_previous(i)
            br=help_brak.find_all(i)
            if nxt:
                self.macierz[i][0] = nxt[0]
                for j in range(1, len(nxt)):
                    self.macierz[i][nxt[j - 1] + 3] = nxt[j]
                self.macierz[i][nxt[-1] + 3] = nxt[-1]
            else:
                self.macierz[i][0] = None

            if pre:
                self.macierz[i][1] = pre[0]
                for j in range(1, len(pre)):
                    if pre[j]!=0:
                        self.macierz[i][pre[j - 1] + 3] = -pre[j]
                    else:
                        self.macierz[i][pre[j - 1] + 3] = "-0"
                if pre[-1]!=0:
                    self.macierz[i][pre[-1] + 3] = -pre[-1]
                else:
                    self.macierz[i][pre[-1] + 3] = "-0"
            else:
                self.macierz[i][1] = None
            if br:
                self.macierz[i][2] = br[0]
                for j in range(1, len(br)):
                    self.macierz[i][br[j - 1] + 3] = br[j] + self.V
                self.macierz[i][br[-1] + 3] = br[-1] + self.V

            else:
                self.macierz[i][2] = None
    def find_next(self,indeks):
        return self.macierz[indeks][0]
    def connection(self,poprzednik,nastepnik):
        return self.macierz[poprzednik][0]==nastepnik and self.macierz[nastepnik][1]==poprzednik
    def find_all_next(self,poprzednik):
        result=[]
        indeks=0
        if self.macierz[poprzednik][indeks]:

            while self.macierz[poprzednik][indeks]!=indeks-3:
                result.append(self.macierz[poprzednik][indeks])
                indeks=self.macierz[poprzednik][indeks]+3

        return result
    def find_all_next_recalculated(self,poprzednik):
        result=[]
        indeks=0
        if self.macierz[poprzednik][indeks]:

            while self.macierz[poprzednik][indeks]!=indeks-2:
                result.append(self.macierz[poprzednik][indeks])
                indeks=self.macierz[poprzednik][indeks]+2

        return result
    def recalculate(self):
        for i in range(self.V):
            for j in range(self.V+3):
                if self.macierz[i][j]!=None:
                    if self.macierz[i][j]=="-0":
                        self.macierz[i][j]=-1
                    elif self.macierz[i][j]>=0:
                        self.macierz[i][j]+=1
                    else:
                        self.macierz[i][j]-=1
                else:
                    self.macierz[i][j]=0
        self.macierz.append([])
        for i in range(self.V,0,-1):
            self.macierz[i]=self.macierz[i-1]
        self.macierz[0]="pusty wiersz"
    def poprzednicy_recalculated(self):
        result=[]
        for i in range(self.V+1):
            result.append(0)
        for i in range(1,self.V+1):
            for j in self.find_all_next_recalculated(i):
                result[j]+=1
        return result
    def BFS_sort_recalculated(self):
        unsorted=self.V
        result=[]
        poprz=self.poprzednicy_recalculated()
        while unsorted!=0:
            for i in range(1,len(poprz)):
                if poprz[i]==0 and i not in result:
                    result.append(i)
                    unsorted-=1
                    for j in self.find_all_next_recalculated(i):
                        poprz[j]-=1
        return result
    def DFS_sort_recalculated(self):
        def DFS(i):
            visited[i]=True
            for j in self.find_all_next_recalculated(i):
                if not visited[j]:
                    DFS(j)

        visited=[]
        for i in range(self.V+1):
            visited.append(False)
        result=[]
        for i in range(1,self.V+1):
            if  not visited[i]:
                DFS(i)
            result.append(i)
        return result

def time_measure(starting_value,interval):
    result_DFS=[]
    result_BFS=[]
    for i in range(3):
        result_DFS.append([])
        result_BFS.append([])

    test2 = lista_nastepnikow()
    for i in range(starting_value,starting_value+9*interval+1,interval):
        test0 = macierz_sasiedztwa(i)
        test3=macierz_grafu(i)
        test0.fill()
        test2.fill(test0)
        test3.fill(test0)
        start=time.time()
        test0.DFS_sort()
        end=time.time()
        result_DFS[0].append(end-start)
        start = time.time()
        test2.DFS_sort()
        end = time.time()
        result_DFS[1].append(end - start)
        start = time.time()
        test3.DFS_sort()
        end = time.time()
        result_DFS[2].append(end - start)
        start=time.time()
        test0.BFS_sort()
        end=time.time()
        result_BFS[0].append(end-start)
        start = time.time()
        test2.BFS_sort()
        end = time.time()
        result_BFS[1].append(end - start)
        start = time.time()
        test3.BFS_sort()
        end = time.time()
        result_BFS[2].append(end - start)
    return "DFS macierz: "+str(result_DFS[0])+"\nDFS lista: "+str(result_DFS[1])+"\nDFS macierz grafu: "+str(result_DFS[2])+"\nBFS macierz: "+str(result_BFS[0])+"\nBFS lista: "+str(result_BFS[1])+"\nBFS macierz grafu: "+str(result_BFS[2])
def time_measure_tabela(starting_value,interval):
    result_DFS=[]
    result_BFS=[]
    test1 = tabela_krawedzi()
    for i in range(starting_value,starting_value+9*interval+1,interval):
        test0 = macierz_sasiedztwa(i)
        test0.fill()
        test1.fill(test0)
        start = time.time()
        test1.DFS_sort()
        end = time.time()
        result_DFS.append(end - start)
        start = time.time()
        test1.BFS_sort()
        end = time.time()
        result_BFS.append(end - start)
    return "DFS tabela:"+str(result_DFS)+"\nBFS tabela: "+str(result_BFS)
test_macierz=macierz_sasiedztwa(10)
test_macierz.fill()
"""test_macierz.set_connection(0,1)
test_macierz.set_connection(0,4)
test_macierz.set_connection(1,2)
test_macierz.set_connection(3,0)
test_macierz.set_connection(3,2)
test_macierz.set_connection(4,3)"""
print (test_macierz.find_next(1))
print(test_macierz.find_all_next(1))
print(test_macierz.connection(1, 3))
print(test_macierz.E == test_macierz.default_E)
print(test_macierz)
print(test_macierz.DFS_sort())
print(test_macierz.BFS_sort())
test_tabela=tabela_krawedzi()
test_tabela.fill(test_macierz)
print(test_tabela)
print(test_tabela.DFS_sort())
print(test_tabela.BFS_sort())

print(test_tabela.find_next(1))
print(test_tabela.find_all_next(1))
print(test_tabela.connection(1,3))
test_lista=lista_nastepnikow()
test_lista.fill(test_macierz)
print(test_lista)
print(test_lista.DFS_sort())
print(test_lista.BFS_sort())

print(test_lista.find_next(1))
print(test_lista.find_all_next(1))
print(test_lista.connection(1,3))
test=lista_nastepnikow()
test.set_connection(0,1)
test.set_connection(1,2)
test.set_connection(0,3)
test.set_connection(3,0)
print(test.find_all_next(3))
test.delete_connection(0,1)
test.delete_connection(0,3)

print(test)
print(time_measure(50,50))
print(time_measure_tabela(10,10))
testpoprz=lista_poprzednikow()
testpoprz.fill(test_macierz)
testbrak=lista_braku()
testbrak.fill(test_macierz)
testgraf=macierz_grafu(10)
testgraf.fill(test_macierz)
print(testgraf)
testgraf.recalculate()
print(testgraf)
print(testgraf.find_all_next_recalculated(2))

print(testgraf.DFS_sort_recalculated())
print(testgraf.BFS_sort_recalculated())


