#!/usr/bin/env python
#coding=utf-8

import csv,time,asyncio,discord,random
from fcts import utilities,lang_tr


async def slowon(message):
    """Met le slowmode à un salon"""
    if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
        return
    if utilities.staff_finder(message.author,"slowmode"):
        slowmode = read_slowmode()
        liste=str(message.content).split(' ')
        ident=str(message.guild.id)+"-"+str(message.channel.id)
        try:
            lol=int(liste[1])
            sous_dict={}
            sous_dict["valeur"]=liste[1]
            slowmode[ident]=sous_dict
            write_slowmode(slowmode)
            await message.channel.send(lang_tr.tr(message.guild.name,"modo","slowon-0").format(message.channel.name,liste[1]))
        except ValueError:
            await message.channel.send(lang_tr.tr(message.guild.name,"modo","slowon-1"))
        except:
            await message.channel.send(lang_tr.tr(message.guild.name,"modo","slowon-2"))
            utilities.erreur()
    else:
        await message.channel.send(lang_tr.tr(message.guild.name,"modo","slowon-3"))

async def slowoff(message):
    """Enlève le slowmode d'un salon"""
    slowmode = read_slowmode()
    if utilities.staff_finder(message.author,"slowmode") and slow_finder(message,slowmode)==True:
        ident=str(message.guild.id)+"-"+str(message.channel.id)
        sous_dict={}
        sous_dict["valeur"]='0'
        slowmode[ident]=sous_dict
        write_slowmode(slowmode)
        await message.channel.send(lang_tr.tr(message.guild.name,"modo","slowoff-0").format(message.channel.name))
    elif utilities.staff_finder(message.author,"slowmode") and slow_finder(message,slowmode)==False:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","slowoff-1"))
    elif utilities.staff_finder(message.author,"slowmode")==False:
        await message.channel.send(lang_tr.tr(message.guild.name,"modo","slowon-2"))

def read_slowmode():
    """Renvoie le dictionnaire du slowmode"""
    slowmode={}
    try:
        with open('../bot-stats/slowmode.csv', newline='') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                slowmode[row[0]]=row[1]
    except:
        utilities.print2("Erreur lors de la lecture du fichier")
        utilities.erreur()
    return slowmode

def write_slowmode(slowmode):
    """Réécrit le dictionnaire du slowmode"""
    with open('../bot-stats/slowmode.csv',"w",newline='') as csvfile:
        logw = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for k,v in slowmode.items():
            logw.writerow([k,v])
    return

def slow_finder(message,slowmode):
    """Retourne "True" si le salon est en slowmode, "False" si il ne l'est pas"""
    ident=str(message.guild.id)+"-"+str(message.channel.id)
    for i,v in slowmode.items():
        if str(i) == str(ident):
            v=eval(v)
            if v["valeur"]!='0':
                return True
    return False

async def slow_check(message,client):
    """Supprime le message si slowmode non respecté"""
    if message.guild!=None:
        slowmode = read_slowmode()
        if slow_finder(message,slowmode) and utilities.staff_finder(message.author,"slowmode")==False and message.author.bot==False and message.author.id != 279568324260528128:
            ident=str(message.guild.id)+"-"+str(message.channel.id)
            sous_dict = eval(slowmode[ident])
            try:
                v = sous_dict[str(message.author.id)]
                t=time.time()-v
                if t < int(sous_dict["valeur"]):
                    await message.delete()
                    rep=await message.channel.send(lang_tr.tr(message.guild.id,"modo","slow_check-0").format(message.author.display_name,message.channel.name))
                    await asyncio.sleep(3.5)
                    await rep.delete()
                    return True
            except KeyError:
                sous_dict[str(message.author.id)]=float(time.time())
                slowmode[ident]=sous_dict
            except:
                utilities.erreur()
            write_slowmode(slowmode)


