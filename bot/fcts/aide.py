#!/usr/bin/env python
#coding=utf-8

import discord
from fcts import common, lang_tr

async def msg(channel):
    """Envoie la liste des commandes disponibles, en fonction du type de salon (mp ou serveur)"""
    
    from fcts import common
    text = ""
    text2 = ""
    text3 = ""
    if type(channel)==discord.DMChannel:
        text = "Voici la liste des commandes disponibles en mp :"
        liste = sorted(common.commands_mp)
        for cmd in liste :
            text=text+"\n"+cmd
        await channel.send(text)
    else:
        if channel.permissions_for(channel.guild.me).send_messages==False:
            return
        liste = sorted(common.commands_server)
        for i in liste:
            if i.startswith('(everyone)'):
                text += i.replace('(everyone) ','')+"\n"
            elif i.startswith('(staff)') or i.startswith('(owner)'):
                text2 += i.replace('(owner) ','').replace('(staff) ','')+"\n"
            else:
                text3 += i+"\n"
        embed2 = discord.Embed(title=lang_tr.tr(channel.guild.id,"aide","staff"),colour=discord.Colour(0xf54623), description=text2)
        embed = discord.Embed(title =lang_tr.tr(channel.guild.id,"aide","everyone"),colour=discord.Colour(0x7ed321), description=text)
        try:
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
        except discord.errors.Forbidden:
            await channel.send("Impossible d'envoyer l'embed :confused: Vérifiez mes permissions svp")
        if text3 != "":
            await channel.send(text3)
        
