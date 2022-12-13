import discord
import random

TOKEN = 'MTA1MTk4NDc3Nzk1NzM1NTY4MA.G_OMu4.cY3mUT0TQhNl6vZV1kb2EmAjNDX3bq5TpDX5Tk'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents) #discord requires intent in order to run

@client.event
async def on_ready():
        print('Up and running as {0.user}'.format(client)) #indicated bot is online


@client.event
async def on_message(message):
        username = str(message.author).split('#')[0] #grabs username with hashtag
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if message.author == client.user:
            return #stops bots endless loop

        if message.channel.name == 'general': #only responds to general chat
            if user_message.lower() == 'hello': #simple responses the bot can make
                await message.channel.send(f'yo whatup {username}!')
                return
            elif user_message.lower() == 'bye':
                await message.channel.send(f'See ya later alligator!')
                return
            elif user_message.lower() == '!roll':
                response = f'You rolled a(n): {random.randrange(1, 20)}' #rollsa random die
                await message.channel.send(response)
                return

        if user_message.lower() == 'knock knock':
            await message.channel.send('*silence*') #Same as above but instead of general chat it will reply in every channel
            return

client.run(TOKEN)
