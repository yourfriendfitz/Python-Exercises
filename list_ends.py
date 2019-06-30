#Take an array and make a new array of only the first and last elements. 

arr = [8,3,5,2,90]

arr3 = [1,3,6,2,89,0]

arr2 = []

#Make a function that takes the first and last item in an array and sends it to a new array. 

def first_last(n):
    return [n[0], n[len(n)-1]]

arr2 = first_last(arr)

print(arr2)

arr2 = first_last(arr3)

print(arr2)






