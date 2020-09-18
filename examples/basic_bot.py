import discord
from discord.ext import commands
import random
import requests

token_url = 'http://metadata.google.internal/computeMetadata/v1/instance/attributes/DISCORD_BOT_TOKEN'
response = requests.get(token_url, headers={'Metadata-Flavor': 'Google'})
token = response.text
channel_url = 'http://metadata.google.internal/computeMetadata/v1/instance/attributes/BOOT_LOG_CHANNEL_ID'
response = requests.get(channel_url, headers={'Metadata-Flavor': 'Google'})
channel = response.text

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = client = discord.Client().get_channel(channel)
    await channel.send(bot.user.name + 'が起動しました。')  

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

# メッセージ受信時実行イベント
async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith('にゃー'):
            rand = ('ー' * random.randint(0, 30))
            msg = "にゃ" + rand + "ん"
            await message.channel.send(msg)
            return

        if self.user in message.mentions:
            msg = message.author.mention + message.content
            await message.channel.send(msg)

bot.run(token)
