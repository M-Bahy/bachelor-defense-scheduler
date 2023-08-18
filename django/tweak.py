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
    examiners = [item["Examiner"] for item in json_object]
    supervisors = [item["Supervisor"] for item in json_object]
    students = [item["Student"] for item in json_object]
    student_names = [item["Studentname"] for item in json_object]
    student_emails = [item["Studentemail"] for item in json_object]
    topics = [item["Topic"] for item in json_object]
    times = [item["Time"] for item in json_object]
    colors = [item.get("Color") for item in json_object]
    input_data = dt.load_data(infile)
    corrupted_indices = [
        colors.index(item) for item in colors if item is not None
    ]
    reasons = [colors[item] for item in corrupted_indices]
    errors = [
        "Examiner assigned for less than 3 slots per day or more than 10 slots per day",
        "Examiner assigned for more than 2 days",
        "more than 2 per slot for examiner",
        "more than 2 per slot for supervisor",
        "more slots than room",
        "Examiner assigned in his day off",
        "Supervisor assigned in his day off",
    ]

    for i in range(len(corrupted_indices)):
        pass


if __name__ == "__main__":
    main(None)
