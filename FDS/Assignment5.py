# a) Write a python program to store names and mobile numbers of your friends in sorted
# order on names. Search your friend from list using binary search (recursive and nonrecursive). 
# Insert friend if not present in phonebook
# b) Write a python program to store names and mobile numbers of your friends in sorted
# order on names. Search your friend from list using Fibonacci search. Insert friend if not
# present in phonebook.

def binr(lst,e,l,h):
    if l<=h:
        mid=(h+l)//2
        if lst[mid][0]==e:
            return mid
        elif lst[mid]<e:
            binr(lst,e,l,mid-1)
        elif lst[mid]>e:
            binr(lst,e,mid+1,h)
    else:
        return -1

def bini(lst):
    r=input("Enter name to search: ")
    l=0
    h=len(lst)-1
    fnd=False
    while(l<=h):
        mid=(l+h)//2
        if lst[mid][0]==r:
            fnd=True
            break
        elif lst[mid][0]<r:
            l=mid+1
        else:
            h=mid-1
    if fnd:
        print("Name found at position: ",mid+1)
    else:
        inp=input("Name not found|Enter name and roll with " " to store:")
        lst.append(inp.split(" "))
        print("New list: ",lst)



def fibb(lst):
    inp=input("Enter name to search: ")
    n=len(lst)
    f2=0
    f1=1
    f=f1+f2
    offset=-1
    ch=False
    while(f<n):
        f2=f1
        f1=f
        f=f1+f2
    while(f>1):
        i=min(offset+f2,n)
        if lst[i][0]==inp:
            print("Name found at position: ",i+1)
            break
        elif lst[i][0]<inp:
            f=f1
            f1=f2
            f2=f-f1
            offset=i
        elif lst[i][0]>inp:
            f=f2
            f1=f1-f2
            f2=f-f1
    else:
        ind=input("Name not found|Enter name and number with " ": ")
        lst.append(ind.split(" "))
        print("New list: ",lst)


def main():
    while True:
        print("Enter 1 to store names and numbers")
        print("Enter 2 to search/add using binary search(recursive)")
        print("Enter 3 to search/add using binary search(iterative)")
        print("Enter 4 to sraech/add using fibinacci search")
        print("Enter 5 to STOP!")
        ch=int(input("Enter your choice here: "))
        if ch==5:
            print("THANK YOU! ")
            break
        if ch==1:
            ele=None
            lst=[]
            while ele!="":   
                ele=input("Enter name and number with " " in between|Enter blank when done: ")
                if ele!="":
                    lst.append(ele.split(" "))
            print(lst)
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[j][0]>lst[i][0]:
                    temp=lst[j]
                    lst[j]=lst[i]
                    lst[i]=temp
        print(lst)

        if ch==2:
            h=len(lst)-1
            l=0
            e=input("Enter name to search: ")
            ind=binr(lst,e,l,h)
            if ind>-1:
                print("Name found at position: ",ind+1)
            else:
                inp=input("Name not found|Please enter name and number with " "to store: ")
                lst.append(inp.split(" "))
                print("New list: ",lst)
                        
        if ch==3:
            bini(lst)
        if ch==4:
            fibb(lst)
main()
