#IN SELECTION SORT THE SMALLER VALUE IS SORTED FIRST
#O(N)2
x=[12,5,89,3,6,74,51,13]
n=len(x)
n
for i in range(n):
    min=i
    for j in range(i+1,n):
        if(x[min]>x[j]):
            min=j
    temp=x[i]
    x[i]=x[min]
    x[min]=temp
print(x)
'----------------------------------------------------------------------'
#BUBBLE SORT THE LARGEST ELEMENT IS SORTED FIRST
#O(N)2
def manu():
    x=[12,54,7,36,87,10,5,4,9]
    print(x)
    n=len(x)
    print(n)
    swap=False
    for i in range(n):
        for j in range (0,n-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
                swap=True
        if(swap==False):
            break
    print(x)
if __name__ =='__main__':
    manu()
'---------------------------------------------------------------------------'
#insrtion sort
#o(n)2
x=[23,1,4,12,7,65]
n=len(x)
for i in range(1,n):
    key=x[i]
    j=i-1
    while(j>=0 and key <x[j]):
        x[j+1]=x[j]
        j-=1
    x[j+1]=key
print(x)
'----------------------------------------------------------------------------'
#QUICK SORT
#o(n log n)
def pivot(arr,l,h):
    p=arr[h]
    i=l-1
    for j in range(l,h):
        if(arr[j]<p):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
def quick(arr,l,h):
    if l<h:
        pi=pivot(arr,l,h)
        quick(arr,l,pi-1)
        quick(arr,pi+1,h)
x=[12,2,56,3,9,34,7]
n=len(x)
quick(x,0,n-1)
print(x)
'--------------------------------------------------------------------------------'
#MERGE SORT
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
'--------------------------------------------------------------------------------'
#lINEAR SEARCHING
#o(n)
x=list(map(int,input().split()))
s=int(input())
n=len(x)
for i in range(n):
    if(x[i]== s):
        a=i
print("this position for {} is {}".format(s,a))
'------------------------------------------------------------------------------------'
#BINARY SEARCHING
#o(log n)
def binary(arr,l,h,s):
    if(l<h):
        mid=l+(h-1)//2
        if(arr[mid]==s):  
            return mid
        elif(arr[mid] > s):
            return binary(arr,l,mid-1,s)
        else:
            return binary(arr,mid+1,h,s)
x=list(map(int,input().split()))
s=3
n=len(x)
result = binary(x,0,n-1,s)
print(result)
'--------------------------------------------------------------------------------------'