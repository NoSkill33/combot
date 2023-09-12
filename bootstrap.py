import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1MTI0MDEyMjYyNTQzMzcxMg.GzH02_.bOKuoeHeUNgJflXp_BQyPxv2i9Gip5KDkYQxOU')