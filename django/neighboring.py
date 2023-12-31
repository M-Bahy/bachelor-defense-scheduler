from pickle import TRUE
import random
import math
from copy import deepcopy


def neighbor(solution, flag1, days, slots):
    candidates = []

    for Examiner in solution[1]:  # check if <3 or >10 slots in a day
        for day in range(days):
            temp1 = 0
            for slot in range(15):
                time1 = day * 15 + slot
                if len(solution[1][Examiner][time1]) >= 1:
                    temp1 += 1
            if temp1 > 10 or (temp1 < 3 and temp1 > 0):
                for k in range(len(solution[0])):
                    if (
                        solution[0][k]["Examiner"] == Examiner
                        and solution[0][k]["Time"] >= day * 15
                        and solution[0][k]["Time"] < (day * 15 + 15)
                    ):
                        candidates.append((k, "maxAndMin"))

    for Examiner in solution[1]:  # check if examiner has more than 2 days
        working_days = 0
        for day in range(days):
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    working_days += 1
                    if working_days > 2:
                        for k in range(len(solution[0])):
                            if (
                                solution[0][k]["Examiner"] == Examiner
                                and solution[0][k]["Time"] >= day * 15
                                and solution[0][k]["Time"] < (day * 15 + 15)
                            ):
                                candidates.append((k, "moreThan2Days"))
                    break
    # check if assignments are more than rooms in a given time slot
    for slot in range(slots):
        x1 = 0
        w = []
        for i in range(len(solution[0])):
            if solution[0][i]["Time"] == slot:
                x1 += 1
                w.append(i)
        if x1 > len(solution[3]):
            for t in range(len(w)):
                candidates.append((w[t], "slotMoreThanRooms"))

    for i in range(len(solution[0])):
        w = solution[0][i]["Time"]
        # byshoof law fe 2 slot 2bleha aw 1 slot b3deha
        if not (w - 2 < 0 or w + 2 >= slots):
            if (
                not (
                    len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] - 1
                        ]
                    )
                    == 1
                    or len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] - 2
                        ]
                    )
                    == 1
                    or len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] + 1
                        ]
                    )
                    == 1
                )
                and solution[0][i]["Time"] % 15 == 13
            ):
                candidates.append((i, "continuity"))

            elif (
                not (
                    len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] - 1
                        ]
                    )
                    == 1
                    or len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] - 2
                        ]
                    )
                    == 1
                )
                and solution[0][i]["Time"] % 15 == 14
            ):
                candidates.append((i, "continuity"))

            elif (
                not (
                    len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] + 1
                        ]
                    )
                    == 1
                    or len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] + 2
                        ]
                    )
                    == 1
                )
                and solution[0][i]["Time"] % 15 == 0
            ):
                candidates.append((i, "continuity"))

            elif (
                not (
                    len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] + 1
                        ]
                    )
                    == 1
                    or len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] + 2
                        ]
                    )
                    == 1
                    or len(
                        solution[1][solution[0][i]["Examiner"]][
                            solution[0][i]["Time"] - 1
                        ]
                    )
                    == 1
                )
                and solution[0][i]["Time"] % 15 == 1
            ):
                candidates.append((i, "continuity"))

            elif not (
                len(
                    solution[1][solution[0][i]["Examiner"]][
                        solution[0][i]["Time"] - 1
                    ]
                )
                == 1
                or len(
                    solution[1][solution[0][i]["Examiner"]][
                        solution[0][i]["Time"] - 2
                    ]
                )
                == 1
                or len(
                    solution[1][solution[0][i]["Examiner"]][
                        solution[0][i]["Time"] + 1
                    ]
                )
                == 1
                or len(
                    solution[1][solution[0][i]["Examiner"]][
                        solution[0][i]["Time"] + 2
                    ]
                )
                == 1
            ):
                candidates.append((i, "continuity"))

        if (
            len(
                solution[1][solution[0][i]["Examiner"]][solution[0][i]["Time"]]
            )
            > 1
        ):
            candidates.append((i, "examinerRepeat"))

        if (
            solution[2][solution[0][i]["Supervisor"]][solution[0][i]["Time"]]
            > 1
        ):
            candidates.append((i, "supervisorRepeat"))

        if (
            len(
                solution[1][solution[0][i]["Examiner"]][solution[0][i]["Time"]]
            )
            >= 1
            and solution[4][solution[0][i]["Examiner"]][solution[0][i]["Time"]]
            == 1
        ):
            candidates.append((i, "examinerConstraint"))

        if (
            solution[2][solution[0][i]["Supervisor"]][solution[0][i]["Time"]]
            >= 1
            and solution[5][solution[0][i]["Supervisor"]][
                solution[0][i]["Time"]
            ]
            == 1
        ):
            candidates.append((i, "supervisorConstraint"))

    reason = []
    if not candidates or flag1:
        i = random.randrange(len(solution[0]))

    else:
        tuple = random.choice(candidates)
        i = tuple[0]
        for choice in candidates:
            if choice[0] == i:
                reason.append(choice[1])

    time = solution[0][i]["Time"]
    selected_examiner = solution[0][i]["Examiner"]
    selected_supervisor = solution[0][i]["Supervisor"]
    selected_room = solution[0][i]["Room"]

    # Remove assignment from slot
    solution[1][selected_examiner][time].remove(selected_room)
    solution[2][selected_supervisor][time] -= 1
    solution[3][selected_room][time] -= 1

    # Swap Room for the external
    sday = (math.ceil(time / 15) - 1) * 15
    eday = math.ceil(time / 15) * 15

    # check if this day doesnt break his constraint

    # if exists continous slots check before them and after them for free slot

    # if no continous slots exist then check next and previous slots

    # search for highest working day for external and insert in that day if possible else find 2nd highest else randomize

    # Find the day with most slots then most continous if no continous randmoize in a position that is continous

    #     #insert gaps when inserting slot randomly

    # Find the most continous slots in the day

    # generate el continous slots including 1 slot gap
    # max is the value of continous slots
    # endslot where the continous slots stop

    max = 0
    mwday = 0

    for day in range(days):
        noOfSlots = 0
        mwday = 0
        for slot in range(15):
            if solution[4][selected_examiner][(day * 15) + slot] == 1:
                continue  # examiner in his day off
            if slot % 5 == 0 and not (slot % 3 == 0):
                continue  # break slot
            if len(solution[1][selected_examiner][(day * 15) + slot]) >= 1:
                noOfSlots += 1
            # >12 then all slots in one day
        if (
            solution[6][selected_examiner] > 12
            and noOfSlots < 10
            and noOfSlots > max
        ):
            mwday = day
            max = noOfSlots
            # noOfSlots = 0
        elif (
            solution[6][selected_examiner] == 11
            and noOfSlots < 8
            and noOfSlots > max
        ):
            mwday = day
            max = noOfSlots
            # noOfSlots = 0
        elif (
            solution[6][selected_examiner] == 12
            and noOfSlots < 9
            and noOfSlots > max
        ):
            mwday = day
            max = noOfSlots
            # noOfSlots = 0
        # <12 then we can fill
        elif solution[6][selected_examiner] <= 10 and noOfSlots > max:
            mwday = day
            max = noOfSlots
            # noOfSlots = 0
    max = 0
    temp = 0
    endslot = 0
    sday = mwday * 15
    eday = sday + 15
    flag = True

    for x in range(sday, eday):
        if x % 5 == 0 and not (x % 3 == 0):
            continue
        if len(solution[1][selected_examiner][x]) >= 1:
            temp += 1
        elif x + 1 != slots:
            if len(solution[1][selected_examiner][x + 1]) >= 1:
                temp += 1
        else:
            if temp > max:
                max = temp
                temp = 0
                endslot = x

    r = random.randint(0, 14)

    if mwday != 0:
        r = r + (mwday * 15)

    c = 0
    while flag:
        c += 1
        r = random.randint(0, 14)

        if mwday != 0:
            r = r + (mwday * 15)
        if (
            len(solution[1][selected_examiner][r]) == 0
            and c > 45
            and not (r % 5 == 0 and not (r % 3 == 0))
        ):
            flag = False
        elif r + 1 < slots and r - 1 >= 0:
            if (
                len(solution[1][selected_examiner][r]) == 0
                and (
                    len(solution[1][selected_examiner][r + 1]) >= 1
                    or len(solution[1][selected_examiner][r - 1]) >= 1
                )
                and not (r % 5 == 0 and not (r % 3 == 0))
            ):
                flag = False
        elif r == 0:
            if (
                len(solution[1][selected_examiner][r]) == 0
                and len(solution[1][selected_examiner][r + 1]) >= 1
                and not (r % 5 == 0 and not (r % 3 == 0))
            ):
                flag = False
        elif r == slots - 1:
            if (
                len(solution[1][selected_examiner][r]) == 0
                and len(solution[1][selected_examiner][r - 1]) >= 1
                and not (r % 5 == 0 and not (r % 3 == 0))
            ):
                flag = False

    # if "slotMoreThanRooms" in reason:
    #     while(r == solution[0][i]['Time']):
    #         r  = random.randint(0,14)
    #         r = r + (mwday*15)
    # if external is wrong and supervisor is right work on external
    if (
        len(solution[1][selected_examiner][r]) > 1
        and solution[2][selected_supervisor][r] == 0
    ):
        flago = True
        while flago:
            w = random.randint(0, 2)
            if endslot - max >= 0:
                if (
                    solution[3][selected_room][endslot - max] == 0
                    and not (
                        endslot - max % 5 == 0 and not (endslot - max % 3 == 0)
                    )
                    and w == 0
                    and endslot != 0
                ):
                    solution[0][i]["Time"] = endslot - max
                    solution[1][selected_examiner][endslot - max].append(
                        selected_room
                    )
                    solution[2][selected_supervisor][endslot - max] += 1
                    solution[3][selected_room][endslot - max] += 1
                    return solution, candidates

            if endslot + 1 < slots:
                if (
                    solution[3][selected_room][endslot + 1] == 0
                    and not (
                        endslot + 1 % 5 == 0 and not (endslot + 1 % 3 == 0)
                    )
                    and w == 1
                    and endslot != 0
                ):
                    solution[0][i]["Time"] = endslot + 1
                    solution[1][selected_examiner][endslot + 1].append(
                        selected_room
                    )
                    solution[2][selected_supervisor][endslot + 1] += 1
                    solution[3][selected_room][endslot + 1] += 1
                    return solution
            if (
                solution[3][selected_room][r] == 0
                and not (r % 5 == 0 and not (r % 3 == 0))
                or w == 2
            ):
                solution[0][i]["Time"] = r
                solution[1][selected_examiner][r].append(selected_room)
                solution[2][selected_supervisor][r] += 1
                solution[3][selected_room][r] += 1
                return solution
            elif (
                solution[3][selected_room][r] >= 1
                and not (r % 5 == 0 and not (r % 3 == 0))
                or w == 2
            ):
                solution[0][i]["Time"] = r
                solution[1][selected_examiner][r].append(selected_room)
                solution[2][selected_supervisor][r] += 1
                solution[3][selected_room][r] += 1
                return solution
    # if external is right and supervisor is wrong or if external and supervisor wrong randomize

    # elif "maxAndMin" in reason and not ("slotMoreThanRooms" in reason):
    #     solution[0][i]['Time'] = r
    #     solution[1][selected_examiner][r].append(selected_room)
    #     solution[2][selected_supervisor][r] += 1
    #     solution[3][selected_room][r] += 1
    #     return solution

    else:
        yes = True
        while yes:
            r1 = random.randint(0, slots - 1)
            if not (r1 % 5 == 0 and not (r1 % 3 == 0)):
                yes = False

        solution[0][i]["Time"] = r1
        solution[1][selected_examiner][r1].append(selected_room)
        solution[2][selected_supervisor][r1] += 1
        solution[3][selected_room][r1] += 1
        return solution
    return solution


def maxWorkingDay(exception, solution, selected_examiner, days, slots):
    max = 0
    mwday = 0
    for day in range(days):
        noOfSlots = 0
        if day == exception:
            continue
        for slot in range(15):
            if solution[4][selected_examiner][(day * 15) + slot] == 1:
                continue
            if slot % 5 == 0 and not (slot % 3 == 0):
                continue
            if len(solution[1][selected_examiner][(day * 15) + slot]) >= 1:
                noOfSlots += 1
            # >12 then all slots in one day
        if (
            solution[6][selected_examiner] > 12
            and noOfSlots < 10
            and noOfSlots > max
        ):
            mwday = day
            max = noOfSlots
            noOfSlots = 0
        elif (
            solution[6][selected_examiner] == 11
            and noOfSlots < 8
            and noOfSlots > max
        ):
            mwday = day
            max = noOfSlots
            noOfSlots = 0
        elif (
            solution[6][selected_examiner] == 12
            and noOfSlots < 9
            and noOfSlots > max
        ):
            mwday = day
            max = noOfSlots
            noOfSlots = 0
        # <12 then we can fill
        elif solution[6][selected_examiner] <= 10 and noOfSlots > max:
            mwday = day
            max = noOfSlots
            noOfSlots = 0

    return mwday
