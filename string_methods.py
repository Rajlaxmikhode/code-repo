st="Python_Programming"
st2=" by guido van rossum"
print(st.lower())
print(st.upper())
print(st.find("ython"))
print(st.casefold())
print(st.replace("Programming","Language"))
print(st.isalpha())
print(st.endswith("ing"))
print(st.index("g"))
s="hello {}"
print(s)
print(s.format("World"))
print("hon" in st)
print("py" not in st)
print(s in st)
print(s is not st)
print(s.title())
print(isinstance(st,str)) # returns true if the specified object is of specified type
st+=st2 # performs both oncatenation and assignment opertion
print(st)
print(f'{st} is a high level programminng {st2}')# intterpolaration is the process of inserting variables and expressions directly into string 'f-string is one of the method'