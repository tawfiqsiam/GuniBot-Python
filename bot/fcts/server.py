#!/usr/bin/env python
#coding=utf8


import csv,discord,datetime,time
from fcts import utilities

syntax = {'serveur':0,
          'clear':1,
          'slowmode':2,
          'mute':3,
          'kick':4,
          'ban':5,
          'say':6,
          'hunter':7,
          'welcome':8,
          'welcome_channel':9,
          'leave':10,
          'auto_role':11,
          'bot_news':12,
          'save_roles':13,
          'langage':14,
          'xp':15}

presentation = {'clear':"ID des rôles pouvant utiliser les commandes clear et purge : ",
                'slowmode':"ID des rôles pouvant utiliser la commande slowmode : ",
                'mute':"ID des rôles pouvant utiliser la commande mute : ",
                'kick':"ID des rôles pouvant utiliser la commande kick : ",
                'ban':"ID des rôles pouvant utiliser la commande ban : ",
                'say':"ID des rôles pouvant utiliser la commande say : ",
                'hunter':"ID du salon pour le jeu *Hunter* : ",
                'welcome':"Message lorsqu'un membre rejoint le serveur : ",
                'welcome_channel':'ID du salon de bienvenue : ',
                'leave':"Message lorsqu'un membre quitte le serveur : ",
                'auto_role':'ID des rôles donnés automatiquement aux nouveaux membres : ',
                'bot_news':'ID du salon pour les news du bot : ',
                'save_roles':"Doit-on restaurer les rôles d'un membre après qu'il ai quitté puis rejoint le serveur ? ",
                'langage':'Langue activée : ',
                'xp':"Système d'xp activé ? "
                }
                
                
def find_staff(serverid,option):
    """Renvoie les valeurs d'une options dans un serveur"""
    global syntax
    serverid=str(serverid)
    with open('../bot-stats/server-options.csv', newline='',encoding='utf-8') as csvfile:
        f = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in f:
            if row[0]==serverid:
                try:
                    s = str(row[syntax[option]])
                except IndexError:
                    s = []
                while type(s) == str:
                    try:
                        s = eval(s)
                    except:
                        utilities.erreur()
                        s = []
                return s
    return []

def server_staff(serverid):
    """Renvoie la liste de toutes les configurations d'un serveur"""
    liste=None
    with open('../bot-stats/server-options.csv', newline='',encoding='utf-8') as csvfile:
        f = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in f:
            if row[0]==serverid:
                liste = row
    return liste

def server_tuple(serverid):
    """Renvoie une liste de tuples contenant le nom de l'option et sa valeur dans le serveur"""
    global syntax
    liste=[]
    for k in syntax.keys():
        if k != 'serveur':
            liste.append((k,find_staff(serverid,k)))
    return liste

def all_staff():
    """Renvoie une liste de listes contenant toutes les configurations"""
    liste=[]
    with open('../bot-stats/server-options.csv', newline='',encoding='utf-8') as csvfile:
        f = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in f:
            liste.append(row)
    return liste

async def check_len(channel):
    """Ajoute des cases aux lignes csv si il en manque"""
    global syntax
    liste = all_staff()
    count=0
    nbre = len(syntax.keys())
    with open('../bot-stats/server-options.csv','w',newline='') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for server in liste:
            if len(server)<nbre:
                for i in range(nbre-len(server)):
                    server.append([])
                count+=1
            f.writerow(server)
    
    await channel.send(str(count)+" serveurs modifiés !")

