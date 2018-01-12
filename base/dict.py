d = {1: "123", 2: "asd", "q": 4}
key = d.get("w", -1)
print(d.get("w", -1))
print(d.get("q"))
print(d.get(2))
print(type(d.get("w")))
if d.get("w") is None:
    print("kong")
else:
    print("exist")

if key == -1:
    print("kong")
else:
    print("exist")

b = "w" in d
print(b)
if not b:
    print("kong")
else:
    print("exist")
