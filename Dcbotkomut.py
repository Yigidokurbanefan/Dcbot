import discord
import time
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command() #Replikler
async def MyBot(ctx, message, message1= "", message2="", message3 = "", message4 = ""):
    d = random.randint(1,10)
    e = random.randint(1,10)
    f = random.randint(1,10)
    g = random.randint(1,10)
    h = random.randint(1,10)
    i = random.randint(1,10)
    j = random.randint(1,10)
    k = random.randint(1,10)
    ulke = "Türkiye'nin Başkenti Ankara'dır.","İspanya'nın Başkenti Madrid'dir.","Rusya'nın Başkenti Moskova'dır."
    if message == "Nasılsın?":
        await ctx.send("İyi Senden?")
    elif message == "Çok":
        if message1 == "İyiyim":
            await ctx.send("Daha İyi Olun Efendim")
    elif message == "Çok":
        if message1 == "Kötüyüm":
            await ctx.send("Geçmiş Olsun Efendim")
    elif message == "Bana":
        if message1 == "Bir":
            if message2 == "Espri":
                if message3 =="Yap":
                    if message4 == "No:1":
                        await ctx.send("Adamın Biri Varmış İkinci Dönem Düzeltmiş")
    elif message == "Bana":
        if message1 == "Bir":
            if message2 == "Espri":
                if message3 =="Yap":
                    if message4 == "No:2":
                        await ctx.send("Adamın Biri Varmış, Diğer Yolda Kalmış")
    elif message == "Bana":
        if message1 == "Bir":
            if message2 == "Espri":
                if message3 =="Yap":
                    if message4 == "No:3":
                        await ctx.send("Köfte İle Möftenin Arasındaki Fark Nedir?")
                        time.sleep(1)
                        await ctx.send("...")
                        time.sleep(3)
                        await ctx.send("Biri Kıymadan, Diğeri İse Mıymadan Yapılır")
    elif message == "Matematik":
        if message1 == "Sorusu":
            secim = random.randint(1,4)
            if secim == 1:
                await ctx.send(f"{d} + {e}")
                tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                kullanici_tahmini = tahmin_mesaji.content
                try:
                    kullanici_tahmini = int(kullanici_tahmini)
                    if kullanici_tahmini == (d+e):
                        await ctx.send("Tebrikler!")
                    else:
                        await ctx.send("Yanlış")
                except:
                    await ctx.send("Lütfen Sayı Gönderin")
            elif secim == 2:
                await ctx.send(f"{f} - {g}")
                tahminmesaji1 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                kullanici_tahmini1 = tahminmesaji1.content
                try:
                    kullanici_tahmini1 = int(kullanici_tahmini1)
                    if kullanici_tahmini1 == (f-g):
                        await ctx.send("Tebrikler!")
                    else:
                        await ctx.send("Yanlış")
                except:
                    await ctx.send("Lütfen Sayı Gönderin")
            elif secim == 3:
                await ctx.send(f"{h} * {i}")
                tahminmesaji2 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                kullanici_tahmini2 = tahminmesaji2.content
                try:
                    kullanici_tahmini2 = int(kullanici_tahmini2)
                    if kullanici_tahmini2 == (h*i):
                        await ctx.send("Tebrikler!")
                    else:
                        await ctx.send("Yanlış")
                except:
                    await ctx.send("Lütfen Sayı Gönderin")
            elif secim == 4:
                await ctx.send(f"{j} / {k}")
                tahminmesaji3 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                kullanici_tahmini3 = tahminmesaji3.content
                try:
                    kullanici_tahmini3 = float(kullanici_tahmini3)
                    if kullanici_tahmini3 == (h/i):
                        await ctx.send("Tebrikler!")
                    else:
                        await ctx.send("Yanlış")
                except:
                    await ctx.send("Lütfen Sayı Gönderin")
    elif message == "Ülke-Başkent":
        await ctx.send(random.choice(ulke))



    elif message == "MurathanTümay":
        await ctx.send("(M)Adam")

@bot.command()
async def BenimBot(ctx):
    z = random.choice(os.listdir("Resimler"))
    with open(f"Resimler/{z}","rb") as x:
        y = discord.File(x)
    await ctx.send(file = y)

@bot.command()
async def BenimHayvan(ctx):
    a = random.choice(os.listdir("Hayvanlar"))
    with open(f"Hayvanlar/{a}","rb") as b:
        c = discord.File(b)
    await ctx.send(file = c)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def Duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def Dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    

    

bot.run()
