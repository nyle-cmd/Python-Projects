import discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
import responses #import discord and response file


async def send_message(message, user_message, is_private): #define everything
    try: #add a try and catch block
            response = responses.handle_response(user_message) #grabs user message
            await message.author.send(response) \
                if is_private \
                else await message.channel.send(response)
    except Exception as e:
            print(e) #incase of exception code will print it out

def run_discord_bot():
    TOKEN = 'SECRET WORDS'
    client = discord.Client(intents=discord.Intents.default()) #adds token and client

    @client.event
    async def on_ready():
        print(f'{client.user} is up and running!') #bot says if client is running correctly

    @client.event
    async def on_message(message):
        embeds = message.embeds  # return list of embeds
        for embed in embeds:
            print(embed.to_dict())  # it's content of embed
        if message.author == client.user:
            return # <- prevents endless loops

        username = str(message.author) #grabs username of whoever called bot
        user_message = str(message.content)
        channel = str(message. channel)  #grabs channel

        print(f"{username} said: '{user_message}' ({channel})") #for debugging

        # will send private message
        if user_message.startswith("!"):
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
        else:
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
