import math
from sqlalchemy import null
import data as dt
from tabulate import tabulate
import cost_function
import neighboring
from copy import deepcopy
import Inputcreation
import Outputcreation
import json
import random


cost_function = cost_function.cost


def drawschedule(f):
    u = [""] * 10000000
    for x in range(len(f[0])):
        u[f[0][x]["Time"]] += (
            "("
            + (f[0][x]["Examiner"] + " , " + f[0][x]["Supervisor"])
            + " , "
            + f[0][x]["Room"]
            + ")  "
        )
    x1 = [
        "Day 1",
        u[0],
        u[1],
        u[2],
        u[3],
        u[4],
        u[5],
        u[6],
        u[7],
        u[8],
        u[9],
        u[10],
        u[11],
        u[12],
        u[13],
        u[14],
    ]
    x2 = [
        "Day 2",
        u[15],
        u[16],
        u[17],
        u[18],
        u[19],
        u[20],
        u[21],
        u[22],
        u[23],
        u[24],
        u[25],
        u[26],
        u[27],
        u[28],
        u[29],
    ]
    x3 = [
        "Day 3",
        u[30],
        u[31],
        u[32],
        u[33],
        u[34],
        u[35],
        u[36],
        u[37],
        u[38],
        u[39],
        u[40],
        u[41],
        u[42],
        u[43],
        u[44],
    ]
    x4 = [
        "Day 4",
        u[45],
        u[46],
        u[47],
        u[48],
        u[49],
        u[50],
        u[51],
        u[52],
        u[53],
        u[54],
        u[55],
        u[56],
        u[57],
        u[58],
        u[59],
    ]
    x5 = [
        "Day 5",
        u[60],
        u[61],
        u[62],
        u[63],
        u[64],
        u[65],
        u[66],
        u[67],
        u[68],
        u[69],
        u[70],
        u[71],
        u[72],
        u[73],
        u[74],
    ]
    x6 = [
        "Day 6",
        u[75],
        u[76],
        u[77],
        u[78],
        u[79],
        u[80],
        u[81],
        u[82],
        u[83],
        u[84],
        u[85],
        u[86],
        u[87],
        u[88],
        u[89],
    ]
    x7 = [
        "Day 7",
        u[90],
        u[91],
        u[92],
        u[93],
        u[94],
        u[95],
        u[96],
        u[97],
        u[98],
        u[99],
        u[100],
        u[101],
        u[102],
        u[103],
        u[104],
    ]
    x8 = [
        "Day 8",
        u[105],
        u[106],
        u[107],
        u[108],
        u[109],
        u[110],
        u[111],
        u[112],
        u[113],
        u[114],
        u[115],
        u[116],
        u[117],
        u[118],
        u[119],
    ]
    x9 = [
        "Day 9",
        u[120],
        u[121],
        u[122],
        u[123],
        u[124],
        u[125],
        u[126],
        u[127],
        u[128],
        u[129],
        u[130],
        u[131],
        u[132],
        u[133],
        u[134],
    ]
    x10 = [
        "Day 10",
        u[135],
        u[136],
        u[137],
        u[138],
        u[139],
        u[140],
        u[141],
        u[142],
        u[143],
        u[144],
        u[145],
        u[146],
        u[147],
        u[148],
        u[149],
    ]
    x11 = [
        "Day 11",
        u[150],
        u[151],
        u[152],
        u[153],
        u[154],
        u[155],
        u[156],
        u[157],
        u[158],
        u[159],
        u[160],
        u[161],
        u[162],
        u[163],
        u[164],
    ]
    x12 = [
        "Day 12",
        u[165],
        u[166],
        u[167],
        u[168],
        u[169],
        u[170],
        u[171],
        u[172],
        u[173],
        u[174],
        u[175],
        u[176],
        u[177],
        u[178],
        u[179],
    ]

    with open("Solution.txt", "w") as e:
        e.write(
            tabulate(
                [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12],
                headers=[
                    "9 am",
                    "9:30 am",
                    "10 am",
                    "10:30 am",
                    "11 am",
                    "Break",
                    " 12 pm",
                    "12:30 pm,",
                    "1 pm",
                    "1:30 pm",
                    "Break",
                    "2:30 pm",
                    "3 pm",
                    "3:30 pm",
                    "4 pm",
                ],
                tablefmt="grid",
            )
        )


def get_iterations():
    f = open("iterations.txt", "r")
    iter = f.readline()
    f.close()
    return iter


