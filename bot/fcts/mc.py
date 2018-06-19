#!/usr/bin/env python
#coding=utf-8

import requests,discord,datetime,asyncio,time
from fcts import utilities,hunter,lang_tr

urle = 'http://minecraft-ids.grahamedgecombe.com/entities.json' #liste json des entités
urli = 'http://minecraft-ids.grahamedgecombe.com/items.json'     #liste json des items
urlfb = 'https://api.minetools.eu/ping/fb.serveurs-frm.net/25565'  #infos du freebuild

def save_item():
    """Importe la liste d'items depuis l'API"""
    r = requests.get(urli) #request
    c = eval(r.content)    #contenu (list)
    with open('../bot-stats/mc-items.txt','w',encoding='utf-8') as fichier:
        fichier.write(str(c))

def find_item(ID=None,meta=0,name='',message=True):
    """Renvoie un item à partir d'une de ses données"""
    Item=None
    with open('../bot-stats/mc-items.txt','r',encoding='utf-8') as fichier:
        items = fichier.read()
        items=eval(items)
    for i in items:
        if (str(i['type'])==str(ID) and i['meta']==meta) or i['name'].lower()==name.lower():
            Item = i
    if Item != None and message:
        print("Nom :",Item['name'],"\nID :",Item['type'],"\nDamage :",Item['meta'],"\nType :",Item['text_type'])
    elif Item !=None and message==False:
        return Item
    else:
        return None


def save_entity():
    """Importe la liste d'entités depuis l'API"""
    r = requests.get(urle) #request
    c = eval(r.content)    #contenu (list)
    with open('../bot-stats/mc-entity.txt','w',encoding='utf-8') as fichier:
        fichier.write(str(c))

def find_entity(ID=None,name='',message=True):
    """INCOMPLÈTE Renvoie une entité à partir de son ID"""
    Entity=None
    with open('../bot-stats/mc-entity.txt','r',encoding='utf-8') as fichier:
        entities = fichier.read()
        entities=eval(entities)
    for i in entities:
        if str(i['type'])==str(ID) or i['name'].lower()==name.lower() or i['text_type'].lower()==name.lower():
            Entity = i
    if Entity != None and message:
        utilities.print2("Nom :",Entity['name'],"\nID numérique :",Entity['type'],"\ID :",Entity['text_type'])
    elif Entity !=None and message==False:
        return Entity
    else:
        utilities.print2("Introuvable :/")
        return None

async def msg_init(message):
    if message.guild == None:
        await msg_mp(message)
    else:
        await msg_guild(message)

async def msg_guild(message):
    liste = message.content.split(" ")
    if len(liste)<3 and liste[1] != 'help':
        await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-0"))
        return
    if liste[1]=='entity':
        e=None
        if str(liste[2]).isnumeric():
            e = find_entity(ID=liste[2],message=False)
        else:
            e = find_entity(name=" ".join(liste[2:]),message=False)
        if e != None:
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-1").format(e['name'],e['type'],e['text_type']))
            return
        else:
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-10"))
            return
    elif liste[1] in ['item','bloc','block']:
        if str(liste[2]).isnumeric():
            i = find_item(ID=liste[2],message=False)
        else:
            i = find_item(name=" ".join(liste[2:]),message=False)
        if i != None:
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-2").format(i['name'],i['type'],i['meta'],i['text_type']))
            return
        else:
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-3"))
    elif liste[1]=='reload' and message.author.id==279568324260528128:
        if liste[2]=='item':
            save_item()
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-4"))
        elif liste[2]=='entity':
            save_entity()
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-5"))
        elif liste[2]=='all':
            save_item()
            save_entity()
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-6"))
        else:
            await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-7"))
    elif liste[1]=='help':
        await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-8"))
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"mc","msg-9"))