async def mute_check(message):
    """Supprime le message si le membre est mute"""
    if utilities.mute_finder(message.author) and message.author.id != 279568324260528128:
        await utilities.suppr(message)
        return True


async def mute(client,message):
    """Ajoute le role muted à un membre"""
    if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
        return
    liste=str(message.content).split(' ')
    print(liste[1],type(liste[1]))
    membre = message.mentions[0] if len(message.mentions)>0 else utilities.user_finder(message.guild.id,liste[1],client.guilds)
    if liste[1] == 'help':
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-help"))
    elif membre == None:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-0"))
    elif utilities.mute_finder(membre):
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-1").format(membre.display_name))
    elif utilities.staff_finder(message.author,"mute"):
        mute_role = utilities.role_finder(message.guild,"muted",False)
        if membre!=None and utilities.staff_finder(membre,"mute"):
            await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-2"))
        elif mute_role != None:
            try:
                await membre.add_roles(mute_role)
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-3").format(membre.display_name,message.author.display_name))
                utilities.print2("{0} a été réduit au silence par {1}".format(membre.display_name,message.author.display_name))
            except discord.Forbidden:
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-4"))
        if mute_role == None:
            await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-5"))
    elif utilities.staff_finder(message.author,"mute")==False:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-6"))

async def unmute(client,message):
    """Enlève le role muted à un membre"""
    if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
        return
    liste=str(message.content).split(' ')
    membre = message.mentions[0] if len(message.mentions)>0 else utilities.user_finder(message.guild.id,liste[1],client.guilds)
    if membre==None:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-0"))
    elif utilities.mute_finder(membre)==False:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","unmute-0").format(membre.display_name))
    elif utilities.staff_finder(message.author,"mute"):
        mute_role = utilities.role_finder(message.guild,"muted",True)
        if mute_role != None:
            try:
                await membre.remove_roles(mute_role)
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","unmute-1").format(membre.display_name))
                utilities.print2(lang_tr.tr(message.guild.id,"modo","unmute-2").format(membre.display_name,message.author.display_name))
            except discord.Forbidden:
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","unmute-3"))
        else:
            await message.channel.send("Oops, something went wrong in Mee007 land...")
    elif utilities.staff_finder(message.author,"mute")==False:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","mute-6"))

async def mutelist(message):
    """Renvoie la liste des membres muets"""
    if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
        return
    listem=[]
    for membre in message.guild.members:
        if utilities.mute_finder(membre):
            listem.append(membre.display_name)
    if listem==[]:
        texte=lang_tr.tr(message.guild.id,"modo","mutelist-0")
    else:
        texte=lang_tr.tr(message.guild.id,"modo","mutelist-1")+", ".join(listem)
    await message.channel.send(texte)

async def ban(client,message):
    """Bannis un membre du serveur"""
    if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
        return
    if utilities.staff_finder(message.author,"ban"):
        liste=str(message.content).split(' ')
        membre = message.mentions[0] if len(message.mentions)>0 else utilities.user_finder(message.guild.id,liste[1],client.guilds)
        nom=liste[1]
        del liste[0]
        del liste[0]
        raison=" ".join(liste)
        if membre==None:
            try:
                membre=client.get_user(int(nom))
            except:
                utilities.erreur()
                pass
        if membre==None:
            await message.channel.send(lang_tr.tr(message.guild.id,"modo","ban-0").format(nom))
        else:
            try:
                if utilities.staff_finder(membre,"ban"):
                    await message.channel.send(lang_tr.tr(message.guild.id,"modo","ban-1")+random.choice[':rofl','<:excusemewhat:418154673523130398>',':no_mouth:',''])
                    return
            except:
                pass
            try:
                if raison != "":
                    text=lang_tr.tr(message.guild.id,"modo","ban-2").format(message.guild.name,raison)
                else:
                    text=lang_tr.tr(message.guild.id,"modo","ban-3").format(message.guild.name)
                await membre.send(text)
            except discord.Forbidden:
                pass
            try:
                await message.guild.ban(user=membre,reason=raison)
                if raison != "":
                    text = membre.name+lang_tr.tr(message.guild.id,"modo","ban-4")+raison
                else:
                    text=membre.name+lang_tr.tr(message.guild.id,"modo","ban-5")
                await message.channel.send(text)
                utilities.print2("("+str(message.created_at)+") "+str(message.author)+" a banni "+str(membre))
            except discord.Forbidden:
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","unmute-3"))
                utilities.print2("("+str(message.created_at)+") Impossible de ban (Forbidden)")
                await membre.send(lang_tr.tr(message.guild.id,"modo","ban-6"))
            except:
                await membre.send(lang_tr.tr(message.guild.id,"modo","ban-6"))
                utilities.erreur()
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","ban-7"))

