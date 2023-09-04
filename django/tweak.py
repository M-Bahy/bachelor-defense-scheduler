import json
import os
import data as dt


def main(solution):
    outfile = None
    infile = None
    if os.path.exists("Solution.json"):
        outfile = open("Solution.json", "r")
    else:
        outfile = open("django/Solution.json", "r")
    if os.path.exists("InputData.json"):
        infile = "InputData.json"
    else:
        infile = "django/InputData.json"

    json_object = json.load(outfile)

    rooms = [item["Room"] for item in json_object]
    unique_rooms = list(dict.fromkeys(rooms))
    examiners = [item["Examiner"] for item in json_object]
    supervisors = [item["Supervisor"] for item in json_object]
    students = [item["Student"] for item in json_object]
    student_names = [item["Studentname"] for item in json_object]
    student_emails = [item["Studentemail"] for item in json_object]
    topics = [item["Topic"] for item in json_object]
    times = [item["Time"] for item in json_object]
    input_data = dt.load_data(infile)
    colors = []
    corrupted_indices = []
    problems = []
    time_slots = [
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
    for i in range(len(json_object)):
        color = json_object[i].get("Color")
        if color:
            corrupted_indices.append(i)
            colors.append(color)
            problems.append((i, color))
    # colors = [item.get("Color") for item in json_object]
    # corrupted_indices = [
    #     colors.index(item) for item in colors if item is not None
    # ]
    # reasons = [colors[item] for item in corrupted_indices]
    errors = [
        "Examiner assigned for less than 3 slots per day or more than 10 slots per day",
        "Examiner assigned for more than 2 days",
        "more than 2 per slot for examiner",
        "more than 2 per slot for supervisor",
        "more slots than room",
        "Examiner assigned in his day off",
        "Supervisor assigned in his day off",
    ]

    for i in range(len(problems)):
        index = problems[i][0]
        color = problems[i][1]
        if color == errors[0]:
            examiner = examiners[index]
            time = times[index][0:10]
            slots = 0
            for item in json_object:
                if item["Examiner"] == examiner and item["Time"][0:10] == time:
                    slots += 1
            print(f"Examiner {examiner} assigned for {slots} slots on {time}")
            if slots < 3:
                for unique_room in unique_rooms:
                    count = 0
                    booked_times = []
                    for item in json_object:
                        if (
                            item["Room"] == unique_room
                            and item["Time"][0:10] == time
                        ):
                            count += 1
                            booked_times.append(item["Time"][11:16])
                    print(
                        f"The room {unique_room} is booked for {count} times on {time}"
                    )
                    if count < 15:
                        pass
                    print(
                        f"On {time} the room {unique_room} is booked for {count} times , the booked times are {booked_times}"
                    )


if __name__ == "__main__":
    main(None)
