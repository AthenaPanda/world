#dict sample
seq = ('name', 'age', 'class')
dict1 = dict.fromkeys(seq, ('Tom', 23, 3))
print(str(dict1))

dict2 = {"age": 20, "name": "Wind", "pro": "busin"}
print(dict2.items())
print(dict2.keys())
print(dict2.values())
if 'age' in dict1.keys():
    print("find the age!")

dict3 = {"A":30, "B":65, "C":89, "D":80}
for key,value in dict3.items():
    if value > 75:
        print(key)
