import discord
from discord.ext import commands
from model import get_class
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$",intents=intents)

users = []
wanted_list =[]
warning_edge = 10
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
@bot.command()
async def helo(ctx):
    await ctx.send("hi")
@bot.command()
async def check_photo(ctx, name1, surname, plec, group:int):
    global wanted_list
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            ctx.send("Mam załącznik...")
            file_name = attachment.filename
            plEc = ''
            zle = False
            if plec == 'M':
                plEc = 'mezczyzna '
                zle = False
            elif plec == 'K':
                plEc = 'kobieta '
                zle = False
            else:
                await ctx.send("zła odpowiedz")
                zle = True
            if group <= 14 and zle == False:
                plEc += '0-14'
            elif group <= 37 and zle == False:
                plEc += '15-37'
            elif group <= 54 and zle == False:
                plEc += '38-54'
            elif group <= 68 and zle == False:
                plEc += '55-68'
            elif group >= 69 and zle == False:
                plEc += '69+'
            else:
                await ctx.send("zła odpowiedz")
                zle = True
            await attachment.save(f'./{file_name}')
            #await ctx.send(get_class('./keras_model.h5','./labels.txt', f'./{file_name}' ))
            image = Image.open(file_name)
            result_model = get_class("keras_model.h5", "labels.txt", file_name)
            if zle == True:
                break
            if result_model == plEc:
                await ctx.send("Identyfikacja zakończona: Jesteś tym, za kogo się podajesz.")
                users.append({
                    (name1, surname): {"cechy": [plec, group, image]}
                })
                print(users)
            elif result_model == "Nie jestem pewny, kto to jest":
                await ctx.send("Algorytm nie potrafił określić osoby na zdięciu. Spróbuj ponownie.")
            else:
                wanted_list.append({
                    (name1, surname): {"cechy": [plec, group, image], "wynik": result_model}
                })
                print(result_model)
    else:
        await ctx.send("nie przesłałeś załącznika")
    if len(wanted_list)+1 > warning_edge:
        print("wykryto", warning_edege, "osób do sprawdzenia")
        print(wanted_list)
        warning_edge+=5
bot.run("token")
