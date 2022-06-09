import discord
from discord.ext import commands

#SELF-BOTUN ÇALIŞMASI VE PREFİX AYARLAMAK İÇİN OLAN YER
client = commands.Bot(command_prefix=".", self_bot=True, help_command=None) #command_prefix="" - Tırnaklar İçerisine Kendi Prefixsinizi Yazabilirsiniz
token = "" #Kendi HESAP Tokeninizi Gireceksiniz - (Bot Tokeni Değil)


#TERMİNALE DÜŞECEK MESAJI AYARLAYAN YER
@client.event
async def on_ready():
    print("Self-Bot Aktif") #Terminal'e Düşecek Yazı


#PREFİX YAZISINI VE KANALA YAZILACAK MESAJI AYARLADIĞINIZ YER
@client.command()
async def TEST(ctx): #TEST Yazan Yere İstediğinizi Yazabilirsiniz - (test,Test,Deneme vs.)
    await ctx.send("Bu Self-Bot ``ArviS#0011`` Tarafından Yazılmıştır") #.TEST - Yazdığınız Zaman Kanala Atılacak Mesaj

#BOTU ÇALIŞTIRAN YER
client.run(token, bot=False)










#Discord: ArviS#0011
#Discord Sunucum: https://discord.gg/strangerthingstr

#İnstagram: @arvis_here