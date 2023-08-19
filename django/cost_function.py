def cost(solution, days, slots):
    examiner_cost = 0
    supervisor_cost = 0
    room_cost = 0
    examiner_empty = 0
    examiner_distinct_room = 0
    candidates = []

    # Check for hard constraints

    # Examiner, Supervisor and Room can't be reserved more than once
    for Examiner in solution[1]:
        for i in range(slots):
            if len(solution[1][Examiner][i]) > 1:
                examiner_cost += 1
                # print("Examiner reserved in same slot violated")
    for Supervisor in solution[2]:
        for i in range(slots):
            if solution[2][Supervisor][i] > 1:
                supervisor_cost += 1

    # maxmimum number of rooms*13 for day
    # slot*number
    for slot in range(slots):
        x = 0
        for i in range(len(solution[0])):
            if solution[0][i]["Time"] == slot:
                x += 1
        if x > len(solution[3]):
            room_cost += x - len(solution[3])
            # print("More slots than rooms")

    for Examiner in solution[1]:
        for day in range(days):
            temp = 0
            flag1 = False
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    if time - temp - 1 >= 2 and flag1:
                        examiner_cost += time - temp - 1
                        # print("Continouty violated")
                    flag1 = True
                    temp = time

    # #Examiner in more than one room in a single day

    # # Maximum number of rooms in slot

    # Examiner violated time constraints
    for Examiner in solution[1]:
        l = []
        for c in solution[4][Examiner]:
            l.append(c)
        for i in range(len(l)):
            if len(solution[1][Examiner][i]) >= 1 and l[i] == 1:
                examiner_cost += 1
                # print("Examiner time constraint violated")
    for Supervisor in solution[2]:
        l = []
        for c in solution[5][Supervisor]:
            l.append(c)
        for i in range(len(l)):
            if solution[2][Supervisor][i] >= 1 and l[i] == 1:
                supervisor_cost += 1
                # print("Supervisor time constraint violated")

    # Examiner has more than 2 days
    for Examiner in solution[1]:
        working_days = 0
        for day in range(days):
            for slot in range(15):
                time = day * 15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    working_days += 1
                    break
        if working_days > 2:
            examiner_cost += working_days - 2
    # print("Examiner has more than 2 days violated")

    # Time cosntraints
    # for Examiner in solution[1]:
    #     for day in range(days):
    #         for slot in range(15):
    #             time = day * 15 + slot
    #             if (
    #                 len(solution[1][Examiner][time]) >= 1
    #                 and solution[4][Examiner][time] == 1
    #             ):
    #                 examiner_cost += 1

    # less than 3 or more than 10 slots per day

    # less than 3 or more than 10 slots per day

    return examiner_cost, supervisor_cost, room_cost
