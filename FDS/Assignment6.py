# Write a python program to store first year percentage of students in array. Write function
# for sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores

def select(lst):
    for i in range(len(lst)):
        min=i
        for j in range(i+1,len(lst)):
            if lst[min]>lst[j]:
                min=j
        lst[i],lst[min]=lst[min],lst[i]
    print("Sorted listis : ",lst)

def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    print("Sorted list: ",lst)

def top5(lst):
    top=lst
    
    for i in range(len(lst)):
        max=i
        for j in range(i+1,len(lst)):
            if top[max]<top[j]:
                max=j                        
        top[i],top[max]=top[max],top[i]

    print("Top five scores are: ")
    for i in range(5):
        print(top[i])


def main():
    lst=[]
    while True:
        print("Enter 1 to store percentage of students")
        print("Enter 2 to sort using selection sort")
        print("Enter 3 to sort using bubble sort")
        print("Enter 4 to display top five scores")
        print("Enter 5 to STOP!")
        ch=int(input("Enter your choice here: "))
        if ch==1:          
            inp=None  
            while inp!="":                                
                    inp=input("Enter marks to store|Enter blank if done: ")
                    if inp!="":
                        lst.append(inp)
            print(lst)
        if ch==2:
            select(lst)
        if ch==3:
            bubble(lst)
        if ch==4:
            top5(lst)
        if ch==5:
            print("THANK YOU!")
            break
main()