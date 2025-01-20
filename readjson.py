import json


def read_josn(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(type(data))
        print(data)
        return data

file_path = "D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\data.json"
read_josn(file_path)