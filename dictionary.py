d= {"name":"yohan", "age":10,"Gender":"male"}
print(d)
print(type(d))

data=[("name","yohan"),("age",10),("Gender","male")]
d=dict(data)
print(d)
print(type(d))

print(d["name"])
print(d["age"])
print(d["Gender"])

#print(d["City"])  - error

print(d.get("name"))
print(d.get("age"))
print(d.get("Gender"))
print(d.get("City"))    # None

print(d.get("City","Jaffna"))

d["age"]=20
print(d["age"])

d.update({"City":"Jaffna"})
print(d["City"])


d["NIC"]="2548323"
print(d)


d["NIC"]="2548323"
#d["age"]=70       add for single value
d.update({"age":70,"NIC":567856156})
print(d)

print("name" in d)

del d["name"]
print(d)

d.pop("age")
print(d)

d.popitem()
print(d)

#d.clear()
print(d)

key= d.keys()
print(key)

value= d.values()
print(value)

item= d.items()
print(item)

for key in d.keys():
    print(key,d[key])

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)
    
  
