import discord

terminator = discord.Client()
token = "bot token inside here"

# channels not to leave: down here
whitelist = [
    775232281954353183,
    841202740507181106
]


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
