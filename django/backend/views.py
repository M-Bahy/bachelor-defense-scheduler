from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import data as dt
import json
import algorithm as algo
from Inputcreation import Create_input
from django.http import HttpResponse


@api_view(["POST"])
def uploadFile(request):
    if request.method == "POST":
        upload = request.data.get("File")
        data = upload.read()
        f = open(upload.name, "wb")
        f.write(data)
        f.close()
        Create_input(
            upload.name,
            request.data.get("Dates").split(","),
            request.data.get("Rooms").split(","),
        )
        return Response({"data": "done"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def downloadFile(request):
    if request.method == "GET":
        f = open("Solution.csv", "r")
        response = HttpResponse(f.read(), content_type="text/csv")
        return response


@api_view(["POST"])
def generate(request):
    if request.method == "POST":
        res = []
        with open("InputData.json", "r") as read_file:
            inputData = json.load(read_file)
        w = algo.evolutionary_algorithm()
        for i in w[0]:
            if i.get("color") == "Red":
                res.append(i)
        return Response(w, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_iterations(request):
    if request.method == "GET":
        iterations = algo.get_iterations()
        return Response({"iterations": iterations}, status=status.HTTP_200_OK)


@api_view(["POST", "GET", "DELETE"])
def external(request):
    if request.method == "POST":
        with open("InputData.json", "r") as read_file:
            inputData = json.load(read_file)
        print(inputData[1])
        ename = list(request.data.keys())[0]
        eslots = request.data[ename]
        inputData[1][ename] = eslots
        json_object = json.dumps(inputData, indent=4)
        with open("InputData.json", "w") as outfile:
            outfile.write(json_object)

        return Response(inputData)
    elif request.method == "DELETE":
        pass
    elif request.method == "GET":
        data = request.data
        inputData = dt.load_data("InputData.json")
        if data.get("Name"):
            res = [{}] * 180
            for i in inputData:
                if data.get("Name") == i["Examiner"]:
                    res[i.get("Time")] = i
            return Response({"data": res}, status=status.HTTP_200_OK)
        return Response({"data": inputData}, status=status.HTTP_200_OK)


@api_view(["GET"])
def getAllExternals(request):
    if request.method == "GET":
        (
            defense,
            rooms,
            external_constraints,
            supervisor_constraints,
            external,
            supervisor,
            ex,
            dates,
        ) = dt.load_data("InputData.json")
        return Response(
            {"externals": external, "dates": dates}, status=status.HTTP_200_OK
        )


@api_view(["POST", "GET", "DELETE"])
def supervisor(request):
    if request.method == "POST":
        inputData = dt.load_data("InputData.json")
        print(request)
        inputData["Supervisor constraints"]
        return Response(inputData)
    elif request.method == "DELETE":
        pass
    elif request.method == "GET":
        inputData = dt.load_solution("Solution.json")
        data = request.data
        if data.get("Name"):
            res = [{}] * 180
            for i in inputData:
                if data.get("Name") == i["Supervisor"]:
                    res[i.get("Time")] = i
            return Response({"data": res}, status=status.HTTP_200_OK)
        return Response({"data": inputData}, status=status.HTTP_200_OK)


@api_view(["GET"])
def getAllSupervisors(request):
    if request.method == "GET":
        (
            defense,
            rooms,
            external_constraints,
            supervisor_constraints,
            external,
            supervisor,
            ex,
        ) = dt.load_data("inputData.json")
        return Response({"data": supervisor}, status=status.HTTP_200_OK)


@api_view(["POST", "GET", "DELETE"])
def student(request):
    if request.method == "POST":
        inputData = dt.load_data("InputData.json")
        print(request)
        inputData["Student constraints"]
        return Response(inputData)
    elif request.method == "DELETE":
        pass
    elif request.method == "GET":
        inputData = dt.load_solution("Solution.json")
        data = request.data
        if data.get("Name"):
            res = [{}] * 180
            for i in inputData:
                if data.get("Name") == i["Student"]:
                    res[i.get("Time")] = i
            return Response({"data": res}, status=status.HTTP_200_OK)
        return Response({"data": inputData}, status=status.HTTP_200_OK)
