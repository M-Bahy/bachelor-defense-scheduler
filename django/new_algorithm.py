import data as dt
import os
import json
import csv
import math


def create():
    infile = None
    if os.path.exists("InputData.json"):
        infile = "InputData.json"
    else:
        infile = "django/InputData.json"
    data = dt.load_data(infile)
    dates = data[7]  # 3/3/2023  , 4/3/2023
    days = len(dates)  # 2
    slots = len(dates) * 15  # 2 X 15 = 30
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
    solution = checks(solution, days, slots)
    solution = write_output(solution, data, 1)
    prof = profile(solution)
    solution2 = dt.generate_solution(
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
    solution2 = checks(solution2, days, slots)
    solution2 = write_output(solution2, data, 2)
    prof2 = profile(solution2)
    print(f"Profile 1 is : \n {prof}")
    print("--------------------------------------------------")
    print(f"Profile 2 is : \n {prof2}")
    print("--------------------------------------------------")
    for examiner in prof:
        first_percentage = float(prof[examiner].replace("%", ""))
        second_percentage = float(prof2[examiner].replace("%", ""))
        if second_percentage < first_percentage:
            print(f"Examiner {examiner} is better in solution 2")
        else:
            print(f"Examiner {examiner} is better in solution 1")


def checks(solution, days, slots):
    flagc = True
    c = 0

    # the slots of the least working day for the examiner

    for Examiner in solution[1]:
        for day in range(days):
            temp1 = 0
            for slot in range(15):
                time1 = day * 15 + slot
                # print(f"the time is {time1}")
                if len(solution[1][Examiner][time1]) >= 1:
                    temp1 += 1
            # print(f"{Examiner} has {temp1} slots in day {day}")
            if temp1 > 10 or (temp1 < 3 and temp1 > 0):
                for k in range(len(solution[0])):
                    if (
                        solution[0][k]["Examiner"] == Examiner
                        and solution[0][k]["Time"] >= day * 15
                        and solution[0][k]["Time"] < (day * 15 + 15)
                    ):
                        solution[0][k][
                            "Color"
                        ] = "Examiner assigned for less than 3 slots per day or more than 10 slots per day"
    for Examiner in solution[1]:
        working_days = 0
        min = 13
        lwday = 0
        for day in range(days):
            temp = 0
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    temp += 1
                if temp < min and temp > 0:
                    lwday = day
                    min = temp
            if temp >= 1:
                working_days += 1
        if working_days > 2:
            u = lwday * 15
            ue = lwday * 15 + 15
            for k in range(len(solution[0])):
                if (
                    solution[0][k]["Examiner"] == Examiner
                    and solution[0][k]["Time"] >= u
                    and solution[0][k]["Time"] < ue
                ):
                    solution[0][k][
                        "Color"
                    ] = "Examiner assigned for more than 2 days"
    flagc = True
    c = 0

    # more than 2 per slot for examiner
    for Examiner in solution[1]:
        flagc = True
        c = 0
        for i in range(slots):
            if len(solution[1][Examiner][i]) > 1:
                while flagc:
                    if (
                        solution[0][c]["Examiner"] == Examiner
                        and solution[0][c]["Time"] == i
                    ):
                        solution[0][c][
                            "Color"
                        ] = "more than 2 per slot for examiner"
                        flagc = False
                    c += 1
    flagc = True
    c = 0

    # more than 2 per slot for supervisor
    for Supervisor in solution[2]:
        flagc = True
        c = 0
        for i in range(slots):
            if solution[2][Supervisor][i] > 1:
                while flagc:
                    if (
                        solution[0][c]["Supervisor"] == Supervisor
                        and solution[0][c]["Time"] == i
                    ):
                        solution[0][c][
                            "Color"
                        ] = "more than 2 per slot for supervisor"
                        flagc = False
                    c += 1
    flagc = True
    c = 0
    # more slots than room
    for slot in range(slots):
        x = 0
        flagc = True
        c = 0
        for i in range(len(solution[0])):
            if solution[0][i]["Time"] == slot:
                x += 1
            if x > len(solution[3]):
                c = 0
                while flagc:
                    if solution[0][c]["Time"] == slot:
                        solution[0][c]["Color"] = "more slots than room"
                        flagc = False
                    c += 1
    flagc = True
    c = 0
    # slot of examiner in external constraint
    for Examiner in solution[1]:
        l = []
        check = []
        position = 0
        for g in solution[4][Examiner]:
            if solution[4][Examiner][g] == 1:
                l.append(g)
                check.append(position)
            position += 1
        for index in check:
            flagc = True
            c = 0
            if (
                len(solution[1][Examiner][index]) >= 1
                and solution[4][Examiner][index] == 1
            ):
                # print(
                #     "There is a violation in external constraint for examiner"
                # )
                while flagc:
                    if (
                        solution[0][c]["Examiner"] == Examiner
                        and solution[0][c]["Time"] == index
                    ):
                        solution[0][c][
                            "Color"
                        ] = "Examiner assigned in his day off"
                        flagc = False
                    c += 1

    flagc = True
    c = 0

    # internal in his day off

    for Examiner in solution[2]:
        l = []
        check = []
        position = 0
        for g in solution[5][Examiner]:
            if solution[5][Examiner][g] == 1:
                l.append(g)
                check.append(position)
            position += 1
        for index in check:
            flagc = True
            c = 0
            if (
                solution[2][Examiner][index] >= 1
                and solution[5][Examiner][index] == 1
            ):
                # print(
                #     "There is a violation in external constraint for examiner"
                # )
                while flagc:
                    if (
                        solution[0][c]["Supervisor"] == Examiner
                        and solution[0][c]["Time"] == index
                    ):
                        solution[0][c][
                            "Color"
                        ] = "Supervisor assigned in his day off"
                        flagc = False
                    c += 1

    flagc = True
    c = 0

    return solution


def write_output(solution, data, number):
    with open(f"fs.txt{number}", "w") as f:
        for i, element in enumerate(solution):
            f.write(f"Index {i}:\n {element}\n")
    slottimes = [
        "9 am",
        "9:30 am",
        "10 am",
        "10:30 am",
        "11 am",
        "11:30 am",
        "12 pm",
        "12:30 pm",
        "1 pm",
        "1:30 pm",
        "2 pm",
        "2:30 pm",
        "3 pm",
        "3:30 pm",
        "4 pm",
    ]
    for i in range(len(solution[0])):
        ctime = solution[0][i]["Time"]
        cslottime = slottimes[ctime % 15]
        datetime = data[7][(math.ceil((ctime + 1) / 15) - 1)]
        solution[0][i]["Time"] = "" + datetime + " " + cslottime + ""
    final = json.dumps(solution[0], indent=6, allow_nan=True)
    jsonFile = open(f"Solution{number}.json", "w")
    jsonFile.write(final)
    jsonFile.close()
    Create_output(number)
    return solution


def profile(solution):
    profile = {}
    total_assignments = solution[6]
    problems = 0
    for examiner in total_assignments:
        problems = 0
        for index in solution[0]:
            if index["Examiner"] == examiner:
                try:
                    problem = index["Color"]
                    problems += 1
                except:
                    pass
        persentage = problems / (total_assignments[examiner]) * 100
        # print(
        #     f"The examiner {examiner} have {problems} problems which means {persentage}%"
        # )
        profile[examiner] = f"{persentage}%"
    return profile


def Create_output(number):
    with open(f"Solution{number}.json") as json_file:
        data = json.load(json_file)
    # csv_file = csv.writer(json_file,lineterminator='\n')

    student_data = data
    solution_file = open(f"Solution{number}.csv", "w", newline="")
    csv_writer = csv.writer(solution_file)

    # Counter variable used for writing headers to the CSV file
    count = 0
    for emp in student_data:
        if count == 0:
            # Writing headers of CSV file
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(emp.values())

    solution_file.close()
    return


create()
