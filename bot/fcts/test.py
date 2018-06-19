#!/usr/bin/env python
#coding=utf-8

from fcts import admin,utilities
import discord,datetime,asyncio,random

import os

async def test(client,message):
    long = []
    count = []
    text = []
    for m in client.guilds:
        if len(str(m.id)) not in long:
            long.append(len(str(m.id)))
            count.append(1)
        else:
            count[long.index(len(str(m.id)))] += 1
    for i in range(len(long)):
        text.append(str(long[i])+":"+str(count[i]))
    await message.channel.send(" / ".join(text))
    

