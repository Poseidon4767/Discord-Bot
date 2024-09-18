# Discord-Bot
How to make a discord bot?
A simple auto-moderation bot made in python.

Python Modules Requirements:
1. atexit
2. discord.py
3. dotenv (optional but recommended)

HIGHLY RECOMMENDED!
Make an environment variable in the same directory, named ".env". Save your bot token inside like this:
"TOKEN=YOUR_BOT_TOKEN".

If you do not want to use environment variables, remove the lines "from dotenv import load_dotenv" and "load_dotenv()" from the code, and modify the line "BOT_TOKEN = os.getenv('TOKEN')" with BOT_TOKEN = your actual token here".
