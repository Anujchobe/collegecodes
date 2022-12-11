# Write a Python program for department library which has N books, write functions for
#following:
# a) Delete the duplicate entries
# b) Display books in ascending order based on cost of books
# c) Count number of books with cost more than 500.
# d) Copy books in a new list which has cost less than 500

def delete(alst):
    dset=[]
    cnt=0
    for i in  range(len(alst)):
        for j in range(len(alst)):              
            if alst[i]==alst[j]:
                cnt+=1
                if cnt>1:
                    alst[i]=0

        cnt=0     
    for k in alst:
        if k==0:
            alst.remove(0)       

    print("Books without duplicate entries: ") 
    print(alst)

def display(blst):
    for i in range (len(blst)):
        for j in range(len(blst)):
            if int(blst[j][1])>int(blst[i][1]) and int(blst[i][1])!=int(blst[j][1]):
                temp=blst[i]
                blst[i]=blst[j]
                blst[j]=temp
    print("Books in ascending order based on cost of books")
    print(blst)   


def cnthigh(clst):
    cnt=0
    for i in clst:
        if int(i[1]) >500:
            cnt+=1
    print("Number of books with cost more than 500: ",cnt)        

def cntlow(dlst):
    lolst=[]
    for i in dlst:
        if int(i[1]) < 500:
            lolst.append(i)
    print("List of books costing less than 500: ")
    print(lolst)

def main():   
    lst=[]
    book=[]
    while True: 
        print("Enter 1 to enter cost of books")
        print("Enter 2 to Delete the duplicate entries")
        print("Enter 3 for Displaying books in ascending order based on cost of books")
        print("Enter 4 to Count number of books with cost more than 500")
        print("Enter 5 to Copy books in a new list which has cost less than 500")
        print("Enter 6 to STOP")
        ch=int(input("Enter choice here: "))
        if ch==1:
            cst=0
            while cst!="":                
                cst=input("Enter name & cost of book OR press blank enter if done: ")   
                if cst!="":
                    book=cst.split(" ")
                    print (book)
                    lst.append(book)
                    print(lst)
        if ch==2:
            delete(lst)
        if ch==3:
            display(lst)
        if ch==4:
            cnthigh(lst)
        if ch==5:
            cntlow(lst)
        if ch==6:
            print("THANK YOU")
            break
main()