async def unban(client,message):
    """Dé-banni un membre du serveur"""
    if utilities.staff_finder(message.author,"ban"):
        liste=str(message.content).split(' ')
        ident=liste[1]
        del liste[0]
        del liste[0]
        raison = " ".join(liste)
        banliste = await message.guild.bans()
        membre = utilities.user_finder(message.guild.id,ident,client.guilds)
        if membre!=None:
            await message.channel.send(membre.name+lang_tr.tr(message.guild.id,"modo","unban-0"))
            return
        for u in banliste:
                if u[1].name == ident or str(u[1].id) == ident:
                    membre=u[1] 
        if membre==None:
            await message.channel.send(ident+lang_tr.tr(message.guild.id,"modo","unban-1"))
        else:
            print(membre)
            try:
                await message.guild.unban(user=membre,reason=raison)
                await message.channel.send(membre.name+lang_tr.tr(message.guild.id,"modo","unban-2"))
                utilities.print2("("+str(message.created_at)+") "+str(message.author)+" a unban "+str(membre))
            except discord.Forbidden:
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","unmute-3"))
                utilities.print2("("+str(message.created_at)+") Impossible de unban (Forbidden)")
            except:
                utilities.erreur()
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","unban-3"))

async def kick(client,message):
    """Expulse un membre du serveur"""
    if message.channel.permissions_for(message.channel.guild.me).send_messages==False:
        return
    if utilities.staff_finder(message.author,"kick"):
        liste=str(message.content).split(' ')
        membre = message.mentions[0] if len(message.mentions)>0 else utilities.user_finder(message.guild.id,liste[1],client.guilds)
        nom=liste[1]
        del liste[0]
        del liste[0]
        raison=" ".join(liste)
        if membre==None:
            await message.channel.send(lang_tr.tr(message.guild.id,"modo","ban-0").format(nom))
        else:
            try:
                if raison != "":
                    text = lang_tr.tr(message.guild.id,"modo","kick-0").format(message.guild.name,raison)
                else:
                    text=lang_tr.tr(message.guild.id,"modo","kick-1").format(message.guild.name)
                m = await membre.send(text)
                await message.guild.kick(user=membre,reason=raison)
                if raison != "":
                    text = lang_tr.tr(message.guild.id,"modo","kick-2").format(membre.name,raison)
                else:
                    text = lang_tr.tr(message.guild.id,"modo","kick-3").format(membre.name)
                await message.channel.send(text)
                utilities.print2("("+str(message.created_at)+") "+str(message.author)+" a kick "+str(membre))
            except discord.Forbidden:
                await message.channel.send(lang_tr.tr(message.guild.id,"modo","unmute-3"))
                utilities.print2("("+str(message.created_at)+") Impossible de kick (Forbidden)")
                try:
                    await membre.send(lang_tr.tr(message.guild.id,"modo","kick-4"))
                except:
                    utilities.print2("("+str(message.created_at)+") Impossible d'envoyer un mp au membre kick")
            except:
                utilities.erreur()
    else:
        await message.channel.send(lang_tr.tr(message.guild.id,"modo","unban-3"))


