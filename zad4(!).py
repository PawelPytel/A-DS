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
        zeros = 0
        helper = []
        for i in range(self.V):
            for j in range(i + 1, self.V):
                helper.append([i, j])
        for i in range(self.V - 1):
            row = i
            col = random.randrange(i + 1, self.V)
            self.macierz[row][col] = 1
            ones -= 1
            position = 0
            for i in range(row):
                position += self.V - 1 - i
            position += col - row - 1 - zeros
            del helper[position]
            zeros += 1
        while ones != 0:
            coordinates = random.choice(helper)
            row = coordinates[0]
            col = coordinates[1]
            self.macierz[row][col] = 1
            position = 0
            for i in range(coordinates[0]):
                position += self.V - 1 - i
            position += col - row - 1 - zeros
            del helper[position]
            ones -= 1
            zeros += 1
        self.E = self.default_E
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
    def fill_hamilton(self):
        self.clean()
        self.fill_euler(50)
        change=random.randrange(self.V)
        for i in range(self.V):
            self.macierz[i][change]=0
            self.macierz[change][i]=0
        connected=random.randrange(self.V)
        while connected==change:
            connected = random.randrange(self.V)
        self.macierz[change][connected]=1
        self.macierz[connected][change]=1
    def fill_euler(self,procenty):
        self.clean()
        begin=random.randrange(self.V)
        count=self.V*(self.V-1)*(procenty/100)//2
        self.E=count
        visited=[]
        visited2=[]
        for i in range(self.V):
            visited.append(i)
        visited.remove(begin)
        visited2.append(begin)
        previous = random.choice(visited)
        self.set_connection(begin,previous)
        self.set_connection(previous,begin)
        visited.remove(previous)
        visited2.append(previous)
        count-=1
        while visited!=[]:
            next=random.choice(visited)
            self.set_connection(previous, next)
            self.set_connection(next, previous)
            visited.remove(next)
            visited2.append(next)
            previous=next
            count-=1
        self.set_connection(previous,begin)
        self.set_connection(begin,previous)
        count-=1
        while count>0:
            a=random.randrange(self.V)
            b=random.randrange(self.V)
            c=random.randrange(self.V)
            while c == a or c == b or a==b or self.connection(a,b)or self.connection(b, c) or self.connection(c, a):
                a = random.randrange(self.V)
                b = random.randrange(self.V)
                c = random.randrange(self.V)
            self.set_connection(a,b)
            self.set_connection(b,a)
            self.set_connection(a,c)
            self.set_connection(c,a)
            self.set_connection(b,c)
            self.set_connection(c,b)
            count-=3
        """while count>0:
            a=random.randrange(self.V)
            b=self.V%(a+self.V//3)
            while b==a or self.connection(a,b):
                b=random.randrange(self.V)
            c=self.V%(b+self.V//3)
            while c==a or c==b or self.connection(b,c) or self.connection(c,a):
                c=random.randrange(self.V)
            self.set_connection(visited2[a],visited2[b])
            self.set_connection(visited2[b],visited2[a])
            self.set_connection(visited2[a],visited2[c])
            self.set_connection(visited2[c],visited2[a])
            self.set_connection(visited2[b],visited2[c])
            self.set_connection(visited2[c],visited2[b])
            count-=3"""



    def Euler(self):
        def euler_helper(i):
            nast=self.find_all_next(i)
            for j in nast:
                if self.connection(i,j):
                    self.macierz[i][j] = 0
                    self.macierz[j][i] = 0
                    euler_helper(j)
            sol.append(i)
        sol=[]
        euler_helper(0)
        return sol
    def Hamilton(self):
        start=time.time()
        def hamilton_helper(i):
            end=time.time()
            if end-start>1:             #tutaj ta jedynke mozna zmienic na maksymalny czas szukania cyklu
                return
            visited[i] = True
            sol.append(i)


            for j in self.find_all_next(i):
                if not visited[j]:
                    hamilton_helper(j)
            if len(sol) == self.V and self.connection(sol[-1],sol[0]):

                    return
            else:
                visited[i]=False
                sol.remove(sol[-1])
        sol=[]
        visited=[]
        for i in range(self.V):
            visited.append(False)
        hamilton_helper(0)
        return sol




test=macierz_sasiedztwa(200)
test.fill_euler(70)
start=time.time()
print(test)
print(test.Hamilton())
end=time.time()
print(end-start)
#print(test)
start=time.time()
print(test.Euler())
end=time.time()
print(end-start)




#print(test)
"""test2=macierz_sasiedztwa(6)
test2.set_connection(0,1)
test2.set_connection(1,0)
test2.set_connection(1,2)
test2.set_connection(2,1)
test2.set_connection(2,3)
test2.set_connection(3,2)
test2.set_connection(3,4)
test2.set_connection(4,3)
test2.set_connection(3,5)
test2.set_connection(5,3)
test2.set_connection(1,5)
test2.set_connection(5,1)
test2.set_connection(1,3)
test2.set_connection(3,1)
test2.set_connection(0,2)
test2.set_connection(2,0)
test2.set_connection(0,5)
test2.set_connection(5,0)"""
#print(test2.Hamilton())
#test3=macierz_sasiedztwa(10)
#test3.fill_hamilton()
#print(test3.Hamilton())

def time_measure_euler_30(starting_value,interval):
    result=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):
        test = macierz_sasiedztwa(i)
        test.fill_euler(30)
        start=time.time()
        test.Euler()
        end=time.time()
        result.append(end-start)
    return result
def time_measure_euler_70(starting_value,interval):
    result=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):
        test = macierz_sasiedztwa(i)
        test.fill_euler(70)
        start=time.time()
        test.Euler()
        end=time.time()
        result.append(end-start)
    return result
def time_measure_hamilton_30(starting_value,interval):
    result=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):

        test = macierz_sasiedztwa(i)
        test.fill_euler(30)
        start=time.time()
        test.Hamilton()
        end=time.time()
        result.append(end-start)
    return result
def time_measure_hamilton_70(starting_value,interval):
    result=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):
        test = macierz_sasiedztwa(i)
        test.fill_euler(70)
        start=time.time()
        test.Hamilton()
        end=time.time()
        result.append(end-start)
    return result
def time_measure_no_hamilton(starting_value,interval):
    result=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):
        test = macierz_sasiedztwa(i)
        test.fill_hamilton()
        start=time.time()
        test.Hamilton()
        end=time.time()
        result.append(end-start)
    return result
#print(time_measure_euler_30(40,10))
#print(time_measure_euler_70(50,10))
#print(time_measure_hamilton_30(40,10))
#print(time_measure_hamilton_70(40,10))
#print(time_measure_no_hamilton(10,2)) #to jest ten wariant ze na pewno nie ma cyklu


