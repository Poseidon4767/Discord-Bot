import atexit
import discord
from discord.ext import commands
from discord import app_commands
from time import sleep
from dotenv import load_dotenv
import os

mod_list = {"username": user_id}
OWNER_ID = "add your own user id here as an integer value"
insults = ["Add your custom insults here, like this", "You're so fat!"]
banned = ["Add your list of blocked words here, like this", "BlockedWord1"]

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, interactions=discord.Interaction)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}!")


@bot.tree.command(name="info", description="Shows bot's bio!")
async def info_slash(interactions):
    await interactions.response.send_message(f"Add your bot's bio data here.")


#Greetings
@bot.tree.command(name="hello", description="Greets the user")
async def hello_slash(interactions):
    await interactions.response.send_message(f"Hello <@{interactions.user.id}>!"
                                             f" {bot.user} at your service!😎")


#Show modlist
@bot.tree.command(name="modlist", description="Shows the bot's mod list")
async def modlist_slash(interactions):
    await interactions.response.send_message("Mods:\n" + "\n".join(mod_list.keys()))


#Shutdown MB
@bot.tree.command(name="shutdown", description="Bot shuts down"
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
@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping_slash(interactions):
    latency = bot.latency * 1000
    await interactions.response.send_message(f"Pong! 🏓\n{latency:.2f} ms")


#Bot Updates
@bot.tree.command(name="post_update", description="Posts new bot updates! (authorised "
                                                  "to the bot's owner only)")
@app_commands.describe(message="Bot Updates")
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
                    await channel.send(f"# Updates!\n{message}")
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