async def freeze_on(message):
    """Freeze un salon"""
    if utilities.staff_finder(message.author,"slowmode"):
        freezer = read_freeze_server(message.guild.id)
        if freezer == []:
            freezer = read_freeze_all()
            freezer.append([message.guild.id,message.channel.id])
            write_freeze_all(freezer)
        elif str(message.channel.id) in freezer:
            await message.channel.send("Ce salon est déjà gelé "+random.choice([':upside_down:',':thinking:',':rofl:',':innocent:',':no_mouth:',':snowman:',':snowflake:',':sweat_smile:']))
        else:
            freezer.append(message.channel.id)
            write_freeze_server(freezer)
            await message.channel.send("Le salon "+message.channel.name+" est maintenant gelé ! :snowflake: ")
    else:
        await message.channel.send("Vous ne semblez pas posséder les permissions suffisantes pour faire cela...")

async def freeze_off(message):
    """Enlève le slowmode d'un salon"""
    freezer = read_freeze_server(message.guild.id)
    if freezer == [] or str(message.channel.id) not in freezer[1:]:
        await message.channel.send("Ce salon n'est pas gelé :upside_down:")
        return
    if utilities.staff_finder(message.author,"slowmode") == False:
        await message.channel.send("Vous ne possédez pas la permission de faire ceci <:red_cross:447509074771312652>")
        return
    if freezer == [str(message.guild.id),str(message.channel.id)]:
        freezer = read_freeze_all()
        while [str(message.guild.id),str(message.channel.id)] in freezer:
            freezer.remove([str(message.guild.id),str(message.channel.id)])
        write_freeze_all(freezer)
        await message.channel.send(random.choice(["Le salon n'est plus givré !","Le salon est dégelé !","Le salon n'est plus gelé !"]))
        return
    if str(message.channel.id) in freezer[1:]:
        channels = freezer[1:]
        channels.remove(str(message.channel.id))
        freezer = freezer[0]+channels
        write_freeze_server(freezer)
        await message.channel.send(random.choice(["Le salon n'est plus givré !","Le salon est dégelé !","Le salon n'est plus gelé !"]))
        return
        
def read_freeze_server(ID):
    """Renvoie la liste des salons gelés, pour le serveur"""
    try:
        with open('../bot-stats/freeze.csv', newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                if row[0]==str(ID):
                    return row
    except:
        utilities.print2("Erreur lors de la lecture du fichier")
        utilities.erreur()
    return []

def read_freeze_all():
    """Renvoie la liste des serveurs contenant la liste des salons gelés"""
    freezer = list()
    try:
        with open('../bot-stats/freeze.csv', newline='',encoding='utf-8') as csvfile:
            f = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in f:
                freezer.append(row)
    except:
        utilities.print2("Erreur lors de la lecture du fichier")
        utilities.erreur()
    return freezer

def write_freeze_all(freezer):
    """Réécrit la liste du freezer"""
    with open('../bot-stats/freeze.csv',"w",newline='',encoding='utf-8') as csvfile:
        logw = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for server in freezer:
            logw.writerow(server)
    return

def write_freeze_server(freezer):
    """Réécrit la liste du freezer"""
    fr = read_freeze_all()
    count = 0
    for i in fr:
        if i[0]==freezer[0]:
            i = freezer
            count = 1
    if count == 0:
        fr.append([freezer])
    write_freeze_all(fr)
    return

async def freeze_check(message):
    """Supprime le message si le salon est gelé"""
    if message.guild!=None:
        freeze = read_freeze_server(message.guild.id)
        if freeze ==[]:
            return
        if str(message.channel.id) in freeze[1:] and utilities.staff_finder(message.author,"slowmode")==False and message.author.bot==False and message.author.id != 279568324260528128:
            await utiliities.suppr(message)
            await message.channel.send(":snowflake:  **Ce salon est gelé !**",delete_after=2.0)
