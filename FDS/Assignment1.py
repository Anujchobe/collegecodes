# Write a Python program to store marks scored in subject “Fundamental of Data
# Structure” by N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency


def getmarks(mrklist):
    n=int(input("Enter total number of students"))

    #input
    for i in range(n):
        mrk=(input("Enter marks obtained or 'ab' if student is absent"))
        if mrk!="ab":
            mrklist.append(int(mrk))
        else:
            mrklist.append(mrk)    

#average
def avg(mrklist):
    sum=0
    ctr=0
    for mk in mrklist:
        if mk!="ab":
            sum+=mk
            ctr=ctr+1
    print(f"Average score of class = {sum/ctr}")  

#highest and lowest score
def highlow(mrklist):
    min=0
    max=0
    ct=0
    for i in mrklist:        
        if i!="ab":
            if ct==0 :
                min=i
                ct+=1
            if min>i:
                min=i
            if max<i:
                max=i    
    print(f"Highest score of class = {max} and Lowest score of class= {min}")        

#absent
def absent(mrklist):
    ab=0
    for i in mrklist:
        if i=="ab":
            ab+=1
    print(f"Number of students that were absent = {ab}")

#Frequency
def frequency(mrklist):
    freq={}
    mfreq=0
    for i in mrklist:
        if i !="ab":
            if i!=freq.keys():
                freq[i]=1
            else:
                freq[i]+=1

    for i in freq:
        if mfreq<freq[i]:
                mfreq=freq[i]        
    key=list(freq.keys()) 
    val=list(freq.values())                     
    pos=val.index(mfreq)
    print("Marks with highest Frequency = ",key[pos])

def main():
    mrklist=[]
    while True:
        print("Enter '1' for entering marks")
        print("Enter '2' to display average marks")
        print("Enter '3' to diaplay highest and lowest marks ")
        print("Enter '4' to display number of absent students")
        print("Enter '5' to display marks with highest frequency")
        print("Enter '6' to STOP")
        ch=int(input("Enter your choice here: "))
        if ch==1:
            getmarks(mrklist)
        if ch==2:
            avg(mrklist)    
        if ch==3:
            highlow(mrklist)
        if ch==4:
            absent(mrklist)    
        if ch==5:
            frequency(mrklist)
        if ch==6:
            print("Thank You!")
            break
main()        