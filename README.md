# Palmi'BOT

## Goal of this bot

- manage deadlines of projects
- manage categories (creating all the needed channels) and setting the permissions
  - modular creation of the channels (selecting all the needed channels)
- communicate with the Google Calendar of the association
  - adding events, depending on the user for the needed tasks

### TODOs

- [ ] todo1 

## Installation  requierements

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
VAR1 = "<SECRET_TOKEN>"
``` 
