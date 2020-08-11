a={"name":"Tithi","age":20,"branch":"CSE",("h","w"):(119,60.5)}
print(a)
a[("h","w")]
print(a)
a["stud"]="Bachlor"
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a.get("age"))
print(a.get("ag"))#default as no key present named ag
print(a.popitem())
print(a)
print(a.pop("branch"))
print(a)
print(a.update({"name":"Tithi P"}))
print(a)
print(a[("h","w")])
print(a[("h","w")][0])
