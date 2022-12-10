# Write a Python program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as following: D
# 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
# withdraw and deposit) D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be: 500

bbal=0
def log(loglst):
    ctr=1
    inp=None
    while True:
        inp=input(f"Enter {ctr} transaction in specfied format eg :d 200 | enter '-1' to stop entering log: ")
        ctr+=1
        if inp !="-1":
            loglst.append(inp)
        else:
            break    
    print(loglst)

def dep(oplst):
    global bbal
    bbal+=int(oplst[1])   

def withd(oplst):
    global bbal
    if bbal>=int(oplst[1]):
        bbal-=int(oplst[1])
    else:
        print("Insufficient balance for withdrawal")



def main():
    loglst=[]
    while True:
        print("Enter '1' for log entry")
        print("Enter '2' to display bank balance")
        print("Enter '3' to stop the progam")
        ch= int(input("Enter you choice here: "))
        if ch==1:
            log(loglst)
        if ch==2:
            for i in loglst:
                oplst=i.split(" ")
                if oplst[0]=="w":
                    withd(oplst)
                if oplst[0]=="d":
                    dep(oplst)
                oplst=""
            print("Your final bank balance is = ",bbal)    
        if ch==3:
            print("Thank You")
            break
main()               