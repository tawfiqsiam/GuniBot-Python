 #!/usr/bin/env python
#coding=utf-8

from fcts import utilities,server,common,lang_tr
from random import choice
import discord

def welcome_msg(serverid,Type):
    """Renvoie le message de bienvenue"""
    if Type not in ['welcome','leave']:
        return None
    try:
        msg = ", ".join(server.find_staff(serverid,Type))
        if msg == "":
            return None
        msg = msg.replace("{random}",choice(common.bvn_msg))
        return msg.replace('¬',"'")
    except:
        utilities.erreur()
        return None
    
def find_channel(serverid):
    """Renvoie l'ID du salon de bienvenue"""
    try:
        channel = "".join(server.find_staff(serverid,"welcome_channel"))
        if channel == "":
            return None
        else:
            return channel
    except:
        utilities.erreur()
        return None

def find_autorole(serveur):
    """Renvoie le role donné automatiquement"""
    roles = []
    try:
        for r in server.find_staff(serveur.id,"auto_role"):
            r2 = utilities.role_finder(serveur,r,False)
            if r2 != None:
                roles.append(r2)
        return roles
    except:
        utilities.erreur()
        return None

async def new_member(client,member):
    """Envoie un message lorsqu'un nouveau membre arrive"""
    await server.apply_roles(member)
    salon = find_channel(member.guild.id)
    msg = welcome_msg(member.guild.id,"welcome")
    roles = find_autorole(member.guild)
    if salon==None or msg==None:
        utilities.print2("Aucun message/salon paramétré pour le serveur n°"+str(member.guild.id)+" (join)")
        utilities.print2(str(salon)+"      "+str(msg))
    else:
        salon = utilities.canal_finder_name(client,member.guild.id,salon)
        try:
            await salon.send(msg.format(server=member.guild.name,user=member.mention,owner=member.guild.owner.display_name,member_count=str(len(member.guild.members))))
        except:
            utilities.erreur()
    for i in roles:
        try:
            await member.add_roles(i,reason="Automated action")
        except discord.errors.Forbidden:
            utilities.print2("(auto-roles) Impossible de donner le role "+i.name+" (serveur "+member.guild.name+")")

async def ex_member(client,member):
    """Envoie un message lorsqu'un membre part et sauvegarde ses roles"""
    server.save_roles(member)
    salon = find_channel(member.guild.id)
    msg = welcome_msg(member.guild.id,"leave")
    if salon==None or msg==None:
        utilities.print2("Aucun message/salon paramétré pour le serveur n°"+str(member.guild.id)+" (leave)")
    else:
        salon = utilities.canal_finder_name(client,member.guild.id,salon)
        try:
            await salon.send(msg.format(server=member.guild.name,user=member.name,owner=member.guild.owner.name,member_count=str(len(member.guild.members))))
        except:
            utilities.erreur()

async def aide(channel):
    await channel.send(lang_tr.tr(channel.guild.id,"bvn","aide"))
