# Write a Python program to store marks scored in subject “Fundamental of Data
# Structure” by N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

mrklist=[]

n=int(input("Enter total number of students"))

#input
for i in range(n):
    mrk=(input("Enter marks obtained or 'ab' if student is absent"))
    if mrk!="ab":
        mrklist.append(int(mrk))
    else:
        mrklist.append(mrk)    

#average
sum=0
ctr=0
for mk in mrklist:
    if mk!="ab":
        sum+=mk
        ctr=ctr+1
print(f"Average score of class = {sum/ctr}")  

#highest and lowest score
ab=0
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
    else:
        ab+=1
print(f"Highest score of class = {max} and Lowest score of class= {min}")        
print(f"Number of students that were absent = {ab}")

#Frequency
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


