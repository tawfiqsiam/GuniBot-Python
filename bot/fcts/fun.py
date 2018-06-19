#!/usr/bin/env python
#coding=utf-8

from math import *
from random import *
from fcts import admin,utilities,common,citations,lang_tr
import discord,random,re,string

async def count(message):
    counter = 0
    tmp = await message.channel.send(lang_tr.tr(message.guild,'fun','count-0'))
    async for log in message.channel.history(limit=500):
        if log.author == message.author:
            counter += 1
    await tmp.edit(content=lang_tr.tr(message.guild,'fun','count-1').format(count=counter))

async def msg(client,message):
    if message.guild != None:
        if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
            return
    from fcts import emoji
    import discord
    liste=message.content.split(" ")
    if message.content.startswith("!run"): #
        await message.channel.send("ε=ε=ε=┏( >_<)┛")
    elif message.content.startswith("!cookie"): #
        await message.channel.send(lang_tr.tr(message.guild,"fun","msg-0").format(message.author.mention))
    elif message.content.startswith("!ping"): #
         await message.channel.send("Pong!")
    elif message.content.startswith('!pong'): #
        await message.channel.send("Ping !")
    elif message.content.startswith("!gg"): #
        await message.channel.send(file=discord.File(utilities.image_finder('gg.gif')))
    elif message.content.startswith('!shrug'): #
        await message.channel.send(file=discord.File(utilities.image_finder('shrug.gif')))
    elif message.content.startswith('!starwars'): #
        await message.channel.send(file=discord.File(utilities.image_finder('starwars.jpg')))
    elif message.content.startswith("!kill "): #
        victime=str(message.content).replace("!kill ","").replace('@everyone','everyone')
        await message.channel.send(str(choice(common.kill_msg)).format(message.author.mention,victime,victime.replace(" ","_")))
    elif message.content.startswith('!hey') or message.content.startswith('!hi') or message.content.startswith('!cc'): #
        liste = str(message.content).split(" ")
        liste.append(message.author.name)
        await message.channel.send(lang_tr.tr(message.guild,'fun','msg-1').format(liste[1]))
    elif message.content.startswith('!money'): #
        await message.channel.send(file=discord.File(utilities.image_finder('money.gif')))
    elif message.content.startswith("!osekour") or message.content.startswith("!au secour"): #
        await message.channel.send(str(choice(common.osekour_msg)))
    elif message.content.startswith("!mojang"): #
        await message.channel.send(file=discord.File(utilities.image_finder('mojang.png')))
    elif message.content.startswith('!hep'): #
        await message.channel.send(lang_tr.tr(message.guild,'fun','msg-2'))
    elif message.content.startswith('!parrot'): #
        await message.channel.send(lang_tr.tr(message.guild,'fun','msg-3'))
        await message.channel.send(file=discord.File(utilities.image_finder('parrot.gif')))
    elif message.content.lower() == '!citation': #
        c = choice(citations.liste)
        texte = "\"*{0}*\" \n     __{1}__".format(c[0],c[1])
        await message.channel.send(texte)
    elif message.content.startswith("!party"): #
        await message.channel.send(lang_tr.tr(message.guild,'fun','msg-3'))
        await message.channel.send(file=discord.File(utilities.image_finder('discord_party.gif')))
    elif message.content.startswith('!say ') and utilities.staff_finder(message.author,'say'): #
        await message.channel.send(message.content.replace("!say ",""))
        await utilities.suppr(message)
    elif message.content.startswith('!me '): #
        await message.channel.send(message.content.replace('!me','*'+message.author.display_name)+'*')
        await utilities.suppr(message)
    elif message.content.startswith('!report'): #
        await message.channel.send(lang_tr.tr(message.guild.id,'fun','msg-4')+" :arrow_right: https://support.discordapp.com/hc/en-us/articles/360000291932-How-to-Properly-Report-Issues-to-Trust-Safety")
    elif message.content.startswith('!react '): #
        try:
            msg = await message.channel.get_message(liste[1])
        except discord.errors.HTTPException:
            await message.channel.send(lang_tr.tr(message.guild,"fun",'msg-5'))
            return
        try:
            await msg.add_reaction(emoji.e_to_u(liste[2]))
        except:
            try:
                await msg.add_reaction(liste[2])
            except:
                utilities.erreur()
        await utilities.suppr(message)
    elif message.content.startswith('!invit') and message.guild != None: #
        await invitation(client,message)        
    elif message.content.startswith('!piece'): #
        text = random.choice(['Pile !','Face !'])
        if random.random()<0.04:
            text = lang_tr.tr(message.guild,'fun','msg-6')
        await message.channel.send(text)
    elif message.content.startswith('!nuke'): #
        await message.channel.send(file=discord.File(utilities.image_finder('nuke.gif')))
    elif message.content.startswith('!cparty'): #
        await message.channel.send(file=discord.File(utilities.image_finder('cameleon.gif')))
    elif message.content.lower().startswith('!pibkac'): #
        await message.channel.send(file=discord.File(utilities.image_finder('pibkac.png')))
    elif message.content.lower().startswith('!pikachu'): #
        await message.channel.send(file=discord.File(utilities.image_finder('cookie-pikachu.gif')))
    elif message.content.lower().startswith('!pizza'): #
        await message.channel.send(file=discord.File(utilities.image_finder('pizza.gif')))
    elif message.content.startswith('!lmgtfy ') or message.content.startswith('!search '): #
        link = message.content.replace('!lmgtfy ','').replace('!search ','')
        link = "http://lmgtfy.com/?q="+link.replace(" ","+")
        utilities.print2(link)
        await message.channel.send(link)
        await message.delete()
    elif message.content.lower().startswith('!blurple'): #
        await message.channel.send(file=discord.File(utilities.image_finder('Blurple_Info.png')))
    elif message.content.lower()=='bouh !' or message.content.lower()=='bouh!' and random.random()<0.1:#
        await message.channel.send(file=discord.File(utilities.image_finder('herobrine.gif')))
    elif message.content.startswith('!loading'):#
        await message.channel.send(file=discord.File(utilities.image_finder('loading.gif')))
    elif message.content.lower().split(" ")[0] == '!magic': #
        await message.channel.send(file=discord.File(utilities.image_finder('magic.gif')))
    elif message.content.startswith('!citation list') and message.author.id==279568324260528128:#
        text=""
        for i in citations.liste:
            text+=i[0]+"\n"
        await message.channel.send(text)
    elif message.content.startswith("!ragequit"): #
        await message.channel.send(file=discord.File(utilities.image_finder('ragequit{0}.gif'.format(1+random.choice(range(5))))))
    elif message.content.startswith('!discord'): #
        await message.channel.send(file=discord.File(utilities.image_finder('discooord.png')))
    elif message.content.startswith('!avengers'):#
        await message.channel.send(random.choice(["*Groot:* I am Groot.\n*Steve Rogers:* I am Steve Rogers.","*Rocket Raccoon:* You speak Groot?\n*Thor:* They taught it on Asgard. It was an elective.","*Dr. Stephen Strange [realizing both teams are against Thanos]:* Ok, let me ask you this, one time: What master do you serve?\n*Start Lord:* Oh, what master do I serve? What am I supposed to say, Jesus?","*Tony Stark:* You can't park here, buddy. Earth is closed today. Take your tractor beam and skedaddle. ","*Peter Parker:* There can't be a friendly neighborhood spiderman if there's no neighborhood. Okay, that doesn't make sense but... "]))
    elif message.content.lower().startswith('footlose'):#
        await message.channel.send("*Drax:* Tell him about the dance-off to save the Universe.\n*Tony Stark:* What dance-off?\n*Star Lord:* It's not a thing.\n*Peter Parker:* Like in Footloose, the movie?\n*Star Lordl:* Exactly like Footloose. Is it still the greatest movie in history?\n*Peter Parker:* It never was. ")
    elif message.content.startswith('!thanos'): #
        await message.channel.send(random.choice(lang_tr.tr(message.guild,'fun','msg-7')).format(message.author.mention))
    elif message.content.startswith('!bigtext '): #
        await big_text(message)
    elif message.content.startswith('!info'):
        await infos(message)

