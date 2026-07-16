letter="""
Dear   <name>,
you are selected 
<date>"""

print(letter.replace("<name>","Sheela").replace("<date>","25, sep, 2026"))
print(letter.find("  "))

print(letter) # strings are immutable you cannot change them by running functions on them