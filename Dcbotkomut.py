import discord
import time
import random
import os
import requests
import dcbotimg
import gemini
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
    skor1 = random.randint(1,5)
    skor2 = random.randint(1,5)
    futbolcular = ["Lionel Messi", "Cristiano Ronaldo", "Diego Maradona", "Pele", "Robert Lewandowski", "Karim Benzema", "Sergio Ramos", "Paolo Maldini", "Giangluigi Buffon", "Iker Cassillas"]
    cevap = random.choice(futbolcular)
    mesaj = "Bir şey", "Ciddi bir şey", "Çok ciddi bir şey"
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
                    if kullanici_tahmini3 == (j/k):
                        await ctx.send("Tebrikler!")
                    else:
                        await ctx.send("Yanlış")
                except:
                    await ctx.send("Lütfen Sayı Gönderin")
    elif message == "Ülke-Başkent":
        await ctx.send(random.choice(ulke))
    elif message == "Rastgele":
        if message1 == "Bilgi":
            await ctx.send(random.choice(mesaj))
    elif message == "Telefon":
        if message1 == "Bakma":
            if message2 == "Süresi":
                await ctx.send("Kaç Saat Telefona Bakıyorsun ?")
                alinan_mesaj = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                kullanici_mesaj = alinan_mesaj.content
                if int(kullanici_mesaj) <= 2 :
                    await ctx.send("Bağımlı değilsin.")
                elif int(kullanici_mesaj) > 2 and int(kullanici_mesaj) <= 4 :
                    await ctx.send("Dikkat et.")
                elif int(kullanici_mesaj) >= 5 :
                    await ctx.send("SEN TAM BİR BAĞIMLISIN.")
    elif message == "Maç":
        if message1 == "Skoru":
            if message2 == "Simulasyonu":
                await ctx.send("...")
                time.sleep(3)
                await ctx.send("Birinci takımın ismini girin")
                takim_mesaj = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                ilktakim_mesaj = takim_mesaj.content
                await ctx.send("...")
                time.sleep(3)
                await ctx.send("İkinci takımın ismini girin")
                takim_mesaj1 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                ikincitakim_mesaj = takim_mesaj1.content
                await ctx.send("...")
                time.sleep(3)
                if ilktakim_mesaj == "Galatasaray" or "Beşiktaş" and ikincitakim_mesaj == "Galatasaray" or "Beşiktaş":
                    await ctx.send("Maç sonucu Beşiktaş5-0Galatasaray")
                    await ctx.send("Maçı Beşiktaş kazandı!")
                else:
                    await ctx.send(f"{ilktakim_mesaj}{skor1}-{skor2}{ikincitakim_mesaj}")
                    if skor1 > skor2:
                        await ctx.send(f"Maçı {ilktakim_mesaj} kazandı!")
                    elif skor1 == skor2:
                        await ctx.send("Maç berabere!")
                    else:
                        await ctx.send(f"Maçı {ikincitakim_mesaj} kazandı!")
    elif message == "Üs":
        if message1 == "Hesaplayıcı":
            baslangic = []
            await ctx.send("...")
            time.sleep(3)
            await ctx.send("Kuvveti alınacak sayıyı girin.")
            sayi_mesaj = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            taban_mesaj = sayi_mesaj.content
            baslangic.append(int(taban_mesaj))
            await ctx.send("...")
            time.sleep(3)
            await ctx.send("Kuvveti girin.")
            sayi_mesaj1 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            kuvvet_mesaj = sayi_mesaj1.content
            for i in range(int(kuvvet_mesaj) - 1):
                taban_mesaj = int(taban_mesaj)*baslangic[0]
            await ctx.send("...")
            time.sleep(3)
            await ctx.send(f"Sonuç {taban_mesaj}")
    elif message == "Kök":
        if message1 == "İçine":
            if message2 == "Tam":
                if message3 == "Kare": 
                    if message4 == "Alma":
                        await ctx.send("...")
                        time.sleep(3)
                        await ctx.send("Tam kare sayıyı girin.")
                        tam_mesaj = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                        sonuc_mesaj = int(tam_mesaj.content)
                        if sonuc_mesaj**(1/2) == int(sonuc_mesaj**(1/2)):
                            await ctx.send(f"Sonuç {int(sonuc_mesaj**(1/2))}")
                        else:
                            await ctx.send("Bu bir tam kare değil.")
    elif message == "Futbolcu":
        if message1 == "Tahmin":
            if message2 == "Etme":
                if cevap == "Lionel Messi":
                    await ctx.send("En iyisi, Arjantin, Sağ Kanat")
                    gercekcevap = await bot.wait_for("message", check=lambda m: m.author == ctx.author) 
                    yenicevap = gercekcevap.content
                    if yenicevap == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Cristiano Ronaldo":
                    await ctx.send("Gol, Portekiz, Sol Kanat")
                    gercekcevap1 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap1 = gercekcevap1.content
                    if yenicevap1 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Diego Maradona":
                    await ctx.send("El, Arjantin, 1986")
                    gercekcevap2 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap2 = gercekcevap2.content
                    if yenicevap2 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Pele":
                    await ctx.send("Dünya Kupası, Brezilya, Edson")
                    gercekcevap3 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap3 = gercekcevap3.content
                    if yenicevap3 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Robert Lewandowski":
                    await ctx.send("Goalski, Polonya, Santrafor")
                    gercekcevap4 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap4 = gercekcevap4.content
                    if yenicevap4 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Karim Benzema":
                    await ctx.send("Bandaj, Fransa, Gölge")
                    gercekcevap5 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap5 = gercekcevap5.content
                    if yenicevap5 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Sergio Ramos":
                    await ctx.send("Kart, İspanya, Stoper")
                    gercekcevap6 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap6 = gercekcevap6.content
                    if yenicevap6 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Paolo Maldini":
                    await ctx.send("Milan, İtalya, Stoper")
                    gercekcevap7 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap7 = gercekcevap7.content
                    if yenicevap7 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Gianluigi Buffon":
                    await ctx.send("45, İtalya, Kaleci")
                    gercekcevap8 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap8 = gercekcevap8.content
                    if yenicevap8 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")
                elif cevap == "Iker Cassillas":
                    await ctx.send("Kaptan, İspanya, Kaleci")
                    gercekcevap9 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                    yenicevap9 = gercekcevap9.content
                    if yenicevap9 == cevap:
                        await ctx.send("Doğru")
                    else:
                        await ctx.send("Yanlış")


                     

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
    

