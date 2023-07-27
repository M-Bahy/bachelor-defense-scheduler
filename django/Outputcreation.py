import json
import csv

def Create_output():

    with open('Solution.json') as json_file:
        data = json.load(json_file)
    #csv_file = csv.writer(json_file,lineterminator='\n')

    student_data = data
    solution_file = open('Solution.csv', 'w', newline="")
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
