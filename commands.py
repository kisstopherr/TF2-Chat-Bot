import os

file_path = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/console_chatlog.txt"

def loadCommand(functionName):
    try:
        globals()[functionName]()
        clearChatLog()
        #print(f"Command '{functionName}' executed successfully.")
    except KeyError:
        print(f"Function '{functionName}' is not defined.")
    except Exception as e:
        print(f"An error occurred while executing '{functionName}': {e}")

def clearChatLog():
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("")


#COMMAND FUNCTIONS-----------------

def ping():
    print("PONG")

def help():
    print("GITHUB")