@bot.command()
async def Photograph(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"KullaniciResimleri/{dosya.filename}")
            await ctx.send("Fotoğrafın Geldi")
        x,y = dcbotimg.dcaktar(f"KullaniciResimleri/{dosya.filename}")
        z = str(y*100)
        if x == "Python\n":
            await ctx.send(f"Python. %{z[:4]} Olasılıkla Eminim.")
            await ctx.send("Benim Yapı Taşım")
        elif x == "C++\n":
            await ctx.send(f"C++. %{z[:4]} Olasılıkla Eminim.")
            await ctx.send("Benim Sahibim Bile Bilmiyor")
        elif x == "Lua\n":
            await ctx.send(f"Lua. %{z[:4]} Olasılıkla Eminim.")
            await ctx.send("Artık Yok :(")
        elif x == "C#\n":
            await ctx.send(f"C#. %{z[:4]} Olasılıkla Eminim.")
            await ctx.send("Sahibimin Eskiden Öğrendiği Dil")
    else:
        await ctx.send("Fotoğrafın Gelmedi")

@bot.command()
async def EBOB(ctx, *args):
    sayilar = list(map(int, args))
    if not sayilar:
        await ctx.send("Lütfen en az bir sayı giriniz.")
        return

    bolunenler = []
    b = 1
    while b <= min(sayilar):
        if min(sayilar) % b == 0:
            bolunenler.append(b)
        b = b + 1

    while bolunenler:
        if all(sayi % max(bolunenler) == 0 for sayi in sayilar):
            await ctx.send(f"EBOB: {max(bolunenler)}")
            return
        bolunenler.remove(max(bolunenler))



def EKOK_Hazirlik(numbers):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = abs(lcm * number) // gcd(lcm, number)
    return lcm

@bot.command()
async def EKOK(ctx, *args):
    if len(args) < 2:
        await ctx.send("Lütfen en az iki sayı girin.")
        return

    try:
        numbers = [int(arg) for arg in args]
    except ValueError:
        await ctx.send("Lütfen geçerli sayılar girin.")
        return

    result = EKOK_Hazirlik(numbers)
    await ctx.send(f"Girdiğiniz sayıların EKOK'u: {result}")



@bot.command()
async def Secim(ctx, * , secim):
    eleman = secim.split("-")
    await ctx.send(random.choice(eleman))

@bot.command()
async def Gemini(ctx, * , bildir):
    gemini.geminim(bildir)
    gonder = "output.txt"
    await ctx.send(file=discord.File(gonder))
    


@bot.command()
async def Rastgele(ctx):
    komut = random.randint(1,100)
    await ctx.send(komut)

@bot.command()
async def RastgeleCıkartma(ctx):
    komut1 = random.randint(1,100)
    komut2 = random.randint(1,100)
    await ctx.send(komut1 - komut2)

@bot.command()
async def RastgeleToplama(ctx):
    komut3 = random.randint(1,100)
    komut4 = random.randint(1,100)
    await ctx.send(komut3 + komut4)

@bot.command()
async def RastgeleCarpma(ctx):
    komut5 = random.randint(1,100)
    komut6 = random.randint(1,100)
    await ctx.send(komut5 * komut6)

@bot.command()
async def RastgeleBolme(ctx):
    komut7 = random.randint(1,100)
    komut8 = random.randint(1,100)
    await ctx.send(komut7 / komut8)



bot.run()
