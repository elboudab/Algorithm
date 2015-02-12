__author__ = 'Zhenxin Lei'

a=[0,2,3,6,8,9]
b=[3,5,7,8,9,10,13]

def merge(a,b):
    i=0
    j=0
    temp=[None]*(len(a)+len(b))
    while (i<len(a)and j<len(b)):
        if (a[i]<b[j]):
            temp[i+j]=a[i]
            i+=1
        else:
            temp[i+j]=b[j]
            j+=1
    while(i>=len(a) and j<len(b)):
        temp[i+j]=b[j]
        j+=1
    while j>=len(b) and i<len(a):
        temp[i+j]=a[i]
        i+=1
    return temp

temp=merge(a,b)
print(temp)


