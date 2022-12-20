# Write a python program to store roll numbers of student array who attended training
# program in sorted order. Write function for searching whether particular student
# attended training program or not, using Binary search and Fibonacci search

def binary(lst):
    print(lst)
    num=int(input("Enter roll number to find: "))
    f=0
    l=len(lst)-1
    check=False
    while f<=l:
        m= (f+l)//2
        if int(lst[m])==int(num):
            check=True
            break
        elif int(lst[m])<int(num):
            f=m+1
        else:
            l=m-1
    if check:
        print("Roll number found at position: ",m+1)
    else:
        print("Roll number not found")


def fibb(lst):
    print(lst)
    x=int(input("Enter roll number to search: "))
    fib2=0
    fib1=1
    fib=fib1+fib1
    n=len(lst)
    offset=-1

    while (fib<n):
        fib2=fib1 
        fib1=fib
        fib=fib1+fib2   
    
    while(fib>1):
        i=min(offset+fib2,n-1)
    
        if int(lst[i])<x:
            fib=fib1
            fib1=fib2
            fib2=fib-fib1
            offset=i
    
        elif int(lst[i])>x:
            fib=fib2
            fib1=fib1-fib2
            fib2=fib-fib1
    
        elif int(lst[i])==x:
            print("Roll number found at position: ",i+1)
            break
    else:
        print("Roll number not found! ")



def main():
    lst=[]
    while True:
        print("Enter 1 to store roll numbers")
        print("Enter 2 to search roll number using binary search")
        print("Enter 3 to search roll number using fibinacci search")
        print("Enter 4 to STOP")
        ch=int(input("Enter your choice here: "))
        roll=-1
        if ch==1:
            while roll!="":            
                roll=input("Enter roll numbers | enter blank space if done: ")
                if roll!="":
                    lst.append(roll)
        for i in range(len(lst)):
            for j in range(len(lst)):
                if int(lst[j])>int(lst[i]):
                    temp=lst[j]
                    lst[j]=lst[i]
                    lst[i]=temp    
        if ch==2:
            binary(lst)
        if ch==3:
            fibb(lst)
        if ch==4:
            print("THANK YOU")
            break    
main()