def change_option(serverid,option,new_opt):
    """Modifie la valeur d'une option pour un serveur donné"""
    global syntax
    ex_pref = server_staff(serverid)
    liste = all_staff()
    count=0 #Modification du serveur ?
    ident = syntax[option]
    if ident==None:
        return None
    with open('../bot-stats/server-options.csv','w',newline='',encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for i in liste:
            if str(i[0])==str(serverid):
                utilities.print2("(config) MàJ des préférences de serveur pour "+str(serverid)+" (option "+option+")")
                try:
                    i[ident]=new_opt
                except IndexError:
                    i.append(new_opt)
                count=1
            c=i
            c=eval(str(c)) #c=eval(utilities.anti_code(str(c)))
            f.writerow(c)
    if count==0:
        with open('../bot-stats/server-options.csv','a',newline='') as csvfile:
            f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            c=[serverid]
            for i in range(len(syntax)-1):
                c.append([])
            f.writerow(c)
            utilities.print2("(config) Nouveau serveur détécté : "+str(serverid))
        change_option(serverid,option,new_opt)
    utilities.print2("Terminé !")

async def msg(client,message):
    liste=message.content.replace('!sconfig ','').split(" ")
    if liste[0]=='change':
        if len(liste)<3:
            await message.channel.send("Hum... il semble manquer un paramètre :thinking:")
            return
        bot = await client.application_info()
        if message.author == message.guild.owner or message.author == bot.owner:
            if liste[1] in syntax.keys():
                chang = message.content.replace('!sconfig '+liste[0]+" "+liste[1]+" ","")
                if liste[1] not in ['welcome','leave']:
                    liste2=chang.split(', ')
                else:
                    liste2=chang.replace("'",'¬').split(', ',0)
                if liste[2] == 'del':
                    liste2 = []
                if type(liste2)==list:
                    liste3=[]
                    for i in liste2:
                        role = utilities.role_finder(message.guild,i,False)
                        if role != None:
                            liste3.append(str(role.id))
                        else:
                            liste3.append(i)
                    change_option(message.guild.id,liste[1],liste3)
                    await message.channel.send("Option modifiée !")
                else:
                    await message.channel.send("Pour modifier les préférences de modération, vous devez insérer une liste des options\nPar exemple, pour attribuer des rôles à la commande !mute, entrez `!sconfig change mute helpers, modo, admin`")
                    return
            else:
                await message.channel.send("Hum... option invalide. C'est raté :upside_down:")
        else:
            await message.channel.send("Désolé, mais seuls les propriétaires d'un serveur peuvent modifier ces options :confused:")
        return
    elif liste[0]=='see':
        if len(liste)<2:
            bot = await client.application_info()
            embed = discord.Embed(title="Options de configuration - "+message.guild.name, colour=discord.Colour(0x3fb9ef), url=message.guild.icon_url_as(format='jpg'),description="Voici la liste des configurations du serveur :", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=message.guild.icon_url_as(format='png'))
            embed.set_footer(icon_url=bot.icon_url)
            for i in server_tuple(message.guild.id):
                if i[1]==[]:
                    embed.add_field(name=i[0], value=" Ø ")
                else:
                    liste2=[]
                    for j in i[1]:
                        k = utilities.role_finder(message.guild,j,False)
                        if k == None:
                            k = utilities.canal_finder_name(client,message.guild,j,False)
                            if k == None:
                                liste2.append(j.replace('¬',"'"))
                            else:
                                liste2.append(k.mention)
                        else:
                            liste2.append(k.mention)
                    embed.add_field(name=i[0], value=", ".join(liste2))
            try:
                await message.channel.send(embed=embed)
            except discord.errors.Forbidden:
                await message.channel.send("Impossible d'envoyer l'embed. Vérifiez mes permissions svp :confused:")
            return
        if liste[1] in syntax.keys():
            staff = find_staff(message.guild.id,liste[1])
            if staff == None:
                await message.channel.send("Oups, une erreur est survenue :confused:\nVous êtes sûr d'avoir rentré des arguments valides ?")
            else:
                opt = ", ".join("staff")
                await message.channel.send(presentation[liste[1]]+", ".join(staff))
        else:
            await message.channel.send("Oops, option invalide :/")
    elif liste[0]=='help':
        await message.channel.send("Cette commande sert principalement à configurer votre serveur. En faisant `!sconfig see [option]` vous obtiendrez l'aperçu des configurations actuelles, \
et le propriétaire du serveur (actuellement {0}) peut entrer `!sconfig change <option> role1, role2, role3...` pour modifier une configuration, ou `!sconfig change <option> del` pour réinitialiser l'option !".format(message.guild.owner.name))
    else:
        await message.channel.send("Oops, mauvais syntaxe :upside_down:\nChoisissez entre `see` et `change` !")

async def msg_admin(client,channel,content,guild):
    liste=content.replace('sconfig ','').split(" ")
    if liste[0]=='change':
        if len(liste)<3:
            await channel.send("Hum... il semble manquer un paramètre :thinking:")
            return
        bot = await client.application_info()
        if liste[1] in syntax.keys():
            chang = content.replace('sconfig '+liste[0]+" "+liste[1]+" ","")
            if liste[1] not in ['welcome','leave']:
                liste2=chang.split(', ')
            else:
                liste2=chang.replace("'",'¬').split(', ',0)
            if liste[2] == 'del':
                liste2 = []
            if type(liste2)==list:
                liste3=[]
                for i in liste2:
                    role = utilities.role_finder(guild,i,False)
                    if role != None:
                        liste3.append(str(role.id))
                    else:
                        liste3.append(i)
                change_option(guild.id,liste[1],liste3)
                await channel.send("Option modifiée !")
            else:
                await channel.send("Pour modifier les préférences de modération, vous devez insérer une liste des options\nPar exemple, pour attribuer des rôles à la commande !mute, entrez `!sconfig change mute helpers, modo, admin`")
                return
        else:
            await channel.send("Hum... option invalide. C'est raté :upside_down:")
        return
    elif liste[0]=='see':
        if len(liste)<2:
            bot = await client.application_info()
            embed = discord.Embed(title="Options de configuration - "+guild.name, colour=discord.Colour(0x3fb9ef), url=guild.icon_url_as(format='jpg'),description="Voici la liste des configurations du serveur :", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=guild.icon_url_as(format='png'))
            embed.set_footer(icon_url=bot.icon_url)
            for i in server_tuple(guild.id):
                if i[1]==[]:
                    embed.add_field(name=i[0], value=" Ø ")
                else:
                    liste2=[]
                    for j in i[1]:
                        k = utilities.role_finder(guild,j,False)
                        if k == None:
                            k = utilities.canal_finder_name(client,guild,j,False)
                            if k == None:
                                liste2.append(j.replace('¬',"'"))
                            else:
                                liste2.append(k.mention)
                        else:
                            liste2.append(k.mention)
                    embed.add_field(name=i[0], value=", ".join(liste2))
            try:
                await channel.send(embed=embed)
            except discord.errors.Forbidden:
                await channel.send("Impossible d'envoyer l'embed. Vérifiez mes permissions svp :confused:")
            return
        if liste[1] in syntax.keys():
            staff = find_staff(guild.id,liste[1])
            if staff == None:
                await channel.send("Oups, une erreur est survenue :confused:\nVous êtes sûr d'avoir rentré des arguments valides ?")
            else:
                opt = ", ".join("staff")
                await channel.send(presentation[liste[1]]+", ".join(staff))
        else:
            await channel.send("Oops, option invalide :/")
    elif liste[0]=='help':
        await channel.send("Cette commande sert principalement à configurer votre serveur. En faisant `!sconfig see [option]` vous obtiendrez l'aperçu des configurations actuelles, \
et le propriétaire du serveur (actuellement {0}) peut entrer `!sconfig change <option> role1, role2, role3...` pour modifier une configuration, ou `!sconfig change <option> del` pour réinitialiser l'option !".format(message.guild.owner.name))
    else:
        await channel.send("Oops, mauvais syntaxe :upside_down:\nChoisissez entre `see` et `change` !")


# [userid,role1,role2...]
def find_all_roles(serverid):
    """Renvoie la backup des roles pour tout un serveur"""
    liste=[]
    try:
        with open('../bot-stats/roles-backup-{}.csv'.format(serverid), newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                liste.append(row)
    except FileNotFoundError:
        pass
    return liste

def save_roles(member):
    """Sauvegarde les rôles d'un membre lorsqu'il quitte un serveur"""
    liste = find_all_roles(member.guild.id)
    count = 0
    with open('../bot-stats/roles-backup-{}.csv'.format(member.guild.id),'w',newline='',encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for i in liste:
            if str(i[0])==str(member.id):
                i = [member.id]
                utilities.print2("(role-backup) MàJ des backup des rôles pour "+str(member.id))
                for r in member.roles:
                    if r.name != '@everyone':
                        i.append(r.id)
                count=1
            c=eval(str(i))
            f.writerow(c)
    if count==0:
        with open('../bot-stats/roles-backup-{}.csv'.format(member.guild.id),'a',newline='') as csvfile:
            f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            c=[member.id]
            for i in member.roles:
                c.append(i.id)
            f.writerow(c)
            utilities.print2("(role-backup) Nouveau membre détécté : "+str(member.id))

async def apply_roles(member):
    """Applique les rôles à un nouveau-membre"""
    opt = find_staff(member.guild.id,'save_roles')
    if opt not in [["true"],["oui"],["True"]]:
        return
    liste = find_all_roles(member.guild.id)
    for i in liste:
        if i[0]==str(member.id) and len(i)>1:
            for r in i[1:]:
                role = utilities.role_finder(member.guild,r)
                if role != None:
                    try:
                        await member.add_roles(role,reason="Backup des rôles automatique")
                    except:
                        pass
            return

async def delete_server(client,channel,argument):
    server = utilities.server_finder(client,argument)
    if server==None and argument.isnumeric()==False:
        await channel.send("Impossible de trouver ce serveur")
        return
    elif server != None:
        server = server.id
    elif server == None and argument.isnumeric():
        server = argument
    configs = all_staff()
    liste = []
    with open('../bot-stats/server-options.csv','w',newline='',encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for i in configs:
            if str(i[0]) != str(server):
                f.writerow(i)
            else:
                await channel.send("Serveur reset !")
    
        
