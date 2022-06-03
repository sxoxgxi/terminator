import discord

terminator = discord.Client()
token = "bot token inside here"

# servers not to leave: down here
whitelist = []


@terminator.event
async def on_ready():
    for guild in terminator.guilds:
        try:
            if guild.id not in whitelist:
                server = terminator.get_guild(guild.id)
                await server.leave()
        except Exception as uwu:
            print(uwu)

# when the bot runs it will leave all the server except for the whitelisted ones
terminator.run(token, bot=True)
