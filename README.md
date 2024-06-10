# Chat Bot for Team Fortress 2

This project is a simple chat bot for Team Fortress 2. The bot reads chat messages from a log file and executes predefined commands.

## Features

- Execute predefined commands based on chat messages.
- Commands are defined in a JSON file for easy customization.
- Endless customization ideas

## Setup

### Prerequisites

- At least Python 3.10 installed on your system.
- Team Fortress 2 installed.

### Installation

1. Clone the repository to your local machine or download the files:

    ```sh
    git clone https://github.com/kisstopherr/TF2-Chat-Bot.git
    cd TF2-Chat-Bot
    ```

2. Create an `autoexec.cfg` file in your TF2 game (C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\cfg) directory with the following content:
   
    ```cfg
    developer 1
    con_logfile console_chatlog.txt
    con_timestamp 0
    con_filter_enable 1
    con_filter_text "/"
    bind F10 exec chatbotmsg.cfg
    ```
NOTE:
The `con_filter_text` is your bots prefix so make sure your `con_filter_text` and `botPrefix` are the same.
You can change the `F10` to any button, but make sure its the same in the `main.py` file too. 

### Setup

- Edit the `main.py` file to set the `username` and `log_file` and `botPrefix` variables as needed.

    ```python
    username = "your name"
    log_file = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/console_chatlog.txt"1
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

2. Implement the corresponding function in `commands.py`:

    ```python
    def newFunction():
        print("New command executed!")
    ```

3. The bot will now recognize and execute the new command.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
