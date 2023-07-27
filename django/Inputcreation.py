from sqlite3 import Date
import pandas as pd
import numpy as np
import json


def Create_input(Name,dates,rooms):
    df_excel = pd.read_csv(Name,sep=",", encoding='cp1252')
    slots = len(dates) * 15
    # print(len(df_excel))
    External = []
    Supervisor = []
    ID = []
    Room = []
    name = []
    email = []
    topic = []

    # Dates = [""]
    # for i in range(len(df_excel)-1):
    #     Dates.append(df_excel["Defense Date"][i])
    for i in range(len(df_excel)-1):
        External.append(df_excel["External Reviewer Name"][i])
    for i in range(len(df_excel)-1):
        Supervisor.append(df_excel["GUC Supervisor"][i])
    for i in range(len(df_excel)-1):
        ID.append(df_excel["Student ID"][i])
    for i in range(len(df_excel)-1):
        name.append(df_excel["Student Name"][i])
    for i in range(len(df_excel)-1):
        email.append(df_excel["Student Email"][i])
    for i in range(len(df_excel)-1):
        if df_excel["Topic Title"][i] != None:
            topic.append(df_excel["Topic Title"][i])
        else:
            topic.append("")
        
        
    Room2=list(set(Room))
    External2=list(set(External))
    Supervisor2=list(set(Supervisor))


    dictionary = {
        "Rooms": rooms,
        "Defense": []
    }
    dic2 ={}
    for i in range(len(External)):
        dic ={
            "Examiner":External[i],
            "Supervisor":Supervisor[i],
            "Student": ID[i],
            "Studentname": name[i],
            "Studentemail": email[i],
            "Topic": topic[i]
        }
        dictionary["Defense"].append(dic)
    dic2 = {}   
    for i in range(len(External2)):
        dic2[External2[i]]=[0]*slots  

    
    dic3 = {}
    for i in range(len(Supervisor2)):
        dic3[Supervisor2[i]]=[0]*slots
        
    dic4 = {}
    dic4["Dates"] = dates
        
    dictionary = dictionary , dic2 , dic3 , dic4

    # Serializing json
    json_object = json.dumps(dictionary, indent=4 ,allow_nan=True)

    # Writing to sample.json
    with open("InputData.json", "w") as outfile:
        outfile.write(json_object)
    return "InputData.json"