async def msg_mp(message):
    liste = message.content.split(" ")
    if len(liste)<3 and liste[1] != 'help':
        await message.channel.send("Oops, il manque un paramètre")
        return
    if liste[1]=='entity':
        e=None
        if str(liste[2]).isnumeric():
            e = find_entity(ID=liste[2],message=False)
        else:
            e = find_entity(name=" ".join(liste[2:]),message=False)
        if e != None:
            await message.channel.send("Nom : {}\nID numérique : {}\nID : {}".format(e['name'],e['type'],e['text_type']))
            return
        else:
            await message.channel.send("Impossible de trouver cette entité")
            return
    elif liste[1] in ['item','bloc','block']:
        if str(liste[2]).isnumeric():
            i = find_item(ID=liste[2],message=False)
        else:
            i = find_item(name=" ".join(liste[2:]),message=False)
        if i != None:
            await message.channel.send("Nom : {}\nID numérique : {}:{}\nID : {}".format(i['name'],i['type'],i['meta'],i['text_type']))
            return
        else:
            await message.channel.send("Impossible de trouver cet item")
    elif liste[1]=='reload' and message.author.id==279568324260528128:
        if liste[2]=='item':
            save_item()
            await message.channel.send("Items importés !")
        elif liste[2]=='entity':
            save_entity()
            await message.channel.send("Entités importées !")
        elif liste[2]=='all':
            save_item()
            save_entity()
            await message.channel.send("Items et entités importés !")
        else:
            await message.channel.send("Paramètre invalide. Sélectionnez `item`, `entity` ou `all`")
    elif liste[1]=='help':
        await message.channel.send("Cette commande permet de trouver un bloc ou une entité de Mineraft® à partir de son nom ou de son ID. Vous n'avez qu'à entrer `!mc <item/entity> <data>` pour obtenir les informations correspondantes !\n*PS : la base de donnée est actuellement en 1.12*")
    else:
        await message.channel.send("Paramètres invalides. Sélectionnez `help`, `item` ou `entity`")

async def info_fb(client,messageid):
    """"Met à jour le message d'info du freebuild"""
    salon = utilities.canal_finder_all(client,393116580546084876,message=True)
    r = requests.get(urlfb)
    try:
        r = eval(r.content)
    except:
        utilities.print2("(infos-fb) Erreur : ")
        utilities.erreur()
        r = r.content
    players=[]
    try:
        for p in r['players']['sample']:
            players.append(p['name'])
        online = str(r['players']['online'])+"/"+str(r['players']['max'])
    except KeyError:
        players=['Aucun']
        online = "0"
    if players==[]:
        players=['Aucun']
    latence = str(r['latency'])+" ms"
    version = r['version']['name']

    embed = discord.Embed(title="Serveur FreeBuild - Etat du serveur", colour=discord.Colour(0x417505), url="http://serveurs-frm.net/", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_thumbnail(url="http://fr-minecraft.net/css/img/creeper.png")
    embed.add_field(name="Version", value=version)
    embed.add_field(name="Nombre de joueurs", value=online)
    embed.add_field(name="Liste des joueurs connectés", value=", ".join(players))
    embed.add_field(name="Latence", value=latence)
    if messageid==0:
        await salon.send(embed=embed)
    else:
        try:
            message = await salon.get_message(messageid)
            await message.edit(embed=embed)
            utilities.print2("(fb) FB rechargé")
            return messageid
        except:
            m = await salon.send(embed=embed)
            utilities.erreur(True)
            return m.id

async def fb(client,messageid,wait=True):
    """Boucle freebuild"""
    if wait:
        await asyncio.sleep(10)
    await info_fb(client,messageid)
    while not client.is_closed():
        await asyncio.sleep(30)
        if int(datetime.datetime.now().minute)%5==0:
            try:
                messageid = await info_fb(client,messageid)
            except:
                utilities.print2("(fb) Erreur lors de la boucle : ")
                utilities.erreur()
            await asyncio.sleep(30)
