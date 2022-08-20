def Linearsearch(a,b,n):
    for i in range(0,n):
        if a[i]==b:
            return i
    return -1            
a=list(map(int,input("Enter the numbers : ").split(",")))
b=int(input("Enter the number to be searched : "))
n=len(a)
if Linearsearch(a,b,n)==-1:
    print("The Element is not found")
else:
    print("The Element is present at the index position :",Linearsearch(a,b,n))
