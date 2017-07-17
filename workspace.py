col_string = "?"
for i in range(10):
    col_string += "?,"
# col_string += "?"
print(col_string)

conv = {"id":"", "test": ""}
conv["id"] = 123
conv["id"] = 2323
conv["test"] = conv["id"]
print(conv)
print(conv.keys())
print(type(conv.keys()))