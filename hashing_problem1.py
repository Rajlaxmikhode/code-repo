def duplicate(*li):
    seen=set()
    for x in li:
        if x in seen :
            return True
        seen.add(x)
    return False

print(duplicate(8,23,29,8,2,9))