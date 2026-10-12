d = {"a": 10, "b":20, "c":30, "d":40}

keys = list(d.keys())
reverse = {}

for i in range(len(keys)-1, -1, -1):
    key = keys[i]
    reverse[keys] = d[keys]

print(reverse)