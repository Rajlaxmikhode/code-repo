def group_words(*words):
   
   group={}
   for word in words:
       length=len(word)
       if length not in group:
           group[length]=[]
       group[length].append(word)
   print(group)


group_words("hi","by","keema","chicken","fries")


# method-2
#clear pythonic way
words = ["hi", "hello", "cat", "dog", "python", "go"]

group = {}

for word in words:
    group.setdefault(len(word), []).append(word)

print(group)
