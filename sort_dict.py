data = {"a": 5, "b": 2, "c": 8, "d": 1}

sorted_dict=dict(sorted(data.items(), key=lambda item: item[1],reverse=True))

print(sorted_dict)