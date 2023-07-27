
def cost(solution,days,slots):
    examiner_cost = 0
    supervisor_cost = 0
    room_cost = 0
    examiner_empty = 0
    examiner_distinct_room = 0
    candidates = []

    #Check for hard constraints

    # for single_assignment in solution[0]:
    #     for i in range(179):
    #         for Examiner in single_assignment['Examiner']:
    #             if len(solution[1][Examiner][i]) > 1:
    #                 examiner_cost += 1
    #         for Supervisor in single_assignment['Supervisor']:
    #             if solution[2][Supervisor][i] > 1:
    #                 supervisor_cost += 1
    #         if solution[3][single_assignment['Room']][i] > 1:
    #             room_cost += 1

    #Examiner, Supervisor and Room can't be reserved more than once
    for Examiner in solution[1]:
        for i in range(slots):
            if len(solution[1][Examiner][i]) > 1:
                examiner_cost += 1
                # print("Examiner reserved in same slot violated")
    for Supervisor in solution[2]:
        for i in range(slots):
            if solution[2][Supervisor][i] > 1:
                supervisor_cost += 1
    # for Room in solution[3]:
    #     for i in range(179):
    #         if solution[3][Room][i] > 1:
    #             room_cost += 1
    
    # maxmimum number of rooms*13 for day 
    # slot*number
    for slot in range(slots):
        x=0
        for i in range(len(solution[0])):
            if(solution[0][i]['Time']==slot):
                x+=1
        if(x>len(solution[3])):
            room_cost += x-len(solution[3])
            # print("More slots than rooms")       

    for Examiner in solution[1]:
        for day in range(days):
            temp = 0
            flag1=False
            for slot in range(15):
                time = day * 15 + slot
                if (len(solution[1][Examiner][time]) >= 1):
                    if (time - temp - 1 >= 2 and flag1):
                            examiner_cost += (time - temp - 1)
                            # print("Continouty violated")
                    flag1=True
                    temp = time  

    # for Examiner in solution[1]:
    #     for day in range(12):
    #         last_seen = 0
    #         found = False
    #         for slot in range(15):
    #             time = day * 15 + slot
    #             if len(solution[1][Examiner][time]) >= 1:
    #                 if not found:
    #                     found = True
    #                 else:
    #                     if (time - last_seen - 1) >= 2:
    #                         examiner_cost += (time - last_seen - 1)
    #                     found = False
    #                 last_seen = time

    # #Examiner in more than one room in a single day
    # for Examiner in solution[1]:
    #     for day in range(12):
    #         rooms = []
    #         for slot in range(15):
    #             time = day * 15 + slot
    #             if len(solution[1][Examiner][time]) >= 1:
    #                 rooms=[set(solution[1][Examiner][time])]
    #         if len(rooms) > 1:
    #             examiner_cost += len(rooms)
    
    
    # # Maximum number of rooms in slot
    # nrooms = len(solution[7])
    # arooms = [0]*180
    # z=0
    # while(z<len(solution[0])):
    #     time = solution[0][z]['Time']
    #     arooms[time] +=1
    #     z+=1
    # for x in arooms:
    #     if(x>nrooms):
    #         room_cost+=x-nrooms



    #Examiner violated time constraints
    for Examiner in solution[1]:
        l = []
        for c in solution[4][Examiner]:
            if(solution[4][Examiner][c]==1):
                l.append(c)
        for i in range(len(l)):
            if len(solution[1][Examiner][l[i]]) >= 1:
                examiner_cost += 1
                # print("Examiner time constraint violated")


    # Examiner has more than 2 days
    for Examiner in solution[1]:
        working_days = 0
        for day in range(days):
            for slot in range(15):
                time = day*15 + slot
                if len(solution[1][Examiner][time]) >= 1:
                    working_days += 1
                    break
        if working_days > 2:
            examiner_cost += working_days-2
    # print("Examiner has more than 2 days violated")

    #Time cosntraints
    for Examiner in solution[1]:
        for day in range(days):
            for slot in range(15):
                time = day*15 + slot
                if len(solution[1][Examiner][time]) >= 1 and solution[4][Examiner][time] == 1:
                    examiner_cost += 1


    


    #less than 3 or more than 10 slots per day
    # for Examiner in solution[1]:
    #         for day in range(12):
    #             temp = 0        
    #             for slot in range(15):
    #                 time1 = day*15 + slot
    #                 if len(solution[1][Examiner][time1]) >= 1:
    #                     temp +=1
    #             if solution[6][Examiner] <= 10:
    #                 if(temp<3 and temp>0):
    #                     examiner_cost+=1
    #             else:
    #                 if (temp > 10):
    #                     examiner_cost+=1
    #                 if(temp<3 and temp>0):
    #                     examiner_cost+=1 
    # for Examiner in solution[1]:
    #         for day in range(12):
    #             temp1 = 0        
    #             for slot in range(15):
    #                 time1 = day*15 + slot
    #                 if len(solution[1][Examiner][time1]) >= 1:
    #                     temp1 +=1
    #             if(temp1>10 or (temp1<3 and temp1>0)):
    #                 examiner_cost += 1
    


    # less than 3 or more than 10 slots per day
    # for Examiner in solution[1]:
    #         for day in range(12):
    #             temp = 0        
    #             for slot in range(15):
    #                 time1 = day*15 + slot
    #                 if len(solution[1][Examiner][time1]) >= 1:
    #                     temp +=1
    #             if(temp>10):
    #                 examiner_cost+=1
    #             if(temp<3 and temp>0):
    #                 examiner_cost+=1
                    


    
    return examiner_cost,supervisor_cost,room_cost


    
