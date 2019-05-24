import discord

from discord.ext import commands

discordToken = open("token.not_bananice").readline()

discordClient = commands.Bot(command_prefix = 'n!')

@discordClient.event
async def on_ready():
    print('Bot ready')
    await discordClient.change_presence(activity = discord.Game("with Elicchi"))

discordClient.run(discordToken)