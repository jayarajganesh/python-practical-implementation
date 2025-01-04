import csv

def read_csv(file_path):
    with open(file_path, mode = 'r') as file:
        csv_reader = csv.reader(file)
        #skip header
        next(csv_reader)
        #read
        for row in csv_reader:
            print(row)

file_path = r"D:\\JOB Mission 2024-25\\BigData Engineer\\Level-1-Mock\\MockInterviewProgram\\data.csv"
read_csv(file_path)