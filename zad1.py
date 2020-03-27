import random
import time
import sys
sys.setrecursionlimit(50000)


def create_random_data(length):
    data=[]
    for i in range(length):
        data.append(random.randint(1,20))
    return data
def create_rosnacy_ciag(length):
    data=[]
    data.append(random.randint(1,100000))
    for i in range(length-1):
        data.append(data[-1]+random.randint(1,5))
    return data
def create_malejacy_ciag(length):
    data=[]
    data.append(random.randint(1,1000000))
    for i in range(length-1):
        data.append(data[-1]-random.randint(1,5))
    return data
def create_ciag_A_ksztaltny(length):
    data = []
    data.append(random.randint(1, 1000000))
    for i in range(length//2-1):
        data.append(data[-1] + random.randint(1, 5))
    for i in range(length-length//2):
        data.append(data[-1]-random.randint(1,5))
    return data
def create_ciag_staly(length):
    data=[]
    data.append(random.randint(1,1000000))
    for i in range(length-1):
        data.append(data[-1])
    return data

def selection(data):
    for a in range(len(data) - 1):
        record_place = a
        for b in range(a, len(data)):
            if data[b]<data[record_place]:
                record_place=b
        data[a], data[record_place]= data[record_place], data[a]
    return data

def insertion(data):
    for a in range(1,len(data)):
        element=data[a]
        for b in range(a-1,-1,-1):
            if data[b]>element:
                data[b+1]=data[b]
                data[b]=element
            else:
                break
    return data

def shell(data):
    h=1
    n=len(data)
    while h<n:
        h=3*h+1
    h=h//9
    if h==0:
        h=1
    while h>0:
        for a in range(h,n,h):
            element=data[a]
            for b in range(a-h,-1,-h):
                if data[b]>element:
                    data[b + h] = data[b]
                    data[b] = element
                else:
                    break
        h=h//3
    return data

def quick_recursive(data, key, l, r):
    finished=False
    if len(data[l:r+1])>1:
        if key=="random":
            x = random.choice(data[l:r + 1])
        elif key=="right":
            x=data[r]
        i = l
        j = r
        while not finished:

            while data[i]<x and i<r:
                i+=1
            while data[j]>x and j>l:
                j-=1
            if i<j:
                data[i],data[j]=data[j],data[i]
                i+=1
                j-=1
            elif i == j:
                quick_recursive(data, key ,l, i - 1)
                quick_recursive(data, key ,i + 1, r)
                finished=True
            elif i > j:
                quick_recursive(data, key ,l, j)
                quick_recursive(data, key ,i, r)
                finished=True
    return data
def quick(data,key):
    quick_recursive(data, key, 0, len(data) - 1)
    return data

def buildheap(data,i,heap_length):
    while True:
        k = i
        if (2 * k < heap_length and data[2 * k] > data[i]):
            i = 2 * k
        if 2 * k + 1 < heap_length and data[2 * k + 1] > data[i]:
            i = 2 * k + 1
        data[k], data[i] = data[i], data[k]
        if i == k:
            break
def heap(data):
    build=0
    data.insert(0, "empty")
    for i in range(len(data)//2,0,-1):
        buildheap(data,i,len(data))
    for x in range(len(data)-1, 1, -1):
        data[1],data[x]=data[x],data[1]
        build += 1
        buildheap(data,1,len(data)-build)
    data.remove("empty")
    return data

test=create_random_data(10)
selection_test=test[:]
insertion_test=test[:]
shell_test=test[:]
quick_test_random_key=test[:]
quick_test_right_key=test[:]
heap_test=test[:]
print(test)
#selection(selection_test)
#insertion(insertion_test)
#shell(shell_test)
quick(quick_test_random_key,"random")
quick(quick_test_right_key, "right")
#heap(heap_test)
print(sorted(test)==quick_test_random_key==quick_test_right_key)
def time_measure(sort_function,create_function,starting_value,interval):
    array=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):
        x=create_function(i)
        start=time.time()
        sort_function(x)
        end=time.time()
        result=end-start
        array.append(result)
    return array

def time_measure_quick_sort(sort_function,quick_key,create_function,starting_value,interval):
    array=[]
    for i in range(starting_value,starting_value+9*interval+1,interval):
        x=create_function(i)
        start=time.time()
        sort_function(x,quick_key)
        end=time.time()
        result=end-start
        array.append(result)
    return array


time_time=time_measure_quick_sort(quick,"random",create_ciag_staly,100,100)
print(time_time)