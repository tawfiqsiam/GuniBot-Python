#!/usr/bin/env python
#coding=utf-8

from fcts.common import *
from fcts import emoji,server
import discord,re,traceback,sys,time,datetime,string


def print2(text):
    try:
        print(text)
    except UnicodeEncodeError:
        text=anti_code(str(text))
        try:
            print(text)
        except UnicodeEncodeError:
            try:
                print(emoji.anti_code(text))
            except UnicodeEncodeError:
                print(text.encode("ascii","ignore").decode("ascii"))

def anti_code(text):
    if type(text)==str:
        for i,j in [('é','e'),('è','e'),('à','a'),('î','i'),('ê','e'),('ï','i'),('ü','u'),('É','e'),('ë','e'),('–','-'),('“','"'),('’',"'"),('û','u'),('°','°'),('Ç','C'),('ç','c')]:
            text=text.replace(i,j)
        text=emoji.anti_code(text)
        return text
    elif type(text)==list:
        text2=[]
        for i,j in [('é','e'),('è','e'),('à','a'),('î','i'),('ê','e'),('ï','i'),('ü','u'),('É','e'),('ë','e'),('–','-'),('“','"'),('’',"'"),('û','u'),('°','°'),('Ç','C'),('ç','c')]:
            for k in text:
                k=emoji.anti_code(k)
                text2.append(k.replace(i,j))
        return text2

def anti_md(text):
    """Supprime le markdown d'un texte"""
    if type(text)==str:
        for i,j in [('*','\*'),('_','\_')]:
            text=text.replace(i,j)
        for c in text:
            if c not in string.printable:
                text = text.replace(c,'\\'+c)
        return text
    elif type(text)==list:
        text2=[]
        for i,j in [('é','e')]:
            for k in text:
                for c in k:
                    if c not in string.ascii:
                        k = k.replace(c,'\\'+c)
                text2.append(k.replace(i,j))
        return text2

async def rep(message):
    m = await message.channel.send("Temps de réponse (aller-retour) : ")
    t = (m.created_at - message.created_at).total_seconds()
    await m.edit(content="Temps de réponse (aller-retour) : "+str(round(t*1000,3))+"ms")

async def suppr(message):
    """Tente de supprimer un message"""
    try:
        await message.delete()
    except discord.errors.Forbidden:
        print2("Oups, impossible de supprimer ce message (permissions manquantes)")
    except discord.errors.NotFound:
        print2("Impossible de supprimer ce message (probablement déjà supprimé)")

def erreur(send=False):
    text = "Traceback (most recent call last):\n"
    text += " ".join(traceback.format_tb(sys.exc_info()[2]))
    text += str(sys.exc_info()[0]).split("<class '")[1].split("'>")[0]+' : '+str(sys.exc_info()[1])
    print2(text)
    if send:
        return "```python\n"+text+"\n```"

def translater(chain=''):
    """Traduit un message donné"""
    global traducteur
    for cle,valeur in traducteur.items():
        chain=chain.replace(cle,valeur)
    return chain

def date(d):
    """Traduit un objet de type time.struct_time en chaine de caractère  lisible. Renvoie un str"""
    global day,month
    if type(d)==datetime.datetime:
        if len(str(d.day))==1:
            jour="0"+str(d.day)
        else:
            jour = str(d.day)
        h=[]
        for i in ['hour','minute','second']:
            a = eval(str("d."+i))
            if len(str(a))==1:
                h.append("0"+str(a))
            else:
                h.append(str(a))
        date = jour+" "+month[str(d.month)]+" "+str(d.year)+"  "+":".join(h)
    elif type(d)==time.struct_time:
        if len(str(d.tm_mday))==1:
            jour="0"+str(d.tm_mday)
        else:
            jour = str(d.tm_mday)
        h=[]
        for i in ['tm_hour','tm_min','tm_sec']:
            a = eval(str("d."+i))
            if len(str(a))==1:
                h.append("0"+str(a))
            else:
                h.append(str(a))
        date = day[str(d.tm_wday+1)]+" "+jour+" "+month[str(d.tm_mon)]+" "+str(d.tm_year)+"  "+":".join(h)
    else:
        return None
    return date

def server_finder(client,server):
    """Retourne un objet de type server à partir de son nom"""
    server=str(server)
    serveur = None
    for guild in client.guilds:
        if str(guild.id) == server or guild.name == server:
            serveur = guild
    if serveur==None:
        return None
    else:
        return serveur

def canal_finder_name(client,server,channel,message=True):
    """Retourne un objet de type channel à partir de son nom/ID"""
    if type(server)==int or type(server) == str:
        server=server_finder(client,server)
    channel=str(channel)
    canal = None
    for chan in server.channels:
        if chan.name == str(channel) or str(chan.id) == str(channel) or str(chan.mention)==str(channel):
            canal = chan
    if canal==None and message:
        print2("Impossible de trouver le salon "+channel)
    else:
        return canal

