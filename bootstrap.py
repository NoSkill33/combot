import discord
from discord import app_commands
from discord.ext import commands

import webbrowser

import os
from datetime import datetime

# pobieranie aktualnej daty na starcie programu w celu stworzenia min. plików z logami itp
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# definicje
version = "[0.0.02] " # wersja bota ( kiedyś można dodać "checka" czy bot jest aktualny z wersja z githuba )
botname = "[combot] " # nazwa bota z reguły będziemy z niej korzystać tylko do textu w konsoli ale kto wie
developermode = 1 # ustawić na 0 kiedy nic nie aktualizujemy(czyli kiedy pushujemy zmiane na discord)!!! ( wtedy "reklama" naszego repozytorium z botem sie odpala na starcie programu )

# przekształcenie informacji w string
str_current_datetime = str(current_datetime)

# ścieżki do folderów(?)
logs_folder = os.path.join(os.getcwd(), 'logs')
messages_folder = os.path.join(os.getcwd(), 'messages')

# ładowanie tokenu z pliku...
with open('token.txt', 'r') as file:
    token = file.read()

# funkcja zapisująca treść do pliku
def logsave(text):
    # na starcie logsave niech "zdobedzie" aktualna date lol
    actualdate = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    logs_folder = os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_folder, exist_ok=True)

    direct = os.path.join(logs_folder, current_datetime + ".log")

    with open(direct, 'a') as file:
        file.write("[" + actualdate + "] " + text + "\n")

def messagelog(text):
    # na starcie logsave niech "zdobedzie" aktualna date lol
    actualdate = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    messages_folder = os.path.join(os.getcwd(), 'messages')
    os.makedirs(messages_folder, exist_ok=True)

    direct = os.path.join(messages_folder, current_datetime + ".log")

    with open(direct, 'a', encoding="utf-8") as file:
        file.write("[" + actualdate + "] " + text + "\n")
# koniec tej funkcji

# początek classy bota
class MyClient(discord.Client):
    # otwieranie oficjalnej strony bota tak zwana "reklama"
    if developermode == 0: # jeśli edytujemy kod == 0( == nie ) wtedy dopiero odpal aby nie spamiło NAM tym xd
        webbrowser.open_new_tab("https://github.com/NoSkill33/combot")

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f"[debug] Connecting with discord api...")

    async def on_ready(self): # on_ready to jest prosty event logger... po tym jesli on_ready zostanie wykonany( czyli bot sie odpali ) ma wykonać listę rzeczy np napisanie ze bot został załadowany i tak dalej...
        if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle    
            print(f"[debug] Connected with discord api")

        # kolejność działań... najpierw najważniejsze rzeczy niech się wczytują a dopiero potem reszta
        await tree.sync() # synchronizacja komend(?) inni to robią czemu my byśmy nie mieli
        await client.change_presence(activity=discord.CustomActivity('https://github.com/NoSkill33/combot')) # jak sam opis wskazuje... ustawienie statusu gry bota na link do naszego bota na githubie
        if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
            print(f'[debug] Data & Time: {str_current_datetime}') # sprawdzałem czy wszystko działa na ten moment niech zostanie... potrzebne jeśli chcesz coś sprawdzić i nie chcesz się pierdolić i sprawdzać kiedy bota odpaliłeś :)
       
        logsave(f'Logged on as {self.user}!')
        print(f"{botname}Bot was successfully loaded")
        #print(f'Logged on as {self.user}!')

    async def on_message(self, message): # tak samo jak z on_ready, jest to prosty even logger który czeka aż user napisze jakąś wiadomość jeśli napisze to wtedy zapisuje to w pliku tekstowym
         messagelog(f'{message.author}: {message.content}')
         #print(f'Message from {message.author}: {message.content}')

# definicje
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

# komenda test
@tree.command(name = "test", description = "testowa komenda bota")
async def Testcommand(interaction: discord.Interaction):
    await interaction.response.send_message("hejka!")
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

# komenda help
@tree.command(name = "help", description = "pokazuje pomoc(?) xd")
async def helpcommand(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "HELP",
        description = "**🤖Bot** \n /ping - *komenda na ping bota* \n **Info** \n /userinfo - *komenda na informacje*",
        color = 0x8daee0,
        type = 'rich')
        
    sendto = interaction.user.id
    await interaction.response.send_message("Lista komend wysłana została wysłana prywatnie do użytkownika!")
    await interaction.user.send(embed=embed)
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

# komenda na tworzenie embed
@tree.command(name = "embed", description = "tworzenie embed(color podac 0x'hex coloru')")
async def embedcommand(interaction: discord.Interaction, title: str, description: str, color: int):
    embed = discord.Embed(title=title, description=description, color=color)
    await interaction.response.send_message(embed=embed)
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')



# komenda na ping bota
@tree.command(name = "ping", description = "komenda na ping")
async def testcommand(interaction: discord.Interaction):
    pinglatency = format(round(client.latency, 1))
    await interaction.response.send_message(f'{interaction.user.id} Ping to {pinglatency}!')
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

# komenda na id uzytkownika
@tree.command(name="userinfo", description="userinfo")
async def UserInfocommand(interaction: discord.Interaction, user: discord.User = None):
    if user is None:
        user = interaction.user

    creationdate = user.created_at
    creationdatebetter = creationdate.strftime("%Y-%m-%d %H-%M-%S")

    if user.guild:
        joindate = user.joined_at
        joindatebetter = joindate.strftime("%Y-%m-%d %H-%M-%S")
    else:
        joindatebetter = "Not a member of any server"

    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

    # Ustaw kolor embeda na kolor banera lub na inny domyślny kolor
    embed_color = 0x8daee0

    embed = discord.Embed(
        title="User Info",
        description=f'Id: **{user.id}**\n'
                    f'Name: **{user.name}**\n'
                    f'Member of discord since: **{creationdatebetter}**\n'
                    f'Member of server since: **{joindatebetter}**',
        colour = embed_color
    )

    # Ustaw awatar użytkownika jako miniaturę embeda
    embed.set_thumbnail(url=avatar_url)

    await interaction.response.send_message(embed=embed)

    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')


    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

# startup bota
client.run(token) # token jest wklejany z pliku token.txt który każdy musi sobie sam stworzyć