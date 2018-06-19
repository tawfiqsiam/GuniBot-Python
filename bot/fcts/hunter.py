#!/usr/bin/env python
#coding=utf-8

import random,discord,asyncio,datetime,time
from fcts import utilities,common,emoji,lang_tr

n_balles = 10
c_balle = 30

async def pan(client,message):
    """Renvoie un message au hasard"""
    m =  hunter(message.author.id)
    m_random = message.author
    while m_random == message.author:
        m_random = random.choice(message.guild.members)
    msg = m[0].format(m_random.display_name,message.author.mention,utilities.user_finder_all(client,random.choice(['279568324260528128','375598088850505728']),True).name)
    if m[1]>=0:
        msg+=" (+"+str(m[1])+" xp)"
    else:
        msg+=" ("+str(m[1])+" xp)"
    lvl = new_rank(message.author.id,m[1])
    await message.channel.send(msg)
    if lvl != None:
        if lvl>0:
            text = lang_tr.tr(message.guild.id,"hunter","pan-0").format(message.author.mention,lvl)
        elif lvl<-1:
            text = lang_tr.tr(message.guild.id,"hunter","pan-1").format(message.author.mention,-lvl)
        else:
            return
        try:
            await message.channel.send(text)
        except discord.errors.Forbidden:
            utilities.erreur()

async def msg(client,message):
    if message.content.lower() in ['!pan','!bang'] :
        await hunting_check(client,message)
    #-----
    elif message.content.lower() == '!phelp':
        await aide(message.channel)
    #-----
    elif message.content.startswith('!shop'):
        await shop(message)
    #-----
    elif message.content.startswith('!reload'):
        await reload(message)

async def hunting_check(client,message):
    """Vérifie si le chargeur n'est pas vide"""
    if message.guild!=None:
        rangs = read_file()
        try:
            if rangs[message.author.id][2]>0:  #Si il reste des cartouches
                rangs[message.author.id][2]-=1
            else:                          #Sinon
                a = datetime.datetime.now()
                await message.channel.send(lang_tr.tr(message.guild.id,"hunter","check-0").format(3-a.hour%4,60-a.minute))
                return
        except IndexError:                          #Si les cartouches n'ont pas été créées
            rangs[message.author.id].append(n_balles)
            await message.channel.send(lang_tr.tr(message.guild.id,"hunter","check-1").format(message.author.mention))
        except KeyError:
            rangs[message.author.id] = [0,0,n_balles]
            await message.channel.send(lang_tr.tr(message.guild.id,"hunter","check-1").format(message.author.mention))
        write_file(rangs)
        await pan(client,message)            

async def shop(message):
    rangs = read_file()
    liste = message.content.split(" ")
    liste.append(1)
    try:
        xp = rangs[message.author.id][0]
    except:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","shop-0").format(message.author.mention))
        return
    if liste[1]=='help':
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","shop-4").format(c_balle))
        return
    try:
        numb = int(liste[1])
    except ValueError:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","shop-5"))
        return
    if xp>=numb*c_balle and numb>0:
        rangs[message.author.id][0] = xp - c_balle*numb
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","shop-1").format(message.author.mention,numb,numb*c_balle))
        rangs[message.author.id][2] += numb
    elif numb<0:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","shop-2"))
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","shop-3").format(xp))
    write_file(rangs)

async def reload(guildID,msg=None):
    """"Recharge les munitions de tout le monde (None) ou uniquement de l'owner (msg)"""
    rangs = read_file()
    if msg != None:
        if msg.author.id==279568324260528128:
            rangs[msg.author.id][2] = 15
            await msg.delete()
        else:
            await msg.channel.send(lang_tr.tr(msg.guild.id,"hunter","reload-0").format(n_balles,c_balle))
    else:
        for k in rangs.keys():
            rangs[k][2] = n_balles
    write_file(rangs)

def hunter(ID):
    """Tire au hasard un tuple(message,xp)"""
    liste=[]
    if random.random()>0.04 or ID in [279568324260528128,375598088850505728]:
        for k,v in common.pan_msg.items():
            for i in range(101-v):
                liste.append((k,v))
        return random.choice(liste)
    for k,v in common.special_pan.items():
        for i in range(50+v):
            liste.append((k,v))
    return random.choice(liste)

async def rank(client,message):
    """Renvoie l'xp d'un joueur"""
    liste=str(message.content).split(' ')
    liste.append(str(message.author.id))
    rangs = read_file()
    membre = utilities.user_finder_all(client,liste[1])
    if membre!=None:
        if membre.id in rangs.keys():
            xp = rangs[membre.id][0]
            niveau = update_level(xp)
            munitions = rangs[membre.id][2]
        else:
            niveau=0
            xp=0
            munitions = n_balles
        c = update_classement(membre,client)
        if c[0] != "Non classé":
            c2 = str(c[0])+"/"+str(count_hunters())
        else:
            c2 = c[0]
        text=lang_tr.tr(message.guild.id,"hunter","rank-0").format(c2,niveau,xp,munitions)
        em = discord.Embed(title=str(membre.name), description=text)
        try:
            await message.channel.send(embed=em)
        except:
            utilities.print2("(xp-rank) Impossible d'envoyer l'embed")
            return
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","rank-1").format(liste[1]))

