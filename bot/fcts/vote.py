#!/usr/bin/env python
#coding=utf-8

import re
from fcts import utilities

async def vote(message):
    texte = str(message.content).replace("!vote ","")
    if texte.lower()=="help":
        await message.channel.send("Entrez `!vote <texte>` pour créer un vote. Les autres membres auront ensuite le choix de répondre \"oui\" ou \"non\".\n\
Le texte que vous entrez sera exactement celui affiché")
    else:
        texte = texte.replace('@everyone','Everyone').replace('@here','Here')
        msg = await message.channel.send(texte)
        await msg.add_reaction('\U0001F44D')
        await msg.add_reaction('\U0001F44E')
        utilities.print2("("+utilities.date(message.created_at)+") "+utilities.anti_emoji(message.author.name)+" a créé un vote : "+message.content)
        if message.guild != None:
            await message.delete()

async def sondage(message):
    from fcts import common
    liste=str(message.content).split(' ')
    try:
        n = int(liste[1])
        c=1
    except:
        if liste[1] != 'help':
            await message.channel.send("Hum... il semble y avoir une erreur :thinking:\nPour rappel, la syntaxe est `!sondage <options> <texte>`")
        c=0
    if c==1:
        if n<11 and n>1:
            utilities.print2("("+utilities.date(message.created_at)+") "+utilities.anti_emoji(message.author.name)+" a créé un sondage : "+message.content)
            if message.guild != None:
                await message.delete()
            texte = str(message.content).replace("!sondage "+liste[1]+" ","")
            texte = texte.replace('@everyone','Everyone').replace('@here','Here')
            msg = await message.channel.send(texte)
            i=0
            while i<n:
                i+=1
                code = common.emojis[str(i)]
                try:
                    await msg.add_reaction(code)
                except:
                    lol=0
        else:
            await message.channel.send("Oups, vous ne pouvez pas mettre un nombre supérieur à 10 ou inférieur à 2 ^^")
    elif liste[1]=='help':
        await message.channel.send("Entrez `!sondage <nombre> <texte>` pour créer un sondage. Les autres membres auront ensuite le choix de voter pour l'une des options.\n\
Le texte que vous entrez sera exactement celui affiché")
