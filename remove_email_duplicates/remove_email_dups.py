file_name = "emails.txt"

duplicate_free_emails = []

with open(file_name) as file_object:
    content = file_object.read()

# print(content)

emails = content.split(", ")

# print(emails)

for email in emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

print(duplicate_free_emails)



#Run our own local test to see if split function works. 

# fake_emails = "Johndoe@gmail.com, maryjoe@gmail.com"
# print(fake_emails.split(", "))