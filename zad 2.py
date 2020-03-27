import random
import time
import sys
sys.setrecursionlimit(50000)


class Element:
    def __init__(self,first_data):
        self.data=first_data
        self.next=None
    def getData(self):
        return self.data
    def setData(self,new_data):
        self.data=new_data
    def setNext(self,new_next):
        self.next=new_next
    def getNext(self):
        return self.next
class Lista:
    def __init__(self):
        self.head=None

    def __str__(self):
        current = self.head
        result = []
        while current != None:
            result.append(current.getData())
            current = current.getNext()
        result=str(result)
        return result
    def isEmpty(self):
        return self.head==None
    def size(self):
        count=0
        temp=self.head
        while temp!=None:
            count+=1
            temp=temp.getNext()
        return count
    def search(self,data):
        temp=self.head
        found=False
        while not found and temp!=None:
            if temp.getData()==data:
                found=True
            else:
                temp=temp.getNext()
        return found
    def remove_list(self):
        if self.head!=None:
            removed=self.head
            newfirst=removed.getNext()
            while self.head!=None:
                self.head=removed.getNext()
                removed=newfirst
                if removed!=None:
                    newfirst=removed.getNext()


    def add(self,data):
        if self.head==None:
            temp=Element(data)
            self.head=temp
        else:
            previous=None
            current=self.head
            while current!=None:
                if data>current.getData():
                    previous=current
                    current=current.getNext()
                else:
                    break
            if previous != None:
                temp = Element(data)
                temp.setNext(current)
                previous.setNext(temp)

            else:
                temp=Element(data)
                temp.setNext(current)
                self.head=temp

    def remove(self,data):
        previous=None
        current=self.head
        while current!=None and current.getData()!=data:
            previous=current
            current=current.getNext()
        if current.getData()==data:
            if previous==None:
                self.head=current.getNext()
                current.setNext(None)
            else:
                previous.setNext(current.getNext())
                current.setNext(None)

test=Lista()
test.add(13)
test.add(2)

test.add(6)
test.add(1)
test.add(17)
test.add(14)
test.add(12)
test.add(22)

test.remove_list()
print(test.size())
print(test)


class Elementdrzewa:
    def __init__(self,first_data):
        self.data=first_data
        self.left=None
        self.right=None
        self.father=None
        self.height=-1
    def is_leaf(self):
        return (self.height==0)
    def balance(self):
        bal=0
        if self.left:
            bal+=(self.left.height+1)
        if self.right:
            bal-=(self.right.height+1)
        return bal
    def max_height(self):
        if self.left and self.right:
            return (max(self.left.height,self.right.height)+1)
        if self.left and not self.right:
            return (self.left.height+1)
        if self.right and not self.left:
            return self.right.height + 1
        if not self.right and not self.left:
            return 0

