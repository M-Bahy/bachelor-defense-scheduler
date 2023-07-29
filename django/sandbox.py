import data as dt

count = 0
data = dt.load_data("django\InputData.json")
dates = data[7]
days = len(dates)
slots = len(dates) * 15
solution = dt.generate_solution(
    data[0],
    data[1],
    data[4],
    data[5],
    data[2],
    data[3],
    data[6],
    days,
    slots,
)
print(solution)
# for i in data:
#     print(f"At index {count} there is : ", i)
#     count += 1
