import json
import random

def load_data(path):
    with open(path, 'r') as read_file:
        data = json.load(read_file)
    external = []
    supervisor = []
    rooms = data[0]["Rooms"]
    defense = data[0]["Defense"]
    external_constraints = data[1]
    supervisor_constraints = data[2]
    dates = data[3]["Dates"]
    # external_constraints = {}
    # supervisor_constraints = {}

    for i in range(len(data[0]["Defense"])):
        external.append(data[0]["Defense"][i]['Examiner'])
    for i in range(len(data[0]["Defense"])):
        supervisor.append(data[0]["Defense"][i]['Supervisor'])

    return defense,rooms,external_constraints,supervisor_constraints,set(external),set(supervisor),external,dates

def generate_solution(defense, rooms, external, supervisor,external_constraints,supervisor_constraints,externalc,days,slots):
    externals = {}
    supervisors = {}
    room = {}
    new_defense = {}
    new_data = []
    externalslots = {}


    number_of_runs = 0
    number_of_rooms = len(rooms)
    for single_external in external:
        externals[single_external] = [[]*number_of_rooms for i in range(slots)] #create 2d list of external and his rooms
        #external_constraints[single_external] = [0]*180
        externalslots[single_external] = externalc.count(single_external)
    for single_supervisor in supervisor:
        supervisors[single_supervisor] = [0]*slots
        # supervisor_constraints[single_supervisor] = [0]*180

    for single_room in rooms:
        room[single_room] = [0] * slots

    
    for single_assignment in defense:
        new_defense = single_assignment.copy()
        number = random.randrange(0,slots-1)
        while number % 5  == 0 and not(number % 3 == 0)  :
            number = random.randrange(0,slots-1)
        new_defense['Time'] = number
        room1 = random.choice(rooms)
        new_defense['Room'] = room1
        new_data.append(new_defense)
        
        externals[new_defense['Examiner']][number].append(room1)
        supervisors[new_defense['Supervisor']][number] += 1
        room[new_defense['Room']][number] += 1
        
        
    
    return new_data, externals, supervisors,room,external_constraints,supervisor_constraints,externalslots,rooms

# data = load_data("InputData.json")

# sol = generate_solution(data[0],data[1],data[4],data[5],data[2],data[3],data[6])

# print(sol[0])
# neighboring.neighbor(sol)
# print("After Swap Testing")
# print(sol[0])
# print(sol[6])
# print(sol[4])
# print(data[2])