fun_msg=["!bigtext <texte>","!piece","!thanos","!ragequit","!discord","!loading","!avengers","!pizza","!blurple","!pibkac","!cparty","!nuke","!count","!react <id du message> <emoji>","!me <texte>","!report","!run","!cookie","!ping","!kill <something>","!gg","!starwars","!shrug","!hey","!cc","!money","!hep","!osekour","!mojang","!parrot","!citation","!party"]

async def infos(message):
    await message.channel.send(lang_tr.tr(message.guild,"infos","text-0").format(message.guild.me.mention))

async def invitation(client,message):
    liste2 = message.content.split(" ")
    liste=[]
    inv=None
    try:
        if len(liste2)>1:
            if liste2[1].startswith('<#'):
                salon = utilities.canal_finder_name(client,message.guild.id,liste2[1])
                if salon != None:
                    liste = await salon.invites()
                    if liste==[]:
                        inv = await salon.create_invite(max_uses=1,reason="commande !invite sur le bot fr-minecraft#8427")
                else:
                    inv = await message.channel.create_invite(max_uses=1,reason="commande !invite sur le bot fr-minecraft#8427")
        else:
            liste = await message.guild.invites()
            if liste == []:
                inv = await message.channel.create_invite(max_uses=1,reason="commande !invite sur le bot fr-minecraft#8427")
    except discord.Forbidden:
        utilities.erreur(True)
        await message.channel.send(lang_tr.tr(message.guild.id,'fun','invitation-0'))
        return
    if inv == None:
        for i in liste:
            if i.channel==message.channel:
                inv = liste[0]
    if inv == None:
        for i in liste:
            if i.max_uses==0 and i.temporary==True:
                inv = liste[0]
    if inv == None:
        for i in liste:
            if i.max_age==0 or i.temporary==True:
                inv = liste[0]
    if inv == None:
        inv = liste[0]
    if inv.max_uses == 0:
        uses = "∞"
    else:
        uses = inv.max_uses-inv.uses
    temp = inv.max_age
    if temp == 0:
        temp="∞"
    channel = inv.channel.mention
    utilities.print2("("+str(message.created_at)+") "+"lien d'invitation : "+inv.url+" (serveur : "+message.guild.name+")")
    await message.channel.send(lang_tr.tr(message.guild.id,'fun','invitation-1').format(channel,uses,temp))
    await message.channel.send(inv.url)

