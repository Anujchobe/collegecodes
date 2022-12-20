# Write a python program to store roll numbers of student in array who attended
# training program in random order. Write function for searching whether particular
# student attended training program or not, using Linear search and Sentinel search. 

def linear(lst):
    print(lst)
    cnt=0
    r=input("Enter Roll number to search: ")
    for i in lst:
        if i==r:
            cnt+=1
            pos=lst.index(i)+1
    if cnt!=0:
        print("Roll number found at position: ",pos)
    else:
        print("Roll number not found")

def senti(lst):
    print("")
    r=input("Enter Roll number to search: ")
    last=lst[len(lst)-1]
    lst[-1]=r
    i=0
    while lst[i]!=r:
            i+=1
    lst[-1]=last
    if (i<len(lst)-1 or lst[-1]==r):
        print("Roll number found at position: ",i+1)
    else:    
        print("Roll number not found! ")

def main():
    lst=[]
    while True:
        print("Enter 1 to store roll number students")
        print("Enter 2 to search using linear search")
        print("Enter 3 to search using sentinel search")
        print("Enter 4 to STOP")
        ch=int(input("Enter you choice here: "))
        if ch==1:
            roll=None
            while roll!="":
                print("")
                roll=input("Enter roll number of students | Press blank enter if done: ")                
                lst.append(roll)                
        if ch==2:
            linear(lst)
        if ch==3:
            senti(lst)
        if ch==4:
            print("THANK YOU")
            break
main()