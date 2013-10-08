from collections import defaultdict

d = defaultdict(defaultdict)

a = [("key1", {"a1":22, "a2":33}),
     ("key2", {"a1":32, "a2":55}),
     ("key3", {"a1":43, "a2":44})]

for i in a:
    d[i[0]] = i[1]
    

d["key1"].update({"a53":22, "a5":33})


d = defaultdict(list)
