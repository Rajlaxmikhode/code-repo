def sum_letters(s):
    letters=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum=0
    if not isinstance(s,str):
            return 0
    for letter in s.upper():
        if letter in letters:
            sum+=letters.index(letter)
    return sum
    
user_input=input("Enter any value in string: ")
print(sum_letters(user_input))