class Drzewo:
    def __init__(self):
        self.root=None
    def isEmpty(self):
        return self.root==None
    def add(self,value):
        temp=Elementdrzewa(value)
        if self.root==None:
            self.root=temp
            self.repair_height(temp)
        else:
            previous=None
            current=self.root
            while current:
                if value>current.data:
                    previous=current
                    current=current.right
                else:
                    previous=current
                    current=current.left
            if value>previous.data:
                previous.right=temp
            else:
                previous.left=temp
            temp.father = previous
            self.repair_height(temp)
            while temp:
                self.rebalance(temp)
                temp=temp.father
    def check_balance(self,temp):
        if temp:
            if temp.balance()>1 or temp.balance()<-1:
                return False
            else:
                self.check_balance(temp.right)
                self.check_balance(temp.left)
        return True

    def rebalance(self,elem):
        if elem.balance() < -1:
                if elem.right.balance()<0:
                    B=elem
                    A=elem.right
                    D_exists=False
                    D=None
                    if elem.right.left:
                        D=elem.right.left
                        D_exists=True
                    if elem.father:
                        F=elem.father
                        if B==F.right:
                            F.right=A
                            A.father=F
                        elif B==F.left:
                            F.left=A
                            A.father=F


                    else:
                        self.root=A
                        A.father=None
                    A.left=B
                    B.father=A
                    if D_exists:
                        B.right=D
                        D.father=B
                    else:
                        B.right=None
                    self.repair_height(B)
                    self.repair_height(A)
                elif elem.right.balance()>0:
                    E=None
                    G=None
                    G_exists=False
                    E_exists=False
                    C=elem
                    B=elem.right
                    A=B.left
                    if A.left:
                        E=A.left
                        E_exists=True
                    if A.right:
                        G=A.right
                        G_exists=True
                    if elem.father:
                        F=elem.father
                        if C==F.right:
                            F.right=A
                            A.father=F
                        elif C==F.left:
                            F.left=A
                            A.father=F
                    else:
                        self.root=A
                        A.father=None
                    A.right=B
                    B.father=A
                    A.left=C
                    C.father=A
                    if E_exists:
                        C.right=E
                        E.father=C
                    else:
                        C.right=None
                    if G_exists:
                        B.left=G
                        G.father=B
                    else:
                        B.left=None
                    self.repair_height(C)
                    self.repair_height(B)
                    self.repair_height(A)

        elif elem.balance()>1:
            if elem.left.balance() > 0:
                D_exists = False
                D = None
                B = elem
                A = elem.left
                if elem.left.right:
                    D = elem.left.right
                    D_exists = True
                if elem.father:
                    F = elem.father
                    if B == F.right:
                        F.right = A
                        A.father = F
                    elif B == F.left:
                        F.left = A
                        A.father = F


                else:
                    self.root = A
                    A.father = None
                A.right = B
                B.father = A
                if D_exists:
                    B.left = D
                    D.father = B
                else:
                    B.left = None
                self.repair_height(A)
                self.repair_height(B)
            elif elem.left.balance() < 0:
                E = None
                G = None
                G_exists = False
                E_exists = False
                C = elem
                B = elem.left
                A = B.right
                if A.right:
                    E = A.right
                    E_exists = True
                if A.left:
                    G = A.left
                    G_exists = True
                if elem.father:
                    F = elem.father
                    if C == F.right:
                        F.right = A
                        A.father = F
                    elif C == F.left:
                        F.left = A
                        A.father = F
                else:
                    self.root = A
                    A.father = None
                A.left = B
                B.father = A
                A.right = C
                C.father = A
                if E_exists:
                    C.left = E
                    E.father = C
                else:
                    C.left = None
                if G_exists:
                    B.right = G
                    G.father = B
                else:
                    B.right = None
                self.repair_height(C)
                self.repair_height(B)
                self.repair_height(A)
    def repair_height(self,elem):
        changed=True
        while elem and changed:
            old=elem.height
            elem.height=elem.max_height()
            elem = elem.father
            if elem:
                if old == elem.height:
                    changed = False
    def inorder(self,elem, result=None):
        if elem==None:
            return"Tree is empty"
        else:
            if result is None:
                result = []
            if elem.left:
                self.inorder(elem.left,result)
            result.append(elem.data)
            if elem.right:
                self.inorder(elem.right,result)
            return result
    def preorder(self,elem, result=None):
        if elem==None:
            return"Tree is empty"
        if result is None:
            result = []
        result.append(elem.data)
        if elem.left:
            self.preorder(elem.left,result)
        if elem.right:
            self.preorder(elem.right,result)
        return result
    def postorder_delete(self,elem):
        if elem==None:
            return"Tree is empty"
        if elem.left:
            self.postorder_delete(elem.left,)
        if elem.right:
            self.postorder_delete(elem.right)
        if elem.father:
            if elem.father.left is elem:
                elem.father.left = None
            elif elem.father.right is elem:
                elem.father.right = None
        else:
            self.root = None
        del elem

    def remove(self,value):
        if self.root==None:
            return "Tree is empty"
        else:
            current=self.root
            while current:
                if value>current.data:
                    current=current.right
                elif value<current.data:
                    current=current.left
                else:
                    if current.is_leaf():
                        if current.father:
                            if current.father.left is current:
                                current.father.left=None
                            elif current.father.right is current:
                                current.father.right=None
                        else:
                            self.root=None
                        temp=current
                        self.repair_height(temp)
                        while temp:
                            self.rebalance(temp)
                            temp=temp.father
                        del current


                    elif current.left and not current.right:
                        if current.father:
                            if current.father.left is current:
                                current.father.left=current.left
                                current.left.father=current.father
                            elif current.father.right is current:
                                current.father.right=current.left
                                current.left.father=current.father
                        else:
                            self.root=current.left
                            current.left.father=None
                        temp=current
                        self.repair_height(temp)
                        while temp:
                            self.rebalance(temp)
                            temp=temp.father
                        del current
                    elif not current.left and  current.right:
                        if current.father:
                            if current.father.left is current:
                                current.father.left=current.right
                                current.right.father=current.father
                                current.father = None
                            elif current.father.right is current:
                                current.father.right=current.right
                                current.right.father=current.father

                        else:
                            self.root=current.right
                            current.right.father=None
                        temp=current
                        self.repair_height(temp)
                        while temp:
                            self.rebalance(temp)
                            temp = temp.father
                        del current
                    elif current.left and current.right:
                        temp=current.right
                        while temp.left:
                            temp=temp.left


                        if temp is current.right:
                            temp_to_repair = temp
                            if current.father:
                                if current.father.left is current:
                                    current.father.left = temp
                                    temp.father.left=None
                                    temp.father = current.father
                                elif current.father.right is current:
                                    current.father.right = temp
                                    temp.father.left=None
                                    temp.father = current.father
                            else:
                                self.root = temp
                                temp.father = None
                            temp.left=current.left
                            current.left.father=current.left
                        else:
                            temp_to_repair = temp.father
                            if current.father:
                                if current.father.left is current:
                                    current.father.left=temp
                                    temp.father.left=None
                                    temp.father = current.father
                                elif current.father.right is current:
                                    current.father.right=temp
                                    temp.father.left=None
                                    temp.father = current.father
                            else:
                                self.root = temp
                                temp.father.left = None
                                temp.father = None
                            temp.right=current.right
                            temp.left=current.left
                            current.right.father=temp
                            current.left.father=temp
                        del current
                        self.repair_height(temp_to_repair)


                        while temp_to_repair:
                            self.rebalance(temp_to_repair)
                            temp_to_repair = temp_to_repair.father
                    break
            else:
                print("Can't find an element")


    def search (self,value):
        if self.root==None:
            return "Tree is empty"
        else:
            path=[]
            current=self.root
            while current:
                if value>current.data:
                    path.append(current.data)
                    current=current.right
                elif value<current.data:
                    path.append(current.data)
                    current=current.left
                else:
                    path.append(current.data)
                    return path
            else:
                return False
    def tree_height(self):
        if self.root:
            return self.root.height
        else:
            return "Tree is empty"

