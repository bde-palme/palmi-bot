# Palmi'BOT

## Goal of this bot

- manage deadlines of projects
- manage categories (creating all the needed channels) and setting the permissions
  - modular creation of the channels (selecting all the needed channels)
- communicate with the Google Calendar of the association
  - adding events, depending on the user for the needed tasks
- find avaible time slots for meetings by searching across the members's agendas via the .ics file exported from ADE.

## Commands :

- [ ] create project (name) : create the channels (suggestions are made and the user can choose between them or add other channels) and set the permissions for the project (create a role...)
- [ ] add task (name, description, deadline, person in charge, reminders frequency, task it depends on, type of result) : add a task to the project and set the deadline and the person in charge. From there, the bot will send reminders to the person in charge, if the task is not done yet and that the tasks it depends on are done. When the task is done the person in charge have to send the result (a file, a message, a link, or nothing if the task has no result).
- [ ] add agenda : add the .ics file of the user to the bot's database
- [ ] find meeting (deadline) : find the avaible time slots for a meeting, depending on the members's agendas. The bot will send private message to the members to ask them if they are avaible at the time slots found. After the deadline, the bot will send a message in a channel to tell the time of the meeting.

### TODOs

- [ ] todo1

## Installation requierements

### Virtual Environment

Create the virtual environment (if not created) :

```bash
python3 -m venv .palmibot-venv/
```

Then activate the environment to properly install the depedencies :

```bash
source .palmibot-venv/bin/activate
```

Finally install the depedencies :

```bash
python3 -m pip install -r requirements.txt
```

### Config File

The file `config.py` will contain all the private tokens and informations needed to run your bot. **You have to define it yourself**. Its content is the following :

```python
# --------------------------------------------------------------
# FILE config.py
# contains all needed secret data to operate properly
# --------------------------------------------------------------

DISCORD_TOKEN="<SECRET_TOKEN>" 
GOOGLE_API_FILE="<PATH_TO_FILE>"  
```
