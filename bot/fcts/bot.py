#!/usr/bin/env python
#coding=utf8

from fcts import utilities,server

async def new_news(client,message):
    if message.channel.id not in [444623108658298890,444623204108075008] or message.guild.id != 356067272730607628 or message.content.startswith("!"):
        return
    for s in client.guilds:
        channels = server.find_staff(s.id,"bot_news")
        if channels != []:
            for c in channels :
                channel = utilities.canal_finder_name(client,s,c)
                if channel != None:
                    await channel.send(content=message.content,tts=message.tts)
                
