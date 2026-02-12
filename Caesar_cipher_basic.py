# shift means how many letters we move forward in the alphabet

alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
print(shifted_alphabet)

'''
The str.maketrans() method takes two strings of equal length and returns a translation table that maps each character 
of the first string with the corresponding character of the second string. 
Each character in the translation table is stored as a Unicode ordinal, 
a number that uniquely identifies the character
'''

lower_chars="abc"
upper_chars="ABC"
table=str.maketrans(lower_chars,upper_chars)
print(table)
translation_table=str.maketrans(alphabet,shifted_alphabet)
print(translation_table)
"""
maketrans() = making a dictionary of replacements
translate() = applying those replacements to a string
"""
message = "ate"
encrypted = message.translate(translation_table)
print("encrypted message: ",encrypted)

t=str.maketrans("hl","bi")
sentence="hello world"
print(sentence.translate(t))





