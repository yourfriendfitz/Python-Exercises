#Function that duplicates an Array into a new array

arr1 = [1,2,3,4,5]

def cloning(n):
    arr2 =[]
    for i in n:
        arr2.append(i)
    arr2 += n
    return arr2

print(cloning(arr1))