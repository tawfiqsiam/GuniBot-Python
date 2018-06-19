#!/usr/bin/env python
#coding=utf-8

import asyncio,discord
from fcts import utilities,lang_tr

async def clear(client,message):
    #await logs(client,message) 
    from fcts import common,utilities
    liste=str(message.content).split(' ')
    liste.append('true')
    aide=False
    if message.channel.permissions_for(message.guild.me).send_messages==False:
        return
    if liste[1].lower()=='help':
        await message.channel.send(lang_tr.tr(message.guild.id,"clear","help"))
        aide=True
    if message.guild!=None and utilities.staff_finder(message.author,"clear") and not aide:
        var=[]
        counter=0
        try:
            msg=int(liste[1])
        except:
            if message.guild.id != None:
                msg = utilities.user_finder(message.guild.id,liste[1],client)
        if type(msg)==int:
            msg+=1
            if liste[2].lower()=="false":
                async for log in message.channel.history(limit=msg):
                    var.append(log)
                    counter+=1
                    if len(var)>50:
                        try:
                            await message.channel.delete_messages(var)
                            var=[]
                        except:
                            utilities.print2("erreur : "+str(len(var)))
            elif liste[2].lower()=='true':
                pinned = await message.channel.pins()
                async for log in message.channel.history(limit=msg+len(pinned)):
                    if counter<msg and log.pinned==False:
                        counter += 1
                        var.append(log)
                        if len(var)>50:
                            try:
                                await message.channel.delete_messages(var)
                            except:
                                utilities.print2("erreur : "+str(len(var)))
                            var=[]
            else:
                await message.channel.send(lang_tr.tr(message.guild.id,"clear","arg"))
        elif type(msg)==discord.member.Member:
            if liste[2].lower()=="false":
                async for log in message.channel.history(limit=10000):
                    if log.author == msg:
                        counter += 1
                        var.append(log)
                        if len(var)>50:
                            try:
                                await message.channel.delete_messages(var)
                            except:
                                utilities.print2("erreur : "+str(len(var)))
                            var=[]
            elif liste[2].lower()=="true":
                async for log in message.channel.history(limit=10000):
                    if log.author == msg and log.pinned==False:
                        counter += 1
                        var.append(log)
                        if len(var)>50:
                            try:
                                await message.channel.delete_messages(var)
                                var=[]
                            except:
                                utilities.print2("erreur : "+str(len(var)))
            else:
                await message.channel.send(lang_tr.tr(message.guild.id,"clear","arg"))
        try:
            await message.channel.delete_messages(var)
        except discord.errors.HTTPException:
            for m in var:
                try:
                    await m.delete()
                except:
                    break
            utilities.print2("(clear) Erreur HTTP : ")
            utilities.erreur()
        if counter>0:
            texte=str(counter-1)+lang_tr.tr(message.guild.id,"clear","msg-1")
            rep = await message.channel.send(texte)
            texte = "("+str(message.created_at)+") "+texte
            utilities.print2(texte)
            await asyncio.sleep(3)
            try:
                await rep.delete()
            except discord.errors.NotFound:
                utilities.print2('Oups, le message est déjà supprimé')
    elif message.guild==None and not aide:
        await message.channel.send(lang_tr.tr(message.guild.id,"clear","msg-2").format(message.author.name))
    elif not aide:
        await message.channel.send(lang_tr.tr(message.guild.id,"clear","msg-3").format(message.author.name))

ID = 0
async def big_purge(client,message):
    global ID
    if utilities.staff_finder(message.author,"clear") == False:
        await message.channel.send(lang_tr.tr(message.guild.id,"clear","msg-3").format(message.author.name))
        return
    ID = message.author.id
    def check_answer(m):
        global ID
        return m.content.lower() in ['oui','yes'] and m.author.id == ID
    await message.channel.send(lang_tr.tr(message.guild.id,"clear","purge-0"))
    try:
        msg = await client.wait_for('message',check=check_answer,timeout=30.0)
    except asyncio.TimeoutError:
        await message.channel.send(lang_tr.tr(message.guild.id,"clear","purge-1"))
        return
    except:
        utilities.erreur(True)
        return
    def check_pinned(m):
        return not m.pinned
    utilities.print2("Purge du salon "+message.channel.name+" (serveur : "+message.guild.name+") par "+message.author.name)
    try:
        await message.channel.purge(limit=50000,check=check_pinned,bulk=True)
    except:
        await message.channel.send(lang_tr.tr(message.guild.id,"clear","purge-2"))
        utilities.erreur(True)
