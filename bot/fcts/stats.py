#!/usr/bin/env python
#coding=utf-8

from fcts import utilities,common,server
import discord,datetime,csv,time,os

async def userinfo(client,message):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    liste=str(message.content).split(' ')
    liste.append(message.author.name)
    lister=[]
    image=None
    if message.guild==None:
        await message.channel.send("Cette commande n'est pour l'instant pas disponible en message privé")
        return
    membre = message.mentions[0] if len(message.mentions)>0 else utilities.user_finder(message.guild.id,liste[1],client.guilds)
    if membre==None:
        await message.channel.send( "Aucun membre n'a été trouvé :confused:")
        return
    for role in membre.roles:
        if str(role)!='@everyone':
            lister.append(str(role))
    m_roles =", ".join(lister) if lister!=[] else "Aucun"
    try:
        m_desc = common.user_desc[str(membre.id)]
    except KeyError:
        m_desc = "..."
    for k,v in common.user_img.items():
        if k==str(membre.id):
            image=discord.File('userimg/'+v)
    m_statut=utilities.translater(str(membre.status))
    couleur = membre.color
    if membre.activity==None:
        m_activity="Aucune"
    elif membre.activity.type==discord.ActivityType.playing:
        m_activity="Joue à "+membre.activity.name
    elif membre.activity.type==discord.ActivityType.streaming:
        m_activity="Stream ("+membre.activity.name+")"
    elif membre.activity.type==discord.ActivityType.listening:
        m_activity="Écoute "+membre.activity.name
    elif membre.activity.type==discord.ActivityType.watching:
        m_activity="Regarde "+membre.activity.name
    else:
        m_activity="Error"
    m_place = str(sorted(message.guild.members, key=lambda m: m.joined_at).index(utilities.user_finder(message.guild.id,liste[1],client.guilds,False)) + 1) + "/" + str(len(message.guild.members))
    avatar = membre.avatar_url_as(format='png')
    #cr = membre.created_at
    #date_create = str(cr.day)+'/'+str(cr.month)+'/'+str(cr.year)+' '+str(cr.hour)+':'+str(cr.minute)+':'+str(cr.second)+' (UTC'+str(cr.tzinfo).replace('None','')+")"
    date_create = utilities.date(membre.created_at)
    #cr = membre.joined_at
    #date_join = str(cr.day)+'/'+str(cr.month)+'/'+str(cr.year)+' '+str(cr.hour)+':'+str(cr.minute)+':'+str(cr.second)+' (UTC'+str(cr.tzinfo).replace('None','')+")"
    date_join = utilities.date(membre.joined_at)
    
    embed = discord.Embed(colour=couleur,url=membre.avatar_url_as(static_format='png'))
    embed.set_thumbnail(url=avatar)
    embed.set_author(name=str(membre), icon_url=avatar)
    embed.add_field(name="Nom", value=membre.name, inline=True)
    embed.add_field(name="Surnom", value=membre.display_name, inline=True) if membre.name != membre.display_name else embed.add_field(name="Surnom :", value="Aucun", inline=True)
    embed.add_field(name="ID", value=membre.id, inline=True)
    embed.add_field(name="Créé le", value=date_create, inline=True)
    embed.add_field(name="A rejoint le", value=date_join, inline=True)
    embed.add_field(name="Position d'arrivée", value=m_place, inline=True)
    embed.add_field(name="Statut", value=m_statut.capitalize(), inline=True)
    embed.add_field(name="Activité", value=m_activity, inline=True)
    embed.add_field(name="Roles "+str([len(membre.roles)-1]), value=m_roles, inline=True)
    embed.set_footer(text=m_desc)
    try:
        await message.channel.send(embed=embed)
    except discord.Forbidden:
        await message.channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")
    if image!=None:
        await message.channel.send(file=image)

async def membercount(message):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    bots = c_co = 0
    total = len(message.guild.members)
    for u in message.guild.members:
        if u.bot:
            bots+=1
        if str(u.status) != "offline":
            c_co+=1
    embed = discord.Embed(colour=message.guild.me.color)
    embed.add_field(name="Nombre de membres total", value=str(total), inline=True)
    embed.add_field(name="Nombre de bots", value=str(bots), inline=True)
    embed.add_field(name="Nombre d'humains", value=str(total-bots), inline=True)
    embed.add_field(name="Nombre de membres connectés", value=str(c_co), inline=True)
    try:
        await message.channel.send(embed=embed)
    except discord.Forbidden:
        await message.channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")