def canal_finder_all(client,channelid,message=True):
    """Retourne un objet de type channel à partir de son identifiant/sa mention"""
    channelid=int(channelid)
    canal = None
    for server in client.guilds:
        for channel in server.channels:
            if str(channel.id) == str(channelid) or str(channel.mention)==channelid:
                canal = channel
    if canal==None and message==True:
        print2("Impossible de trouver le salon "+str(channelid))
    elif canal==None and message==False:
        return None
    else:
        return canal

def owners_finder(guilds,Type="name"):
    """Renvoie une liste contenant tous les propriétaires de serveurs"""
    liste=[]
    for s in guilds:
        if Type=="name":
            liste.append(s.owner.name)
        elif Type=="id":
            liste.append(s.owner.id)
        elif Type=="user":
            liste.append(s.owner)
    return liste

def user_finder(serverid,username,serveurs,message=True):
    """Retourne un objet de type member à  partir de son nom"""
    if type(serveurs)==discord.Client:
        serveurs=serveurs.guilds
    serverid=int(serverid)
    username=str(username)
    nom = None
    for server in serveurs:
        if server.id == serverid:
            for name in server.members:
                if str(name.name).lower().startswith(username.lower()) or username==str(name.mention):
                    nom = name
                    break
            if nom==None:
                for name in server.members:
                    if username.lower() in str(name.name).lower() or username==str(name.id):
                        nom = name
                        break
    if nom==None and message==True and username!='help':
        print2("Impossible de trouver le membre "+username)
        return None
    else:
        return nom

def user_finder_all(client,username,message=True):
    """Retourne un objet de type member à  partir de son nom/ID"""
    nom = None
    for server in client.guilds:
        for name in server.members:
            if username.lower() in str(name.name).lower() or username==str(name.mention) or username==str(name.id):
                nom = name
    if nom==None and message==True:
        print2("Impossible de trouver le membre "+username)
        return None
    elif nom==None and message==False:
        return None
    else:
        return nom

def staff_finder(membre,staff):
    """Retourne "True" si le membre appartient au staff, "False" si il n'y appartient pas"""
    try:
        staff = server.find_staff(membre.guild.id,staff)  #list
    except AttributeError:
        return True
    c=0
    try:
        if membre.roles!=None:
            for role in membre.roles:
                if str(role.id) in str(staff).lower() or anti_code(role.name) in str(staff).lower():
                    c=1
    except:
        print2(str(membre)+" n'a pas de role !")
    if c==1 or membre.id == 279568324260528128:
        return True
    else:
        return False

def is_hunter(message):
    """Renvoie True si le salon fiat partie du jeu Hunter"""
    try:
        salons = server.find_staff(message.guild.id,"hunter") #list
        return str(message.channel.id) in salons
    except:
        erreur()
        return False

def mute_finder(member):
    """Retourne "True" si le membre est mute, "False" si il ne l'est pas"""
    try:
        if role_finder(member.guild,"muted",False) in member.roles:
           return True
        else:
            return False
    except AttributeError:
        print2("message en mp => "+member.name+" n'a pas de role")
        return False

def count_class():
    """Renvoie le nombre de personnes inscrites au classement"""
    c=0
    try:
        with open('../bot-stats/ranks.txt','r') as fichier:
            texte = fichier.read()
        rangs = eval(texte)
    except:
        rangs={}
    for m in rangs:
        c+=1
    return c

async def message_finder(channel,text):
    async for log in channel.history(limit=1000):
        if log.content.startswith(text):
            return log
    return None

def anti_emoji(txt):
    """Essaie de supprimer les caractères non-ascii d'un texte"""
    try:
        # UCS-4
        highpoints = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        highpoints = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return highpoints.sub(u'\u25FD',txt)

def count_maj(texte):
    """Comte le pourcentage de majuscules dans un texte"""
    c=0
    from fcts import common
    l=len(texte)
    for letter in texte:
        if letter==letter.upper() and letter.lower() in common.letters:
            c+=1
    if l>0:
        return (c*100)/l
    else:
        return 0

def role_finder(server,rolename,message=True):
    """Retourne un objet de type channel à partir de son identifiant"""
    rolename=str(rolename)
    role = None
    for rolef in server.roles:
        if str(rolef.name).lower() == str(rolename).lower() or str(rolef.id)==str(rolename) or rolef.mention == str(rolename):
            role = rolef
    if role==None:
        if message==True:
            print2("Impossible de trouver le role "+rolename)
        return None
    else:
        return role

def image_finder(name):
    """Retourne le chemin d'accès à une image"""
    return "../images/"+str(name)
