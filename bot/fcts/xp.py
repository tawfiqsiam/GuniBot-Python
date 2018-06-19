#!/usr/bin/env python
#coding=utf-8

import discord,datetime,time
from fcts import utilities,emoji,server,lang_tr

ban_channels=[437232231816101898,399203240799109120,366530955613044736,400368447894323214,391972183770923008]

def new_rank(userid,xp):
    """Modifie le niveau d'un joueur"""
    try:
        with open('../bot-stats/ranks.txt','r') as fichier:
            texte = fichier.read()
        rangs = eval(texte)
    except:
        rangs={}
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
    with open('../bot-stats/ranks.txt','w') as fichier:
        fichier.write(str(rangs))
    if ex_level !=rangs[userid][1]:
        return rangs[userid][1]

def update_level(xp):
    """Renvoie le niveau correspondant au nombre d'xp"""
    lvl=0
    x=30
    while x<xp:
        lvl+=1
        x=x+pow(lvl,1.4)*4.4
    return lvl
        
def update_classement(membre,client):
    """Renvoie la position d'un membre dans le classement, et tout le classement"""
    l=[]
    noms=[]
    c=0
    ident=str(membre.id)
    try:
        with open('../bot-stats/ranks.txt','r') as fichier:
            texte = fichier.read()
        rangs = eval(texte)
    except:
        rangs={}
    for k,v in rangs.items():
        a=[v,k]
        l.append(a)
    l = sorted(l,reverse=True)
    for i in l:
        #name = utilities.user_finder_all(client,i[1],message=False)
        name = client.get_user(i[1]) #1000 fois plus rapide x)
        if name!=None:
            nom=str(name.name)
            nom = nom.replace("_","").replace("*","").replace("~","")
            if name.id == 125722240896598016:
                i[0][1] = 0-i[0][1]
            nom = [nom,i[0][1]]
            noms.append(nom)
    for i in l:
        c+=1
        if str(i[1])==ident:
            return [c,noms]
    return [-1,noms]

async def message_xp(message,rank_sys):
    """Check général pour l'xp - A appeler à chaque nouveau message"""
    if message.guild == None:
        return
    if message.channel.id in ban_channels or server.find_staff(message.guild.id,"xp") in [["false"],["non"],["wrong"],["faux"]]:
        return rank_sys
    from fcts import common
    import time,random
    try:
        m = rank_sys[message.author.id]
    except :
        m = time.time()
        rank_sys[message.author.id] = m
    if time.time()-m > 20:
        m = time.time()
        rank_sys[message.author.id] = m
        bonus=(len(str(message.content))-3)/7.5
        a=new_rank(message.author.id,bonus)
        if a != None:
            utilities.print2(utilities.anti_emoji(message.author.display_name)+" est passé niveau "+str(a))
            msg=str(random.choice(common.levelup_msg))
            try:
                await message.channel.send(msg.format(message.author.mention,a))
            except:
                utilities.erreur()
    return rank_sys

async def reload(salon):
    """Recalcule les niveaux de tout le monde - A appeler si on a modifié la fonction de calcul"""
    c=0
    try:
        with open('../bot-stats/ranks.txt','r') as fichier:
            texte = fichier.read()
        rangs = eval(texte)
    except:
        rangs={}
    for k,v in rangs.items():
        l = new_rank(k,0)
        if l !=v[1] and l!=None:
            utilities.print2("Changement de niveau pour "+str(k)+" (de "+str(v[1])+" à "+str(l)+")")
            c+=1
    await salon.send("Niveau mis à jour pour "+str(c)+" personnes")

async def rank(client,message):
    """Pour la commande !rank"""
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    import discord
    liste=str(message.content).split(' ')
    liste.append(message.author.name)
    try:
        with open('../bot-stats/ranks.txt','r') as fichier:
            texte = fichier.read()
        rangs = eval(texte)
    except:
        rangs={}
    membre = utilities.user_finder_all(client,liste[1])
    if membre!=None:
        if membre.bot and membre != message.guild.me:
            await message.channel.send(lang_tr.tr(message.guild,"xp","rank-0").format(membre.display_name))
            return
        if membre == message.guild.me:
            niveau = xp = "∞"
            rang = "∞"
        elif membre.id in rangs.keys():
            niveau=rangs[membre.id][1]
            xp=rangs[membre.id][0]
            rang = str(update_classement(membre,client)[0])+"/"+str(utilities.count_class())
        else:
            niveau=0
            xp=0
            rang = "Non classé"
        if membre.id == 125722240896598016:
            niveau = 0-niveau
        text="**Rang :** "+rang+"\n\n**Niveau :** "+str(niveau)+"\n\n**Points :** "+str(xp)
        em = discord.Embed(title=str(membre.name), description=text)
        try:
            await message.channel.send(embed=em)
        except:
            utilities.print2("(xp-rank) Impossible d'envoyer l'embed")
            return
    else:
        await message.channel.send(lang_tr.tr(message.guild,"xp","rank-1").format(liste[1]))

async def top(client,message):
    """Pour la commande !top"""
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    liste=str(message.content).split(' ')
    liste.append('5')
    if not liste[1].isnumeric():
        await message.channel("Oups, il semble y avoir une erreur dans la commande.\nPour rappel, la syntaxe est `!top [nombre]` :innocent:")
        return
    n = c = update_classement(message.author,client)
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
    emb = discord.Embed(title="Niveaux d'xp - TOP "+str(len(places)), colour=discord.Colour(0xbda4d), timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    emb.add_field(name="Place", value="\n".join(places), inline=True)
    emb.add_field(name="Nom", value="\n".join(noms), inline=True)
    emb.add_field(name="Niveau", value="\n".join(niveaux), inline=True)
    await message.channel.send(embed=emb)
    if c[0]==1:
        await message.channel.send("Bravo, vous êtes le premier !")
    elif c[0]==-1:
        await message.channel.send("Oups, vous n'êtes pas encore classé")
    else:
        await message.channel.send("Vous êtes classés à la {}ème position !".format(c[0]))
