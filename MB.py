import atexit
import discord
from discord.ext import commands
from discord import app_commands
from time import sleep
from dotenv import load_dotenv
import os

mod_list = {"poseidon4767": 770668401471389716}
insults = ["Your momma's so fat that she's blocking my panoramic view!🤣",
           "If laughter is the best medicine, your face must be curing the world!🤣",
           "You're so dense, light bends around you!🤣",
           "You're so old, your birth certificate says 'expired' on it!🤣",
           "You're like Monday mornings—everyone wants to skip over you!🤣",
           "You are the proof that even evolution can go in reverse!🤣",
           "You're like a cloud. When you disappear, it's a beautiful day!",
           "You're not completely useless. You can always serve as a bad example!🤣",
           "Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology!🤣",
           "I'd agree with you, but then we'd both be wrong!🤣",
           "You're like a software update. Whenever I see you, I think, 'Not now.'",
           "You're as bright as a black hole and twice as dense!🤣",
           "You bring everyone so much joy when you leave the room!🤣",
           "You're like a candle in the wind—utterly useless during a power outage!🤣",
           "If ignorance is bliss, you must be the happiest person on the planet!🤣",
           "You must have been born on a highway, because that's where most accidents happen!🤣",
           "You're not stupid; you just have bad luck thinking!🤣"]
banned = ["fuck", "motherfucker", "bitch", "fucking", "fucker", "penis",
          "tits", "boobs", "ass", "adolf", "hitler", "nazism", "dogshit",
          "shitheads", "hoe", "nazi", "hentai", "porn", "nigger", "nigga",
          "whore", "slut", "asshole", "dick", "rape"]

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
OWNER_ID = 770668401471389716

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, interactions=discord.Interaction)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}!")


@bot.tree.command(name="info", description="Shows MB bio!")
async def info_slash(interactions):
    await interactions.response.send_message(f"Hey I'm MB👋🏽  It's so nice to "
                                             f"meet you <@{interactions.user.id}>!\n"
                                             "I was developed by Poseidon as an "
                                             "experimental project. I am your one-stop "
                                             "solution for **FREE** auto moderation on your "
                                             "server!\nJust type '/' and you will get a "
                                             "list of commands that you can use!"
                                             " Descriptions are also attached for "
                                             "newbies😄.\n\nPS: I'm still under development"
                                             " so you might face some issues. Please don't "
                                             "get angry on me🥺. Poseidon will fix all "
                                             "issues, if you're facing any ASAP, I promise!")


#Greetings
@bot.tree.command(name="hello", description="Greets the user")
async def hello_slash(interactions):
    await interactions.response.send_message(f"Hello <@{interactions.user.id}>!"
                                             f" MB at your service!😎")


#Show modlist
@bot.tree.command(name="modlist", description="Shows MB mod list")
async def modlist_slash(interactions):
    await interactions.response.send_message("Mods:\n" + "\n".join(mod_list.keys()))


#Shutdown MB
@bot.tree.command(name="shutdown", description="MB shuts down"
                                               "(authorised to Poseidon only)")
async def shutdown_slash(interactions):
    author_id = interactions.user.id
    if author_id == OWNER_ID:
        await interactions.response.send_message("Shutting down...")
        sleep(1.3)
        await bot.close()
    else:
        await interactions.response.send_message("Bro doesn't have the perms to do "
                                                 "that, lol!")


#add numbers
@bot.tree.command(name="add", description="Adds numbers")
@app_commands.describe(number1="First number", number2="Second number",
                       number3="Third number", number4="Fourth number",
                       number5="Fifth number")
async def add_slash(interactions: discord.Interaction, number1: int,
                    number2: int = 0, number3: int = 0,
                    number4: int = 0, number5: int = 0):
    numbers = [number1, number2, number3, number4, number5]
    result = sum(numbers)
    await interactions.response.send_message(f"Sum: {result}")


#subtract numbers
@bot.tree.command(name="subtract", description="Subtracts numbers")
@app_commands.describe(number1="First number", number2="Second number",
                       number3="Third number", number4="Fourth number",
                       number5="Fifth number")
async def subtract_slash(interactions: discord.Interaction, number1: int,
                         number2: int = 0, number3: int = 0,
                         number4: int = 0, number5: int = 0):
    numbers = [number1, number2, number3, number4, number5]
    result = number1 - sum(numbers[1:])
    await interactions.response.send_message(f"Difference: {result}")


#multiply numbers
@bot.tree.command(name="multiply", description="Multiplies numbers")
@app_commands.describe(number1="First number", number2="Second number",
                       number3="Third number", number4="Fourth number",
                       number5="Fifth number")
async def multiply_slash(interactions: discord.Interaction, number1: int,
                         number2: int = 1, number3: int = 1,
                         number4: int = 1, number5: int = 1):
    numbers = [number1, number2, number3, number4, number5]
    product = 1
    for number in numbers:
        product *= number
    await interactions.response.send_message(f"Product: {product}")


#ping
@bot.tree.command(name="ping", description="Check MB's latency")
async def ping_slash(interactions):
    latency = bot.latency * 1000
    await interactions.response.send_message(f"Pong! 🏓\n{latency:.2f} ms")


#Bot Updates
@bot.tree.command(name="post_update", description="Posts new MB updates! (authorised "
                                                  "to Poseidon only)")
@app_commands.describe(message="MB Updates")
async def post_update_slash(interactions, message: str):
    if interactions.user.id != OWNER_ID:
        await interactions.response.send_message("Bro doesn't have the perms to do that, "
                                                 "lol!", ephemeral=True)
        pass
    else:
        for guild in bot.guilds:
            channel = discord.utils.get(guild.text_channels, name="announcements")
            if not channel:
                channel = discord.utils.get(guild.text_channels, name="general")
            if not channel:
                channel = discord.utils.get(guild.text_channels, name="chat")

            if channel and isinstance(channel, discord.TextChannel):
                try:
                    await channel.send(f"# MB new updates!\n{message}")
                    print(f"Sent update to {guild.name} in {channel.name}")
                except discord.Forbidden:
                    print(f"Missing permissions to update in {guild.name}")
            else:
                print(f"No suitable channel found in {guild.name}")

        await interactions.response.send_message("Update posted in all servers.",
                                                 ephemeral=True)


@atexit.register
def cleanup():
    print("Cleaning up resources...")
    bot.http.connector.close()


bot.run(BOT_TOKEN)