import discord
from discord import app_commands
from discord.utils import get

import webbrowser

import os
import time
from datetime import datetime

<<<<<<< HEAD



#-------------------------------------------------------------------------------------------------------------------------
#---------------------------POBIERANIE DATY NA STRACIE PROGRAMU BO LOGI ITP-----------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")





#-------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------DEFINICJE------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# pobieranie aktualnej daty na starcie programu w celu stworzenia min. plików z logami itp
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# definicje
>>>>>>> parent of 71196bc (improved readability)
version = "[0.0.02] " # wersja bota ( kiedyś można dodać "checka" czy bot jest aktualny z wersja z githuba )
botname = "[combot] " # nazwa bota z reguły będziemy z niej korzystać tylko do textu w konsoli ale kto wie
developermode = 1 # ustawić na 0 kiedy nic nie aktualizujemy(czyli kiedy pushujemy zmiane na discord)!!! ( wtedy "reklama" naszego repozytorium z botem sie odpala na starcie programu )

<<<<<<< HEAD




#-------------------------------------------------------------------------------------------------------------------------
#------------------------------------------ZMIENIANIE NA STRING-----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
str_current_datetime = str(current_datetime)





#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------ŚCIEŻKI DO FOLDERÓW--------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
logs_folder = os.path.join(os.getcwd(), 'logs')
messages_folder = os.path.join(os.getcwd(), 'messages')





#-------------------------------------------------------------------------------------------------------------------------
#---------------------------------------ŁADOWANIE TOKNU Z PLIKU----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
with open('token.txt', 'r') as file:
    token = file.read()






#-------------------------------------------------------------------------------------------------------------------------
#------------------------------------------ZAPISUJE TREŚĆ DO PLIKU--------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# przekształcenie informacji w string
str_current_datetime = str(current_datetime)

# ścieżki do folderów(?)
logs_folder = os.path.join(os.getcwd(), 'logs')
messages_folder = os.path.join(os.getcwd(), 'messages')

# ładowanie tokenu z pliku...
with open('token.txt', 'r') as file:
    token = file.read()

# funkcja zapisująca treść do pliku
>>>>>>> parent of 71196bc (improved readability)
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

<<<<<<< HEAD



#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------POCZĄTEK KLASY BOTA--------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# początek classy bota
>>>>>>> parent of 71196bc (improved readability)
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
         print(f'Message from {message.author}: {message.content}')

<<<<<<< HEAD





#-------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------DEFINICJE-------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# definicje
>>>>>>> parent of 71196bc (improved readability)
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

<<<<<<< HEAD


# -------------------------------------------------K O M E N D Y----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------K O M E N D Y----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------K O M E N D Y----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------K O M E N D Y----------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------KOMENDA NA KALKULATOR--------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# komenda na kalulator
>>>>>>> parent of 71196bc (improved readability)
import discord

import discord

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

<<<<<<< HEAD




#-------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------KOMENDA NA PING ADMINA------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# komenda admin
>>>>>>> parent of 71196bc (improved readability)
storeussage = {}
@tree.command(name = "admin", description = "oznacza administratora")
async def pingadmin(interaction: discord.Interaction):
    cooldownperuser = 800
    inforole = get(interaction.guild.roles, name = 'pingadmin')
    if interaction.user.id not in storeussage or time.time() - storeussage[interaction.user.id] >= cooldownperuser:
        storeussage[interaction.user.id] = time.time()
        await interaction.response.send_message(f'{inforole.mention}')
        logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

        if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
            print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p
    else:
        await interaction.response.send_message(f'nie tak często!')





#-------------------------------------------------------------------------------------------------------------------------
#------------------------------------------KOMENDA NA HELP---------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
@tree.command(name = "help", description = "pokazuje pomoc(?) xd")
async def helpcommand(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "HELP",
        description = "**🤖Bot** \n\
        /ping - *komenda na ping bota* \n\
        **Info** \n\
         /userinfo - *komenda na informacje*",
        color = 0x8daee0,
        type = 'rich')
        
    sendto = interaction.user.id
    await interaction.response.send_message("Lista komend wysłana została wysłana prywatnie do użytkownika!")
    await interaction.user.send(embed=embed)
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

<<<<<<< HEAD






#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------KOEMNDA NA TWORZENIE EMBED-------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# komenda na tworzenie embed
>>>>>>> parent of 71196bc (improved readability)
@tree.command(name = "embed", description = "tworzenie embed(color podac 0x'hex coloru')")
async def embedcommand(interaction: discord.Interaction, title: str, description: str, color: int):
    embed = discord.Embed(title=title, description=description, color=color)
    await interaction.response.send_message(embed=embed)
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')



<<<<<<< HEAD




#-------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------KOEMNDA NA PING BOTA---------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# komenda na ping bota
>>>>>>> parent of 71196bc (improved readability)
@tree.command(name = "ping", description = "komenda na ping")
async def testcommand(interaction: discord.Interaction):
    pinglatency = format(round(client.latency, 1))
    await interaction.response.send_message(f'{interaction.user.id} Ping to {pinglatency}!')
    logsave(f'{interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!')

    if developermode == 1: # jesli developermode to 1 ( czyli to z czego my mamy korzystać ) wtedy wykonaj, jesli nie to nie wykonuj i tyle
        print(f'[debug] {interaction.user.name}({interaction.user.id}) used {interaction.command.name} command!') # potrzebne jeśli chcemy sprawdzić co spowodowało dany błąd bez wchodzenia w logi ;p

<<<<<<< HEAD






#-------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------KOMENDA NA USER INFO---------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# komenda na id uzytkownika
>>>>>>> parent of 71196bc (improved readability)
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

<<<<<<< HEAD




#-------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------STARTUP BOTA----------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
=======
# startup bota
>>>>>>> parent of 71196bc (improved readability)
client.run(token) # token jest wklejany z pliku token.txt który każdy musi sobie sam stworzyć