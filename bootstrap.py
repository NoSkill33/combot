import discord
from discord import app_commands
from discord.utils import get

import webbrowser
import random
import os
import ctypes
import logging

import time
from datetime import datetime

# pobieranie aktualnej daty na starcie programu w celu stworzenia min. plików z logami itp
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# definicje
version = "[0.0.02] " # wersja bota ( kiedyś można dodać "checka" czy bot jest aktualny z wersja z githuba )
botname = "[combot] " # nazwa bota z reguły będziemy z niej korzystać tylko do textu w konsoli ale kto wie
developermode = 1 # ustawić na 0 kiedy nic nie aktualizujemy(czyli kiedy pushujemy zmiane na discord)!!! ( wtedy "reklama" naszego repozytorium z botem sie odpala na starcie programu )

# ustawia nazwe konsoli na combot - wersja bota
ctypes.windll.kernel32.SetConsoleTitleW(f'combot - {version}')

# pozbywamy się powiadomień w ten sposób od discorda :)
logging.basicConfig(level=logging.WARNING)
logging.getLogger('discord').setLevel(logging.WARNING)
logging.getLogger('discord.client').setLevel(logging.WARNING)
logging.getLogger('discord.gateway').setLevel(logging.WARNING)

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
    print(f'{botname}is starting...')
    if developermode == 0: # jeśli edytujemy kod == 0( == nie ) wtedy dopiero odpal aby nie spamiło NAM tym xd
        webbrowser.open_new_tab("https://github.com/NoSkill33/combot")

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f"[debug] Connecting with discord api...")

    print(f'{botname}Connecting using {token[:18]}********** discord bot token')

    async def on_ready(self): # on_ready to jest prosty event logger... po tym jesli on_ready zostanie wykonany( czyli bot sie odpali ) ma wykonać listę rzeczy np napisanie ze bot został załadowany i tak dalej...
        if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle    
            print(f'[debug] Connected with discord api')
            
        print(f'{botname}Please wait...')

        # kolejność działań... najpierw najważniejsze rzeczy niech się wczytują a dopiero potem reszta
        await tree.sync() # synchronizacja komend(?) inni to robią czemu my byśmy nie mieli
        await client.change_presence(activity=discord.CustomActivity('https://github.com/NoSkill33/combot')) # jak sam opis wskazuje... ustawienie statusu gry bota na link do naszego bota na githubie
        if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
            print(f'[debug] Saved data & time: {str_current_datetime}') # sprawdzałem czy wszystko działa na ten moment niech zostanie... potrzebne jeśli chcesz coś sprawdzić i nie chcesz się pierdolić i sprawdzać kiedy bota odpaliłeś :)
            print(f'[debug] Listening to {len(client.guilds)} servers')
        
        logsave(f'Logged on as {self.user}, lisetning to {len(client.guilds)} servers!')
        print(f"{botname}Bot is ready!")
        #print(f'Logged on as {self.user}!')

    async def on_message(self, message): # tak samo jak z on_ready, jest to prosty even logger który czeka aż user napisze jakąś wiadomość jeśli napisze to wtedy zapisuje to w pliku tekstowym
         messagelog(f'{message.author}: {message.content}')
         # Wykrywanie invite do discorda i usuwanie
         if message.guild:
             if 'discord.gg/' in message.content: # jesli zrobilibysmy https://discord.gg/ to wtedy jak ktos by usunal https:// mogl by juz wyslac a zaproszenie i tak by sie wyswietlilo
                 #if message.author.guild_permissions.administrator:
                    # return

                 await message.delete()
                 await message.channel.send(f"{message.author.mention}, you're not allowed to send invite links here!")
         #print(f'Message from {message.author}: {message.content}')

# definicje
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

# komenda na kalulator
@tree.command(name="calculator", description="Kalkulator")
async def calculate(interaction: discord.Interaction, num1: str, operation: str, num2: str):
    if operation not in ['+', '-', '*', '/']:
        await interaction.response.send_message('Podaj prawidłową operację (+, -, *, /).')
        return
    
    try:
        # Sprawdzenie, czy num1 i num2 są zbyt długie
        if len(num1) > 12:
            await interaction.response.send_message('Błąd: "num1" nie może mieć więcej niż 12 znaków.')
            return
        if len(num2) > 12:
            await interaction.response.send_message('Błąd: "num2" nie może mieć więcej niż 12 znaków.')
            return
        
        # Konwersja num1 i num2 na float
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                await interaction.response.send_message('Nie można dzielić przez zero.')
                return
            result = num1 / num2

        await interaction.response.send_message(f'{num1:.2f} {operation} {num2:.2f} = {result:.2f}')
    except ValueError:
        await interaction.response.send_message('Błąd: Podane wartości num1 i num2 nie są liczbami.')
    except Exception as e:
        await interaction.response.send_message(f'Wystąpił błąd podczas obliczeń: {str(e)}')



    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

