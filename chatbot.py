import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.event
async def on_message(message):
    # noooo bot reply to itself
    if message.author == bot.user:
        return

    #questions and reply accordingly
    user_message = message.content.lower()

    #ways of asking about entering
    if any(phrase in user_message for phrase in ["how to enter", "how do i enter", "enter", "joining", "how do i join"]):
        await message.channel.send("Check the pinned comment for details on how to enter!")

    #getting a gate key
    elif any(phrase in user_message for phrase in ["how to get gate key", "where is gate key", "gate key", "how do i get the gate key"]):
        await message.channel.send("The gate key can be found in the pinned comment.")

    #asking about the general channel
    elif any(phrase in user_message for phrase in ["how to go to general channel", "general channel", "where is the general channel", "where do i go for general channel"]):
        await message.channel.send("You can find the General channel by looking at the sidebar on the left!")

    #asking about roles
    elif any(phrase in user_message for phrase in ["how to get roles", "getting roles", "role access", "how do i get roles", "how to obtain roles"]):
        await message.channel.send("Check out the #welcome channel for more info on how to get your roles.")

    
    await bot.process_commands(message)

# token
bot.run("my token wont work needs doran or liberta ig")
