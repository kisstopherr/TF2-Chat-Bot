# Chat Bot for Team Fortress 2

This project is a simple chat bot for Team Fortress 2. The bot reads chat messages from a log file and executes predefined commands.

## Features

- Execute predefined commands based on chat messages.
- Commands are defined in a JSON file for easy customization.
- Includes a command to clear the chat log.

## Setup

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/chat-bot.git
    cd chat-bot
    ```

2. Create a `commands.json` file in the project directory with the following content:

    ```json
    {
      "commands": [
        {
          "ping": {
            "function": "ping"
          }
        },
        {
          "clear": {
            "function": "clearChatLog"
          }
        }
      ]
    }
    ```

### Configuration

- Edit the `chat_bot.py` file to set the `username` and `log_file` variables as needed.

    ```python
    username = "kisstopherr"
    log_file = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/console_chatlog.txt"
    ```

## Usage

1. Run the bot:

    ```sh
    python chat_bot.py
    ```

2. The bot will read the chat log every second and execute commands based on messages in the log.

### Example Commands

- **Ping Command**: Responds with "Pinging..." when a message with `/ping` is detected.
- **Clear Command**: Clears the contents of the chat log file when a message with `/clear` is detected.

## Adding New Commands

1. Define the command in `commands.json`:

    ```json
    {
      "new_command": {
        "function": "newFunction"
      }
    }
    ```

2. Implement the corresponding function in `chat_bot.py`:

    ```python
    def newFunction():
        print("New command executed!")
    ```

3. The bot will now recognize and execute the new command.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