async def calc(client,message):
    calcul = message.content.replace('!calc ','')
    calcul = calcul.replace('x','*')
    calcul = calcul.replace('@','')
    if calcul!='help':
        try:
            while "^" in calcul:
                c = re.search(r'\b(\d+\.\d+|\d+)\^(\d+\.\d+|\d+)\b',calcul)
                calcul = calcul.replace(c.group(0),str(pow(float(c.group(1)),float(c.group(2)))))
            r = eval(calcul)
        except:
            r = lang_tr.tr(message.guild,'fun','calc-0')
    else:
        r = lang_tr.tr(message.guild,'fun','calc-1')
    if r==1.2246467991473532e-16:
        r=0
    r = str(r).replace('@everyone','@.everyone')
    for i in range(0,len(r),2000):
        await message.channel.send(r[:2000])
        r = r[2000:]

async def liste(salon):
    if type(salon)== discord.DMChannel:
        texte = "Voici la liste des commandes *inutiles donc indispensables* que je possède :"
    else:
        if salon.permissions_for(salon.guild.me).send_messages==False:
            return
        texte=lang_tr.tr(salon.guild.id,'fun','liste-0')
    liste = sorted(fun_msg)
    for cmd in liste:
        texte+="\n"+cmd 
    await salon.send(texte)

async def big_text(message):
    text1 = []
    emojis = common.numbers_emojis
    contenu = utilities.anti_code(message.content.replace("\n","¬¬")).split()[1:]
    new_line = False
    for l in " ".join(contenu):
        if l in string.ascii_letters:
            text1.append(":regional_indicator_{0}:".format(l.lower()))
        elif l in string.digits:
            text1.append("{0}".format(emojis[l]))
        elif l == " ":
            text1.append("<:_nothing:446782476375949323>")
        elif l == "#":
            text1.append(":hash:")
        elif l == "*":
            text1.append(":asterisk:")
        elif l == "?":
            text1.append(":grey_question:")
        elif l == "!":
            text1.append(":grey_exclamation:")
        elif l == '-':
            text1.append(":heavy_minus_sign:")
        elif l == "+":
            text1.append(":heavy_plus_sign:")
        elif l == "÷":
            text1.append(":heavy_division_sign:")
        elif l == ".":
            text1.append(":small_blue_diamond:")
        elif l in ["(",")",",","'","\"","=","/","¬"]:
            text1.append(l)
        caract = len("".join(text1))
        if caract>1970:
            await message.channel.send(str("".join(text1)).replace("¬¬","\n"))
            text1 = []
            new_line = False
    if text1 != []:
        await message.channel.send(str("".join(text1)).replace("¬¬","\n"))
    if utilities.staff_finder(message.author,"slowmode"):
        await utilities.suppr(message)
    
