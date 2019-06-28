#Program that Remove Duplicates from the Array 

#Here are the Names
original_names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

#Loop through each Name, drop that name into a new array if the new array does not already contain that name (value).
final_names = []

for i in original_names:
    if i not in final_names:
        final_names.append(i)
  

print(final_names)
    
