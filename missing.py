#Function to determine which Number 0-9 is Missing? 
#Numbers 0 & 9 are not functional. 
#Entering all numbers is not functional. 

array = [0,1,2,3,4,5,7,8,9]

def missing(n):
    for i in range(0, len(n)-1):
        if n[i] != n[i+1] - 1:
           print(i +1, " seems to be missing")

print(missing(array))