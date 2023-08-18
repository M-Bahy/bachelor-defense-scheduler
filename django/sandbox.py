import data as dt
import json

count = 0
data = dt.load_data("django\InputData.json")
for i in data:
    print()
    print()
    print(f"At index : {count} : ")
    print()
    print(i)
    count += 1
# data = json.load(open("django\InputData.json", "r"))
# print(data)