# komenda admin
storeussage = {}
@tree.command(name = "admin", description = "oznacza administratora")
async def pingadmin(interaction: discord.Interaction):
    cooldownperuser = 800
    inforole = get(interaction.guild.roles, name = 'pingadmin')
    if inforole is None:
        await interaction.response.send_message(f'Aby uzyc tej komendy to trzeba stwotzyc role o nazwie "pingadmin"')
        return
    
    if interaction.user.id not in storeussage or time.time() - storeussage[interaction.user.id] >= cooldownperuser:
        storeussage[interaction.user.id] = time.time()
        await interaction.response.send_message(f'{inforole.mention}')
        logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

        if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
            print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p
    else:
        await interaction.response.send_message(f'nie tak często!')


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
        joindatebetter = "Not a member of server"

    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

    # Ustaw kolor embeda na kolor banera lub na inny domyślny kolor
    embed_color = 0x8daee0

    if user.guild_permissions.administrator:
        isadmin = "(administrator)"
    else:
        isadmin = ""

    embed = discord.Embed(
        title="User Info",
        description=f'Id: **{user.id}**\n'
                    f'Name: **{user.name}**\n'
                    f'Member of discord since: **{creationdatebetter}**\n'
                    f'Member of server since: **{joindatebetter}**\n'
                    f'Server role: **{user.top_role} {isadmin}**',
        colour = embed_color
    )

    # Ustaw awatar użytkownika jako miniaturę embeda
    embed.set_thumbnail(url=avatar_url)

    await interaction.response.send_message(embed=embed)

    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')


    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

# komenda na info o serwerze
#...

# komenda na iq
@tree.command(name="iq", description="pokazuje iq")
async def iqcom(interaction: discord.Interaction):

    if interaction.user.id == 741339798500802572: # mieszko
        await interaction.response.send_message(f'Twoj wynik iq: {random.randint(125, 150)}!')
    elif interaction.user.id == 886353376957321307: # noskill
        await interaction.response.send_message(f'Twoj wynik iq: {random.randint(125, 150)}!')
    else: # inni XD
        await interaction.response.send_message(f'Twoj wynik iq: {random.randint(15, 125)}!')


    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')


    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p


# komenda na rzut kostkami
@tree.command(name="roll", description="rzut kostkami")
async def rollcom(interaction: discord.Interaction):

    n1 = random.randint(1, 6); n2 = random.randint(1, 6); n3 = random.randint(1, 6)
    sum = n1 + n2 + n3
    embed_color = 0x8daee0

    embed = discord.Embed(
        title="**Rzut**",
        description=f'Wyrzuciles: {n1}, {n2}, {n3}\nRazem: **{sum}**!',
        colour = embed_color
    )
    await interaction.response.send_message(embed=embed)

    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')


    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p


# koemnda na zarzadzanie rolami
@tree.command(name="role", description="Komenda na zarządzanie rolami")
async def role(interaction: discord.Interaction, option: str, user: discord.Member, role: discord.Role):
    mapermisje = interaction.user.guild_permissions.manage_roles
    
    if mapermisje:
        if option == "add":
            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f'Dodano rolę {role.mention} użytkownikowi {user.mention}.')
            else:
                await interaction.response.send_message(f'Użytkownik {user.mention} już ma rolę {role.mention}.')
        elif option == "del":
            if role in user.roles:
                await user.remove_roles(role)
                await interaction.response.send_message(f'Usunięto rolę {role.mention} użytkownikowi {user.mention}.')
            else:
                await interaction.response.send_message(f'Użytkownik {user.mention} nie ma roli {role.mention}.')
        else:
            await interaction.response.send_message('Nieprawidłowa opcja. Dostępne opcje to "add" i "del".')
    else:
        await interaction.response.send_message('Nie masz odpowiednich uprawnień do zarządzania rolami.')

 

    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')


    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p


# koemnda na zarzadzanie kanalami
@tree.command(name="channel", description="Komenda na zarządzanie kanałami")
async def channel(interaction: discord.Interaction, option: str, channel_name: str):
    mapermisje = interaction.user.guild_permissions.manage_channels
    
    if mapermisje:
        if option == "add":
            try:
                # Tworzymy kanał tekstowy
                new_channel = await interaction.guild.create_text_channel(name=channel_name)
                await interaction.response.send_message(f'Kanał o nazwie "{new_channel.name}" został dodany.')
            except discord.Forbidden:
                await interaction.response.send_message('Brak uprawnień do dodawania kanałów.')
            except discord.HTTPException:
                await interaction.response.send_message('Wystąpił błąd podczas tworzenia kanału.')

        elif option == "del":
            existing_channel = discord.utils.get(interaction.guild.channels, name=channel_name)

            if existing_channel:
                try:
                    await existing_channel.delete()
                    await interaction.response.send_message(f'Kanał o nazwie "{existing_channel.name}" został usunięty.')
                except discord.Forbidden:
                    await interaction.response.send_message('Brak uprawnień do usuwania kanałów.')
                except discord.HTTPException:
                    await interaction.response.send_message('Wystąpił błąd podczas usuwania kanału.')
            else:
                await interaction.response.send_message(f'Kanał o nazwie "{channel_name}" nie istnieje.')
        else:
            await interaction.response.send_message('Nieprawidłowa opcja. Dostępne opcje to "add" i "del".')
    else:
        await interaction.response.send_message('Nie masz odpowiednich uprawnień do zarządzania kanałami.')


 

    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')


    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p


# startup bota
client.run(token) # token jest wklejany z pliku token.txt który każdy musi sobie sam stworzyć