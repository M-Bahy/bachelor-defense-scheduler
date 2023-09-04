import data as dt


def create():
    data = dt.load_data("InputData.json")
    dates = data[7]  # 3/3/2023  , 4/3/2023
    days = len(dates)  # 2
    slots = len(dates) * 15  # 2 X 15 = 30
    first_solution = dt.generate_solution(
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
