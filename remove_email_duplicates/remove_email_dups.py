#file_name is now the arg passed to the function
def rm_dupl_emails_from_file(file_name):
    unique_emails = []

    with open(file_name) as file_object:
        content = file_object.read()

    # print(content)

    emails = content.split(", ")

    # print(emails)

    for email in emails:
        # changed a variable name here to make it more readable
        if email not in emails:
            unique_emails.append(email)
    
    # a return statement is used to make the function more versatile
    # a print method can be called on any returned value
    return unique_emails

print(rm_dupl_emails_from_file("emails.txt"))



#Run our own local test to see if split function works. 

# fake_emails = "Johndoe@gmail.com, maryjoe@gmail.com"
# print(fake_emails.split(", "))
