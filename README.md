# Chat Bot for Team Fortress 2

This project is a simple chat bot for Team Fortress 2. The bot reads chat messages from a log file and executes predefined commands.

## Features

- Execute predefined commands based on chat messages.
- Commands are defined in a JSON file for easy customization.
- Endless customization ideas.

## Setup

### Prerequisites

- At least Python 3.10 installed on your system.
- Python `Keyboard` libary installed.  
- Team Fortress 2 installed.

### Installation

1. Clone the repository to your local machine or download the files:

    ```sh
    git clone https://github.com/kisstopherr/TF2-Chat-Bot.git
    cd TF2-Chat-Bot
    ```

2. Install the `keyboard` libary:

    ```sh
    pip install keyboard
    ```

3. Create an `autoexec.cfg` file in your TF2 game directory (C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\cfg) with the following content:
   
    ```cfg
    developer 1
    con_logfile console_chatlog.txt
    con_timestamp 0
    con_filter_enable 1
    con_filter_text "/"
    bind F10 exec chatbotmsg.cfg
    ``` 

4. Create an `chabotmsg.cfg` file in your TF2 game directory (C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\cfg) and leave it blank, as it will always be changing.

NOTE:
- The `con_filter_text` is your bots prefix so make sure your `con_filter_text` and `botPrefix` are the same.
- You can change the `F10` to any button, but make sure its the same in the `commands.py` file too.

### Setup

- Edit the `main.py` file to set the `username` and `log_file` and `botPrefix` variables as needed.

    ```python
    username = "your name"
    log_file = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/console_chatlog.txt"
    botPrefix = "/"
    ```

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. The bot will read the chat log every second and execute commands based on messages in the log.

### Example Commands

- **Ping Command**: Responds with "Pong" when `/ping` is detected.
- **Help Command**: Responds with "Look at the Github" when `/help` is detected.

## Adding New Commands

1. Define the command in `commands.json`:

    ```json
    {
      "new_command": {
        "function": "newFunction"
      }
    }
    ```
- The `new_command` is what the command message will look like not including the bot prefix.
- The `newFunction` should be the same as the corresponding function name in `commands.py`

2. Implement the corresponding function in `commands.py`:

    ```python
    def newFunction():
        print("New command executed!")
    ```

3. The bot will now recognize and execute the new command.

## In-Game Chat Messging

1. Make sure to have the Keyboard libary installed.

2. In your `commands.py` there is a function called `chatMessage`. To use it input a string and it will print the inputed string into the In-Game Chat.

3. Add it to your functions:

   ```python

    def ping():
       chatMessage("Pong")
   ```

- The `Keyboard` libary is required because the `chatMessage` function uses it to press F10 which runs `exec chatMessage.cfg` which prints the inputed string into the chat.

# How it works?

- The bot itself may same hard to understand, but its very simple when looked at what each file does.

1. The first thing the script does is delete the contents of the `console_chatlog.txt`.
   
2. Next it reads the contents of the file every 1 second. If it finds anything that starts with the `username` variable and the `botPrefix` then it calleds the `findCommands` function with the `currentCommand` string as an input.
   
3. In the `findCommands` function it reads the `commands.json` file and checks if the inputed string matches any commands in the `commands.json` file. If it doesn't it returns `False` otherwise it returns `True`.
   
4. If the function returns `True` it runs `commands.loadCommand(function_name)`.
   
5. In the `loadCommand` function it trys to run `globals()[functionName]()` which try to find a function name in the script with the name of the inputed `funcionName`. After that it clears the `console_chatlog.txt`
    
6. After that if no errors happen the `loadCommand` will run the inputed function which will run whatever is in it!