def count_hunters():
    rangs = read_file()
    count=0
    for k in rangs.keys():
        count+=1
    return count

def update_level(xp):
    """Renvoie le niveau correspondant au nombre d'xp"""
    lvl=0
    x=25
    while x<xp:
        lvl+=1
        x=x+pow(lvl,2.1)*30
    return lvl

def read_file():
    """Renvoie le fichier"""
    try:
        with open('../bot-stats/hunter.txt','r') as fichier:
            texte = fichier.read()
        rangs = eval(texte)
    except:
        rangs={}
    return rangs

def write_file(rangs):
    """Ecrase le fichier"""
    with open('../bot-stats/hunter.txt','w') as fichier:
        fichier.write(str(rangs))

def new_rank(userid,xp):
    """Modifie le niveau d'un joueur"""
    rangs = read_file()
    xp=int(xp)
    c=0
    for u in rangs.keys():
        if u == int(userid):
            ex_level = rangs[u][1]
            rangs[u][0]=rangs[u][0]+xp
            rangs[u][1]=update_level(rangs[u][0])
            c=1
    if c==0:
        rangs[int(userid)]=[xp,0]
        ex_level=0
    write_file(rangs)
    if ex_level < rangs[userid][1]:
        return rangs[userid][1]
    elif ex_level > rangs[userid][1]:
        return -rangs[userid][1]
    else:
        return None

def update_classement(membre,client):
    """Renvoie la position d'un membre dans le classement, et tout le classement"""
    l=[]
    noms=[]
    c=0
    ident=int(membre.id)
    rangs = read_file()
    for k,v in rangs.items():
        a=(v,k)
        l.append(a)
    l = sorted(l,reverse=True)
    for i in l:
        name = utilities.user_finder_all(client,str(i[1]),message=False)
        if name!=None:
            nom=str(name.name)
            nom = nom.replace("_","")
            nom = nom.replace("*","")
            nom = nom.replace("~","")
            nom = (nom,i[0][0])
            noms.append(nom)
    for i in l:
        c+=1
        if i[1]==ident:
            return [c,noms]
    return ["Non classé",noms]

async def loop(client):
    """Boucle magique qui rempli les chargeurs toutes les 4h"""
    count = 1
    while not client.is_closed():
        if int(datetime.datetime.now().hour)%4==0 and count != int(datetime.datetime.now().hour):
            await reload(None)
            count = int(datetime.datetime.now().hour)
            utilities.print2("("+utilities.date(datetime.datetime.now())+") Armes rechargées !")
        a = datetime.datetime.now()
        await asyncio.sleep((60-a.minute)*60)

async def top(client,message):
    """Affiche le top (5) des joueurs"""
    liste=str(message.content).split(' ')
    liste.append('5')
    try:
        lol = int(liste[1])
    except:
        await message.channel(lang_tr.tr(message.guild.id,"hunter","top-0"))
        return
    n = update_classement(message.author,client)
    n=n[1]
    places=[]
    noms=[]
    niveaux=[]
    i=0
    for nom in n:
        i+=1
        nom2=utilities.anti_md(nom[0])
        if i<=int(liste[1]):
            places.append(str(i)+".")
            if len(nom2)>11:
                nom2=nom2[0:10]+"..."
            noms.append(emoji.del_emoji("`"+nom2+"`").replace("`",""))
            niveaux.append(str(nom[1]))
        else:
            break
    c = update_classement(message.author,client)
    emb = discord.Embed(title=lang_tr.tr(message.guild.id,"hunter","top-1")+str(len(places)), colour=discord.Colour(0xbda4d), timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    emb.add_field(name=lang_tr.tr(message.guild.id,"hunter","top-2"), value="\n".join(places), inline=True)
    emb.add_field(name=lang_tr.tr(message.guild.id,"hunter","top-3"), value="\n".join(noms), inline=True)
    emb.add_field(name=lang_tr.tr(message.guild.id,"hunter","top-4"), value="\n".join(niveaux), inline=True)
    await message.channel.send(embed=emb)
    if c[0]==1:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","top-5"))
    elif c[0]==-1:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","top-6"))
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"hunter","top-7").format(c[0]))

async def aide(salon):
    """Renvoie un message d'aide"""
    await salon.send(lang_tr.tr(salon.guild.id,"hunter","aide").format(c_balle))

async def infos(salon):
    """Renvoie un message d'information"""
    await salon.send("<:_nothing:446782476375949323>"+lang_tr.tr(salon.guild.id,"hunter","infos").format(n_balles,c_balle))
