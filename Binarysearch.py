def Binarysearch(a,x,n,l):
    if n>=1:
        mid=l+(n-l)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            return Binarysearch(a,x,mid-1,l)
        else:
            return Binarysearch(a,x,n,mid+1)
    return -1
a=list(map(int,input("Enter the numbers : ").split(",")))
x=int(input("Enter the number to be searched : "))
for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
print("The sorted array is ",a)
res=Binarysearch(a,x,len(a)-1,0)
if res==-1:
    print("The Element is not found")
else:
    print("The element is present in the index ",res)
