#Function to determind which Item in the Array is the Smallest?

original = [4,6,7,99,21,11,4,2,9]

def small(n):
    min = n[0]
    for i in range(0, len(n)):
        if n[i] < min:
            min = n[i]
    return min
    
print(small(original))
