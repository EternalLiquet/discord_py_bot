import discord

from discord.ext import commands

DiscordToken = open("token.not_bananice").readline()

DiscordClient = commands.Bot(command_prefix = 'n!')

@DiscordClient.event
async def on_ready():
    print('Bot ready')

DiscordClient.run(DiscordToken)