def evolutionary_algorithm():
    """
    This function implements an evolutionary algorithm to generate an optimal timetable for a bachelor defense scheduler.
    It generates a solution by creating the first timetable randomly
    then changes the new solution by calling the neighbor function from neighboring file.
    It calculates the cost for the solution
    if the cost for the new solution is less than or equal to the cost of the current solution
    Then it changes the value of the solution to the new solution.
    It checks for hard constraints such as the number of examiners, supervisors, and classrooms per slot and continuity of the schedule.
    """
    # f = True
    max_generations = 2000
    num_runs = 1
    best_timetable = None
    data = dt.load_data("InputData.json")
    dates = data[7]  # 3/3/2023  , 4/3/2023
    days = len(dates)  # 2
    slots = len(dates) * 15  # 2 X 15 = 30
    neighbor = (
        neighboring.neighbor
    )  # call the neighbor function from neighboring file

    for i in range(num_runs):
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
        )  # generate a solution by creating the first timetable by random
        # index = 0
        # if f:
        #     print("The solution is : ")
        #     for x in solution:
        #         print()
        #         print()
        #         print(f"At index {index}")
        #         print()
        #         print("The value is : ")
        #         print(x)
        #         print()
        #         print()
        #         index += 1
        #     f = False
        flag = False
        c = 0
        for j in range(max_generations):
            # change the new solution by calling the neighbor from neighboring by getteing a deepcopy from the original chromosom

            new_solution = neighbor(deepcopy(solution), flag, days, slots)

            # calculate the cost for the solution
            ft = cost_function(solution, days, slots)
            fti = []
            fti = ft[0] + ft[1] + ft[2]
            # if the cost for the solution == 0 -> optimal solution (no violate of hard and soft constraint)
            if fti == 0:
                break
            # calculate the cost for the solution
            ftn = cost_function(new_solution, days, slots)
            ftni = []
            ftni = ftn[0] + ftn[1] + ftn[2]
            # ---- if the cost for the new_solution less than or equal the cost solution
            # change the value of solution to new_solution ----
            if ftni >= fti:
                c += 1
            if c >= 2000:
                flag = True
            if ftni < fti:
                c = 0
                flag = False
            if ftni <= fti:
                solution = new_solution

            # print the iteration number and the cost for the current solution
            if j % 200 == 0:
                f = open("iterations.txt", "w")
                f.write("{}".format(((j / max_generations) * 100) // 1))
                f.close()
                print(
                    "Iteration",
                    j,
                    "cost",
                    cost_function(solution, days, slots),
                )
            # if j % 5000 == 0:

        print(
            "Run",
            i + 1,
            "cost",
            cost_function(solution, days, slots),
            "solution",
            solution,
        )
        print(cost_function(solution, days, slots))
        # Soft constraint not important yet
        # if best_timetable is None or cost_function2(solution) <= cost_function2(best_timetable):
        if best_timetable is None:
            best_timetable = deepcopy(solution)

    solution = best_timetable
    # print(solution[0])

    """
            Soft constraint not important yet
    """
    # for j in range(3 * max_generations):
    #     new_solution = neighbor2(deepcopy(solution))
    #     ft = cost_function2(solution)
    #     ftn = cost_function2(new_solution)
    #     if ftn <= ft:
    #         solution = new_solution
    #     if j % 200 == 0:
    #         print('Iteration', j, 'cost', cost_function2(solution))
    #
    # print('Run', 'cost', cost_function2(solution), 'solution', solution)

    # dt.write_data(solution[0], output_file)

    examiner_hard = True
    supervisor_hard = True
    room_hard = True
    continued = True

    for i in range(len(solution[0])):
        if (
            len(
                solution[1][solution[0][i]["Examiner"]][solution[0][i]["Time"]]
            )
            > 1
        ):
            examiner_hard = False
            # print(solution[0][i])

        if (
            solution[2][solution[0][i]["Supervisor"]][solution[0][i]["Time"]]
            > 1
        ):
            supervisor_hard = False

        if (
            len(
                solution[1][solution[0][i]["Examiner"]][solution[0][i]["Time"]]
            )
            >= 1
            and solution[4][solution[0][i]["Examiner"]][solution[0][i]["Time"]]
            == 1
        ):
            examiner_hard = False

    for Examiner in solution[1]:
        for day in range(days):
            temp = 0
            flag1 = False
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    if time - temp - 1 >= 2 and flag1:
                        continued = False
                        # print("Continouty violated")
                    flag1 = True
                    temp = time

    print("Are hard restrictions for Examiner satisfied:", examiner_hard)
    print("Are hard restrictions for Supervisor satisfied:", supervisor_hard)
    # print('Are hard restrictions for Room satisfied:', room_hard)
    print("Are hard restrictions for Continouity satisfied:", continued)

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
                print(
                    "There is a violation in external constraint for examiner"
                )
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

        # for i in range(len(l)):
        #     flagc = True
        #     c = 0
        #     # print(
        #     #     "The argument is : ",
        #     #     "\n",
        #     #     solution[1][Examiner][l[i]],
        #     #     "\n",
        #     #     "and its length is : ",
        #     #     "\n",
        #     #     len(solution[1][Examiner][l[i]]),
        #     # )
        #     if len(solution[1][Examiner][i]) >= 1 and check[i] == 1:
        #         while flagc:
        #             if (
        #                 solution[0][c]["Examiner"] == Examiner
        #                 and solution[0][c]["Time"] == l[i]
        #             ):
        #                 solution[0][c][
        #                     "Color"
        #                 ] = "Examiner assigned in his day off"
        #                 flagc = False
        #             c += 1

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

    # for Examiner in solution[2]:
    #     l = []
    #     for g in solution[5][Examiner]:
    #         if solution[5][Examiner][g] == 1:
    #             l.append(g)
    #     for i in range(len(l)):
    #         flagc = True
    #         c = 0
    #         if solution[2][Examiner][l[i]] >= 1:
    #             while flagc:
    #                 if (
    #                     solution[0][c]["Supervisor"] == Examiner
    #                     and solution[0][c]["Time"] == l[i]
    #                 ):
    #                     solution[0][c][
    #                         "Color"
    #                     ] = "Supervisor assigned in his day off"
    #                     flagc = False
    #                 c += 1
    flagc = True
    c = 0

    count = 0
    with open("Inspected solution.txt", "w") as f:
        for i in solution:
            f.write("\n")
            f.write("\n")
            f.write(f"At index : {count} : ")
            f.write("\n")
            f.write(str(i))
            count += 1

    examiners = [""] * slots
    numberofexaminers = [0] * slots
    p = [""] * len(solution[7])
    for x in range(len(solution[7])):
        p[x] = solution[7][x]
    availablerooms = [
        [solution[7][f] for f in range(len(solution[7]))] for x in range(slots)
    ]
    for x in range(len(solution[0])):
        examiners[solution[0][x]["Time"]] += (solution[0][x]["Examiner"]) + ","
    for j in range(len(examiners)):
        numberofexaminers[j] += examiners[j].count(",")

    for x in range(days):
        # empty all dics
        examinerroomdict = {}
        for y in range(15):
            f = examiners[(x * 15) + y].split(",")
            if len(f) > 0:
                del f[len(f) - 1 :]
            for w in range(len(f)):
                if f[w] in examinerroomdict:
                    continue
                if len(availablerooms[(x * 15) + y]) == 0:
                    continue
                croom = random.choice(availablerooms[x * 15 + y])
                availablerooms[(x * 15) + y].remove(croom)
                examinerroomdict[f[w]] = croom
                for u in range(len(solution[0])):
                    if (
                        solution[0][u]["Examiner"] == f[w]
                        and solution[0][u]["Time"] == x * 15 + y
                    ):
                        solution[0][u]["Room"] = examinerroomdict[f[w]]
                        break
                for r in range(15):
                    t = examiners[x * 15 + r].split(",")
                    if len(t) > 0:
                        del t[len(t) - 1 :]
                    for z in range(len(t)):
                        if t[z] == f[w]:
                            for u in range(len(solution[0])):
                                if (
                                    solution[0][u]["Examiner"] == f[w]
                                    and solution[0][u]["Time"] == x * 15 + r
                                ):
                                    solution[0][u]["Room"] = examinerroomdict[
                                        f[w]
                                    ]
                                    if (
                                        availablerooms[x * 15 + r].count(
                                            examinerroomdict[f[w]]
                                        )
                                        >= 1
                                    ):
                                        availablerooms[x * 15 + r].remove(
                                            examinerroomdict[f[w]]
                                        )

    drawschedule(solution)
    ndays = len(data[7])
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
    jsonFile = open("Solution.json", "w")
    jsonFile.write(final)
    jsonFile.close()
    Outputcreation.Create_output()

    return solution
