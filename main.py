import time
import json
import os
import commands

username = "yourname"
botPrefix = "/"
commandChat = f"{username} :  {botPrefix}"
currentCommand = ""

def readChatLog(file_path):
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if commandChat in line:
                commandLine = line.strip()
                currentCommand = commandLine[len(commandChat):].strip()
                #print("/" + currentCommand)
                findCommands(currentCommand)

def findCommands(command_string):
    with open('commands.json', 'r') as file:
        commands_data = json.load(file)

    for command_data in commands_data["commands"]:
        for command_name, command_info in command_data.items():
            if command_string == command_name:
                function_name = command_info["function"]
                commands.loadCommand(function_name)
                #print("Command ran:", function_name)
                return True
    #print("Command not found")
    return False

if __name__ == "__main__":
    log_file = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/console_chatlog.txt"
    
    while True:
        readChatLog(log_file)
        time.sleep(1)
