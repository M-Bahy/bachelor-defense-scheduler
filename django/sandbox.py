import data as dt

count = 0
data = dt.load_data("django\InputData.json")
for i in data:
    print()
    print()
    print(f"At index : {count} : ")
    print()
    print(i)
    count += 1
