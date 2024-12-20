import discord
from discord.ext import commands
import random 
import os 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def moneda(ctx):
    x=random.randint(1,2)
    await ctx.send(x)
    if x==1:
        await ctx.send(f"GANASTE {x}")
    else:
        await ctx.send(f"PERDISTE {x}")
@bot.command()
async def mem(ctx):
    with open('img/meme2.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def memepelon(ctx):
    with open('img/momazopelon.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def momazo(ctx):
    with open('img/meme3.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def Dragonzord(ctx):
    with open('img/dragonzord.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


print(os.listdir('img'))
# ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
with open(f'img/{Dragonzord}', 'rb') as f:
            picture = discord.File(f)

bot.run("MTI4NDI5ODMzNDgwMjI4MDQ3Mw.Gbzdpq.2U9OTcnLanI9aaNYH2flCMu4fRAh5u9gIY0ihk")
