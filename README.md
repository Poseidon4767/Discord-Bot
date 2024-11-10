# Discord-Bot
### Read the license first. ###
How to make a discord bot?
A simple auto-moderation bot made in python.

# Requirements
Python Modules Requirements:
1. atexit
2. discord.py
3. dotenv (optional but recommended)

## HIGHLY RECOMMENDED! ##
Make an environment variable in the same directory, named ".env". Save your bot token inside the environment variable  like this:
"TOKEN=YOUR_BOT_TOKEN".

# Important
If you do not want to use environment variables, remove the lines "from dotenv import load_dotenv" and "load_dotenv()" from the code, and modify the line "BOT_TOKEN = os.getenv('TOKEN')" with BOT_TOKEN = your actual token here".