tree=Drzewo()
tree.add(5)
tree.add(10)
tree.add(9)
tree.add(8)
tree.add(7)
#tree.postorder_delete(tree.root)
empty_tree=Drzewo()
print(tree.preorder(tree.root))
print(tree.check_balance(tree.root))
print(tree.tree_height())
print(tree.search(8))

def unique_random_data(length):
    data=[]
    data.append(random.randint(1,100000))
    for i in range(length-1):
        data.append(data[-1]+random.randint(1,5))
    unique=[]
    while data!=[]:
        temp=random.choice(data)
        data.remove(temp)
        unique.append(temp)
    return unique

def time_measure_list(starting_value,interval):
    result=[]
    for c in range(3):
        result.append([])
    lista=Lista()
    for i in range(starting_value,starting_value+9*interval+1,interval):
        x=unique_random_data(i)
        '''start=time.time()
        for a in x:
            lista.add(a)
        end=time.time()
        res=end-start
        result[0].append(res)
        start=time.time()
        for b in range(len(x)//10):
            val=random.choice(x)
            lista.search(val)
        end=time.time()
        res=end-start
        result[1].append(res)'''
        start=time.time()
        lista.remove_list()
        end=time.time()
        res=end-start
        result[2].append(res)
    return result
print(time_measure_list(5000,5000))
def time_measure_tree(starting_value,interval):
    result=[]
    for c in range(3):
        result.append([])
    drzewo=Drzewo()
    for i in range(starting_value,starting_value+9*interval+1,interval):
        x=unique_random_data(i)
        '''start=time.time()
        for a in x:
            drzewo.add(a)
        end=time.time()
        res=end-start
        result[0].append(res)
        start=time.time()
        for b in range(len(x)//10):
            val=random.choice(x)
            drzewo.search(val)
        end=time.time()
        res=end-start
        result[1].append(res)'''
        start=time.time()
        drzewo.postorder_delete(drzewo.root)
        end=time.time()
        res=end-start
        result[2].append(res)
    return result
print(time_measure_tree(5000,5000))










