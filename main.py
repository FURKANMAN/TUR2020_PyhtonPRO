import discord
import random,os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Selamun Aleyküm Kardeşm.Ben {bot.user}, bir Discord sohbet botuyum.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def random_mem(ctx):
    img_list = os.listdir("images")
    img = random.choice(img_list)
    with open(f'images/{img}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def Kagıt_Kirliligi(ctx):
    await ctx.send(f'Kağıt geri dönüşüm kutusuna at')


@bot.command()
async def Plastik_Kirliligi(ctx):
    await ctx.send(f'Plastik geri dönüşüm kutusuna at')

@bot.command()
async def Cam_Kirliligi(ctx):
    await ctx.send(f'Cam geri dönüşüm kutusuna at')

@bot.command()
async def Cevre_Kirliligi(ctx):
    await ctx.send(f'Geri dönüşüm kutularını kullan ve Yenilenebilir enerji kaynağı kullan.')
    

bot.run("")