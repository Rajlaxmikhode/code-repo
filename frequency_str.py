string="woodchuck"
st={}
for ch in string:
    if ch in st:
        st[ch]+=1
    else:
        st[ch]=1
for ch ,count in st.items():
    print(f"{ch}-{count}")
print(st)

