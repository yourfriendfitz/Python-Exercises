#Function to determine which Item in the Array is the largest

original = [4,6,7,99,21,11,4,2,9]

def large(n):
    max = n[0]
    for i in range(0, len(n)):
        if n[i] > max:
            max = n[i]
    return max
    
print(large(original))