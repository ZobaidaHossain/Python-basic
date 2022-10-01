d={"tom":1,"je":3}
print(d)
print(d["tom"])
d['sam']=33
print(d)
del d["sam"]
print(d)
for i in d:
    print("key:",i,"value:",d[i])
print("tom" in d)
d.clear()
print(d)