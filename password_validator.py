password=input("Set a password: ")
has_upper=False
has_lower=False
has_digit=False
has_identifier=False
valid=False
for i in password:
    if i.isupper():
        has_upper=True
    if i.islower():
        has_lower=True
    if i.isnumeric():
        has_digit=True
    if not i.isalnum():
        has_identifier=True
        valid=True
    


if has_upper == False:
    print("must contain one uppercase character")

if has_lower == False:
    print("must contain one lowercase character")
        
if has_digit == False:
    print("must contain one digit")
        
if has_identifier == False:
     print("must contain atleast one special character")

if has_digit and has_identifier and has_lower and has_upper:
    print("valid password")     