async def serverinfo(message):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    lister=[]
    roles=[]
    c_text = c_voice = c_roles = bots = c_co = 0
    server = message.guild
    for role in server.role_hierarchy:
        if str(role)!='@everyone':
            lister.append(str(role))
            c_roles+=1
    if lister!=[]:
        roles=", ".join(lister)
    emojis = len(server.emojis)
    owner = str(server.owner)
    for c in server.channels:
        if type(c)==discord.channel.TextChannel:
            c_text+=1
        elif type(c)==discord.channel.VoiceChannel:
            c_voice+=1
    for m in server.members:
        if m.bot:
            bots+=1
        if str(m.status) != "offline":
            c_co+=1
    members =server.member_count
    image = server.icon_url_as(format='png')
    couleur = server.me.color
    #cr = server.created_at
    #date_create = str(cr.day)+'/'+str(cr.month)+'/'+str(cr.year)+' '+str(cr.hour)+':'+str(cr.minute)+':'+str(cr.second)+' (UTC'+str(cr.tzinfo).replace('None','')+")"
    date_create = utilities.date(server.created_at)
    embed = discord.Embed(colour=couleur,url=image)
    embed.set_thumbnail(url=image)
    embed.add_field(name="Nom :", value=server.name, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Propriétaire", value=owner, inline=True)
    embed.add_field(name="Créé le", value=date_create, inline=True)
    embed.add_field(name="Nombre de membres", value=str(members), inline=True)
    embed.add_field(name="dont bots", value=str(bots), inline=True)
    embed.add_field(name="Membres connectés", value=str(c_co), inline=True)
    embed.add_field(name="Nombre d'émojis", value=emojis, inline=True)
    embed.add_field(name="Nombre de salons texte", value=str(c_text), inline=True)
    embed.add_field(name="Nombre de salons vocaux", value=str(c_voice), inline=True)
    embed.add_field(name="Roles "+str([len(server.roles)-1]), value=roles, inline=True)
    try:
        await message.channel.send(embed=embed)
    except discord.Forbidden:
        await message.channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")

async def channel_info(message):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    channel =  message.channel_mentions[0] if len(message.channel_mentions)>0 else message.channel
    couleur = message.guild.me.color
    image = message.guild.icon_url_as(format='png')
    if channel.topic == None or len(str(channel.topic))<2:
        topic = "Aucune"
    else:
        topic = channel.topic
    embed = discord.Embed(colour=couleur,url=image)
    embed.set_thumbnail(url=image)
    embed.add_field(name="Nom :", value=channel.name, inline=True)
    embed.add_field(name="Mention :", value=channel.mention, inline=True)
    embed.add_field(name="ID :", value=str(channel.id), inline=True)
    embed.add_field(name="Date de création :", value=utilities.date(channel.created_at), inline=True)
    embed.add_field(name="Description :", value=topic, inline=True)
    embed.add_field(name="Catégorie :", value=channel.category.name, inline=True)
    embed.add_field(name="Nombre de membres :", value=str(len(channel.members)), inline=True)
    embed.add_field(name="Nombre de messages épinglés :", value=str(len(await channel.pins())), inline=True)
    try:
        await message.channel.send(embed=embed)
    except discord.Forbidden:
        await message.channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")

async def role_info(message):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    if message.role_mentions != []:
        role = message.role_mentions[0]
    else:
        r = " ".join(message.content.split(" ")[1:])
        role = utilities.role_finder(message.guild,r)
        if role == None:
            await message.channel.send("Aucun rôle n'a été trouvé :confused:")
            return
    cr = role.created_at
    date_create = str(cr.day)+'/'+str(cr.month)+'/'+str(cr.year)+' '+str(cr.hour)+':'+str(cr.minute)+':'+str(cr.second)+' (UTC'+str(cr.tzinfo).replace('None','')+")"
    embed = discord.Embed(colour=role.colour)
    embed.add_field(name="Nom", value=role.name, inline=True)
    embed.add_field(name="Identifiant", value=str(role.id), inline=True)
    embed.add_field(name="Couleur", value="#"+str(role.colour.value), inline=True)
    embed.add_field(name="Mentionnable", value=str(role.mentionable).replace("True","Oui").replace("False","Non"), inline=True)
    embed.add_field(name="Nombre de membres", value=str(len(role.members)), inline=True)
    embed.add_field(name="Affiché séparément", value=str(role.hoist).replace("True","Oui").replace("False","Non"), inline=True)
    try:
        await message.channel.send(embed=embed)
    except discord.Forbidden:
        await message.channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")
    

async def find(message,client):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    from fcts import server
    liste=str(message.content).split(' ')
    if liste[1]=='user' or liste[1]=='membre':
        try:
            user = await client.get_user_info(int(liste[2]))
            rep = "Nom : "+str(user)+"\nID : "+str(user.id)
        except:
            rep = "Aucun membre trouvé :confused: (vérifiez l'ID entrée)"
    elif liste[1] in ['salon','channel'] and len(liste)>2:
        salon = utilities.canal_finder_all(client,liste[2],False)
        if salon==None:
            rep = "Aucun salon trouvé :/"
        else:
            rep = "Nom : "+str(salon.name)+"\nID : "+str(salon.id)+"\nServeur : "+str(salon.guild.name)+" ("+str(salon.guild.id)+")"
    elif liste[1] in ['serveur','server'] and len(liste)>2:
        server = utilities.server_finder(client,liste[2])
        if server==None:
            rep = "Aucun serveur trouvé :/"
        else:
            rep = "Nom : "+str(server.name)+"\nID : "+str(server.id)+"\nPropriétaire : "+str(server.owner)
    elif liste[1]=='staff' and message.guild != None:
        if liste[2] == 'help' or len(liste)<3:
            rep = "Ce paramètre vous permet de trouver les roles associés à une commande de modération (clear, mute...).\nSyntaxe : `!find staff <clear|slowmode|mute|kick|ban>`"
        else:
            staff = server.find_staff(message.guild.id,liste[2])
            if staff == None:
                rep = "Oups, une erreur est survenue :confused:\nVous êtes sûr d'avoir rentré des arguments valides ?"
            else:
                rep = "ID des rôles pouvant utiliser la commande "+liste[2]+" : "+", ".join(staff)
    else:
        rep = "Oups, paramère invalide :upside_down:\nVous pouvez rentrer `user`, `channel`, `server` ou `staff` par exemple !"
    await message.channel.send(rep)


# row1 = [serverID,messagesTotaux,commandes,{channel1:[messages,commandes],channel2:[messages,commandes],channel3:[messages,commandes]...}]
# row2 = [channelID,{user1:[messages,commandes],user2:[messages,commandes],user3:[messages,commandes]...}]
def read_stats_1(serverid):
    """Renvoie la ligne de statistiques correspondant au serveur"""
    try:
        with open('../bot-stats/stats1.csv', newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                if str(row[0])==str(serverid):
                    return [int(row[0]),int(row[1]),int(row[2]),eval(row[3])]
            with open('../bot-stats/stats1.csv','a',newline='') as csvfile:
                f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                f.writerow([serverid,0,0,{}])
                utilities.print2("(stats) Nouveau serveur détecté (id "+str(serverid)+")")
                return [serverid,0,0,{}]
    except FileNotFoundError:
        with open('../bot-stats/stats1.csv','w',newline='',encoding='utf-8') as csvfile:
            f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            f.writerow([serverid,0,0,{}])
        return [serverid,0,0,{}]

def read_stats_2(channelid):
    """Renvoie la ligne de statistiques correspondant au salon"""
    try:
        with open('../bot-stats/stats2.csv', newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                if str(row[0])==str(channelid):
                    return [eval(row[0]),eval(row[1])]
            with open('../bot-stats/stats2.csv','a',newline='') as csvfile:
                f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                f.writerow([channelid,{}])
                utilities.print2("(stats) Nouveau salon détecté (id "+str(channelid)+")")
                return [channelid,{}]
    except FileNotFoundError:
        with open('../bot-stats/stats2.csv','w',newline='',encoding='utf-8') as csvfile:
            f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            f.writerow([channelid,0,0,{}])
        return [channelid,{}]

def all_stats(n=1):
    """Renvoie la liste de tout le fichier csv"""
    liste=[]
    try:
        with open('../bot-stats/stats{}.csv'.format(n), newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                liste.append(row)
    except FileNotFoundError:
        liste=[]
    return liste

def change_stats(message):
    """Met à jour les stats à partir du message"""
    if message.author.bot or message.guild == None:
        return
    row = read_stats_1(message.guild.id)
    if message.content.startswith("!"):
        row[2]+=1
        try:
            row[3][message.channel.id][1]=int(row[3][message.channel.id][1])+1
            row[3][message.channel.id][0]=int(row[3][message.channel.id][0])+1
        except KeyError:
            row[3][message.channel.id]=[1,1]
    else:
        try:
            row[3][message.channel.id][0]=int(row[3][message.channel.id][0])+1
        except KeyError:
            row[3][message.channel.id]=[1,0]
    row[1]+=1
    
    liste = all_stats(1)
    with open('../bot-stats/stats1.csv','w',newline='',encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for i in liste:
            if str(i[0])==str(message.guild.id):
                i=row
            f.writerow(i)
    #-----
    row = read_stats_2(message.channel.id)
    if message.content.startswith("!"):
        try:
            row[1][message.author.id][1]=int(row[1][message.author.id][1])+1
            row[1][message.author.id][0]=int(row[1][message.author.id][0])+1
        except KeyError:
            row[1][message.author.id]=[1,1]
    else:
        try:
            row[1][message.author.id][0]=int(row[1][message.author.id][0])+1
        except KeyError:
            row[1][message.author.id]=[1,0]
    liste = all_stats(2)
    with open('../bot-stats/stats2.csv','w',newline='',encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for i in liste:
            if str(i[0])==str(message.channel.id):
                i=row
            f.writerow(i)

# row1 = [serverID,messagesTotaux,commandes,{channel1:[messages,commandes],channel2:[messages,commandes],channel3:[messages,commandes]...}]
# row2 = [channelID,{user1:[messages,commandes],user2:[messages,commandes],user3:[messages,commandes]...}]

async def msg(client,message):
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    liste = message.content.split(" ")
    liste.append("all")
    embed = discord.Embed(colour=message.guild.me.color)
    try:
        embed.set_footer(text="Depuis le "+utilities.date(datetime.datetime.fromtimestamp(os.stat("../bot-stats/stats1.csv").st_birthtime)))
    except AttributeError:
        pass
        #embed.set_footer(text="date indéfinie :/")
    if liste[1]=='all':
        messages=0
        commandes=0
        g = client.guilds
        for s in g:
            r = read_stats_1(s.id)
            messages+=r[1]
            commandes+=r[2]
        moyenne = round(messages/len(g),2)
        embed.set_author(name="Statistiques globales", url=client.user.avatar_url_as(format='jpg'), icon_url=client.user.avatar_url_as(format='jpg'))
        embed.add_field(name="Nombre de serveurs connectés", value=str(len(g)), inline=False)
        embed.add_field(name="Nombre de messages lus", value=str(messages), inline=False)
        embed.add_field(name="Nombre de commandes lues", value=str(commandes), inline=False)
        embed.add_field(name="Moyenne de messages par serveur", value=str(moyenne), inline=False)
        embed.add_field(name="Nombre de membres visibles",value=str(len(client.users)),inline=False)
    elif liste[1] in ["server","serveur"]:
        r = read_stats_1(message.guild.id)
        channels = users = 0
        for s in r[3].keys():
            r2 = read_stats_2(s)
            channels+=1
            users += len(r2[1].keys())
        moyenne = round(r[1]/channels,2)
        moyenne2 = round(r[1]/users,2)
        embed.set_author(name="Statistiques du serveur", url=message.guild.icon_url_as(format='jpg'), icon_url=message.guild.icon_url_as(format='jpg'))
        embed.add_field(name="Nombre de salons", value=str(len(r[3].keys())), inline=False)
        embed.add_field(name="Nombre de messages lus", value=str(r[1]), inline=False)
        embed.add_field(name="Nombre de commandes lues", value=str(r[2]), inline=False)
        embed.add_field(name="Moyenne de messages par salon", value=str(moyenne), inline=False)
        embed.add_field(name="Moyenne de messages par membre", value=str(moyenne2), inline=False)
    elif liste[1] in ["salon","channel","text"]:
        ID = message.channel.id
        r2 = read_stats_2(ID)
        somme_t = somme_c = users = 0
        for u,v in r2[1].items():
            print(u,v)
            users += 1
            somme_t += int(v[0])
            somme_c += int(v[1])
        moyenne = round(somme_t/users,2)
        moyenne2 = round(somme_c/users,2)
        embed.set_author(name="Statistiques du salon "+message.channel.name, url=message.guild.icon_url_as(format='jpg'), icon_url=message.guild.icon_url_as(format='jpg'))
        embed.add_field(name="Nombre de messages lus", value=str(somme_t), inline=False)
        embed.add_field(name="Nombre de commandes lues", value=str(somme_c), inline=False)
        embed.add_field(name="Nombre de membres", value=str(users), inline=False)
        embed.add_field(name="Moyenne de messages par membre", value=str(moyenne), inline=False)
        embed.add_field(name="Moyenne de commandes par membre", value=str(moyenne2), inline=False)
    else:
        await message.channel.send("Paramètre invalide. Sélectionnez `all`, `server` ou `channel` en paramètres")
        return
    try:
        await message.channel.send(embed=embed)
    except discord.Forbidden:
        await message.channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")
