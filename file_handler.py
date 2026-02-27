import json
import os

FILE_NAME = "tasks.txt" # this avoids hardcoding everywhere.



def load_tasks():
    tasks = [] # to load all the task from file to list
    #Check if file exists
# if not → return empty list
    if not os.path.exists(FILE_NAME):
        return tasks

    with open(FILE_NAME,'r') as file : # with for auto closer
        for line in file: # loop through lines
            line = line.strip()

            if line:
                task = json.loads(line) #convert json to dictionary
                tasks.append(task) #Append to list
    return tasks # Return list

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file: # "w" mode resets the file completly.,
    # If file exists → erase it
    # If not exist → create it
     for task in tasks: #loops through dictionary
        # json.dumps(task)   convert dictionary to json
        file.write(json.dumps(task) + "\n") #"\n makes sure next task goes to a (new )next line
