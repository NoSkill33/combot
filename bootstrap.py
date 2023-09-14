import discord
from discord import app_commands
from discord.ext import commands

import os
from datetime import datetime

# pobieranie aktualnej daty na starcie programu w celu stworzenia min. plików z logami itp
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# przekształcenie informacji w string
str_current_datetime = str(current_datetime)

# ścieżki do folderów(?)
logs_folder = os.path.join(os.getcwd(), 'logs')
messages_folder = os.path.join(os.getcwd(), 'messages')

# ładowanie tokenu z pliku...
with open('token.txt', 'r') as file:
    token = file.read()

# funkcja zapisująca treść do pliku
def logsave(filename, text):
    logs_folder = os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_folder, exist_ok=True)

    direct = os.path.join(logs_folder, filename)

    with open(direct, 'a') as file:
        file.write(text + "\n")

def messagelog(filename, text):
    messages_folder = os.path.join(os.getcwd(), 'messages')
    os.makedirs(messages_folder, exist_ok=True)

    direct = os.path.join(messages_folder, filename)

    with open(direct, 'a') as file:
        file.write(text + "\n")
# koniec tej funkcji

# początek classy bota
class MyClient(discord.Client):
    async def on_ready(self):
        # kolejność działań... najpierw najważniejsze rzeczy niech się wczytują a dopiero potem reszta
        await tree.sync() # synchronizacja komend(?) inni to robią czemu my byśmy nie mieli
        await client.change_presence(activity=discord.Game('https://github.com/NoSkill33/combot')) # jak sam opis wskazuje... ustawienie statusu gry bota na link do naszego bota na githubie
        print(f'[debug] Data & Time: {str_current_datetime}') # sprawdzałem czy wszystko działa na ten moment niech zostanie... potrzebne jeśli chcesz coś sprawdzić i nie chcesz się pierdolić i sprawdzać kiedy bota odpaliłeś :)
        logsave(str_current_datetime, f'Logged on as {self.user}!')
        #print(f'Logged on as {self.user}!')

    async def on_message(self, message):
         messagelog(str_current_datetime, f'{message.author}: {message.content}')
         #print(f'Message from {message.author}: {message.content}')

# definicje
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

# przykładowa komenda / testowa komenda
@tree.command(name = "test", description = "test")
async def testcommand(interaction: discord.Interaction):
    await interaction.response.send_message("test")


# komenda Ping odpowiedz pong
@tree.command(name = "PingPong", description = "PingPong")
async def PingCommand(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

# startup bota
client.run(token)